# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python tool that automatically tracks and ranks popular Python web frameworks on GitHub by star count. It generates a README.md with a ranked table and maintains historical JSON data for trend analysis.

## Core Architecture

**Main Component**: `ReadmeGenerator` class in `get_current_framework_stars.py`
- Fetches GitHub repository data via API
- Generates markdown table sorted by stars
- Maintains time-series data in `framework_stars_history.json`
- Handles authentication via `GITHUB_TOKEN` env var or `access_token.txt` file

**Key Files**:
- `list.txt` - Contains GitHub repository URLs to track (22 frameworks)
- `README.md` - Auto-generated output with current rankings
- `framework_stars_history.json` - Time-series data for graphing (auto-generated)

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

**Run the main script**:
```bash
uv run get_current_framework_stars.py
```

**Add new framework to track**:
```bash
echo "https://github.com/owner/repo" >> list.txt
```

## Dependencies & Requirements

- **Python**: 3.12+ (specified in `.python-version`)
- **Package Manager**: UV (modern Python package manager)
- **Required**: `requests>=2.32.4` for GitHub API calls
- **Authentication**: GitHub personal access token required

## Automation

**GitHub Actions**: `.github/workflows/update-readme.yml`
- Runs weekly on Sundays at 00:00 UTC
- Can be triggered manually
- Only updates if last update was >1 week ago
- Auto-commits changes with timestamp

## Data Structure

**Historical JSON Format**:
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
      "history": [
        {
          "timestamp": "ISO8601",
          "stars": number,
          "forks": number,
          "open_issues": number,
          "last_commit": "ISO8601"
        }
      ]
    }
  }
}
```

## Common Issues

- **ModuleNotFoundError**: Run `uv sync` to install dependencies
- **GitHub API Rate Limits**: Ensure `GITHUB_TOKEN` is set with valid token
- **File Not Found**: `list.txt` must exist with repository URLs
- No formal test suite exists - this is primarily a data collection tool