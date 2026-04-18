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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194769 | 75284 | 41316 | 71428 | 4479 | 2026-04-18 03:16:31 |
| [transformers](https://github.com/huggingface/transformers) | 159527 | 32903 | 18872 | 25980 | 2354 | 2026-04-17 14:36:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 99227 | 27517 | 58082 | 122120 | 18471 | 2026-04-18 02:58:51 |
| [fastapi](https://github.com/fastapi/fastapi) | 97352 | 9090 | 3517 | 5610 | 177 | 2026-04-17 11:43:13 |
| [django](https://github.com/django/django) | 87285 | 33817 | 0 | 21052 | 433 | 2026-04-17 20:28:33 |
| [cpython](https://github.com/python/cpython) | 72372 | 34442 | 76007 | 70411 | 9358 | 2026-04-18 02:20:42 |
| [flask](https://github.com/pallets/flask) | 71424 | 16790 | 2735 | 2805 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65855 | 26955 | 12042 | 20579 | 2050 | 2026-04-17 14:23:57 |
| [keras](https://github.com/keras-team/keras) | 64015 | 19740 | 12728 | 9163 | 271 | 2026-04-18 01:50:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 48535 | 19874 | 28248 | 36945 | 3426 | 2026-04-17 16:02:12 |
| [ray](https://github.com/ray-project/ray) | 42181 | 7454 | 22582 | 39797 | 3588 | 2026-04-18 02:35:30 |
| [gym](https://github.com/openai/gym) | 37166 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33480 | 4672 | 5755 | 4089 | 201 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31870 | 12312 | 13880 | 17315 | 2355 | 2026-04-17 19:58:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29974 | 7067 | 3968 | 4998 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28374 | 5009 | 5269 | 4079 | 782 | 2026-04-16 17:17:47 |
| [dash](https://github.com/plotly/dash) | 24207 | 2275 | 2089 | 1538 | 547 | 2026-04-17 20:07:12 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22722 | 8317 | 11244 | 20221 | 1502 | 2026-04-17 19:14:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22271 | 5543 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22016 | 1424 | 1332 | 6218 | 377 | 2026-04-18 00:19:12 |
| [micropython](https://github.com/micropython/micropython) | 21633 | 8797 | 6031 | 7734 | 1872 | 2026-04-16 13:44:34 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1587 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18458 | 2799 | 3338 | 2074 | 762 | 2026-04-15 23:24:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16404 | 2247 | 3190 | 8870 | 278 | 2026-04-17 10:50:47 |
| [httpx](https://github.com/encode/httpx) | 15206 | 1116 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14610 | 5693 | 11416 | 13593 | 1790 | 2026-04-17 20:19:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13814 | 2098 | 2652 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1864 | 5521 | 6527 | 1243 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12214 | 1158 | 766 | 1869 | 53 | 2026-04-16 07:31:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11760 | 1669 | 8192 | 1057 | 214 | 2026-04-16 20:17:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11757 | 604 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 987 | 1121 | 1432 | 161 | 2026-04-15 16:38:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9014 | 569 | 1028 | 502 | 223 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8757 | 1496 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7242 | 393 | 889 | 2531 | 318 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5548 | 478 | 1249 | 823 | 509 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5241 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4076 | 330 | 1183 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3625 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2438 | 197 | 434 | 610 | 84 | 2026-04-17 21:43:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 904 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1709 | 111 | 5198 | 223 | 747 | 2026-04-17 15:43:12 |
| [jython](https://github.com/jython/jython) | 1498 | 227 | 294 | 125 | 111 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-18T03:21:21*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
