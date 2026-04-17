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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194766 | 75283 | 41314 | 71347 | 4463 | 2026-04-17 03:32:12 |
| [transformers](https://github.com/huggingface/transformers) | 159493 | 32896 | 18870 | 25968 | 2353 | 2026-04-17 03:20:33 |
| [pytorch](https://github.com/pytorch/pytorch) | 99207 | 27515 | 58065 | 122047 | 18467 | 2026-04-17 03:25:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 97314 | 9090 | 3517 | 5609 | 177 | 2026-04-17 00:37:32 |
| [django](https://github.com/django/django) | 87278 | 33819 | 0 | 21046 | 430 | 2026-04-16 18:39:04 |
| [cpython](https://github.com/python/cpython) | 72353 | 34442 | 75995 | 70379 | 9332 | 2026-04-16 23:55:03 |
| [flask](https://github.com/pallets/flask) | 71421 | 16790 | 2731 | 2805 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65848 | 26956 | 12041 | 20570 | 2050 | 2026-04-16 11:39:04 |
| [keras](https://github.com/keras-team/keras) | 64014 | 19742 | 12728 | 9156 | 272 | 2026-04-16 05:56:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 48527 | 19870 | 28248 | 36939 | 3428 | 2026-04-17 00:47:32 |
| [ray](https://github.com/ray-project/ray) | 42164 | 7449 | 22574 | 39767 | 3577 | 2026-04-17 03:25:09 |
| [gym](https://github.com/openai/gym) | 37166 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33473 | 4672 | 5755 | 4089 | 201 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31868 | 12308 | 13879 | 17308 | 2352 | 2026-04-16 23:56:35 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29976 | 7066 | 3968 | 4998 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28366 | 5008 | 5269 | 4078 | 781 | 2026-04-16 17:17:47 |
| [dash](https://github.com/plotly/dash) | 24208 | 2275 | 2089 | 1538 | 549 | 2026-04-17 00:32:26 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22720 | 8317 | 11244 | 20213 | 1499 | 2026-04-17 02:45:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22271 | 5544 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22013 | 1424 | 1332 | 6217 | 385 | 2026-04-16 20:15:27 |
| [micropython](https://github.com/micropython/micropython) | 21629 | 8796 | 6030 | 7732 | 1872 | 2026-04-16 13:44:34 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1587 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18459 | 2800 | 3339 | 2074 | 763 | 2026-04-15 23:24:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16404 | 2243 | 3188 | 8866 | 274 | 2026-04-16 10:59:39 |
| [httpx](https://github.com/encode/httpx) | 15201 | 1112 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14609 | 5694 | 11415 | 13590 | 1789 | 2026-04-16 21:42:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13813 | 2098 | 2652 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1864 | 5521 | 6527 | 1243 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12212 | 1157 | 766 | 1869 | 54 | 2026-04-16 07:31:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11760 | 1668 | 8191 | 1057 | 213 | 2026-04-16 20:17:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11749 | 604 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 987 | 1121 | 1432 | 161 | 2026-04-15 16:38:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9011 | 568 | 1028 | 502 | 223 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1496 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7240 | 393 | 889 | 2531 | 318 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5548 | 477 | 1249 | 823 | 509 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5241 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4074 | 330 | 1183 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3625 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2437 | 196 | 434 | 609 | 86 | 2026-04-15 12:38:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 904 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1709 | 111 | 5198 | 223 | 748 | 2026-04-16 19:40:41 |
| [jython](https://github.com/jython/jython) | 1498 | 227 | 294 | 125 | 111 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-17T03:34:04*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
