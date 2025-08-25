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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191308 | 74790 | 40745 | 56532 | 1488 | 2025-08-24 19:54:11 |
| [transformers](https://github.com/huggingface/transformers) | 148758 | 30158 | 17826 | 22012 | 1974 | 2025-08-24 19:32:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 92652 | 25070 | 53289 | 107630 | 16920 | 2025-08-25 01:59:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 88743 | 7762 | 3466 | 4665 | 280 | 2025-08-20 09:12:14 |
| [django](https://github.com/django/django) | 84727 | 32853 | 0 | 19704 | 363 | 2025-08-23 18:07:08 |
| [flask](https://github.com/pallets/flask) | 70215 | 16519 | 2692 | 2688 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68515 | 32677 | 73380 | 63813 | 9307 | 2025-08-25 01:48:29 |
| [keras](https://github.com/keras-team/keras) | 63361 | 19611 | 12528 | 8299 | 296 | 2025-08-22 17:48:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63116 | 26172 | 11656 | 19217 | 2162 | 2025-08-23 15:40:04 |
| [pandas](https://github.com/pandas-dev/pandas) | 46393 | 18850 | 27669 | 34463 | 3704 | 2025-08-22 16:50:55 |
| [ray](https://github.com/ray-project/ray) | 38612 | 6734 | 20933 | 34589 | 3012 | 2025-08-24 22:05:20 |
| [gym](https://github.com/openai/gym) | 36408 | 8692 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32228 | 4567 | 5718 | 4065 | 200 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30238 | 11253 | 13496 | 16056 | 2342 | 2025-08-24 20:23:17 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29397 | 6995 | 3945 | 4828 | 98 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27078 | 4830 | 5157 | 3642 | 763 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23976 | 2190 | 1978 | 1319 | 552 | 2025-08-22 21:25:47 |
| [tornado](https://github.com/tornadoweb/tornado) | 22110 | 5538 | 1851 | 1670 | 206 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21607 | 7967 | 10950 | 19471 | 1635 | 2025-08-24 14:54:36 |
| [micropython](https://github.com/micropython/micropython) | 20752 | 8381 | 5795 | 7127 | 1774 | 2025-08-25 01:15:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 20431 | 1341 | 1210 | 4832 | 442 | 2025-08-24 08:44:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18483 | 1579 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17643 | 2703 | 3243 | 1945 | 721 | 2025-08-22 14:56:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15938 | 2114 | 3143 | 8006 | 262 | 2025-08-24 23:44:29 |
| [httpx](https://github.com/encode/httpx) | 14493 | 946 | 915 | 1708 | 103 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13952 | 5452 | 10976 | 12508 | 1760 | 2025-08-24 22:18:50 |
| [dask](https://github.com/dask/dask) | 13429 | 1794 | 5426 | 6334 | 1194 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13383 | 2029 | 2624 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11371 | 1032 | 750 | 1682 | 48 | 2025-08-24 13:36:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11171 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10812 | 1577 | 8071 | 978 | 236 | 2025-08-22 17:07:29 |
| [falcon](https://github.com/falconry/falcon) | 9704 | 959 | 1093 | 1361 | 156 | 2025-08-24 13:51:01 |
| [bottle](https://github.com/bottlepy/bottle) | 8648 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8458 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6747 | 364 | 864 | 2445 | 314 | 2025-08-23 20:10:19 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5257 | 435 | 1186 | 711 | 495 | 2025-08-24 10:55:31 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4954 | 927 | 864 | 257 | 158 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4042 | 891 | 1061 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3547 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3409 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2678 | 304 | 649 | 1261 | 307 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2180 | 165 | 399 | 500 | 67 | 2025-08-21 08:46:43 |
| [web2py](https://github.com/web2py/web2py) | 2155 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-18 17:39:32 |
| [pypy](https://github.com/pypy/pypy) | 1481 | 83 | 5142 | 168 | 736 | 2025-08-24 20:03:07 |
| [jython](https://github.com/jython/jython) | 1426 | 218 | 280 | 113 | 99 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 100 | 36 | 15 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-25T02:07:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
