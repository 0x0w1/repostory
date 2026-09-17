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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200151 | 76624 | 41777 | 82166 | 3146 | 2026-09-17 04:25:21 |
| [transformers](https://github.com/huggingface/transformers) | 166262 | 34607 | 19481 | 28630 | 2436 | 2026-09-17 04:22:58 |
| [pytorch](https://github.com/pytorch/pytorch) | 103060 | 29537 | 61012 | 135701 | 17638 | 2026-09-17 04:25:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 102372 | 9900 | 3552 | 6338 | 82 | 2026-09-14 18:49:48 |
| [django](https://github.com/django/django) | 91088 | 34552 | 0 | 21850 | 501 | 2026-09-16 09:59:07 |
| [cpython](https://github.com/python/cpython) | 77187 | 35644 | 78158 | 77139 | 9654 | 2026-09-17 02:59:36 |
| [flask](https://github.com/pallets/flask) | 74744 | 16986 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67279 | 27414 | 12282 | 21497 | 2159 | 2026-09-17 04:21:47 |
| [keras](https://github.com/keras-team/keras) | 64318 | 19793 | 12913 | 9880 | 206 | 2026-09-16 23:51:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 49734 | 20391 | 28546 | 38791 | 2713 | 2026-09-16 21:50:05 |
| [ray](https://github.com/ray-project/ray) | 43837 | 8045 | 23073 | 42731 | 3588 | 2026-09-17 03:28:34 |
| [gym](https://github.com/openai/gym) | 37241 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33903 | 4722 | 5772 | 4123 | 243 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32756 | 12807 | 14100 | 18475 | 2291 | 2026-09-17 01:37:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30183 | 7081 | 3966 | 5067 | 50 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28893 | 5168 | 5301 | 4387 | 729 | 2026-09-17 03:25:09 |
| [dash](https://github.com/plotly/dash) | 24409 | 2313 | 2152 | 1704 | 476 | 2026-09-16 21:10:01 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23220 | 8484 | 11424 | 20869 | 1483 | 2026-09-16 06:18:56 |
| [RustPython](https://github.com/RustPython/RustPython) | 22351 | 1487 | 1425 | 7224 | 397 | 2026-09-16 17:28:31 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5555 | 1883 | 1826 | 259 | 2026-09-16 18:23:07 |
| [micropython](https://github.com/micropython/micropython) | 22069 | 8973 | 6127 | 8098 | 1531 | 2026-09-16 23:31:27 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18789 | 2846 | 3384 | 2186 | 715 | 2026-09-15 21:35:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1598 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16548 | 2410 | 3253 | 10132 | 222 | 2026-09-17 04:20:03 |
| [httpx](https://github.com/encode/httpx) | 15485 | 1341 | 925 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15017 | 5939 | 11647 | 14520 | 1841 | 2026-09-16 21:09:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14023 | 2132 | 2662 | 1223 | 234 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13920 | 1956 | 5558 | 6727 | 1336 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12616 | 1311 | 782 | 2117 | 48 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12162 | 1784 | 8300 | 1209 | 209 | 2026-09-15 21:07:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11898 | 616 | 420 | 331 | 161 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 1033 | 1142 | 1519 | 159 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9192 | 613 | 1045 | 549 | 222 | 2026-09-14 13:10:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1510 | 868 | 651 | 292 | 2026-09-15 07:20:39 |
| [trio](https://github.com/python-trio/trio) | 7330 | 430 | 901 | 2608 | 327 | 2026-09-17 02:12:00 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5631 | 515 | 1270 | 903 | 525 | 2026-09-15 14:26:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5391 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4400 | 376 | 1202 | 250 | 119 | 2026-09-11 19:10:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3991 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3668 | 206 | 287 | 136 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2544 | 265 | 477 | 772 | 109 | 2026-09-15 17:39:30 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 136 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1796 | 125 | 5257 | 303 | 711 | 2026-09-17 04:25:35 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-17T04:39:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
