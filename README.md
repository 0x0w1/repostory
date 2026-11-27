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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201871 | 77376 | 42008 | 85116 | 3397 | 2026-11-27 07:56:20 |
| [transformers](https://github.com/huggingface/transformers) | 169389 | 35319 | 19980 | 30509 | 1183 | 2026-11-27 07:58:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 105804 | 30679 | 63114 | 142989 | 18661 | 2026-11-27 07:57:00 |
| [fastapi](https://github.com/fastapi/fastapi) | 105091 | 10380 | 3556 | 6656 | 47 | 2026-11-24 11:14:37 |
| [django](https://github.com/django/django) | 91933 | 35066 | 0 | 22255 | 536 | 2026-11-26 14:12:47 |
| [cpython](https://github.com/python/cpython) | 78487 | 36536 | 79411 | 80828 | 9379 | 2026-11-26 23:25:38 |
| [flask](https://github.com/pallets/flask) | 75312 | 17307 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68358 | 27705 | 12407 | 21929 | 2167 | 2026-11-26 19:13:44 |
| [keras](https://github.com/keras-team/keras) | 64455 | 19806 | 13125 | 10350 | 278 | 2026-11-26 05:31:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 50657 | 20725 | 28719 | 40191 | 1810 | 2026-11-26 21:28:01 |
| [ray](https://github.com/ray-project/ray) | 44392 | 8311 | 23381 | 44734 | 3901 | 2026-11-27 05:41:36 |
| [gym](https://github.com/openai/gym) | 37233 | 8662 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34095 | 4754 | 5786 | 4156 | 278 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33490 | 13074 | 14228 | 19146 | 2271 | 2026-11-27 03:32:48 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30267 | 7108 | 3966 | 5124 | 58 | 2026-11-26 12:58:43 |
| [celery](https://github.com/celery/celery) | 29273 | 5274 | 5408 | 4767 | 790 | 2026-11-26 14:56:03 |
| [dash](https://github.com/plotly/dash) | 24507 | 2353 | 2192 | 1881 | 403 | 2026-11-26 20:03:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23514 | 8584 | 11474 | 21127 | 1461 | 2026-11-27 01:36:56 |
| [RustPython](https://github.com/RustPython/RustPython) | 22510 | 1511 | 1476 | 8462 | 332 | 2026-11-26 13:47:06 |
| [micropython](https://github.com/micropython/micropython) | 22238 | 9078 | 6193 | 8306 | 1596 | 2026-11-27 00:08:28 |
| [tornado](https://github.com/tornadoweb/tornado) | 22171 | 5624 | 1903 | 1976 | 174 | 2026-11-25 20:27:47 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18945 | 2911 | 3409 | 2306 | 738 | 2026-11-27 07:35:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1621 | 1475 | 1698 | 169 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16624 | 2548 | 3282 | 10821 | 338 | 2026-11-27 03:37:48 |
| [httpx](https://github.com/encode/httpx) | 15863 | 2014 | 925 | 1842 | 164 | 2026-11-26 16:06:39 |
| [scipy](https://github.com/scipy/scipy) | 15262 | 6134 | 11805 | 15004 | 1944 | 2026-11-27 07:46:38 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14125 | 2174 | 2669 | 1272 | 269 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13960 | 2040 | 5585 | 6904 | 1458 | 2026-11-26 13:13:10 |
| [starlette](https://github.com/Kludex/starlette) | 12776 | 1464 | 797 | 2306 | 37 | 2026-11-24 10:49:23 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12313 | 1968 | 8411 | 1265 | 219 | 2026-11-24 19:36:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11949 | 624 | 431 | 349 | 177 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9823 | 1056 | 1154 | 1585 | 161 | 2026-11-25 07:07:00 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9260 | 624 | 1062 | 624 | 168 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1511 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7367 | 478 | 911 | 2677 | 343 | 2026-11-24 00:03:10 |
| [hug](https://github.com/hugapi/hug) | 6869 | 391 | 466 | 466 | 190 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5644 | 552 | 1311 | 1000 | 564 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5462 | 1055 | 940 | 337 | 197 | 2026-11-25 09:36:21 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4486 | 396 | 1212 | 258 | 116 | 2026-11-22 15:57:45 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2762 | 76 | 2026-11-27 06:50:33 |
| [databases](https://github.com/encode/databases) | 3983 | 373 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 216 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 320 | 683 | 1441 | 257 | 2026-11-27 03:43:57 |
| [anyio](https://github.com/agronholm/anyio) | 2577 | 369 | 509 | 929 | 174 | 2026-11-27 00:54:02 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1086 | 1613 | 357 | 2026-11-23 17:40:38 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-23 18:08:22 |
| [pypy](https://github.com/pypy/pypy) | 1828 | 133 | 5307 | 486 | 723 | 2026-11-27 04:09:03 |
| [jython](https://github.com/jython/jython) | 1550 | 238 | 307 | 166 | 111 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 85 | 104 | 40 | 18 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-27T07:59:37*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
