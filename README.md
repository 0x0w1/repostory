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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195270 | 75337 | 41470 | 74441 | 5641 | 2026-05-26 04:14:59 |
| [transformers](https://github.com/huggingface/transformers) | 160953 | 33316 | 18997 | 26503 | 2388 | 2026-05-26 03:10:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 100184 | 27871 | 58892 | 125702 | 18590 | 2026-05-26 04:12:41 |
| [fastapi](https://github.com/fastapi/fastapi) | 98513 | 9343 | 3528 | 5801 | 96 | 2026-05-25 19:57:14 |
| [django](https://github.com/django/django) | 87571 | 33955 | 0 | 21296 | 447 | 2026-05-25 19:53:37 |
| [cpython](https://github.com/python/cpython) | 72885 | 34680 | 76493 | 71634 | 9320 | 2026-05-26 04:03:36 |
| [flask](https://github.com/pallets/flask) | 71581 | 16853 | 2739 | 2832 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66186 | 27046 | 12108 | 20835 | 2028 | 2026-05-25 19:13:27 |
| [keras](https://github.com/keras-team/keras) | 64083 | 19776 | 12765 | 9361 | 196 | 2026-05-22 21:17:15 |
| [pandas](https://github.com/pandas-dev/pandas) | 48849 | 19977 | 28293 | 37349 | 3275 | 2026-05-25 14:09:52 |
| [ray](https://github.com/ray-project/ray) | 42672 | 7609 | 22696 | 40550 | 3444 | 2026-05-25 13:54:09 |
| [gym](https://github.com/openai/gym) | 37206 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33611 | 4685 | 5756 | 4093 | 206 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32093 | 12386 | 13926 | 17504 | 2384 | 2026-05-26 01:54:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30031 | 7066 | 3967 | 5006 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28528 | 5050 | 5280 | 4121 | 781 | 2026-05-25 05:31:20 |
| [dash](https://github.com/plotly/dash) | 24213 | 2284 | 2102 | 1568 | 554 | 2026-05-25 22:58:18 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22835 | 8339 | 11284 | 20403 | 1482 | 2026-05-24 21:34:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5541 | 1872 | 1735 | 220 | 2026-05-21 18:10:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 22074 | 1441 | 1347 | 6560 | 381 | 2026-05-26 01:37:04 |
| [micropython](https://github.com/micropython/micropython) | 21741 | 8838 | 6059 | 7826 | 1731 | 2026-05-25 03:19:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1590 | 1466 | 1686 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18551 | 2806 | 3345 | 2088 | 757 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16443 | 2276 | 3205 | 9160 | 245 | 2026-05-25 17:12:58 |
| [httpx](https://github.com/encode/httpx) | 15290 | 1149 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14718 | 5737 | 11450 | 13750 | 1792 | 2026-05-25 17:51:04 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13887 | 2114 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13844 | 1875 | 5529 | 6582 | 1246 | 2026-05-25 22:33:00 |
| [starlette](https://github.com/Kludex/starlette) | 12330 | 1179 | 769 | 1914 | 64 | 2026-05-25 11:58:40 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11883 | 1688 | 8216 | 1093 | 213 | 2026-05-25 20:09:42 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11791 | 607 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 998 | 1125 | 1449 | 158 | 2026-05-21 04:48:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9065 | 580 | 1036 | 514 | 212 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8767 | 1500 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7272 | 397 | 892 | 2547 | 321 | 2026-05-25 21:57:42 |
| [hug](https://github.com/hugapi/hug) | 6887 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5571 | 483 | 1256 | 838 | 510 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5265 | 1015 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4157 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3634 | 198 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 664 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2472 | 207 | 439 | 641 | 86 | 2026-05-25 19:39:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1520 | 364 | 2026-05-25 20:08:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-05-25 17:51:18 |
| [pypy](https://github.com/pypy/pypy) | 1741 | 113 | 5214 | 250 | 740 | 2026-05-25 19:48:21 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 131 | 109 | 2026-05-25 19:17:48 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-26T04:17:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
