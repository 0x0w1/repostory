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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194817 | 75279 | 41320 | 71723 | 4640 | 2026-04-22 03:25:44 |
| [transformers](https://github.com/huggingface/transformers) | 159715 | 32961 | 18885 | 26025 | 2358 | 2026-04-22 03:11:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 99330 | 27557 | 58146 | 122390 | 18525 | 2026-04-22 03:25:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 97499 | 9116 | 3518 | 5635 | 170 | 2026-04-21 22:23:27 |
| [django](https://github.com/django/django) | 87303 | 33822 | 0 | 21083 | 433 | 2026-04-20 20:49:26 |
| [cpython](https://github.com/python/cpython) | 72410 | 34464 | 76060 | 70508 | 9414 | 2026-04-21 20:31:46 |
| [flask](https://github.com/pallets/flask) | 71436 | 16807 | 2735 | 2809 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65880 | 26970 | 12045 | 20612 | 2071 | 2026-04-21 15:50:14 |
| [keras](https://github.com/keras-team/keras) | 64025 | 19761 | 12739 | 9207 | 290 | 2026-04-22 03:30:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 48545 | 19871 | 28252 | 36992 | 3399 | 2026-04-22 00:45:21 |
| [ray](https://github.com/ray-project/ray) | 42247 | 7479 | 22598 | 39888 | 3607 | 2026-04-22 03:09:46 |
| [gym](https://github.com/openai/gym) | 37172 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33497 | 4675 | 5754 | 4091 | 202 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31870 | 12307 | 13888 | 17336 | 2366 | 2026-04-21 14:57:21 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29984 | 7066 | 3968 | 5000 | 78 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28394 | 5013 | 5270 | 4082 | 781 | 2026-04-20 09:04:05 |
| [dash](https://github.com/plotly/dash) | 24202 | 2277 | 2091 | 1542 | 547 | 2026-04-21 22:45:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22732 | 8324 | 11247 | 20242 | 1500 | 2026-04-21 22:01:06 |
| [tornado](https://github.com/tornadoweb/tornado) | 22260 | 5542 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22024 | 1427 | 1333 | 6248 | 371 | 2026-04-21 23:43:14 |
| [micropython](https://github.com/micropython/micropython) | 21643 | 8803 | 6034 | 7740 | 1878 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18466 | 2802 | 3338 | 2078 | 762 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16411 | 2253 | 3191 | 8888 | 279 | 2026-04-21 19:49:09 |
| [httpx](https://github.com/encode/httpx) | 15216 | 1118 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14623 | 5704 | 11421 | 13614 | 1783 | 2026-04-21 14:31:04 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13824 | 2102 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13805 | 1867 | 5521 | 6530 | 1246 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12225 | 1157 | 766 | 1875 | 55 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11779 | 1671 | 8198 | 1060 | 218 | 2026-04-21 20:26:49 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11762 | 604 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 988 | 1121 | 1432 | 154 | 2026-04-20 21:43:28 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9020 | 569 | 1031 | 505 | 201 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7244 | 392 | 890 | 2536 | 320 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6896 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 733 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5555 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5243 | 1007 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4081 | 331 | 1183 | 218 | 116 | 2026-04-20 21:11:28 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3626 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2737 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2442 | 197 | 434 | 612 | 83 | 2026-04-21 12:21:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1468 | 365 | 2026-04-21 13:14:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1711 | 111 | 5200 | 226 | 748 | 2026-04-21 20:00:43 |
| [jython](https://github.com/jython/jython) | 1499 | 227 | 294 | 126 | 111 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-22T03:32:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
