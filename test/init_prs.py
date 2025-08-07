#!/usr/bin/env python3
"""
GitHub Pull Requests Data Fetcher using GraphQL

Fetches pull requests data from GitHub GraphQL API to avoid REST API pagination limits
and outputs data grouped by date.
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


class GitHubPRsFetcher:
    def __init__(self, token=None):
        self.token = token
        self.headers = {
            "User-Agent": "Python-GraphQL-PRs-Fetcher",
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
            response = requests.post(self.graphql_url, headers=self.headers, json=payload, verify=False)
            response.raise_for_status()

            result = response.json()
            if "errors" in result:
                print(f"GraphQL errors: {result['errors']}")
                return None

            return result.get("data")
        except requests.exceptions.RequestException as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_pull_requests(self, owner, repo):
        """Fetch all pull requests using GraphQL pagination."""
        query = """
        query($owner: String!, $name: String!, $cursor: String) {
          repository(owner: $owner, name: $name) {
            pullRequests(first: 100, after: $cursor, orderBy: {field: CREATED_AT, direction: ASC}) {
              pageInfo { hasNextPage endCursor }
              edges { 
                node { 
                  createdAt
                  state
                  closedAt
                  mergedAt
                }
              }
            }
          }
        }
        """

        pull_requests = []
        cursor = None
        page = 1

        while True:
            data = self.execute_query(query, {"owner": owner, "name": repo, "cursor": cursor})

            if not data or not data.get("repository"):
                break

            edges = data["repository"]["pullRequests"]["edges"]
            if not edges:
                break

            pull_requests.extend(edges)
            print(f"Fetched page {page}, total pull requests: {len(pull_requests)}")

            page_info = data["repository"]["pullRequests"]["pageInfo"]
            if not page_info.get("hasNextPage"):
                break

            cursor = page_info.get("endCursor")
            page += 1

        return pull_requests

    @staticmethod
    def group_by_date(items, date_field):
        """Group items by date."""
        grouped = defaultdict(int)
        for item in items:
            if date_field == "createdAt":
                date_str = item.get("node", {}).get("createdAt")
            else:
                continue

            if date_str:
                date_obj = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                date_key = date_obj.strftime("%Y-%m-%d")
                grouped[date_key] += 1
        return dict(grouped)

    def save_data(self, data, owner, repo):
        """Save data to JSON file."""
        os.makedirs("test/output", exist_ok=True)
        filename = f"test/output/{owner}_{repo}_prs.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

        print(f"Pull requests data saved to {filename}")
        return filename


def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub repository pull requests data using GraphQL")
    parser.add_argument("url", help="GitHub repository URL")
    args = parser.parse_args()

    try:
        token = GitHubPRsFetcher.get_token()
        if not token:
            sys.exit(1)

        fetcher = GitHubPRsFetcher(token)
        owner, repo = fetcher.parse_url(args.url)

        print(f"Fetching pull requests data for {owner}/{repo} using GraphQL...")

        # Test API connection first
        test_query = """
        query($owner: String!, $name: String!) {
          repository(owner: $owner, name: $name) {
            name
            pullRequests(states: [OPEN, CLOSED, MERGED]) {
              totalCount
            }
          }
        }
        """

        test_data = fetcher.execute_query(test_query, {"owner": owner, "name": repo})
        if not test_data or not test_data.get("repository"):
            print(
                f"ERROR: Cannot access repository {owner}/{repo}. Check if repository exists and token has correct permissions."
            )
            sys.exit(1)

        repo_info = test_data["repository"]
        print(f"Repository found: {repo_info['name']}")
        print(f"Total pull requests: {repo_info['pullRequests']['totalCount']}")

        # Fetch data
        print("\n=== Fetching Pull Requests ===")
        pull_requests = fetcher.fetch_pull_requests(owner, repo)

        # Group by date
        pull_requests_by_date = fetcher.group_by_date(pull_requests, "createdAt")

        # Prepare output data
        total_pull_requests = len(pull_requests)

        output_data = {
            "total_pull_requests": total_pull_requests,
            "fetched_at": datetime.now().isoformat(),
            "pull_requests_by_date": dict(sorted(pull_requests_by_date.items())),
        }

        # Save data
        fetcher.save_data(output_data, owner, repo)

        # Print summary
        print(f"Total pull requests fetched: {total_pull_requests}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
