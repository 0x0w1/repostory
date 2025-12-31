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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193128 | 75154 | 41051 | 64079 | 2642 | 2025-12-31 02:16:13 |
| [transformers](https://github.com/huggingface/transformers) | 154429 | 31585 | 18381 | 24089 | 2168 | 2025-12-24 15:30:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 96248 | 26392 | 56094 | 114967 | 17934 | 2025-12-31 02:19:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 93583 | 8448 | 3499 | 5059 | 199 | 2025-12-29 18:54:44 |
| [django](https://github.com/django/django) | 86310 | 33424 | 0 | 20413 | 371 | 2025-12-30 21:21:57 |
| [flask](https://github.com/pallets/flask) | 70990 | 16668 | 2707 | 2742 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70529 | 33778 | 74844 | 67479 | 9240 | 2025-12-31 00:45:44 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64426 | 26547 | 11865 | 19969 | 2127 | 2025-12-29 12:23:49 |
| [keras](https://github.com/keras-team/keras) | 63678 | 19661 | 12607 | 8565 | 239 | 2025-12-30 00:48:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 47450 | 19460 | 27988 | 35466 | 3593 | 2025-12-30 23:48:29 |
| [ray](https://github.com/ray-project/ray) | 40554 | 7056 | 22083 | 37342 | 3265 | 2025-12-31 01:34:04 |
| [gym](https://github.com/openai/gym) | 36917 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33012 | 4630 | 5736 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31117 | 11902 | 13723 | 16764 | 2386 | 2025-12-30 18:27:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29773 | 7047 | 3946 | 4893 | 81 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27801 | 4925 | 5178 | 3753 | 756 | 2025-12-29 21:48:53 |
| [dash](https://github.com/plotly/dash) | 24374 | 2246 | 2039 | 1397 | 555 | 2025-12-30 20:50:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22406 | 5545 | 1862 | 1690 | 210 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22170 | 8163 | 11094 | 19774 | 1544 | 2025-12-30 18:46:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21515 | 1393 | 1271 | 5268 | 394 | 2025-12-31 00:49:04 |
| [micropython](https://github.com/micropython/micropython) | 21266 | 8614 | 5911 | 7461 | 1821 | 2025-12-30 13:40:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1584 | 1457 | 1649 | 122 | 2025-12-29 09:17:46 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18132 | 2768 | 3309 | 1995 | 759 | 2025-12-24 16:24:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16166 | 2170 | 3168 | 8407 | 267 | 2025-12-30 10:34:11 |
| [httpx](https://github.com/encode/httpx) | 14874 | 1000 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14298 | 5571 | 11218 | 13020 | 1766 | 2025-12-30 23:33:35 |
| [dask](https://github.com/dask/dask) | 13674 | 1830 | 5481 | 6431 | 1206 | 2025-12-30 21:46:45 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13648 | 2071 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11798 | 1094 | 760 | 1754 | 55 | 2025-12-24 11:58:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11552 | 594 | 399 | 299 | 151 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11332 | 1612 | 8133 | 1017 | 209 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8817 | 551 | 987 | 475 | 192 | 2025-12-26 14:55:26 |
| [bottle](https://github.com/bottlepy/bottle) | 8719 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7085 | 376 | 877 | 2483 | 312 | 2025-12-30 23:04:16 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5427 | 444 | 1212 | 734 | 510 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5128 | 980 | 882 | 273 | 177 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4019 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3856 | 305 | 1172 | 207 | 119 | 2025-12-26 20:05:52 |
| [quart](https://github.com/pallets/quart) | 3567 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2342 | 181 | 421 | 562 | 75 | 2025-12-31 01:53:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1928 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1617 | 93 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1463 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-31T02:20:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
