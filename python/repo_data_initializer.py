#!/usr/bin/env python3
"""
GitHub Repository Data Fetcher using GraphQL

Fetches stargazers and forks data from GitHub GraphQL API to avoid
REST API pagination limits and outputs data grouped by date.
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from datetime import datetime
from urllib.parse import urlparse

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class GitHubFetcher:
    def __init__(self, token=None):
        self.token = token
        self.headers = {
            "User-Agent": "Python-GraphQL-Fetcher",
            "Content-Type": "application/json",
        }
        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"
        self.graphql_url = "https://api.github.com/graphql"

    @staticmethod
    def get_token():
        """Get GitHub token from environment or file."""
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            return token
        try:
            with open("access_token.txt", "r") as f:
                return f.read().strip()
        except FileNotFoundError:
            print("Error: GitHub token required for GraphQL API access.")
            return None

    @staticmethod
    def parse_url(url):
        """Parse GitHub URL to extract owner and repo."""
        path_parts = urlparse(url).path.strip("/").split("/")
        if len(path_parts) >= 2:
            return path_parts[0], path_parts[1]
        raise ValueError(f"Invalid GitHub URL format: {url}")

    def execute_query(self, query, variables=None):
        """Execute a GraphQL query."""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        try:
            response = requests.post(
                self.graphql_url,
                headers=self.headers,
                json=payload,
                verify=False
            )
            response.raise_for_status()
            
            result = response.json()
            if "errors" in result:
                print(f"GraphQL errors: {result['errors']}")
                return None
            
            return result.get("data")
        except requests.exceptions.RequestException as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_stargazers(self, owner, repo):
        """Fetch all stargazers using GraphQL pagination."""
        query = """
        query($owner: String!, $name: String!, $cursor: String) {
          repository(owner: $owner, name: $name) {
            stargazers(first: 100, after: $cursor, orderBy: {field: STARRED_AT, direction: ASC}) {
              pageInfo { hasNextPage endCursor }
              edges { starredAt }
            }
          }
        }
        """
        
        stargazers = []
        cursor = None
        page = 1
        
        while True:
            data = self.execute_query(query, {
                "owner": owner, "name": repo, "cursor": cursor
            })
            
            if not data or not data.get("repository"):
                break
            
            edges = data["repository"]["stargazers"]["edges"]
            if not edges:
                break
            
            stargazers.extend(edges)
            print(f"Fetched page {page}, total stargazers: {len(stargazers)}")
            
            page_info = data["repository"]["stargazers"]["pageInfo"]
            if not page_info.get("hasNextPage"):
                break
            
            cursor = page_info.get("endCursor")
            page += 1
        
        return stargazers

    def fetch_forks(self, owner, repo):
        """Fetch all forks using GraphQL pagination."""
        query = """
        query($owner: String!, $name: String!, $cursor: String) {
          repository(owner: $owner, name: $name) {
            forks(first: 100, after: $cursor, orderBy: {field: CREATED_AT, direction: ASC}) {
              pageInfo { hasNextPage endCursor }
              edges { node { createdAt } }
            }
          }
        }
        """
        
        forks = []
        cursor = None
        page = 1
        
        while True:
            data = self.execute_query(query, {
                "owner": owner, "name": repo, "cursor": cursor
            })
            
            if not data or not data.get("repository"):
                break
            
            edges = data["repository"]["forks"]["edges"]
            if not edges:
                break
            
            forks.extend(edges)
            print(f"Fetched page {page}, total forks: {len(forks)}")
            
            page_info = data["repository"]["forks"]["pageInfo"]
            if not page_info.get("hasNextPage"):
                break
            
            cursor = page_info.get("endCursor")
            page += 1
        
        return forks

    @staticmethod
    def group_by_date(items, date_field):
        """Group items by date."""
        grouped = defaultdict(int)
        for item in items:
            if date_field == "starredAt":
                date_str = item.get("starredAt")
            else:
                date_str = item.get("node", {}).get("createdAt")
            
            if date_str:
                date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                date_key = date_obj.strftime("%Y-%m-%d")
                grouped[date_key] += 1
        return dict(grouped)

    @staticmethod
    def save_data(data, filename):
        """Save data to compact JSON file."""
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repository data using GraphQL")
    parser.add_argument("repo_url", help="GitHub repository URL")
    parser.add_argument("--output-dir", default="repo_data", help="Output directory")

    args = parser.parse_args()

    try:
        token = GitHubFetcher.get_token()
        if not token:
            sys.exit(1)
        
        fetcher = GitHubFetcher(token)
        owner, repo = fetcher.parse_url(args.repo_url)

        print(f"Fetching data for {owner}/{repo} using GraphQL...")

        # Fetch data
        print("\n=== Fetching Stargazers ===")
        stargazers = fetcher.fetch_stargazers(owner, repo)

        print("\n=== Fetching Forks ===")
        forks = fetcher.fetch_forks(owner, repo)

        # Group by date
        stars_by_date = fetcher.group_by_date(stargazers, "starredAt")
        forks_by_date = fetcher.group_by_date(forks, "createdAt")

        # Prepare output data
        total_stars = len(stargazers)
        total_forks = len(forks)
        
        output_data = {
            "total_stars": total_stars,
            "fetched_at": datetime.now().isoformat(),
            "per_page": 100,
            "last_stargazers_page": (total_stars + 99) // 100,
            "last_forks_page": (total_forks + 99) // 100,
            "stars_by_date": dict(sorted(stars_by_date.items())),
            "forks_by_date": dict(sorted(forks_by_date.items())),
        }

        # Save data
        output_filename = f"{args.output_dir}/{owner}_{repo}.json"
        fetcher.save_data(output_data, output_filename)

        # Print summary
        print(f"\nData saved to {output_filename}")
        print(f"Total stars fetched: {total_stars}")
        print(f"Total forks fetched: {total_forks}")
        print(f"Equivalent pages - Stars: {output_data['last_stargazers_page']}, Forks: {output_data['last_forks_page']}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()