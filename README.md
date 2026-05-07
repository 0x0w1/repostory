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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195025 | 75276 | 41365 | 72949 | 4953 | 2026-05-07 03:49:55 |
| [transformers](https://github.com/huggingface/transformers) | 160325 | 33125 | 18932 | 26229 | 2349 | 2026-05-07 02:55:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 99707 | 27695 | 58552 | 123679 | 18544 | 2026-05-07 03:52:00 |
| [fastapi](https://github.com/fastapi/fastapi) | 97955 | 9209 | 3524 | 5706 | 187 | 2026-05-05 11:43:18 |
| [django](https://github.com/django/django) | 87422 | 33850 | 0 | 21174 | 432 | 2026-05-07 01:39:16 |
| [cpython](https://github.com/python/cpython) | 72594 | 34558 | 76263 | 70917 | 9269 | 2026-05-07 03:52:23 |
| [flask](https://github.com/pallets/flask) | 71495 | 16832 | 2736 | 2817 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65989 | 26991 | 12066 | 20702 | 2026 | 2026-05-06 22:21:16 |
| [keras](https://github.com/keras-team/keras) | 64060 | 19765 | 12748 | 9296 | 213 | 2026-05-06 21:02:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 48680 | 19912 | 28271 | 37139 | 3377 | 2026-05-06 22:24:52 |
| [ray](https://github.com/ray-project/ray) | 42441 | 7531 | 22648 | 40175 | 3554 | 2026-05-07 00:46:28 |
| [gym](https://github.com/openai/gym) | 37181 | 8703 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33546 | 4679 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31981 | 12347 | 13904 | 17419 | 2370 | 2026-05-06 21:51:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29996 | 7069 | 3967 | 5005 | 78 | 2026-05-06 11:55:49 |
| [celery](https://github.com/celery/celery) | 28442 | 5033 | 5273 | 4105 | 774 | 2026-05-07 03:27:59 |
| [dash](https://github.com/plotly/dash) | 24151 | 2277 | 2092 | 1548 | 538 | 2026-05-07 01:41:06 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22771 | 8328 | 11262 | 20307 | 1496 | 2026-05-05 12:04:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5541 | 1871 | 1729 | 219 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22036 | 1436 | 1340 | 6384 | 374 | 2026-05-06 11:44:12 |
| [micropython](https://github.com/micropython/micropython) | 21681 | 8817 | 6048 | 7776 | 1815 | 2026-05-05 05:25:11 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18504 | 2802 | 3344 | 2082 | 766 | 2026-05-04 22:49:02 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16426 | 2262 | 3191 | 8950 | 263 | 2026-05-06 12:40:26 |
| [httpx](https://github.com/encode/httpx) | 15260 | 1139 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14666 | 5720 | 11431 | 13649 | 1783 | 2026-05-05 22:15:47 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13842 | 2110 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13822 | 1868 | 5525 | 6543 | 1248 | 2026-05-05 14:00:47 |
| [starlette](https://github.com/Kludex/starlette) | 12288 | 1168 | 766 | 1886 | 56 | 2026-05-03 06:45:09 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11829 | 1680 | 8202 | 1075 | 218 | 2026-05-05 19:03:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11781 | 605 | 414 | 323 | 154 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1000 | 1125 | 1447 | 158 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9041 | 575 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8761 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7259 | 393 | 891 | 2540 | 320 | 2026-05-01 17:34:53 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5566 | 480 | 1249 | 825 | 504 | 2026-05-05 12:07:41 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5250 | 1012 | 912 | 293 | 204 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4122 | 331 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3631 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2741 | 311 | 663 | 1310 | 306 | 2026-05-04 22:07:07 |
| [anyio](https://github.com/agronholm/anyio) | 2460 | 202 | 437 | 622 | 85 | 2026-05-03 20:13:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 908 | 1084 | 1493 | 359 | 2026-05-06 11:00:56 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1720 | 112 | 5206 | 238 | 739 | 2026-05-06 20:37:02 |
| [jython](https://github.com/jython/jython) | 1507 | 229 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-07T03:52:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
