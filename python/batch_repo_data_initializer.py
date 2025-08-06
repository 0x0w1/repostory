#!/usr/bin/env python3
"""
Batch GitHub Repository Data Fetcher - GitHub Actions Optimized

Processes all repositories from repositories.json in a single process
optimized for GitHub Actions free plan constraints:
- 4 vCPU, 16GB RAM environment
- Conservative API rate limiting for GraphQL
- Maximum 3 concurrent workers to prevent resource exhaustion
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from repo_data_initializer import GitHubFetcher


def debug_print(message, debug=False):
    """Print debug message only if debug mode is enabled."""
    if debug:
        print(message)


def filter_repositories(all_repos, output_dir, debug=False):
    """Filter out repositories that already have data files to avoid subprocess overhead."""
    repos_to_process = []
    skipped_repos = []

    for url in all_repos:
        try:
            # Parse URL to get owner/repo without creating GitHubFetcher instance
            path_parts = url.strip().rstrip("/").split("/")
            if len(path_parts) >= 2:
                owner = path_parts[-2]
                repo = path_parts[-1]
            else:
                # Fallback parsing
                from urllib.parse import urlparse

                path_parts = urlparse(url).path.strip("/").split("/")
                if len(path_parts) >= 2:
                    owner, repo = path_parts[0], path_parts[1]
                else:
                    print(f"[ERROR] Invalid GitHub URL format: {url}")
                    continue

            output_filename = f"{output_dir}/{owner}_{repo}.json"
            if os.path.exists(output_filename):
                debug_print(f"[SKIP] {owner}/{repo} - File already exists", debug)
                skipped_repos.append(
                    {"url": url, "status": "skipped", "reason": "file_exists", "owner": owner, "repo": repo}
                )
            else:
                repos_to_process.append(url)

        except Exception as e:
            print(f"[ERROR] Failed to parse URL {url}: {e}")
            continue

    return repos_to_process, skipped_repos


def process_repository(url, output_dir, token, delay=0, debug=False):
    """Process a single repository with optional delay for rate limiting."""
    try:
        if delay > 0:
            time.sleep(delay)

        # Additional rate limiting for GitHub Actions environment
        # Add small delay between API calls within each repository
        api_delay = 0.2

        fetcher = GitHubFetcher(token, debug)
        owner, repo = fetcher.parse_url(url)

        debug_print(f"[START] Processing {owner}/{repo}", debug)

        # Test API connection first
        test_query = """
        query($owner: String!, $name: String!) {
          repository(owner: $owner, name: $name) {
            name
            stargazerCount
            forkCount
          }
        }
        """

        test_data = fetcher.execute_query(test_query, {"owner": owner, "name": repo})
        if not test_data or not test_data.get("repository"):
            error_msg = f"Cannot access repository {owner}/{repo}"
            print(f"[ERROR] {error_msg}")
            return {"url": url, "status": "error", "reason": error_msg}

        repo_info = test_data["repository"]
        debug_print(
            f"[INFO] {owner}/{repo} - Stars: {repo_info['stargazerCount']}, Forks: {repo_info['forkCount']}", debug
        )

        # Fetch all data with delays between calls for GitHub Actions
        debug_print(f"[FETCH] {owner}/{repo} - Fetching stargazers...", debug)
        stargazers = fetcher.fetch_stargazers(owner, repo)
        time.sleep(api_delay)

        debug_print(f"[FETCH] {owner}/{repo} - Fetching forks...", debug)
        forks = fetcher.fetch_forks(owner, repo)
        time.sleep(api_delay)

        debug_print(f"[FETCH] {owner}/{repo} - Fetching issues...", debug)
        issues = fetcher.fetch_issues(owner, repo)
        time.sleep(api_delay)

        debug_print(f"[FETCH] {owner}/{repo} - Fetching pull requests...", debug)
        pull_requests = fetcher.fetch_pull_requests(owner, repo)

        # Group by date
        stars_by_date = fetcher.group_by_date(stargazers, "starredAt") if stargazers else {}
        forks_by_date = fetcher.group_by_date(forks, "createdAt") if forks else {}
        issues_by_date = fetcher.group_by_date(issues, "createdAt") if issues else {}
        pull_requests_by_date = fetcher.group_by_date(pull_requests, "createdAt") if pull_requests else {}

        # Prepare output data
        total_stars = len(stargazers)
        total_forks = len(forks)
        total_issues = len(issues)
        total_pull_requests = len(pull_requests)

        output_data = {
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_issues": total_issues,
            "total_pull_requests": total_pull_requests,
            "fetched_at": datetime.now().isoformat(),
            "stars_by_date": dict(sorted(stars_by_date.items())),
            "forks_by_date": dict(sorted(forks_by_date.items())),
            "issues_by_date": dict(sorted(issues_by_date.items())),
            "pull_requests_by_date": dict(sorted(pull_requests_by_date.items())),
        }

        # Save data
        output_filename = f"{output_dir}/{owner}_{repo}.json"
        fetcher.save_data(output_data, output_filename)

        debug_print(f"[SUCCESS] {owner}/{repo} - Stars: {total_stars}, Forks: {total_forks}", debug)
        return {
            "url": url,
            "status": "success",
            "total_stars": total_stars,
            "total_forks": total_forks,
            "total_issues": total_issues,
            "total_pull_requests": total_pull_requests,
        }

    except Exception as e:
        error_msg = f"Error processing {url}: {e}"
        print(f"[ERROR] {error_msg}")
        return {"url": url, "status": "error", "reason": str(e)}


def main():
    """Main function to process all repositories."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Batch GitHub Repository Data Fetcher")
    parser.add_argument(
        "--workers", type=int, default=3, help="Number of concurrent workers (CPU cores) to use (default: 3)"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output for detailed processing information")
    args = parser.parse_args()

    # Validate worker count
    if args.workers <= 0:
        print("ERROR: Number of workers must be greater than 0")
        sys.exit(1)

    # Get GitHub token
    token = GitHubFetcher.get_token()
    if not token:
        print("ERROR: GitHub token required")
        sys.exit(1)

    # Load repositories
    try:
        with open("repositories.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("ERROR: repositories.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in repositories.json: {e}")
        sys.exit(1)

    # Collect all repository URLs
    all_repos = []
    for category, urls in data.items():
        print(f"Found category '{category}' with {len(urls)} repositories")
        all_repos.extend(urls)

    print(f"\nTotal repositories found: {len(all_repos)}")

    # Create output directory
    output_dir = "repo_data"
    os.makedirs(output_dir, exist_ok=True)

    # Pre-filter repositories to skip those that already have data files
    print("Pre-filtering repositories to skip existing files...")
    repos_to_process, skipped_repos = filter_repositories(all_repos, output_dir, args.debug)

    print(f"Repositories to process: {len(repos_to_process)}")
    print(f"Repositories already processed (skipped): {len(skipped_repos)}")

    # If no repositories to process, exit early
    if not repos_to_process:
        print("\n✅ All repositories already have data files. Nothing to process!")
        return

    # Process repositories with specified worker count
    # Limit workers to available repositories and specified count
    max_workers = min(args.workers, len(repos_to_process))
    results = []

    # Add skipped repositories to results first
    results.extend(skipped_repos)

    print(f"Starting batch processing with {max_workers} concurrent workers...")

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all jobs with longer delays to respect GitHub API rate limits
        # GitHub GraphQL API allows 5,000 points per hour per token
        future_to_url = {
            executor.submit(process_repository, url, output_dir, token, i * 1.0, args.debug): url
            for i, url in enumerate(repos_to_process)
        }

        # Collect results as they complete
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                results.append(result)

                # Progress indicator (count only the processing jobs, not pre-skipped ones)
                completed_processing = len(results) - len(skipped_repos)
                total_processing = len(repos_to_process)
                print(
                    f"[PROGRESS] {completed_processing}/{total_processing} processed ({completed_processing/total_processing*100:.1f}%)"
                )

            except Exception as e:
                print(f"[ERROR] Unexpected error processing {url}: {e}")
                results.append({"url": url, "status": "error", "reason": str(e)})

    end_time = time.time()

    # Print summary
    print(f"\n{'='*60}")
    print("BATCH PROCESSING SUMMARY")
    print(f"{'='*60}")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"Total repositories: {len(all_repos)}")

    success_count = sum(1 for r in results if r["status"] == "success")
    skip_count = sum(1 for r in results if r["status"] == "skipped")
    error_count = sum(1 for r in results if r["status"] == "error")

    print(f"Successfully processed: {success_count}")
    print(f"Skipped (already exists): {skip_count}")
    print(f"Errors: {error_count}")

    if error_count > 0:
        print(f"\nERROR DETAILS:")
        for result in results:
            if result["status"] == "error":
                print(f"- {result['url']}: {result.get('reason', 'Unknown error')}")

    # Calculate total stats for successful processes
    total_stats = {
        "stars": sum(r.get("total_stars", 0) for r in results if r["status"] == "success"),
        "forks": sum(r.get("total_forks", 0) for r in results if r["status"] == "success"),
        "issues": sum(r.get("total_issues", 0) for r in results if r["status"] == "success"),
        "pull_requests": sum(r.get("total_pull_requests", 0) for r in results if r["status"] == "success"),
    }

    print(f"\nTOTAL STATISTICS:")
    print(f"Total stars collected: {total_stats['stars']:,}")
    print(f"Total forks collected: {total_stats['forks']:,}")
    print(f"Total issues collected: {total_stats['issues']:,}")
    print(f"Total pull requests collected: {total_stats['pull_requests']:,}")

    # Performance summary for GitHub Actions
    avg_time_per_repo = (end_time - start_time) / len(all_repos) if all_repos else 0
    print(f"Average time per repository: {avg_time_per_repo:.2f} seconds")
    print(f"Estimated GitHub Actions minutes used: {(end_time - start_time)/60:.1f} minutes")

    # Exit with error code if any repositories failed
    if error_count > 0:
        print(f"\n❌ {error_count} repositories failed to process")
        sys.exit(1)
    else:
        print(f"\n✅ All repositories processed successfully!")
        print(f"\n📊 Resource usage optimized for GitHub Actions free plan")


if __name__ == "__main__":
    main()
