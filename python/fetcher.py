#!/usr/bin/env python3
"""
Framework Repository Data Fetcher and README Generator

Fetches current repository data (stars, forks, issues, pull requests) from GitHub API,
updates local JSON files, and generates README with current rankings.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import requests


def load_repositories_config(filename: str = "repositories.json") -> List[str]:
    """Load all repository URLs from JSON file and check for existing data files."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not data:
            raise ValueError("Repository configuration is empty")

        # Collect all URLs from all categories
        all_urls = []
        for category, urls in data.items():
            if urls:
                all_urls.extend(urls)

        if not all_urls:
            raise ValueError("No repository URLs found in configuration")

        # Filter URLs to only include those with existing data files
        existing_urls = []
        repo_data_dir = "repo_data"
        
        if not os.path.exists(repo_data_dir):
            raise FileNotFoundError(f"Directory '{repo_data_dir}' not found")
        
        for url in all_urls:
            try:
                repo_path = url.replace("https://github.com/", "")
                owner, repo = repo_path.split("/")
                repo_file = f"{repo_data_dir}/{owner}_{repo}.json"
                
                if os.path.exists(repo_file):
                    existing_urls.append(url)
                else:
                    print(f"Skipping {owner}/{repo}: No data file found at {repo_file}")
            except ValueError:
                print(f"Skipping invalid URL format: {url}")
                continue

        if not existing_urls:
            raise ValueError("No repositories with existing data files found")

        print(f"Found {len(existing_urls)} repositories with existing data files out of {len(all_urls)} total")
        return existing_urls

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in '{filename}': {e}")


