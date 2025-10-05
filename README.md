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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191911 | 74900 | 40837 | 58782 | 1815 | 2025-10-04 21:53:58 |
| [transformers](https://github.com/huggingface/transformers) | 150625 | 30635 | 18013 | 22742 | 2023 | 2025-10-04 09:02:15 |
| [pytorch](https://github.com/pytorch/pytorch) | 93687 | 25477 | 54115 | 110098 | 16900 | 2025-10-05 01:36:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 90366 | 7998 | 3470 | 4758 | 206 | 2025-10-04 05:59:15 |
| [django](https://github.com/django/django) | 85313 | 33052 | 0 | 19853 | 341 | 2025-10-03 21:12:58 |
| [flask](https://github.com/pallets/flask) | 70490 | 16549 | 2698 | 2705 | 9 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69128 | 32995 | 73782 | 64874 | 9310 | 2025-10-05 01:53:16 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63558 | 26291 | 11744 | 19500 | 2164 | 2025-10-03 10:46:08 |
| [keras](https://github.com/keras-team/keras) | 63451 | 19623 | 12562 | 8373 | 261 | 2025-10-04 02:18:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 46734 | 19071 | 27761 | 34770 | 3687 | 2025-10-04 16:29:10 |
| [ray](https://github.com/ray-project/ray) | 39187 | 6851 | 21276 | 35571 | 3143 | 2025-10-05 01:21:49 |
| [gym](https://github.com/openai/gym) | 36617 | 8703 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32583 | 4589 | 5722 | 4070 | 206 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30497 | 11507 | 13571 | 16241 | 2356 | 2025-10-04 16:28:57 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29530 | 7010 | 3945 | 4840 | 104 | 2025-09-25 12:59:12 |
| [celery](https://github.com/celery/celery) | 27291 | 4856 | 5169 | 3674 | 754 | 2025-10-04 11:49:01 |
| [dash](https://github.com/plotly/dash) | 24130 | 2207 | 2004 | 1347 | 577 | 2025-10-03 23:07:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22258 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21763 | 8052 | 10999 | 19590 | 1629 | 2025-10-03 17:30:42 |
| [micropython](https://github.com/micropython/micropython) | 20898 | 8464 | 5839 | 7248 | 1769 | 2025-10-04 06:28:26 |
| [RustPython](https://github.com/RustPython/RustPython) | 20570 | 1350 | 1221 | 4896 | 450 | 2025-09-30 00:07:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18501 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17801 | 2720 | 3258 | 1959 | 719 | 2025-10-03 19:12:17 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16023 | 2126 | 3146 | 8112 | 275 | 2025-10-04 17:49:26 |
| [httpx](https://github.com/encode/httpx) | 14601 | 958 | 918 | 1734 | 100 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14058 | 5490 | 11059 | 12656 | 1756 | 2025-10-04 17:22:59 |
| [dask](https://github.com/dask/dask) | 13507 | 1801 | 5440 | 6355 | 1200 | 2025-10-03 18:13:00 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13478 | 2037 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11516 | 1045 | 754 | 1717 | 47 | 2025-10-02 20:15:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11304 | 575 | 389 | 289 | 143 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10960 | 1584 | 8093 | 988 | 225 | 2025-10-03 19:08:54 |
| [falcon](https://github.com/falconry/falcon) | 9723 | 963 | 1102 | 1372 | 160 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8670 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8600 | 527 | 947 | 439 | 412 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6878 | 367 | 872 | 2457 | 311 | 2025-10-03 07:56:14 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5630 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5317 | 438 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5022 | 946 | 871 | 261 | 169 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3664 | 292 | 1160 | 196 | 117 | 2025-10-04 00:44:51 |
| [quart](https://github.com/pallets/quart) | 3474 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2690 | 303 | 651 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2313 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2229 | 165 | 404 | 522 | 65 | 2025-10-03 08:03:26 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-09-29 17:34:25 |
| [pypy](https://github.com/pypy/pypy) | 1508 | 88 | 5149 | 171 | 739 | 2025-10-03 06:56:12 |
| [jython](https://github.com/jython/jython) | 1437 | 224 | 283 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-09-22 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-05T02:04:40*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
