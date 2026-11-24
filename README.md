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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201713 | 77407 | 41992 | 85035 | 3519 | 2026-11-24 09:37:29 |
| [transformers](https://github.com/huggingface/transformers) | 169280 | 35282 | 19954 | 30341 | 1145 | 2026-11-24 09:32:15 |
| [pytorch](https://github.com/pytorch/pytorch) | 105706 | 30686 | 63021 | 142673 | 18558 | 2026-11-24 09:33:27 |
| [fastapi](https://github.com/fastapi/fastapi) | 104953 | 10360 | 3556 | 6651 | 46 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91832 | 35107 | 0 | 22243 | 537 | 2026-11-23 18:39:57 |
| [cpython](https://github.com/python/cpython) | 78356 | 36554 | 79409 | 80706 | 9400 | 2026-11-24 09:15:53 |
| [flask](https://github.com/pallets/flask) | 75195 | 17292 | 2782 | 2911 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68306 | 27686 | 12404 | 21896 | 2169 | 2026-11-24 07:59:21 |
| [keras](https://github.com/keras-team/keras) | 64446 | 19805 | 13113 | 10329 | 264 | 2026-11-23 22:40:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 50611 | 20712 | 28710 | 40155 | 1788 | 2026-11-23 23:35:13 |
| [ray](https://github.com/ray-project/ray) | 44370 | 8304 | 23368 | 44647 | 3865 | 2026-11-24 08:38:49 |
| [gym](https://github.com/openai/gym) | 37234 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34092 | 4750 | 5785 | 4155 | 276 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33460 | 13066 | 14215 | 19113 | 2262 | 2026-11-24 00:32:29 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30254 | 7110 | 3966 | 5120 | 58 | 2026-11-23 15:09:24 |
| [celery](https://github.com/celery/celery) | 29259 | 5273 | 5406 | 4762 | 804 | 2026-11-24 08:31:31 |
| [dash](https://github.com/plotly/dash) | 24504 | 2348 | 2189 | 1861 | 442 | 2026-11-23 18:51:21 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23495 | 8581 | 11472 | 21115 | 1478 | 2026-11-23 16:01:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 22504 | 1509 | 1474 | 8432 | 350 | 2026-11-23 13:44:13 |
| [micropython](https://github.com/micropython/micropython) | 22225 | 9077 | 6192 | 8287 | 1608 | 2026-11-24 02:26:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22170 | 5615 | 1901 | 1960 | 181 | 2026-11-23 20:57:20 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18926 | 2907 | 3408 | 2297 | 733 | 2026-11-23 19:59:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1618 | 1475 | 1696 | 167 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16619 | 2541 | 3281 | 10781 | 349 | 2026-11-23 13:30:47 |
| [httpx](https://github.com/encode/httpx) | 15845 | 2031 | 925 | 1830 | 156 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15248 | 6124 | 11794 | 14983 | 1955 | 2026-11-24 07:30:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14120 | 2172 | 2669 | 1270 | 267 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13959 | 2031 | 5584 | 6881 | 1451 | 2026-11-24 00:28:54 |
| [starlette](https://github.com/Kludex/starlette) | 12758 | 1457 | 800 | 2305 | 36 | 2026-11-22 13:18:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12307 | 1960 | 8411 | 1264 | 220 | 2026-11-19 21:09:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11947 | 624 | 431 | 349 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9821 | 1055 | 1154 | 1585 | 163 | 2026-11-21 22:54:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9256 | 624 | 1062 | 623 | 167 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8804 | 1512 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 479 | 911 | 2677 | 343 | 2026-11-24 00:03:10 |
| [hug](https://github.com/hugapi/hug) | 6868 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5642 | 550 | 1311 | 998 | 562 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5459 | 1055 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4484 | 397 | 1212 | 259 | 116 | 2026-11-22 15:57:45 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2758 | 79 | 2026-11-24 00:14:05 |
| [databases](https://github.com/encode/databases) | 3984 | 367 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 214 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2760 | 320 | 682 | 1438 | 257 | 2026-11-24 02:26:50 |
| [anyio](https://github.com/agronholm/anyio) | 2573 | 363 | 507 | 918 | 168 | 2026-11-24 00:06:17 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1612 | 355 | 2026-11-23 17:40:38 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-23 18:08:22 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5305 | 478 | 726 | 2026-11-23 21:19:13 |
| [jython](https://github.com/jython/jython) | 1549 | 238 | 306 | 165 | 110 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-24T09:38:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
