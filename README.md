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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194751 | 75280 | 41310 | 71241 | 4426 | 2026-04-16 03:36:34 |
| [transformers](https://github.com/huggingface/transformers) | 159450 | 32883 | 18866 | 25950 | 2345 | 2026-04-16 02:10:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 99163 | 27504 | 58036 | 121964 | 18513 | 2026-04-16 03:31:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 97259 | 9087 | 3517 | 5598 | 184 | 2026-04-15 20:50:54 |
| [django](https://github.com/django/django) | 87281 | 33814 | 0 | 21043 | 431 | 2026-04-15 12:26:53 |
| [cpython](https://github.com/python/cpython) | 72349 | 34433 | 75983 | 70367 | 9336 | 2026-04-15 21:54:01 |
| [flask](https://github.com/pallets/flask) | 71428 | 16788 | 2731 | 2805 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65839 | 26947 | 12038 | 20560 | 2043 | 2026-04-15 16:52:54 |
| [keras](https://github.com/keras-team/keras) | 64008 | 19739 | 12727 | 9152 | 268 | 2026-04-16 02:33:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 48514 | 19868 | 28248 | 36924 | 3456 | 2026-04-15 15:54:55 |
| [ray](https://github.com/ray-project/ray) | 42143 | 7443 | 22569 | 39724 | 3575 | 2026-04-16 02:15:35 |
| [gym](https://github.com/openai/gym) | 37163 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33472 | 4671 | 5755 | 4089 | 201 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31859 | 12307 | 13877 | 17303 | 2349 | 2026-04-14 23:18:17 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29973 | 7066 | 3968 | 4998 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28363 | 5009 | 5268 | 4077 | 786 | 2026-04-15 08:57:58 |
| [dash](https://github.com/plotly/dash) | 24205 | 2276 | 2089 | 1534 | 547 | 2026-04-15 22:56:10 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22718 | 8316 | 11242 | 20205 | 1504 | 2026-04-13 20:51:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22271 | 5544 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22006 | 1425 | 1332 | 6210 | 379 | 2026-04-15 23:52:37 |
| [micropython](https://github.com/micropython/micropython) | 21624 | 8796 | 6026 | 7729 | 1869 | 2026-04-15 06:13:33 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1587 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18456 | 2799 | 3339 | 2072 | 762 | 2026-04-15 23:24:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16403 | 2244 | 3188 | 8864 | 274 | 2026-04-15 18:16:31 |
| [httpx](https://github.com/encode/httpx) | 15202 | 1110 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14604 | 5693 | 11415 | 13583 | 1790 | 2026-04-15 09:40:17 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13812 | 2098 | 2652 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1864 | 5521 | 6527 | 1243 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12209 | 1155 | 766 | 1867 | 52 | 2026-04-15 21:33:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11753 | 1668 | 8190 | 1056 | 214 | 2026-04-15 18:20:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11750 | 604 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 987 | 1121 | 1432 | 161 | 2026-04-15 16:38:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9009 | 569 | 1027 | 502 | 222 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7239 | 393 | 889 | 2531 | 318 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5547 | 476 | 1249 | 823 | 509 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5238 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4071 | 329 | 1183 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3625 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2735 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2437 | 195 | 434 | 609 | 86 | 2026-04-15 12:38:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 904 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1708 | 110 | 5198 | 221 | 747 | 2026-04-15 23:58:50 |
| [jython](https://github.com/jython/jython) | 1501 | 228 | 294 | 125 | 111 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-16T03:37:33*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
