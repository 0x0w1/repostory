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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191427 | 74807 | 40761 | 56797 | 1510 | 2025-09-01 23:28:00 |
| [transformers](https://github.com/huggingface/transformers) | 149052 | 30229 | 17860 | 22163 | 1964 | 2025-09-01 19:55:33 |
| [pytorch](https://github.com/pytorch/pytorch) | 92843 | 25147 | 53440 | 108029 | 17034 | 2025-09-02 01:49:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 89027 | 7813 | 3467 | 4685 | 272 | 2025-09-01 17:33:14 |
| [django](https://github.com/django/django) | 84858 | 32877 | 0 | 19740 | 361 | 2025-09-01 19:31:21 |
| [flask](https://github.com/pallets/flask) | 70270 | 16513 | 2694 | 2692 | 5 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68656 | 32720 | 73460 | 63969 | 9328 | 2025-09-02 00:14:24 |
| [keras](https://github.com/keras-team/keras) | 63382 | 19618 | 12532 | 8311 | 286 | 2025-09-01 21:29:46 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63201 | 26185 | 11670 | 19271 | 2169 | 2025-09-01 12:57:24 |
| [pandas](https://github.com/pandas-dev/pandas) | 46449 | 18867 | 27682 | 34500 | 3699 | 2025-09-01 21:41:42 |
| [ray](https://github.com/ray-project/ray) | 38734 | 6755 | 21008 | 34785 | 3059 | 2025-09-01 19:43:23 |
| [gym](https://github.com/openai/gym) | 36439 | 8688 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32395 | 4573 | 5719 | 4067 | 202 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30284 | 11283 | 13507 | 16075 | 2348 | 2025-09-01 21:12:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29424 | 6999 | 3945 | 4829 | 99 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27121 | 4837 | 5157 | 3650 | 751 | 2025-08-31 09:27:30 |
| [dash](https://github.com/plotly/dash) | 24000 | 2196 | 1983 | 1324 | 559 | 2025-09-01 00:44:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22137 | 5540 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21638 | 7983 | 10960 | 19500 | 1640 | 2025-09-01 23:21:13 |
| [micropython](https://github.com/micropython/micropython) | 20780 | 8398 | 5803 | 7153 | 1782 | 2025-09-01 04:52:08 |
| [RustPython](https://github.com/RustPython/RustPython) | 20453 | 1341 | 1211 | 4844 | 444 | 2025-09-01 19:53:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18483 | 1581 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17676 | 2705 | 3246 | 1946 | 720 | 2025-08-29 20:22:39 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15956 | 2118 | 3144 | 8012 | 263 | 2025-08-31 23:26:33 |
| [httpx](https://github.com/encode/httpx) | 14513 | 948 | 916 | 1711 | 106 | 2025-09-01 21:45:34 |
| [scipy](https://github.com/scipy/scipy) | 13975 | 5460 | 10990 | 12533 | 1757 | 2025-09-01 18:04:47 |
| [dask](https://github.com/dask/dask) | 13452 | 1795 | 5427 | 6337 | 1194 | 2025-08-29 02:11:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13409 | 2029 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11411 | 1034 | 751 | 1685 | 50 | 2025-09-02 00:21:19 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11211 | 570 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10840 | 1577 | 8076 | 979 | 228 | 2025-08-31 21:11:08 |
| [falcon](https://github.com/falconry/falcon) | 9710 | 959 | 1096 | 1364 | 156 | 2025-08-31 19:21:18 |
| [bottle](https://github.com/bottlepy/bottle) | 8655 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8494 | 519 | 937 | 432 | 404 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6893 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6762 | 365 | 864 | 2446 | 312 | 2025-09-01 03:43:09 |
| [eve](https://github.com/pyeve/eve) | 6728 | 747 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5269 | 435 | 1188 | 712 | 496 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4971 | 931 | 865 | 258 | 160 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4043 | 891 | 1061 | 2718 | 88 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3565 | 290 | 1155 | 195 | 115 | 2025-08-28 16:27:29 |
| [quart](https://github.com/pallets/quart) | 3426 | 187 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2681 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2304 | 131 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2189 | 164 | 399 | 502 | 68 | 2025-09-01 17:42:57 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 908 | 1077 | 1458 | 369 | 2025-09-01 17:32:42 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-09-01 17:37:10 |
| [pypy](https://github.com/pypy/pypy) | 1488 | 84 | 5142 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1429 | 219 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-02T02:00:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
