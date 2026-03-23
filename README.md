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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194321 | 75255 | 41250 | 69609 | 3916 | 2026-03-23 02:26:41 |
| [transformers](https://github.com/huggingface/transformers) | 158264 | 32575 | 18755 | 25551 | 2313 | 2026-03-22 23:03:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 98496 | 27274 | 57436 | 120163 | 18069 | 2026-03-23 02:49:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 96503 | 8911 | 3513 | 5496 | 165 | 2026-03-20 17:07:26 |
| [django](https://github.com/django/django) | 87136 | 33780 | 0 | 20897 | 434 | 2026-03-21 14:50:19 |
| [cpython](https://github.com/python/cpython) | 72094 | 34278 | 75668 | 69629 | 9335 | 2026-03-22 23:58:31 |
| [flask](https://github.com/pallets/flask) | 71405 | 16758 | 2724 | 2790 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65509 | 26835 | 12010 | 20438 | 2161 | 2026-03-22 13:11:06 |
| [keras](https://github.com/keras-team/keras) | 63952 | 19741 | 12677 | 8994 | 269 | 2026-03-21 20:39:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 48215 | 19774 | 28197 | 36511 | 3615 | 2026-03-23 01:52:16 |
| [ray](https://github.com/ray-project/ray) | 41841 | 7374 | 22481 | 39139 | 3516 | 2026-03-23 01:19:10 |
| [gym](https://github.com/openai/gym) | 37114 | 8705 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33371 | 4661 | 5746 | 4084 | 196 | 2026-03-22 19:35:31 |
| [numpy](https://github.com/numpy/numpy) | 31641 | 12186 | 13843 | 17138 | 2338 | 2026-03-22 16:04:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29935 | 7077 | 3947 | 4948 | 80 | 2026-03-19 14:26:11 |
| [celery](https://github.com/celery/celery) | 28292 | 4995 | 5209 | 3872 | 772 | 2026-03-20 22:13:14 |
| [dash](https://github.com/plotly/dash) | 24477 | 2269 | 2079 | 1483 | 595 | 2026-03-20 20:04:42 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22612 | 8275 | 11212 | 20088 | 1541 | 2026-03-22 22:57:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5548 | 1865 | 1721 | 213 | 2026-03-20 11:40:59 |
| [RustPython](https://github.com/RustPython/RustPython) | 21897 | 1412 | 1318 | 6091 | 360 | 2026-03-23 02:31:30 |
| [micropython](https://github.com/micropython/micropython) | 21572 | 8754 | 5992 | 7646 | 1835 | 2026-03-22 12:50:38 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1587 | 1465 | 1673 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18372 | 2787 | 3330 | 2058 | 774 | 2026-03-20 15:31:47 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16406 | 2229 | 3184 | 8765 | 278 | 2026-03-19 11:01:01 |
| [httpx](https://github.com/encode/httpx) | 15164 | 1084 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14554 | 5665 | 11383 | 13485 | 1782 | 2026-03-21 22:50:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13777 | 2089 | 2648 | 1165 | 210 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13774 | 1861 | 5518 | 6509 | 1231 | 2026-03-19 09:37:28 |
| [starlette](https://github.com/Kludex/starlette) | 12051 | 1142 | 767 | 1840 | 46 | 2026-03-22 18:27:00 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11712 | 1655 | 8173 | 1050 | 210 | 2026-03-20 20:37:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11710 | 604 | 410 | 318 | 160 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 983 | 1119 | 1422 | 164 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8962 | 565 | 1025 | 497 | 218 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8769 | 1503 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7214 | 392 | 882 | 2516 | 315 | 2026-03-21 21:37:53 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 734 | 979 | 587 | 26 | 2026-03-19 09:45:14 |
| [vibora](https://github.com/vibora-io/vibora) | 5606 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5526 | 469 | 1244 | 805 | 499 | 2026-03-21 22:19:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5214 | 1002 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4024 | 322 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4018 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3610 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 313 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2415 | 190 | 431 | 591 | 85 | 2026-03-22 21:04:57 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-16 17:53:47 |
| [pypy](https://github.com/pypy/pypy) | 1688 | 106 | 5185 | 190 | 764 | 2026-03-22 23:54:45 |
| [jython](https://github.com/jython/jython) | 1493 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-23T02:56:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
