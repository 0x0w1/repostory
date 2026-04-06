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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194485 | 75256 | 41288 | 70494 | 4152 | 2026-04-06 01:04:51 |
| [transformers](https://github.com/huggingface/transformers) | 158848 | 32745 | 18826 | 25791 | 2357 | 2026-04-05 18:19:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 98821 | 27411 | 57656 | 121257 | 18230 | 2026-04-06 03:30:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 96873 | 9011 | 3513 | 5558 | 166 | 2026-04-03 19:43:25 |
| [django](https://github.com/django/django) | 87175 | 33803 | 0 | 20989 | 424 | 2026-04-03 19:30:16 |
| [cpython](https://github.com/python/cpython) | 72166 | 34378 | 75804 | 70019 | 9319 | 2026-04-05 23:49:48 |
| [flask](https://github.com/pallets/flask) | 71371 | 16769 | 2727 | 2796 | 3 | 2026-04-05 19:32:20 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65632 | 26871 | 12022 | 20505 | 2095 | 2026-04-04 17:00:40 |
| [keras](https://github.com/keras-team/keras) | 63925 | 19742 | 12727 | 9109 | 279 | 2026-04-04 01:39:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 48354 | 19825 | 28230 | 36774 | 3480 | 2026-04-05 19:37:35 |
| [ray](https://github.com/ray-project/ray) | 41963 | 7408 | 22529 | 39468 | 3566 | 2026-04-05 05:25:26 |
| [gym](https://github.com/openai/gym) | 37138 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33422 | 4668 | 5750 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31731 | 12239 | 13865 | 17224 | 2346 | 2026-04-06 01:50:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29953 | 7070 | 3947 | 4955 | 75 | 2026-04-02 07:52:04 |
| [celery](https://github.com/celery/celery) | 28300 | 4998 | 5209 | 3893 | 764 | 2026-04-05 19:08:54 |
| [dash](https://github.com/plotly/dash) | 24435 | 2272 | 2085 | 1518 | 551 | 2026-04-02 20:57:51 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22681 | 8309 | 11230 | 20171 | 1533 | 2026-04-04 15:26:20 |
| [tornado](https://github.com/tornadoweb/tornado) | 22388 | 5542 | 1867 | 1726 | 215 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21946 | 1421 | 1326 | 6165 | 369 | 2026-04-06 02:07:57 |
| [micropython](https://github.com/micropython/micropython) | 21607 | 8776 | 6010 | 7685 | 1873 | 2026-04-01 04:01:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18417 | 2793 | 3340 | 2065 | 777 | 2026-04-03 21:03:38 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16369 | 2239 | 3185 | 8810 | 275 | 2026-04-06 02:48:02 |
| [httpx](https://github.com/encode/httpx) | 15150 | 1102 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14588 | 5682 | 11404 | 13556 | 1793 | 2026-04-05 20:31:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13795 | 2092 | 2650 | 1169 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13786 | 1861 | 5520 | 6523 | 1243 | 2026-04-02 08:59:32 |
| [starlette](https://github.com/Kludex/starlette) | 12174 | 1154 | 766 | 1856 | 53 | 2026-04-05 13:21:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11738 | 607 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11698 | 1664 | 8184 | 1053 | 212 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 983 | 1119 | 1424 | 163 | 2026-04-05 19:01:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8985 | 567 | 1025 | 500 | 219 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1499 | 864 | 634 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7229 | 395 | 882 | 2522 | 319 | 2026-04-01 01:25:20 |
| [hug](https://github.com/hugapi/hug) | 6895 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5602 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5539 | 472 | 1244 | 819 | 507 | 2026-04-05 07:06:26 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5227 | 1004 | 908 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1064 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4055 | 326 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4010 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3617 | 195 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 311 | 664 | 1306 | 305 | 2026-04-03 22:07:14 |
| [anyio](https://github.com/agronholm/anyio) | 2435 | 192 | 431 | 600 | 85 | 2026-03-30 19:08:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 905 | 1081 | 1464 | 369 | 2026-04-04 02:24:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 367 | 1785 | 267 | 267 | 2026-03-30 17:40:37 |
| [pypy](https://github.com/pypy/pypy) | 1699 | 109 | 5190 | 193 | 762 | 2026-04-05 20:49:56 |
| [jython](https://github.com/jython/jython) | 1500 | 228 | 294 | 123 | 109 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-06T03:31:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
