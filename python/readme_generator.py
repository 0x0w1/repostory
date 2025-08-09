#!/usr/bin/env python3
"""
README generation module for the repository tracker.

Handles generation of English and Korean README files with data collection capability.
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Optional

import requests


def generate_readme_english(repo_data: List[Dict], output_file: str = "README.md") -> None:
    """Generate English README.md file from repository data."""
    # Sort by stars (descending)
    repo_data.sort(key=lambda x: x["stars"], reverse=True)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    header = """# Python Repository Trends Tracker

A tool that automatically tracks and ranks popular Python projects on GitHub by star count, fork count, and issue count.

## 🚀 Demo

Visit the [demo page](https://0x10.kr) to see real-time rankings and charts.

## 📊 Project Overview

This tool monitors various categories of Python projects and provides the following features:

- **Automatic Data Collection**: Uses GitHub GraphQL API to collect accurate star, fork, issue, and PR counts
- **History Tracking**: Tracks daily changes for trend analysis over time
- **Real-time Updates**: Automated daily updates via GitHub Actions
- **Multiple Categories**: Includes web frameworks, machine learning, data science, Python implementations, and more

## 🎯 Tracked Categories

- **Web Frameworks**: Django, Flask, FastAPI, Tornado, etc.
- **Machine Learning/AI**: TensorFlow, PyTorch, scikit-learn, Keras, etc.
- **Data Science**: Pandas, NumPy, SciPy, Matplotlib, etc.
- **Async Programming**: asyncio, trio, anyio, etc.
- **Python Implementations**: CPython, PyPy, Jython, MicroPython, etc.

## 🛠️ Scripts Documentation

### Core Scripts

- **`fetcher.py`** - Main data collection and README generation script
  - Fetches repository data from GitHub API
  - Updates local JSON data files with daily changes
  - Generates both English and Korean README files
  - Uses GraphQL API for accurate issue/PR counts

- **`readme_generator.py`** - Standalone README generation utility
  - Loads data from existing local JSON files
  - Optionally updates with current GitHub data
  - Generates README files without full data collection
  - Lightweight alternative for quick README updates

- **`repo_data_initializer.py`** - Single repository data collector
  - Initializes data for a single GitHub repository
  - Fetches historical stargazer data using GraphQL
  - Creates initial JSON data file in repo_data/ directory

- **`batch_repo_initializer.py`** - Batch repository processor
  - Processes multiple repositories in parallel
  - Configurable worker threads (default: 3 CPUs)
  - Ideal for initial data collection of all repositories

- **`generate_history_from_repo_data.py`** - History aggregator
  - Converts daily repository data into cumulative totals
  - Generates repository_histories.json for trend analysis
  - Processes all repo_data/*.json files

### Usage Examples

```bash
# Full data collection and README generation
uv run python/fetcher.py

# Quick README update only
uv run python/readme_generator.py

# Initialize single repository
uv run python/repo_data_initializer.py https://github.com/owner/repo

# Process all repositories in batch
uv run python/batch_repo_initializer.py --workers 8

# Generate history aggregation
uv run python/generate_history_from_repo_data.py
```

| Project Name | Stars | Forks | Total Issues | Total PRs | Open Issues | Last Commit |
| ------------ | ----- | ----- | ------------ | --------- | ----------- | ----------- |
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header)

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
        f.write(f"\n*Last Automatic Update: {timestamp}*\n")
        f.write("\n*Inspired by https://github.com/mingrammer/python-web-framework-stars*\n")

    print(f"Generated English {output_file} with {len(repo_data)} projects")


def generate_readme_korean(repo_data: List[Dict], output_file: str = "README-KR.md") -> None:
    """Generate Korean README-KR.md file from repository data."""
    # Sort by stars (descending)
    repo_data.sort(key=lambda x: x["stars"], reverse=True)

    timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    header = """# 파이썬 레포지토리 트랜드 트래커

GitHub에서 인기 있는 파이썬 프로젝트들의 스타 수, 포크 수, 이슈 수를 자동으로 추적하고 순위를 매기는 도구입니다.

## 🚀 데모

실시간 순위 및 차트를 확인하려면 [데모 페이지](https://0x10.kr)를 방문하세요.

## 📊 프로젝트 소개

이 도구는 다양한 카테고리의 파이썬 프로젝트들을 모니터링하여 다음과 같은 기능을 제공합니다:

- **자동 데이터 수집**: GitHub GraphQL API를 사용하여 정확한 스타, 포크, 이슈, PR 수를 수집
- **히스토리 추적**: 일별 변화량을 추적하여 시간에 따른 트렌드 분석 가능
- **실시간 업데이트**: GitHub Actions를 통한 매일 자동 업데이트
- **다양한 카테고리**: 웹 프레임워크, 머신러닝, 데이터 과학, Python 구현체 등 포함

## 🎯 추적 카테고리

- **웹 프레임워크**: Django, Flask, FastAPI, Tornado 등
- **머신러닝/AI**: TensorFlow, PyTorch, scikit-learn, Keras 등  
- **데이터 과학**: Pandas, NumPy, SciPy, Matplotlib 등
- **비동기 프로그래밍**: asyncio, trio, anyio 등
- **Python 구현체**: CPython, PyPy, Jython, MicroPython 등

## 🛠️ 스크립트 문서

### 핵심 스크립트

- **`fetcher.py`** - 메인 데이터 수집 및 README 생성 스크립트
  - GitHub API에서 저장소 데이터 수집
  - 로컬 JSON 데이터 파일을 일별 변경사항으로 업데이트
  - 영어 및 한글 README 파일 생성
  - GraphQL API를 사용한 정확한 이슈/PR 수 조회

- **`readme_generator.py`** - 독립형 README 생성 유틸리티
  - 기존 로컬 JSON 파일에서 데이터 로드
  - 선택적으로 현재 GitHub 데이터로 업데이트
  - 전체 데이터 수집 없이 README 파일 생성
  - 빠른 README 업데이트를 위한 경량화 대안

- **`repo_data_initializer.py`** - 단일 저장소 데이터 수집기
  - 단일 GitHub 저장소 데이터 초기화
  - GraphQL을 사용한 과거 스타 데이터 수집
  - repo_data/ 디렉토리에 초기 JSON 데이터 파일 생성

- **`batch_repo_initializer.py`** - 배치 저장소 처리기
  - 여러 저장소를 병렬로 처리
  - 설정 가능한 워커 스레드 (기본값: 3 CPU)
  - 모든 저장소의 초기 데이터 수집에 이상적

- **`generate_history_from_repo_data.py`** - 히스토리 집계기
  - 일별 저장소 데이터를 누적 합계로 변환
  - 트렌드 분석을 위한 repository_histories.json 생성
  - 모든 repo_data/*.json 파일 처리

### 사용 예시

```bash
# 전체 데이터 수집 및 README 생성
uv run python/fetcher.py

# README만 빠르게 업데이트
uv run python/readme_generator.py

# 단일 저장소 초기화
uv run python/repo_data_initializer.py https://github.com/owner/repo

# 모든 저장소 배치 처리
uv run python/batch_repo_initializer.py --workers 8

# 히스토리 집계 생성
uv run python/generate_history_from_repo_data.py
```

| 프로젝트 이름 | 스타 수 | 포크 수 | 전체 이슈 | 전체 PR | 오픈 이슈 | 최근 커밋 |
| ------------ | ----- | ----- | ------------ | --------- | ----------- | ----------- |
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(header)

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
        f.write(f"\n*Last Automatic Update: {timestamp}*\n")
        f.write("\n*Inspired by https://github.com/mingrammer/python-web-framework-stars*\n")

    print(f"Generated Korean {output_file} with {len(repo_data)} projects")


def update_readme_timestamp(output_file: str = "README.md") -> None:
    """Update only the Last Automatic Update timestamp in README.md."""
    if not os.path.exists(output_file):
        print(f"Warning: {output_file} not found. Cannot update timestamp.")
        return

    try:
        # Read existing README content
        with open(output_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Update timestamp line
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Replace the Last Automatic Update line
        pattern = r"\*Last Automatic Update: [^*]*\*"
        replacement = f"*Last Automatic Update: {timestamp}*"

        if re.search(pattern, content):
            updated_content = re.sub(pattern, replacement, content)
        else:
            # If pattern not found, append timestamp at the end
            updated_content = content.rstrip() + f"\n\n*Last Automatic Update: {timestamp}*\n"

        # Write back to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(updated_content)

        print(f"Updated timestamp in {output_file}")

    except Exception as e:
        print(f"Failed to update timestamp in {output_file}: {e}")


def load_existing_repo_data() -> List[Dict]:
    """Load repository data from existing repo_data files."""
    repo_data_dir = "repo_data"
    
    if not os.path.exists(repo_data_dir):
        print(f"Warning: Directory '{repo_data_dir}' not found")
        return []
    
    all_repo_data = []
    
    # Get all JSON files in repo_data directory
    for filename in os.listdir(repo_data_dir):
        if not filename.endswith(".json"):
            continue
            
        repo_file_path = os.path.join(repo_data_dir, filename)
        
        try:
            with open(repo_file_path, "r", encoding="utf-8") as f:
                repo_data = json.load(f)
            
            # Extract owner and repo name from filename
            name_part = filename.replace(".json", "")
            if "_" in name_part:
                owner, repo_name = name_part.split("_", 1)
                
                # Create repository data structure
                project_data = {
                    "name": repo_name,
                    "html_url": f"https://github.com/{owner}/{repo_name}",
                    "stars": repo_data.get("total_stars", 0),
                    "forks": repo_data.get("total_forks", 0),
                    "open_issues": 0,  # Will be updated if we have current data
                    "total_issues": repo_data.get("total_issues", 0),
                    "total_pull_requests": repo_data.get("total_pull_requests", 0),
                    "last_commit": repo_data.get("last_commit", ""),
                    "fetched_at": repo_data.get("fetched_at", "")
                }
                
                all_repo_data.append(project_data)
                
        except Exception as e:
            print(f"Warning: Failed to load data from {filename}: {e}")
            continue
    
    print(f"Loaded data for {len(all_repo_data)} repositories from local files")
    return all_repo_data


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


def get_current_repo_data(owner: str, repo: str, token: Optional[str] = None) -> Optional[Dict]:
    """Get current repository data from GitHub API for README generation."""
    headers = {"User-Agent": "Python-Framework-Tracker"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        # Get basic repository data
        repo_url = f"https://api.github.com/repos/{owner}/{repo}"
        response = requests.get(repo_url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()

        return {
            "name": repo,
            "html_url": repo_data.get("html_url", ""),
            "stars": repo_data.get("stargazers_count", 0),
            "forks": repo_data.get("forks_count", 0),
            "open_issues": repo_data.get("open_issues_count", 0),
            "total_issues": 0,  # Will use existing data
            "total_pull_requests": 0,  # Will use existing data
            "last_commit": repo_data.get("pushed_at", ""),
            "fetched_at": datetime.now().isoformat(),
        }

    except requests.exceptions.RequestException as e:
        print(f"Warning: Failed to fetch current data for {owner}/{repo}: {e}")
        return None


def update_repo_data_with_current() -> List[Dict]:
    """Update repository data with current GitHub data where possible."""
    existing_data = load_existing_repo_data()
    token = get_github_token()
    
    if not token:
        print("Warning: No GitHub token found. Using existing data only.")
        return existing_data
    
    updated_data = []
    
    for repo in existing_data:
        # Extract owner and repo name from html_url
        try:
            url_path = repo["html_url"].replace("https://github.com/", "")
            owner, repo_name = url_path.split("/")
            
            # Try to get current data
            current = get_current_repo_data(owner, repo_name, token)
            
            if current:
                # Update with current data while keeping historical totals
                repo["stars"] = current["stars"]
                repo["forks"] = current["forks"]
                repo["open_issues"] = current["open_issues"]
                repo["last_commit"] = current["last_commit"]
                repo["fetched_at"] = current["fetched_at"]
                
            updated_data.append(repo)
            
        except Exception as e:
            print(f"Warning: Failed to update data for {repo.get('name', 'unknown')}: {e}")
            updated_data.append(repo)  # Keep existing data
            continue
    
    return updated_data


def main():
    """Main execution function for standalone README generation."""
    print("Starting README generation...")
    
    try:
        # Load and update repository data
        print("Loading repository data...")
        repo_data = update_repo_data_with_current()
        
        if not repo_data:
            print("No repository data found. Exiting.")
            return
        
        # Generate both README files
        print("Generating README files...")
        generate_readme_english(repo_data)
        generate_readme_korean(repo_data)
        
        print("README generation completed successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
