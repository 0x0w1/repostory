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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192445 | 74999 | 40996 | 61516 | 2424 | 2025-11-17 01:11:15 |
| [transformers](https://github.com/huggingface/transformers) | 152578 | 31152 | 18196 | 23432 | 2126 | 2025-11-16 22:32:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 95105 | 25920 | 54891 | 112575 | 17092 | 2025-11-17 02:01:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 91982 | 8233 | 3477 | 4876 | 217 | 2025-11-13 17:05:28 |
| [django](https://github.com/django/django) | 85806 | 33233 | 0 | 20117 | 358 | 2025-11-14 14:26:05 |
| [flask](https://github.com/pallets/flask) | 70789 | 16622 | 2701 | 2724 | 14 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69887 | 33434 | 74369 | 66330 | 9212 | 2025-11-16 22:23:03 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64042 | 26442 | 11814 | 19773 | 2118 | 2025-11-15 09:15:09 |
| [keras](https://github.com/keras-team/keras) | 63561 | 19649 | 12592 | 8473 | 267 | 2025-11-14 19:35:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 47120 | 19309 | 27883 | 35193 | 3621 | 2025-11-16 18:39:47 |
| [ray](https://github.com/ray-project/ray) | 39849 | 6904 | 21832 | 36504 | 3215 | 2025-11-17 00:36:09 |
| [gym](https://github.com/openai/gym) | 36776 | 8711 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32823 | 4624 | 5731 | 4072 | 196 | 2025-11-13 13:25:50 |
| [numpy](https://github.com/numpy/numpy) | 30835 | 11706 | 13649 | 16528 | 2362 | 2025-11-17 00:02:32 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29665 | 7035 | 3946 | 4867 | 87 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27563 | 4893 | 5176 | 3723 | 754 | 2025-11-14 11:29:11 |
| [dash](https://github.com/plotly/dash) | 24254 | 2233 | 2024 | 1369 | 578 | 2025-11-14 15:14:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22348 | 5545 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21994 | 8119 | 11045 | 19664 | 1622 | 2025-11-15 02:19:42 |
| [micropython](https://github.com/micropython/micropython) | 21102 | 8534 | 5875 | 7351 | 1810 | 2025-11-16 23:58:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 20796 | 1358 | 1232 | 4983 | 446 | 2025-11-16 14:25:45 |
| [sanic](https://github.com/sanic-org/sanic) | 18560 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17973 | 2747 | 3291 | 1979 | 749 | 2025-11-14 19:08:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16091 | 2156 | 3163 | 8298 | 284 | 2025-11-13 10:33:58 |
| [httpx](https://github.com/encode/httpx) | 14747 | 978 | 921 | 1755 | 111 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14197 | 5540 | 11142 | 12845 | 1796 | 2025-11-16 21:30:59 |
| [dask](https://github.com/dask/dask) | 13595 | 1824 | 5459 | 6401 | 1194 | 2025-11-14 13:49:23 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13558 | 2047 | 2633 | 1149 | 194 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11665 | 1080 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11424 | 585 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11139 | 1598 | 8117 | 1000 | 209 | 2025-11-16 15:58:47 |
| [falcon](https://github.com/falconry/falcon) | 9758 | 973 | 1111 | 1402 | 162 | 2025-11-16 10:15:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8715 | 537 | 968 | 454 | 175 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8690 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6998 | 372 | 873 | 2469 | 313 | 2025-11-11 03:51:31 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5379 | 444 | 1198 | 716 | 505 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5086 | 963 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 887 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3757 | 300 | 1166 | 200 | 116 | 2025-11-15 18:32:45 |
| [quart](https://github.com/pallets/quart) | 3541 | 191 | 278 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2706 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2297 | 176 | 414 | 546 | 74 | 2025-11-16 22:21:22 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 372 | 1783 | 266 | 264 | 2025-11-16 03:35:42 |
| [pypy](https://github.com/pypy/pypy) | 1568 | 89 | 5163 | 171 | 748 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-17 01:21:40 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-17T02:06:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
