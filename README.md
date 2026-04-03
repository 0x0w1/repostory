# Python Repository Trends Tracker

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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194441 | 75258 | 41294 | 70378 | 4069 | 2026-04-03 03:14:42 |
| [transformers](https://github.com/huggingface/transformers) | 158710 | 32718 | 18813 | 25755 | 2329 | 2026-04-03 01:59:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 98760 | 27384 | 57627 | 121065 | 18210 | 2026-04-03 03:09:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 96787 | 8991 | 3513 | 5554 | 165 | 2026-04-02 18:33:21 |
| [django](https://github.com/django/django) | 87150 | 33803 | 0 | 20977 | 418 | 2026-04-02 19:54:57 |
| [cpython](https://github.com/python/cpython) | 72150 | 34353 | 75776 | 69925 | 9331 | 2026-04-02 21:33:01 |
| [flask](https://github.com/pallets/flask) | 71362 | 16763 | 2726 | 2796 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65601 | 26872 | 12020 | 20493 | 2134 | 2026-04-02 12:14:35 |
| [keras](https://github.com/keras-team/keras) | 63928 | 19744 | 12723 | 9099 | 285 | 2026-04-03 01:45:49 |
| [pandas](https://github.com/pandas-dev/pandas) | 48333 | 19818 | 28225 | 36744 | 3503 | 2026-04-03 00:25:12 |
| [ray](https://github.com/ray-project/ray) | 41926 | 7402 | 22522 | 39433 | 3567 | 2026-04-03 03:17:30 |
| [gym](https://github.com/openai/gym) | 37128 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33410 | 4666 | 5751 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31712 | 12223 | 13860 | 17197 | 2338 | 2026-04-03 01:19:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29946 | 7073 | 3947 | 4955 | 75 | 2026-04-02 07:52:04 |
| [celery](https://github.com/celery/celery) | 28294 | 4996 | 5209 | 3882 | 760 | 2026-04-02 14:55:25 |
| [dash](https://github.com/plotly/dash) | 24434 | 2271 | 2085 | 1518 | 551 | 2026-04-02 20:57:51 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22663 | 8305 | 11225 | 20165 | 1530 | 2026-04-03 02:20:39 |
| [tornado](https://github.com/tornadoweb/tornado) | 22391 | 5542 | 1865 | 1724 | 211 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21931 | 1417 | 1325 | 6160 | 366 | 2026-04-02 16:46:44 |
| [micropython](https://github.com/micropython/micropython) | 21604 | 8776 | 6005 | 7678 | 1862 | 2026-04-01 04:01:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18644 | 1588 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18411 | 2793 | 3337 | 2063 | 773 | 2026-04-02 15:30:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16366 | 2235 | 3185 | 8805 | 274 | 2026-04-03 02:19:51 |
| [httpx](https://github.com/encode/httpx) | 15142 | 1098 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14582 | 5677 | 11400 | 13546 | 1795 | 2026-04-02 14:15:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13793 | 2089 | 2651 | 1168 | 213 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13781 | 1859 | 5520 | 6517 | 1238 | 2026-04-02 08:59:32 |
| [starlette](https://github.com/Kludex/starlette) | 12170 | 1150 | 766 | 1850 | 51 | 2026-04-02 21:30:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11736 | 606 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11692 | 1663 | 8183 | 1053 | 213 | 2026-04-01 20:28:36 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 981 | 1119 | 1422 | 162 | 2026-03-28 18:33:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8982 | 566 | 1025 | 499 | 220 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1498 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7225 | 394 | 882 | 2520 | 317 | 2026-04-01 01:25:20 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5603 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5537 | 471 | 1243 | 814 | 503 | 2026-04-01 22:21:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5225 | 1004 | 908 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4080 | 895 | 1064 | 2735 | 85 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4050 | 325 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4010 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3616 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 311 | 664 | 1305 | 305 | 2026-03-31 20:59:00 |
| [anyio](https://github.com/agronholm/anyio) | 2434 | 190 | 431 | 599 | 84 | 2026-03-30 19:08:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 368 | 1785 | 267 | 267 | 2026-03-30 17:40:37 |
| [pypy](https://github.com/pypy/pypy) | 1696 | 108 | 5190 | 192 | 760 | 2026-04-02 20:27:50 |
| [jython](https://github.com/jython/jython) | 1499 | 228 | 294 | 123 | 110 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-03T03:18:17*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
