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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192553 | 74997 | 41021 | 61996 | 2540 | 2025-11-26 02:05:41 |
| [transformers](https://github.com/huggingface/transformers) | 153007 | 31221 | 18229 | 23580 | 2123 | 2025-11-26 00:27:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 95363 | 26014 | 55550 | 113054 | 17729 | 2025-11-26 01:36:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 92390 | 8278 | 3477 | 4904 | 224 | 2025-11-24 19:17:19 |
| [django](https://github.com/django/django) | 85931 | 33259 | 0 | 20259 | 365 | 2025-11-25 22:17:00 |
| [flask](https://github.com/pallets/flask) | 70834 | 16634 | 2704 | 2725 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69998 | 33508 | 74446 | 66545 | 9185 | 2025-11-26 00:00:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64135 | 26473 | 11826 | 19830 | 2113 | 2025-11-25 14:51:11 |
| [keras](https://github.com/keras-team/keras) | 63600 | 19658 | 12596 | 8482 | 263 | 2025-11-25 23:57:02 |
| [pandas](https://github.com/pandas-dev/pandas) | 47187 | 19341 | 27904 | 35243 | 3616 | 2025-11-25 21:10:02 |
| [ray](https://github.com/ray-project/ray) | 40011 | 6943 | 21919 | 36722 | 3242 | 2025-11-26 02:04:46 |
| [gym](https://github.com/openai/gym) | 36806 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32865 | 4629 | 5732 | 4074 | 183 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30899 | 11749 | 13667 | 16575 | 2365 | 2025-11-25 22:12:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29686 | 7043 | 3946 | 4875 | 94 | 2025-11-25 11:07:20 |
| [celery](https://github.com/celery/celery) | 27618 | 4906 | 5176 | 3730 | 753 | 2025-11-24 16:54:38 |
| [dash](https://github.com/plotly/dash) | 24274 | 2238 | 2029 | 1379 | 579 | 2025-11-25 17:00:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22360 | 5544 | 1854 | 1676 | 204 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22047 | 8129 | 11054 | 19691 | 1615 | 2025-11-25 16:30:45 |
| [micropython](https://github.com/micropython/micropython) | 21128 | 8547 | 5882 | 7381 | 1800 | 2025-11-26 01:59:30 |
| [RustPython](https://github.com/RustPython/RustPython) | 20838 | 1361 | 1237 | 4995 | 444 | 2025-11-25 11:04:30 |
| [sanic](https://github.com/sanic-org/sanic) | 18580 | 1585 | 1453 | 1630 | 151 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18016 | 2747 | 3297 | 1984 | 748 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16107 | 2156 | 3163 | 8308 | 288 | 2025-11-24 16:26:04 |
| [httpx](https://github.com/encode/httpx) | 14775 | 980 | 923 | 1756 | 114 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14209 | 5548 | 11154 | 12889 | 1769 | 2025-11-26 00:31:34 |
| [dask](https://github.com/dask/dask) | 13616 | 1826 | 5467 | 6408 | 1195 | 2025-11-25 14:34:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13578 | 2052 | 2634 | 1149 | 194 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11694 | 1084 | 760 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11448 | 586 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11173 | 1600 | 8120 | 1006 | 211 | 2025-11-25 20:57:02 |
| [falcon](https://github.com/falconry/falcon) | 9760 | 972 | 1113 | 1403 | 163 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8732 | 539 | 974 | 454 | 178 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8699 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7015 | 372 | 874 | 2472 | 314 | 2025-11-24 22:19:44 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 979 | 577 | 33 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5625 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5393 | 446 | 1200 | 719 | 505 | 2025-11-25 02:03:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5095 | 970 | 877 | 263 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4064 | 887 | 1062 | 2722 | 90 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4053 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3779 | 302 | 1168 | 201 | 115 | 2025-11-20 22:26:20 |
| [quart](https://github.com/pallets/quart) | 3549 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2710 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2302 | 177 | 415 | 551 | 74 | 2025-11-25 00:03:59 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 372 | 1784 | 266 | 265 | 2025-11-24 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1578 | 90 | 5164 | 172 | 748 | 2025-11-24 21:06:55 |
| [jython](https://github.com/jython/jython) | 1459 | 225 | 286 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-26T02:06:03*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
