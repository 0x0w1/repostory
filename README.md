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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195625 | 75190 | 41524 | 75650 | 3264 | 2026-06-10 04:24:12 |
| [transformers](https://github.com/huggingface/transformers) | 161466 | 33451 | 19048 | 26769 | 2407 | 2026-06-09 18:20:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 100625 | 27962 | 59140 | 127136 | 18352 | 2026-06-10 04:24:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 99058 | 9406 | 3533 | 5883 | 95 | 2026-06-09 22:07:37 |
| [django](https://github.com/django/django) | 87815 | 33861 | 0 | 21372 | 446 | 2026-06-10 00:58:31 |
| [cpython](https://github.com/python/cpython) | 73155 | 34710 | 76667 | 72219 | 9287 | 2026-06-09 23:33:05 |
| [flask](https://github.com/pallets/flask) | 71644 | 16871 | 2746 | 2836 | 4 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66281 | 27058 | 12128 | 20927 | 2049 | 2026-06-10 04:19:57 |
| [keras](https://github.com/keras-team/keras) | 64079 | 19732 | 12780 | 9430 | 173 | 2026-06-10 01:50:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 48944 | 20005 | 28308 | 37439 | 3216 | 2026-06-09 22:11:48 |
| [ray](https://github.com/ray-project/ray) | 42826 | 7665 | 22732 | 40864 | 3457 | 2026-06-10 04:23:48 |
| [gym](https://github.com/openai/gym) | 37222 | 8705 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33643 | 4687 | 5757 | 4096 | 210 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32167 | 12436 | 13934 | 17574 | 2374 | 2026-06-09 19:14:09 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30058 | 7069 | 3967 | 5012 | 78 | 2026-06-09 21:41:12 |
| [celery](https://github.com/celery/celery) | 28568 | 5072 | 5280 | 4138 | 784 | 2026-06-10 01:29:03 |
| [dash](https://github.com/plotly/dash) | 24243 | 2292 | 2104 | 1581 | 538 | 2026-06-08 16:59:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22875 | 8351 | 11302 | 20506 | 1457 | 2026-06-10 03:06:41 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5535 | 1872 | 1744 | 217 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22104 | 1442 | 1354 | 6641 | 388 | 2026-06-10 02:17:50 |
| [micropython](https://github.com/micropython/micropython) | 21792 | 8859 | 6067 | 7865 | 1672 | 2026-06-10 04:12:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1591 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18594 | 2808 | 3359 | 2094 | 766 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16440 | 2320 | 3211 | 9340 | 221 | 2026-06-10 01:57:33 |
| [httpx](https://github.com/encode/httpx) | 15293 | 1165 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14742 | 5759 | 11471 | 13852 | 1799 | 2026-06-09 19:36:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13903 | 2116 | 2653 | 1183 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13849 | 1884 | 5537 | 6608 | 1243 | 2026-06-09 22:09:57 |
| [starlette](https://github.com/Kludex/starlette) | 12381 | 1196 | 770 | 1939 | 60 | 2026-06-08 08:55:22 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11902 | 1695 | 8226 | 1108 | 212 | 2026-06-09 18:34:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11814 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 999 | 1128 | 1455 | 160 | 2026-06-08 18:21:50 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9085 | 598 | 1037 | 518 | 214 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7277 | 398 | 892 | 2552 | 320 | 2026-06-09 06:57:17 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5593 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5576 | 486 | 1257 | 849 | 516 | 2026-06-09 14:33:27 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5288 | 1021 | 914 | 303 | 212 | 2026-06-09 07:01:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4185 | 337 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4002 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3638 | 200 | 283 | 128 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2751 | 311 | 666 | 1320 | 307 | 2026-06-06 13:02:09 |
| [anyio](https://github.com/agronholm/anyio) | 2479 | 207 | 441 | 648 | 84 | 2026-06-08 17:52:21 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1084 | 1540 | 363 | 2026-06-06 20:15:33 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 268 | 266 | 2026-06-08 17:45:57 |
| [pypy](https://github.com/pypy/pypy) | 1748 | 114 | 5219 | 261 | 737 | 2026-06-10 04:09:35 |
| [jython](https://github.com/jython/jython) | 1515 | 230 | 297 | 135 | 109 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 113 | 78 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-10T04:26:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
