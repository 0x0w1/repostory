# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python tool that automatically tracks and ranks popular Python web frameworks on GitHub by star count. It generates a README.md with a ranked table and maintains historical JSON data for trend analysis.

## Core Architecture

**Data Pipeline**: The project follows a 3-stage data processing pipeline:

1. **Data Collection** - Uses GitHub GraphQL API to fetch stargazers/forks data, avoiding REST API pagination limits. Outputs individual JSON files per repository in `repo_data/`.
   - `repo_data_initializer.py` - Single repository processing
   - `batch_repo_initializer.py` - Batch processing with configurable worker threads (default: 3 CPUs)

2. **Data Processing** (`generate_history_from_repo_data.py`) - Converts daily counts to cumulative totals and generates `repository_histories.json` with comprehensive time-series data.

3. **Output Generation** (`fetcher.py`) - Aggregates history data, generates markdown table sorted by stars, and updates README.md.

**Key Files**:

- `repositories.json` - Contains GitHub repository URLs to track (22 frameworks) in JSON format
- `repo_data/` - Individual JSON files per repository with daily star/fork counts
- `repository_histories.json` - Aggregated time-series data for all frameworks
- `README.md` - Auto-generated output with current rankings

## Development Commands

**Setup**:

```bash
# Install UV package manager (required)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Set GitHub token (required for API access)
export GITHUB_TOKEN="your_token_here"
# OR create access_token.txt file locally
```

**Core Operations**:

```bash
# Fetch data for a single repository
uv run python/repo_data_initializer.py https://github.com/django/django

# Batch process all repositories (with default 3 workers)
uv run python/batch_repo_initializer.py

# Batch process with custom worker count
uv run python/batch_repo_initializer.py --workers 8

# Generate aggregated history from repo data
uv run python/generate_history_from_repo_data.py

# Generate README from aggregated data
uv run python/fetcher.py

# Add new framework to track (edit repositories.json)
# Add URL to the "repostory" array in repositories.json
```

## Dependencies & Requirements

- **Python**: 3.12+ (specified in `.python-version` and `pyproject.toml`)
- **Package Manager**: UV (modern Python package manager)
- **Required**: `requests>=2.32.4` for GitHub API calls, `matplotlib>=3.7.0` for charts
- **Authentication**: GitHub personal access token required

## Data Structure

**Repository Data Format** (`repo_data/*.json`):

```json
{
  "total_stars": 84378,
  "fetched_at": "2025-07-28T23:40:55.409192",
  "stars_by_date": { "2012-04-28": 3772, "2012-04-29": 4 },
  "forks_by_date": { "2012-04-28": 145, "2012-04-29": 2 }
}
```

**Aggregated History Format** (`repository_histories.json`):

```json
{
  "metadata": {
    "first_recorded": "timestamp",
    "last_updated": "timestamp",
    "total_snapshots": number
  },
  "projects": {
    "framework_name": {
      "name": "string",
      "html_url": "string",
      "history": [{"timestamp": "ISO8601", "stars": number, "forks": number}]
    }
  }
}
```

## Automation

**GitHub Actions**:

- `.github/workflows/update-repository-stars.yml` - Daily updates at 00:00 UTC
- `.github/workflows/update-manually.yml` - Manual trigger support
- Both auto-commit changes with timestamps

## Common Issues

- **ModuleNotFoundError**: Run `uv sync` to install dependencies
- **GitHub API Rate Limits**: Ensure `GITHUB_TOKEN` is set with valid token
- **File Not Found**: `repositories.json` must exist with repository URLs
- **Missing Charts**: Workflows expect `charts/` directory with generated chart images
- No formal test suite exists - this is primarily a data collection tool
