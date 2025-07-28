#!/usr/bin/env python3
"""
Repository History Generator from Daily Data

This script reads individual repository JSON files from repo_data directory
and generates a repository_histories.json file with cumulative stars/forks by date.
"""

import json
from datetime import datetime
from pathlib import Path


def parse_filename_to_repo_info(filename):
    """Parse filename like 'django_django.json' to extract owner and repo."""
    base_name = filename.replace('.json', '')
    parts = base_name.split('_')
    if len(parts) >= 2:
        # Handle cases like 'aio-libs_aiohttp' or 'django_django'
        owner = parts[0]
        repo = '_'.join(parts[1:])
        return owner, repo
    return None, None


def calculate_cumulative_data(daily_data):
    """Convert daily star/fork counts to cumulative totals."""
    cumulative = {}
    running_total = 0
    
    # Sort dates to ensure chronological order
    for date in sorted(daily_data.keys()):
        running_total += daily_data[date]
        cumulative[date] = running_total
    
    return cumulative


def process_repository_file(file_path):
    """Process a single repository JSON file and extract cumulative data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract basic info
        total_stars = data.get('total_stars', 0)
        total_forks = data.get('total_forks', 0)
        fetched_at = data.get('fetched_at', datetime.now().isoformat())
        
        # Get daily data
        stars_by_date = data.get('stars_by_date', {})
        forks_by_date = data.get('forks_by_date', {})
        
        # Calculate cumulative data
        cumulative_stars = calculate_cumulative_data(stars_by_date)
        cumulative_forks = calculate_cumulative_data(forks_by_date)
        
        return {
            'total_stars': total_stars,
            'total_forks': total_forks,
            'fetched_at': fetched_at,
            'cumulative_stars': cumulative_stars,
            'cumulative_forks': cumulative_forks
        }
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def generate_github_url(owner, repo):
    """Generate GitHub URL from owner and repo."""
    return f"https://github.com/{owner}/{repo}"


def create_history_entries_from_cumulative(cumulative_stars, cumulative_forks):
    """Create history entries with date-by-date cumulative data."""
    history = []
    
    # Get all unique dates from both stars and forks
    all_dates = set(cumulative_stars.keys()) | set(cumulative_forks.keys())
    
    for date in sorted(all_dates):
        stars = cumulative_stars.get(date, 0)
        forks = cumulative_forks.get(date, 0)
        
        history.append({
            'timestamp': date,  # Use date as-is (yyyy-MM-dd format)
            'stars': stars,
            'forks': forks
        })
    
    return history


def main():
    """Main function to process all repository files and generate history."""
    repo_data_dir = Path('../repo_data')
    
    if not repo_data_dir.exists():
        print("Error: repo_data directory not found")
        return
    
    # Find all JSON files
    json_files = list(repo_data_dir.glob('*.json'))
    
    if not json_files:
        print("No JSON files found in repo_data directory")
        return
    
    print(f"Processing {len(json_files)} repository files...")
    
    # Initialize history structure
    history_data = {
        'metadata': {
            'first_recorded': None,
            'last_updated': datetime.now().isoformat() + 'Z',
            'total_snapshots': 0
        },
        'projects': {}
    }
    
    earliest_date = None
    total_snapshots = 0
    
    for json_file in sorted(json_files):
        print(f"Processing: {json_file.name}")
        
        # Parse filename to get owner and repo
        owner, repo = parse_filename_to_repo_info(json_file.name)
        if not owner or not repo:
            print(f"  ⚠️  Could not parse filename: {json_file.name}")
            continue
        
        # Process the file
        repo_data = process_repository_file(json_file)
        if not repo_data:
            print(f"  ❌ Failed to process")
            continue
        
        # Create project entry
        project_name = repo
        github_url = generate_github_url(owner, repo)
        
        # Create history entries from cumulative data
        history_entries = create_history_entries_from_cumulative(
            repo_data['cumulative_stars'],
            repo_data['cumulative_forks']
        )
        
        history_data['projects'][project_name] = {
            'name': project_name,
            'html_url': github_url,
            'history': history_entries
        }
        
        # Update metadata
        if history_entries:
            first_entry_date = history_entries[0]['timestamp']
            if earliest_date is None or first_entry_date < earliest_date:
                earliest_date = first_entry_date
            
            total_snapshots += len(history_entries)
        
        print(f"  ✅ Created {len(history_entries)} history entries")
    
    # Update metadata
    history_data['metadata']['first_recorded'] = earliest_date
    history_data['metadata']['total_snapshots'] = total_snapshots
    
    # Save the history file
    output_file = '../repository_histories.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(history_data, f, ensure_ascii=False, separators=(',', ':'))
    
    # Print summary
    print(f"\n📊 Generated {output_file}")
    print(f"Total projects: {len(history_data['projects'])}")
    print(f"Total snapshots: {total_snapshots}")
    print(f"First recorded: {earliest_date}")
    print(f"Last updated: {history_data['metadata']['last_updated']}")
    
    # Show top projects by latest stars
    print(f"\n🌟 Top projects by stars:")
    projects_by_stars = []
    for name, project in history_data['projects'].items():
        if project['history']:
            latest_stars = project['history'][-1]['stars']
            projects_by_stars.append((name, latest_stars))
    
    projects_by_stars.sort(key=lambda x: x[1], reverse=True)
    for i, (name, stars) in enumerate(projects_by_stars[:10], 1):
        print(f"  {i:2d}. {name}: {stars:,} stars")


if __name__ == "__main__":
    main()