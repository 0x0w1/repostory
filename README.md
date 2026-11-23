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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201784 | 77417 | 41991 | 84982 | 3488 | 2026-11-23 06:52:13 |
| [transformers](https://github.com/huggingface/transformers) | 169401 | 35273 | 19943 | 30289 | 1125 | 2026-11-23 07:10:04 |
| [pytorch](https://github.com/pytorch/pytorch) | 105827 | 30706 | 62948 | 142521 | 18596 | 2026-11-23 07:10:52 |
| [fastapi](https://github.com/fastapi/fastapi) | 105055 | 10368 | 3555 | 6646 | 49 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91945 | 35119 | 0 | 22238 | 541 | 2026-11-21 16:52:56 |
| [cpython](https://github.com/python/cpython) | 78474 | 36572 | 79391 | 80667 | 9375 | 2026-11-23 01:16:49 |
| [flask](https://github.com/pallets/flask) | 75355 | 17298 | 2782 | 2911 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68298 | 27684 | 12402 | 21881 | 2176 | 2026-11-21 14:45:13 |
| [keras](https://github.com/keras-team/keras) | 64451 | 19807 | 13111 | 10322 | 259 | 2026-11-20 23:54:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 50606 | 20711 | 28708 | 40143 | 1794 | 2026-11-22 18:11:57 |
| [ray](https://github.com/ray-project/ray) | 44364 | 8299 | 23364 | 44612 | 3855 | 2026-11-23 07:08:45 |
| [gym](https://github.com/openai/gym) | 37235 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34090 | 4751 | 5785 | 4155 | 276 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33456 | 13063 | 14213 | 19109 | 2263 | 2026-11-23 00:20:36 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30254 | 7108 | 3966 | 5119 | 58 | 2026-11-19 09:00:18 |
| [celery](https://github.com/celery/celery) | 29261 | 5277 | 5406 | 4755 | 807 | 2026-11-23 06:26:01 |
| [dash](https://github.com/plotly/dash) | 24502 | 2347 | 2185 | 1852 | 427 | 2026-11-20 20:30:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23498 | 8581 | 11469 | 21113 | 1490 | 2026-11-22 21:42:08 |
| [RustPython](https://github.com/RustPython/RustPython) | 22502 | 1509 | 1474 | 8416 | 334 | 2026-11-22 02:15:47 |
| [micropython](https://github.com/micropython/micropython) | 22222 | 9080 | 6187 | 8282 | 1599 | 2026-11-21 05:26:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22175 | 5615 | 1901 | 1955 | 206 | 2026-11-21 03:23:15 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18922 | 2904 | 3408 | 2295 | 737 | 2026-11-19 23:40:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1618 | 1475 | 1696 | 167 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16621 | 2539 | 3280 | 10764 | 339 | 2026-11-22 12:24:50 |
| [httpx](https://github.com/encode/httpx) | 15839 | 2035 | 925 | 1827 | 153 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15242 | 6116 | 11792 | 14968 | 1941 | 2026-11-22 14:49:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14122 | 2169 | 2669 | 1266 | 265 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13959 | 2033 | 5583 | 6855 | 1440 | 2026-11-21 20:29:45 |
| [starlette](https://github.com/Kludex/starlette) | 12755 | 1454 | 800 | 2305 | 36 | 2026-11-22 13:18:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12303 | 1961 | 8409 | 1263 | 218 | 2026-11-19 21:09:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11947 | 623 | 431 | 349 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9821 | 1055 | 1154 | 1583 | 164 | 2026-11-21 22:54:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9253 | 624 | 1062 | 623 | 167 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8803 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7367 | 480 | 911 | 2678 | 344 | 2026-11-18 11:55:16 |
| [hug](https://github.com/hugapi/hug) | 6868 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5641 | 549 | 1311 | 996 | 560 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5458 | 1054 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4482 | 395 | 1212 | 259 | 116 | 2026-11-22 15:57:45 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2754 | 85 | 2026-11-22 03:16:11 |
| [databases](https://github.com/encode/databases) | 3984 | 368 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 214 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1434 | 255 | 2026-11-23 04:40:46 |
| [anyio](https://github.com/agronholm/anyio) | 2572 | 361 | 507 | 915 | 166 | 2026-11-21 14:17:49 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5305 | 475 | 725 | 2026-11-23 05:12:53 |
| [jython](https://github.com/jython/jython) | 1549 | 238 | 306 | 165 | 110 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-23T07:14:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