def get_github_token() -> Optional[str]:
    """Get GitHub token from environment or file."""
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        return token
    try:
        with open("access_token.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def get_repository_data(owner: str, repo: str, token: Optional[str] = None) -> Optional[Dict]:
    """Get complete repository data from GitHub API."""
    headers = {"User-Agent": "Python-Framework-Tracker"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        # Get basic repository data
        repo_url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()

        # Use GitHub GraphQL API for accurate counts with REST API fallback
        total_pulls = 0
        total_issues = 0
        
        # Get token if not provided
        if not token:
            token = get_github_token()
        
        if token and len(token.strip()) > 0:
            try:
                # Primary: Use GraphQL API for accurate counts
                graphql_url = "https://api.github.com/graphql"
                query = f"""{{
                    repository(owner: "{owner}", name: "{repo}") {{
                        issues(states: [OPEN, CLOSED]) {{
                            totalCount
                        }}
                        pullRequests(states: [OPEN, CLOSED, MERGED]) {{
                            totalCount
                        }}
                    }}
                }}"""
                
                graphql_response = requests.post(
                    graphql_url,
                    json={"query": query},
                    headers=headers
                )
                graphql_response.raise_for_status()
                response_data = graphql_response.json()
                
                # Check for GraphQL errors
                if "errors" in response_data:
                    raise requests.exceptions.RequestException(f"GraphQL error: {response_data['errors']}")
                
                data = response_data.get("data", {}).get("repository", {})
                total_issues = data.get("issues", {}).get("totalCount", 0)
                total_pulls = data.get("pullRequests", {}).get("totalCount", 0)
                
            except requests.exceptions.RequestException:
                # Fallback: Use Search API
                try:
                    search_prs_url = f"https://api.github.com/search/issues?q=repo:{owner}/{repo}+type:pr"
                    prs_response = requests.get(search_prs_url, headers=headers)
                    prs_response.raise_for_status()
                    total_pulls = prs_response.json().get("total_count", 0)

                    search_issues_url = f"https://api.github.com/search/issues?q=repo:{owner}/{repo}+type:issue"
                    issues_response = requests.get(search_issues_url, headers=headers)
                    issues_response.raise_for_status()
                    total_issues = issues_response.json().get("total_count", 0)
                    
                except requests.exceptions.RequestException:
                    # Final fallback: use repository data (only open issues, no PRs)
                    total_issues = max(0, repo_data.get("open_issues_count", 0))
                    total_pulls = 0
        else:
            # No token available, use basic repo data (only open issues)
            total_issues = max(0, repo_data.get("open_issues_count", 0))
            total_pulls = 0

        return {
            "name": repo,
            "html_url": repo_data.get("html_url", ""),
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "open_issues": repo_data.get("open_issues_count", 0),
            "total_issues": total_issues,
            "total_pull_requests": total_pulls,
            "last_commit": repo_data.get("pushed_at", ""),
            "fetched_at": datetime.now().isoformat(),
        }

    except requests.exceptions.RequestException as e:
        print(f"Warning: Failed to fetch data for {owner}/{repo}: {e}")
        return None


def update_repo_data_file(owner: str, repo: str, current_data: Dict) -> None:
    """Update repository data file with current differences in stars, forks, issues, and pull requests."""
    repo_file = f"repo_data/{owner}_{repo}.json"
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(repo_file):
        print(f"Skipping {owner}/{repo}: No existing data file")
        return

    try:
        # Load existing data
        with open(repo_file, "r", encoding="utf-8") as f:
            repo_data = json.load(f)

        # Calculate differences
        previous_stars = repo_data.get("total_stars", 0)
        previous_forks = repo_data.get("total_forks", 0)
        previous_issues = repo_data.get("total_issues", 0)
        previous_prs = repo_data.get("total_pull_requests", 0)

        current_stars = current_data["stars"]
        current_forks = current_data["forks"]
        current_issues = current_data["total_issues"]
        current_prs = current_data["total_pull_requests"]

        star_diff = current_stars - previous_stars
        fork_diff = current_forks - previous_forks
        issue_diff = current_issues - previous_issues
        pr_diff = current_prs - previous_prs

        # Track if any changes occurred
        has_changes = False

        # Update data if there are differences
        if star_diff != 0:
            if "stars_by_date" not in repo_data:
                repo_data["stars_by_date"] = {}
            repo_data["stars_by_date"][today] = star_diff
            repo_data["total_stars"] = current_stars
            has_changes = True

        if fork_diff != 0:
            if "forks_by_date" not in repo_data:
                repo_data["forks_by_date"] = {}
            repo_data["forks_by_date"][today] = fork_diff
            repo_data["total_forks"] = current_forks
            has_changes = True

        if issue_diff != 0:
            if "issues_by_date" not in repo_data:
                repo_data["issues_by_date"] = {}
            repo_data["issues_by_date"][today] = issue_diff
            repo_data["total_issues"] = current_issues
            has_changes = True

        if pr_diff != 0:
            if "pull_requests_by_date" not in repo_data:
                repo_data["pull_requests_by_date"] = {}
            repo_data["pull_requests_by_date"][today] = pr_diff
            repo_data["total_pull_requests"] = current_prs
            has_changes = True

        if has_changes:
            repo_data["fetched_at"] = current_data["fetched_at"]

            # Save updated data
            with open(repo_file, "w", encoding="utf-8") as f:
                json.dump(repo_data, f, ensure_ascii=False, separators=(",", ":"))

            changes = []
            if star_diff != 0:
                changes.append(f"stars: {previous_stars} -> {current_stars} ({star_diff:+d})")
            if fork_diff != 0:
                changes.append(f"forks: {previous_forks} -> {current_forks} ({fork_diff:+d})")
            if issue_diff != 0:
                changes.append(f"issues: {previous_issues} -> {current_issues} ({issue_diff:+d})")
            if pr_diff != 0:
                changes.append(f"PRs: {previous_prs} -> {current_prs} ({pr_diff:+d})")

            print(f"Updated {owner}/{repo}: {', '.join(changes)}")
        else:
            print(
                f"No changes for {owner}/{repo}: {current_stars} stars, {current_forks} forks, {current_issues} issues, {current_prs} PRs"
            )

    except Exception as e:
        print(f"Failed to update {owner}/{repo}: {e}")


def fetch_all_repository_data(repo_urls: List[str]) -> List[Dict]:
    """Fetch current data for all repositories and update local files."""
    token = get_github_token()
    if not token:
        print("Warning: No GitHub token found. API rate limits may apply.")

    all_repo_data = []

    for url in repo_urls:
        try:
            # Extract owner and repo name from URL
            repo_path = url.replace("https://github.com/", "")
            owner, repo = repo_path.split("/")

            print(f"Fetching data for {owner}/{repo}...")

            # Get current repository data from GitHub API
            current_data = get_repository_data(owner, repo, token)
            if not current_data:
                continue

            # Update local repo data file with star differences
            update_repo_data_file(owner, repo, current_data)

            # Add to results for README generation
            all_repo_data.append(current_data)

        except Exception as e:
            print(f"Failed to process {url}: {e}")
            continue

    return all_repo_data


def generate_readme(repo_data: List[Dict], output_file: str = "README.md") -> None:
    """Generate README.md file from repository data."""
    # Sort by stars (descending)
    repo_data.sort(key=lambda x: x["stars"], reverse=True)

    # Generic title for all repositories
    title = "Public Repository History - All Categories"

    header = f"""# {title}
A list of popular github projects from all categories (ranked by stars automatically)

## 📈 Current Rankings

"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("| Project Name | Stars | Forks | Total Issues | Total PRs | Open Issues | Last Commit |\n")
        f.write("| ------------ | ----- | ----- | ------------ | --------- | ----------- | ----------- |\n")

        for project in repo_data:
            # Format last commit date
            if project["last_commit"]:
                try:
                    commit_date = datetime.fromisoformat(project["last_commit"].replace("Z", "+00:00")).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                except (ValueError, TypeError):
                    commit_date = "N/A"
            else:
                commit_date = "N/A"

            f.write(
                f"| [{project['name']}]({project['html_url']}) | "
                f"{project['stars']} | "
                f"{project['forks']} | "
                f"{project.get('total_issues', 'N/A')} | "
                f"{project.get('total_pull_requests', 'N/A')} | "
                f"{project['open_issues']} | "
                f"{commit_date} |\n"
            )

        # Add footer
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f"\n*Last Automatic Update: {timestamp}*\n")
        f.write("\n*Inspired by https://github.com/mingrammer/python-web-framework-stars*\n")

    print(f"Generated {output_file} with {len(repo_data)} projects")


def main():
    """Main execution function."""
    try:
        # Load repository configuration for all categories with existing data files
        repo_urls = load_repositories_config()

        # Fetch current data for all repositories
        print("Fetching current repository data from GitHub...")
        repo_data = fetch_all_repository_data(repo_urls)

        if not repo_data:
            print("No repository data fetched. Exiting.")
            return

        # Generate README
        print("Generating README...")
        generate_readme(repo_data)

        print("All tasks completed successfully!")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
