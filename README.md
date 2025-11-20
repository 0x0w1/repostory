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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192490 | 74993 | 40994 | 61715 | 2465 | 2025-11-20 01:53:42 |
| [transformers](https://github.com/huggingface/transformers) | 152736 | 31174 | 18207 | 23481 | 2118 | 2025-11-19 22:18:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 95220 | 25954 | 54960 | 112761 | 17132 | 2025-11-20 02:00:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 92084 | 8242 | 3477 | 4887 | 222 | 2025-11-19 16:52:54 |
| [django](https://github.com/django/django) | 85844 | 33238 | 0 | 20207 | 362 | 2025-11-19 14:58:37 |
| [flask](https://github.com/pallets/flask) | 70799 | 16627 | 2702 | 2723 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69934 | 33458 | 74399 | 66404 | 9212 | 2025-11-20 01:01:49 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64075 | 26451 | 11817 | 19795 | 2109 | 2025-11-20 00:03:25 |
| [keras](https://github.com/keras-team/keras) | 63579 | 19649 | 12593 | 8476 | 269 | 2025-11-18 20:56:49 |
| [pandas](https://github.com/pandas-dev/pandas) | 47150 | 19316 | 27891 | 35210 | 3622 | 2025-11-19 21:50:34 |
| [ray](https://github.com/ray-project/ray) | 39915 | 6918 | 21887 | 36603 | 3226 | 2025-11-20 01:35:06 |
| [gym](https://github.com/openai/gym) | 36789 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32840 | 4627 | 5732 | 4073 | 193 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30856 | 11716 | 13659 | 16543 | 2355 | 2025-11-19 17:27:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29674 | 7036 | 3946 | 4868 | 88 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27591 | 4897 | 5176 | 3726 | 753 | 2025-11-18 11:59:48 |
| [dash](https://github.com/plotly/dash) | 24259 | 2234 | 2026 | 1377 | 585 | 2025-11-19 21:00:31 |
| [tornado](https://github.com/tornadoweb/tornado) | 22351 | 5543 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22018 | 8123 | 11049 | 19672 | 1626 | 2025-11-19 00:44:16 |
| [micropython](https://github.com/micropython/micropython) | 21110 | 8535 | 5876 | 7360 | 1801 | 2025-11-19 06:02:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 20810 | 1358 | 1234 | 4986 | 446 | 2025-11-18 16:00:41 |
| [sanic](https://github.com/sanic-org/sanic) | 18567 | 1583 | 1451 | 1630 | 149 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17994 | 2749 | 3291 | 1984 | 746 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16098 | 2157 | 3163 | 8301 | 286 | 2025-11-17 18:53:12 |
| [httpx](https://github.com/encode/httpx) | 14755 | 979 | 921 | 1756 | 112 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14201 | 5542 | 11147 | 12864 | 1790 | 2025-11-19 23:06:15 |
| [dask](https://github.com/dask/dask) | 13603 | 1823 | 5462 | 6403 | 1191 | 2025-11-19 14:06:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13568 | 2048 | 2633 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11669 | 1079 | 760 | 1744 | 52 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11432 | 585 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11152 | 1599 | 8120 | 1003 | 210 | 2025-11-19 19:13:53 |
| [falcon](https://github.com/falconry/falcon) | 9759 | 972 | 1111 | 1402 | 162 | 2025-11-16 10:15:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8719 | 537 | 969 | 454 | 175 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8691 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7005 | 371 | 873 | 2470 | 313 | 2025-11-17 21:56:02 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5626 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5382 | 445 | 1198 | 716 | 505 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5090 | 967 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 887 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3767 | 300 | 1167 | 201 | 117 | 2025-11-19 22:32:17 |
| [quart](https://github.com/pallets/quart) | 3544 | 191 | 278 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2708 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2298 | 176 | 415 | 548 | 74 | 2025-11-20 02:00:13 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1928 | 372 | 1784 | 266 | 265 | 2025-11-20 00:37:23 |
| [pypy](https://github.com/pypy/pypy) | 1570 | 89 | 5163 | 171 | 748 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1458 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-18 10:59:56 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-20T02:02:23*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
