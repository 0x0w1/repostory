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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193076 | 75153 | 41051 | 63973 | 2562 | 2025-12-28 01:50:27 |
| [transformers](https://github.com/huggingface/transformers) | 154313 | 31560 | 18376 | 24078 | 2163 | 2025-12-24 15:30:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 96158 | 26372 | 56061 | 114836 | 17950 | 2025-12-28 02:21:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 93475 | 8435 | 3499 | 5053 | 196 | 2025-12-27 19:06:15 |
| [django](https://github.com/django/django) | 86267 | 33420 | 0 | 20407 | 375 | 2025-12-27 09:42:24 |
| [flask](https://github.com/pallets/flask) | 70973 | 16667 | 2707 | 2740 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70484 | 33759 | 74829 | 67428 | 9252 | 2025-12-27 17:20:49 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64387 | 26539 | 11863 | 19956 | 2121 | 2025-12-26 10:37:09 |
| [keras](https://github.com/keras-team/keras) | 63662 | 19666 | 12607 | 8560 | 244 | 2025-12-26 18:16:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 47422 | 19443 | 27986 | 35444 | 3612 | 2025-12-26 18:44:46 |
| [ray](https://github.com/ray-project/ray) | 40498 | 7048 | 22076 | 37302 | 3275 | 2025-12-28 00:37:17 |
| [gym](https://github.com/openai/gym) | 36909 | 8720 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33002 | 4630 | 5735 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31096 | 11893 | 13717 | 16748 | 2386 | 2025-12-27 14:55:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29766 | 7044 | 3946 | 4892 | 80 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27781 | 4922 | 5178 | 3749 | 753 | 2025-12-22 17:26:19 |
| [dash](https://github.com/plotly/dash) | 24367 | 2246 | 2039 | 1395 | 553 | 2025-12-22 23:39:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22403 | 5545 | 1862 | 1690 | 210 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22163 | 8157 | 11092 | 19764 | 1542 | 2025-12-27 11:16:11 |
| [micropython](https://github.com/micropython/micropython) | 21258 | 8605 | 5906 | 7457 | 1816 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 20997 | 1372 | 1265 | 5227 | 398 | 2025-12-28 01:27:58 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1585 | 1457 | 1642 | 132 | 2025-12-27 23:19:50 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18126 | 2766 | 3309 | 1995 | 759 | 2025-12-24 16:24:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16162 | 2171 | 3168 | 8402 | 267 | 2025-12-27 22:50:38 |
| [httpx](https://github.com/encode/httpx) | 14871 | 999 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14290 | 5567 | 11215 | 13006 | 1773 | 2025-12-27 22:18:17 |
| [dask](https://github.com/dask/dask) | 13669 | 1828 | 5480 | 6428 | 1206 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13645 | 2070 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11791 | 1093 | 760 | 1750 | 53 | 2025-12-24 11:58:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11547 | 592 | 399 | 299 | 151 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11319 | 1611 | 8133 | 1017 | 209 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9775 | 975 | 1115 | 1404 | 164 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8811 | 550 | 986 | 474 | 190 | 2025-12-26 14:55:26 |
| [bottle](https://github.com/bottlepy/bottle) | 8719 | 1488 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7082 | 376 | 877 | 2483 | 314 | 2025-12-22 21:33:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 740 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5424 | 444 | 1212 | 734 | 512 | 2025-12-27 04:04:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5127 | 978 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4069 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4019 | 259 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3845 | 304 | 1172 | 206 | 118 | 2025-12-26 20:05:52 |
| [quart](https://github.com/pallets/quart) | 3567 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2338 | 181 | 421 | 562 | 75 | 2025-12-27 14:03:59 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2334 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1608 | 93 | 5169 | 172 | 753 | 2025-12-26 12:30:00 |
| [jython](https://github.com/jython/jython) | 1461 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-28T02:30:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
