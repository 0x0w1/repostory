#!/usr/bin/env python3
"""
Framework Stars Fetcher and README Generator

Fetches current repository data from GitHub API, updates local JSON files,
and generates README with current rankings.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

import requests


def load_repositories_config(filename: str = "repositories.json") -> Tuple[str, List[str]]:
    """Load repository configuration from JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Get the first key as category name and its URLs
        if not data:
            raise ValueError("Repository configuration is empty")

        category = list(data.keys())[0]
        urls = data[category]

        if not urls:
            raise ValueError(f"Repository list for '{category}' is empty")

        return category, urls

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
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"User-Agent": "Python-Framework-Tracker"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        return {
            "name": repo,
            "html_url": data.get("html_url", ""),
            "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0),
            "open_issues": data.get("open_issues_count", 0),
            "last_commit": data.get("pushed_at", ""),
            "fetched_at": datetime.now().isoformat(),
        }

    except requests.exceptions.RequestException as e:
        print(f"Warning: Failed to fetch data for {owner}/{repo}: {e}")
        return None


def update_repo_data_file(owner: str, repo: str, current_data: Dict) -> None:
    """Update repository data file with current stars difference."""
    repo_file = f"repo_data/{owner}_{repo}.json"
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(repo_file):
        print(f"Skipping {owner}/{repo}: No existing data file")
        return

    try:
        # Load existing data
        with open(repo_file, "r", encoding="utf-8") as f:
            repo_data = json.load(f)

        # Calculate star difference
        previous_stars = repo_data.get("total_stars", 0)
        current_stars = current_data["stars"]
        star_diff = current_stars - previous_stars

        # Update stars_by_date if there's a difference
        if star_diff != 0:
            if "stars_by_date" not in repo_data:
                repo_data["stars_by_date"] = {}

            repo_data["stars_by_date"][today] = star_diff
            repo_data["total_stars"] = current_stars
            repo_data["fetched_at"] = current_data["fetched_at"]

            # Save updated data
            with open(repo_file, "w", encoding="utf-8") as f:
                json.dump(repo_data, f, ensure_ascii=False, separators=(",", ":"))

            print(f"Updated {owner}/{repo}: {previous_stars} -> {current_stars} (+{star_diff})")
        else:
            print(f"No change for {owner}/{repo}: {current_stars} stars")

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


def generate_readme(category: str, repo_data: List[Dict], output_file: str = "README.md") -> None:
    """Generate README.md file from repository data."""
    # Sort by stars (descending)
    repo_data.sort(key=lambda x: x["stars"], reverse=True)

    # Format category name for title
    title = f"Public Repository History - {category.replace('-', ' ').title()}"

    header = f"""# {title}
A list of popular github projects related to {category.replace('-', ' ')} (ranked by stars automatically)

## 📈 Current Rankings

"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("| Project Name | Stars | Forks | Open Issues | Last Commit |\n")
        f.write("| ------------ | ----- | ----- | ----------- | ----------- |\n")

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
        # Load repository configuration
        category, repo_urls = load_repositories_config()
        print(f"Loaded {len(repo_urls)} repository URLs for category: {category}")

        # Fetch current data for all repositories
        print("Fetching current repository data from GitHub...")
        repo_data = fetch_all_repository_data(repo_urls)

        if not repo_data:
            print("No repository data fetched. Exiting.")
            return

        # Generate README
        print("Generating README...")
        generate_readme(category, repo_data)

        print("All tasks completed successfully!")

    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
