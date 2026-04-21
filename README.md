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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194790 | 75273 | 41318 | 71601 | 4593 | 2026-04-21 03:33:22 |
| [transformers](https://github.com/huggingface/transformers) | 159663 | 32949 | 18881 | 26009 | 2356 | 2026-04-21 01:03:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 99298 | 27537 | 58130 | 122295 | 18525 | 2026-04-21 03:34:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 97451 | 9105 | 3517 | 5624 | 176 | 2026-04-20 21:41:15 |
| [django](https://github.com/django/django) | 87294 | 33813 | 0 | 21081 | 432 | 2026-04-20 20:49:26 |
| [cpython](https://github.com/python/cpython) | 72397 | 34457 | 76045 | 70478 | 9392 | 2026-04-20 23:10:53 |
| [flask](https://github.com/pallets/flask) | 71428 | 16792 | 2735 | 2807 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65869 | 26960 | 12044 | 20606 | 2068 | 2026-04-21 00:06:25 |
| [keras](https://github.com/keras-team/keras) | 64020 | 19748 | 12738 | 9194 | 288 | 2026-04-21 03:02:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 48538 | 19863 | 28249 | 36984 | 3411 | 2026-04-20 20:20:39 |
| [ray](https://github.com/ray-project/ray) | 42229 | 7465 | 22597 | 39859 | 3613 | 2026-04-21 03:02:06 |
| [gym](https://github.com/openai/gym) | 37171 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33495 | 4675 | 5754 | 4091 | 202 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31861 | 12303 | 13885 | 17331 | 2364 | 2026-04-21 00:17:05 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29980 | 7065 | 3968 | 4999 | 78 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28384 | 5010 | 5270 | 4079 | 778 | 2026-04-20 09:04:05 |
| [dash](https://github.com/plotly/dash) | 24199 | 2277 | 2090 | 1540 | 546 | 2026-04-20 19:17:17 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22728 | 8323 | 11247 | 20236 | 1504 | 2026-04-21 03:26:54 |
| [tornado](https://github.com/tornadoweb/tornado) | 22260 | 5542 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22023 | 1426 | 1332 | 6242 | 373 | 2026-04-20 18:43:05 |
| [micropython](https://github.com/micropython/micropython) | 21642 | 8803 | 6033 | 7740 | 1877 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18465 | 2801 | 3338 | 2077 | 763 | 2026-04-21 00:30:41 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16408 | 2252 | 3190 | 8883 | 279 | 2026-04-20 18:58:17 |
| [httpx](https://github.com/encode/httpx) | 15210 | 1115 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14621 | 5702 | 11420 | 13610 | 1791 | 2026-04-21 01:47:12 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13821 | 2100 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1867 | 5521 | 6530 | 1246 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12221 | 1156 | 766 | 1874 | 57 | 2026-04-16 07:31:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11769 | 1670 | 8194 | 1058 | 216 | 2026-04-20 20:32:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11763 | 605 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 988 | 1121 | 1432 | 154 | 2026-04-20 21:43:28 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9017 | 568 | 1030 | 504 | 201 | 2026-04-18 19:04:16 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7245 | 393 | 889 | 2534 | 317 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6896 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5553 | 479 | 1249 | 823 | 508 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5241 | 1007 | 910 | 291 | 200 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4077 | 330 | 1183 | 217 | 116 | 2026-04-20 21:11:28 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3624 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2441 | 197 | 434 | 611 | 83 | 2026-04-20 17:45:50 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 904 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1711 | 111 | 5199 | 226 | 747 | 2026-04-20 19:37:19 |
| [jython](https://github.com/jython/jython) | 1499 | 227 | 294 | 126 | 111 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-21T03:34:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
