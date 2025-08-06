#!/usr/bin/env python3

import os
import sys
import requests
from datetime import datetime, timezone, timedelta


def get_github_token():
    """Get GitHub token from environment or file."""
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        return token
    
    try:
        with open('access_token.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def check_rate_limit():
    """Check GitHub API rate limit status."""
    token = get_github_token()
    if not token:
        print("Error: GitHub token not found. Set GITHUB_TOKEN environment variable or create access_token.txt file.")
        sys.exit(1)
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    try:
        response = requests.get('https://api.github.com/rate_limit', headers=headers)
        response.raise_for_status()
        
        data = response.json()
        
        print("GitHub API Rate Limit Status")
        print("=" * 40)
        
        for api_type, limits in data['resources'].items():
            remaining = limits['remaining']
            limit = limits['limit']
            reset_timestamp = limits['reset']
            reset_time = datetime.fromtimestamp(reset_timestamp, tz=timezone.utc)
            kst_time = reset_time.astimezone(timezone(timedelta(hours=9)))
            
            print(f"\n{api_type.upper()} API:")
            print(f"  Remaining: {remaining:,}/{limit:,}")
            print(f"  Used: {limit - remaining:,}")
            print(f"  Reset at: {kst_time.strftime('%Y-%m-%d %H:%M:%S KST')}")
            
            if remaining == 0:
                print(f"  Status: ❌ EXHAUSTED")
            elif remaining < limit * 0.1:
                print(f"  Status: ⚠️  LOW ({remaining/limit*100:.1f}%)")
            else:
                print(f"  Status: ✅ OK ({remaining/limit*100:.1f}%)")
        
    except requests.exceptions.RequestException as e:
        print(f"Error checking rate limit: {e}")
        sys.exit(1)


if __name__ == '__main__':
    check_rate_limit()