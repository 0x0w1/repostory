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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191404 | 74810 | 40758 | 56775 | 1508 | 2025-09-01 01:24:17 |
| [transformers](https://github.com/huggingface/transformers) | 149009 | 30225 | 17857 | 22142 | 1979 | 2025-08-31 17:14:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 92813 | 25142 | 53420 | 107990 | 16998 | 2025-09-01 02:20:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 88987 | 7808 | 3467 | 4678 | 265 | 2025-08-31 19:34:37 |
| [django](https://github.com/django/django) | 84843 | 32877 | 0 | 19737 | 360 | 2025-08-31 06:18:23 |
| [flask](https://github.com/pallets/flask) | 70263 | 16517 | 2693 | 2692 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68636 | 32719 | 73449 | 63930 | 9327 | 2025-08-31 22:50:29 |
| [keras](https://github.com/keras-team/keras) | 63379 | 19618 | 12532 | 8311 | 290 | 2025-08-29 18:53:49 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63194 | 26182 | 11668 | 19261 | 2171 | 2025-08-31 14:47:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 46449 | 18869 | 27682 | 34497 | 3700 | 2025-08-29 18:19:41 |
| [ray](https://github.com/ray-project/ray) | 38724 | 6749 | 21003 | 34773 | 3048 | 2025-08-31 23:02:08 |
| [gym](https://github.com/openai/gym) | 36431 | 8689 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32385 | 4574 | 5719 | 4067 | 203 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30275 | 11279 | 13505 | 16073 | 2348 | 2025-08-29 02:48:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29421 | 6999 | 3945 | 4828 | 98 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27115 | 4835 | 5157 | 3650 | 751 | 2025-08-31 09:27:30 |
| [dash](https://github.com/plotly/dash) | 23995 | 2194 | 1983 | 1322 | 557 | 2025-09-01 00:44:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22132 | 5541 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21629 | 7983 | 10959 | 19500 | 1640 | 2025-08-31 08:01:08 |
| [micropython](https://github.com/micropython/micropython) | 20776 | 8395 | 5800 | 7152 | 1779 | 2025-08-29 04:03:19 |
| [RustPython](https://github.com/RustPython/RustPython) | 20447 | 1341 | 1211 | 4840 | 442 | 2025-08-29 16:02:38 |
| [sanic](https://github.com/sanic-org/sanic) | 18483 | 1581 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17671 | 2706 | 3245 | 1946 | 719 | 2025-08-29 20:22:39 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15954 | 2117 | 3144 | 8012 | 264 | 2025-08-31 23:26:33 |
| [httpx](https://github.com/encode/httpx) | 14511 | 948 | 916 | 1711 | 107 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13975 | 5460 | 10989 | 12530 | 1756 | 2025-08-31 14:25:11 |
| [dask](https://github.com/dask/dask) | 13449 | 1795 | 5426 | 6337 | 1193 | 2025-08-29 02:11:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13408 | 2028 | 2625 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11406 | 1034 | 751 | 1685 | 51 | 2025-08-24 13:36:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11210 | 570 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10841 | 1577 | 8076 | 979 | 228 | 2025-08-31 21:11:08 |
| [falcon](https://github.com/falconry/falcon) | 9710 | 959 | 1095 | 1364 | 155 | 2025-08-31 19:21:18 |
| [bottle](https://github.com/bottlepy/bottle) | 8655 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8486 | 519 | 936 | 430 | 403 | 2025-08-28 13:12:57 |
| [hug](https://github.com/hugapi/hug) | 6893 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6761 | 365 | 864 | 2446 | 314 | 2025-09-01 02:03:13 |
| [eve](https://github.com/pyeve/eve) | 6728 | 747 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5268 | 435 | 1188 | 712 | 496 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4969 | 932 | 865 | 258 | 160 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4043 | 891 | 1061 | 2718 | 88 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3563 | 290 | 1155 | 195 | 115 | 2025-08-28 16:27:29 |
| [quart](https://github.com/pallets/quart) | 3425 | 186 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2681 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2303 | 131 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2188 | 165 | 399 | 501 | 67 | 2025-08-25 19:02:47 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 908 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-08-30 13:15:28 |
| [pypy](https://github.com/pypy/pypy) | 1487 | 84 | 5142 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1429 | 218 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-01T02:20:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
