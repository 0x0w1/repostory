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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195138 | 75307 | 41452 | 73739 | 5325 | 2026-05-18 03:59:29 |
| [transformers](https://github.com/huggingface/transformers) | 160703 | 33240 | 18962 | 26372 | 2354 | 2026-05-18 04:06:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 99972 | 27807 | 58752 | 124835 | 18528 | 2026-05-18 04:19:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 98288 | 9308 | 3527 | 5751 | 207 | 2026-05-15 15:18:28 |
| [django](https://github.com/django/django) | 87499 | 33898 | 0 | 21237 | 428 | 2026-05-15 07:45:37 |
| [cpython](https://github.com/python/cpython) | 72736 | 34629 | 76389 | 71276 | 9324 | 2026-05-17 18:33:30 |
| [flask](https://github.com/pallets/flask) | 71553 | 16846 | 2737 | 2823 | 3 | 2026-05-13 14:37:58 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66107 | 27030 | 12087 | 20771 | 2025 | 2026-05-16 15:53:37 |
| [keras](https://github.com/keras-team/keras) | 64072 | 19776 | 12760 | 9330 | 196 | 2026-05-16 01:55:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 48787 | 19964 | 28282 | 37304 | 3263 | 2026-05-17 13:24:26 |
| [ray](https://github.com/ray-project/ray) | 42574 | 7583 | 22674 | 40368 | 3526 | 2026-05-17 22:46:33 |
| [gym](https://github.com/openai/gym) | 37205 | 8700 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33584 | 4682 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 32049 | 12372 | 13921 | 17459 | 2377 | 2026-05-17 17:11:23 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30024 | 7066 | 3967 | 5005 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28497 | 5043 | 5276 | 4111 | 774 | 2026-05-14 04:34:35 |
| [dash](https://github.com/plotly/dash) | 24199 | 2284 | 2099 | 1564 | 555 | 2026-05-15 20:55:29 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22812 | 8341 | 11271 | 20367 | 1476 | 2026-05-17 23:16:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5543 | 1871 | 1733 | 220 | 2026-05-12 15:07:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 22054 | 1439 | 1344 | 6489 | 375 | 2026-05-17 15:23:35 |
| [micropython](https://github.com/micropython/micropython) | 21714 | 8833 | 6055 | 7807 | 1762 | 2026-05-15 09:37:52 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18538 | 2810 | 3344 | 2087 | 761 | 2026-05-15 21:11:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16439 | 2269 | 3200 | 9076 | 256 | 2026-05-18 03:06:56 |
| [httpx](https://github.com/encode/httpx) | 15270 | 1144 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14700 | 5726 | 11444 | 13696 | 1786 | 2026-05-18 00:18:19 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13880 | 2113 | 2653 | 1180 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13835 | 1871 | 5528 | 6568 | 1242 | 2026-05-14 21:18:18 |
| [starlette](https://github.com/Kludex/starlette) | 12318 | 1172 | 766 | 1895 | 60 | 2026-05-16 16:04:35 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11858 | 1683 | 8208 | 1081 | 221 | 2026-05-17 20:08:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11784 | 606 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9056 | 579 | 1034 | 512 | 209 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8765 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7268 | 394 | 892 | 2544 | 319 | 2026-05-18 01:23:55 |
| [hug](https://github.com/hugapi/hug) | 6891 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5568 | 482 | 1253 | 833 | 504 | 2026-05-15 10:42:23 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5257 | 1016 | 912 | 299 | 209 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4136 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4005 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2744 | 311 | 663 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2466 | 207 | 439 | 634 | 84 | 2026-05-17 16:19:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1504 | 362 | 2026-05-15 23:44:43 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1732 | 113 | 5208 | 248 | 741 | 2026-05-17 03:43:02 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 130 | 115 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-18T04:21:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
