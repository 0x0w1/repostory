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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194428 | 75259 | 41291 | 70292 | 4044 | 2026-04-02 03:04:35 |
| [transformers](https://github.com/huggingface/transformers) | 158658 | 32708 | 18807 | 25735 | 2335 | 2026-04-02 02:17:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 98728 | 27373 | 57610 | 120974 | 18225 | 2026-04-02 03:15:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 96751 | 8983 | 3513 | 5552 | 165 | 2026-04-01 22:28:50 |
| [django](https://github.com/django/django) | 87143 | 33810 | 0 | 20974 | 422 | 2026-04-01 17:51:37 |
| [cpython](https://github.com/python/cpython) | 72137 | 34349 | 75770 | 69903 | 9332 | 2026-04-01 22:54:06 |
| [flask](https://github.com/pallets/flask) | 71361 | 16760 | 2726 | 2795 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65587 | 26872 | 12020 | 20491 | 2135 | 2026-04-01 18:17:38 |
| [keras](https://github.com/keras-team/keras) | 63923 | 19743 | 12719 | 9094 | 281 | 2026-04-02 03:07:47 |
| [pandas](https://github.com/pandas-dev/pandas) | 48321 | 19808 | 28222 | 36700 | 3506 | 2026-04-01 20:25:28 |
| [ray](https://github.com/ray-project/ray) | 41906 | 7399 | 22521 | 39417 | 3580 | 2026-04-02 03:05:03 |
| [gym](https://github.com/openai/gym) | 37124 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33406 | 4667 | 5751 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31709 | 12221 | 13859 | 17189 | 2342 | 2026-04-01 22:47:47 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29943 | 7073 | 3947 | 4955 | 77 | 2026-04-01 10:34:01 |
| [celery](https://github.com/celery/celery) | 28286 | 4997 | 5209 | 3882 | 762 | 2026-03-31 16:02:38 |
| [dash](https://github.com/plotly/dash) | 24431 | 2269 | 2084 | 1507 | 605 | 2026-04-01 23:46:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22659 | 8303 | 11225 | 20160 | 1533 | 2026-04-01 13:55:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22387 | 5543 | 1865 | 1724 | 211 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21930 | 1415 | 1325 | 6159 | 373 | 2026-03-31 12:06:17 |
| [micropython](https://github.com/micropython/micropython) | 21593 | 8773 | 6004 | 7675 | 1858 | 2026-04-01 04:01:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1588 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18409 | 2792 | 3335 | 2063 | 772 | 2026-03-30 19:12:25 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16362 | 2235 | 3185 | 8803 | 274 | 2026-04-01 14:48:31 |
| [httpx](https://github.com/encode/httpx) | 15136 | 1097 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14574 | 5676 | 11399 | 13540 | 1792 | 2026-04-01 02:20:06 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13791 | 2089 | 2651 | 1168 | 213 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13779 | 1857 | 5519 | 6512 | 1235 | 2026-03-30 22:35:39 |
| [starlette](https://github.com/Kludex/starlette) | 12166 | 1150 | 766 | 1850 | 52 | 2026-04-02 00:04:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11735 | 607 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11687 | 1663 | 8183 | 1053 | 213 | 2026-04-01 20:28:36 |
| [falcon](https://github.com/falconry/falcon) | 9802 | 981 | 1119 | 1422 | 162 | 2026-03-28 18:33:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8982 | 567 | 1024 | 498 | 219 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1499 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7222 | 394 | 882 | 2520 | 317 | 2026-04-01 01:25:20 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5603 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5536 | 471 | 1243 | 814 | 503 | 2026-04-01 22:21:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5224 | 1004 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4080 | 895 | 1064 | 2735 | 85 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4047 | 325 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4010 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3616 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 311 | 664 | 1305 | 306 | 2026-03-31 20:59:00 |
| [anyio](https://github.com/agronholm/anyio) | 2431 | 190 | 431 | 598 | 83 | 2026-03-30 19:08:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 367 | 1785 | 267 | 267 | 2026-03-30 17:40:37 |
| [pypy](https://github.com/pypy/pypy) | 1697 | 108 | 5190 | 192 | 761 | 2026-04-01 15:18:54 |
| [jython](https://github.com/jython/jython) | 1499 | 228 | 294 | 123 | 110 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-02T03:16:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
