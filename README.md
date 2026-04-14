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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194702 | 75279 | 41307 | 71067 | 4384 | 2026-04-14 03:24:36 |
| [transformers](https://github.com/huggingface/transformers) | 159325 | 32864 | 18859 | 25916 | 2358 | 2026-04-14 01:30:14 |
| [pytorch](https://github.com/pytorch/pytorch) | 99099 | 27480 | 57969 | 121817 | 18491 | 2026-04-14 03:31:10 |
| [fastapi](https://github.com/fastapi/fastapi) | 97169 | 9068 | 3517 | 5576 | 171 | 2026-04-14 03:00:07 |
| [django](https://github.com/django/django) | 87258 | 33809 | 0 | 21036 | 431 | 2026-04-13 16:06:47 |
| [cpython](https://github.com/python/cpython) | 72319 | 34418 | 75950 | 70300 | 9338 | 2026-04-14 03:12:37 |
| [flask](https://github.com/pallets/flask) | 71416 | 16787 | 2731 | 2802 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65812 | 26940 | 12028 | 20546 | 2048 | 2026-04-13 16:56:22 |
| [keras](https://github.com/keras-team/keras) | 63984 | 19737 | 12727 | 9145 | 268 | 2026-04-14 00:54:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 48494 | 19867 | 28241 | 36897 | 3434 | 2026-04-13 22:25:47 |
| [ray](https://github.com/ray-project/ray) | 42110 | 7435 | 22561 | 39671 | 3587 | 2026-04-14 03:18:10 |
| [gym](https://github.com/openai/gym) | 37159 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33461 | 4671 | 5753 | 4089 | 199 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31846 | 12302 | 13872 | 17294 | 2346 | 2026-04-13 11:23:30 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29967 | 7066 | 3968 | 4997 | 76 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28351 | 5007 | 5267 | 4072 | 784 | 2026-04-13 16:48:00 |
| [dash](https://github.com/plotly/dash) | 24201 | 2275 | 2088 | 1529 | 543 | 2026-04-13 22:47:21 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22711 | 8317 | 11240 | 20202 | 1503 | 2026-04-13 20:51:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22270 | 5544 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21998 | 1425 | 1331 | 6194 | 380 | 2026-04-14 01:49:26 |
| [micropython](https://github.com/micropython/micropython) | 21617 | 8795 | 6024 | 7719 | 1887 | 2026-04-10 19:14:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1586 | 1465 | 1682 | 132 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18449 | 2797 | 3339 | 2071 | 771 | 2026-04-14 03:30:30 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16401 | 2243 | 3188 | 8853 | 281 | 2026-04-14 00:35:24 |
| [httpx](https://github.com/encode/httpx) | 15194 | 1107 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14599 | 5690 | 11411 | 13579 | 1791 | 2026-04-13 19:33:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13804 | 2094 | 2652 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13801 | 1863 | 5521 | 6527 | 1243 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12200 | 1153 | 766 | 1864 | 53 | 2026-04-14 02:36:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11748 | 604 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11747 | 1667 | 8189 | 1054 | 215 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 988 | 1121 | 1432 | 164 | 2026-04-12 14:11:25 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9005 | 569 | 1027 | 502 | 222 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8754 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7238 | 395 | 889 | 2531 | 321 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5545 | 474 | 1248 | 822 | 507 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5235 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4066 | 329 | 1182 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4008 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3620 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2436 | 194 | 434 | 608 | 89 | 2026-04-13 22:34:56 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 366 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1704 | 110 | 5195 | 219 | 745 | 2026-04-13 21:35:45 |
| [jython](https://github.com/jython/jython) | 1499 | 228 | 294 | 125 | 111 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-14T03:31:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
