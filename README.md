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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194356 | 75252 | 41289 | 69924 | 4013 | 2026-03-27 03:19:43 |
| [transformers](https://github.com/huggingface/transformers) | 158460 | 32627 | 18779 | 25628 | 2294 | 2026-03-27 00:25:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 98604 | 27318 | 57513 | 120528 | 18118 | 2026-03-27 03:20:06 |
| [fastapi](https://github.com/fastapi/fastapi) | 96619 | 8941 | 3514 | 5522 | 166 | 2026-03-26 21:53:12 |
| [django](https://github.com/django/django) | 87131 | 33792 | 0 | 20936 | 423 | 2026-03-26 19:21:00 |
| [cpython](https://github.com/python/cpython) | 72118 | 34314 | 75732 | 69753 | 9323 | 2026-03-27 02:50:35 |
| [flask](https://github.com/pallets/flask) | 71383 | 16760 | 2725 | 2793 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65534 | 26848 | 12018 | 20469 | 2153 | 2026-03-25 18:03:08 |
| [keras](https://github.com/keras-team/keras) | 63932 | 19737 | 12714 | 9037 | 310 | 2026-03-27 02:51:22 |
| [pandas](https://github.com/pandas-dev/pandas) | 48252 | 19788 | 28209 | 36607 | 3596 | 2026-03-26 22:58:27 |
| [ray](https://github.com/ray-project/ray) | 41876 | 7391 | 22500 | 39263 | 3542 | 2026-03-27 02:29:36 |
| [gym](https://github.com/openai/gym) | 37116 | 8707 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33390 | 4661 | 5747 | 4085 | 191 | 2026-03-26 15:08:06 |
| [numpy](https://github.com/numpy/numpy) | 31670 | 12203 | 13848 | 17164 | 2333 | 2026-03-26 23:21:42 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29945 | 7076 | 3947 | 4951 | 78 | 2026-03-24 16:57:27 |
| [celery](https://github.com/celery/celery) | 28288 | 4996 | 5209 | 3879 | 767 | 2026-03-26 22:13:12 |
| [dash](https://github.com/plotly/dash) | 24488 | 2268 | 2082 | 1501 | 599 | 2026-03-27 00:13:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22643 | 8291 | 11219 | 20135 | 1550 | 2026-03-27 03:19:06 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5549 | 1865 | 1723 | 211 | 2026-03-26 17:59:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 21920 | 1413 | 1317 | 6123 | 364 | 2026-03-27 02:27:20 |
| [micropython](https://github.com/micropython/micropython) | 21582 | 8760 | 5996 | 7664 | 1844 | 2026-03-26 19:16:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18393 | 2790 | 3331 | 2061 | 771 | 2026-03-26 19:58:30 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16384 | 2230 | 3183 | 8778 | 276 | 2026-03-27 02:58:34 |
| [httpx](https://github.com/encode/httpx) | 15158 | 1089 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14567 | 5675 | 11385 | 13509 | 1778 | 2026-03-26 22:47:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13784 | 2092 | 2650 | 1168 | 212 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13776 | 1858 | 5517 | 6511 | 1233 | 2026-03-24 00:04:43 |
| [starlette](https://github.com/Kludex/starlette) | 12128 | 1147 | 766 | 1844 | 50 | 2026-03-26 17:52:14 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11724 | 606 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11704 | 1659 | 8174 | 1051 | 209 | 2026-03-26 14:25:25 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 982 | 1119 | 1422 | 164 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8971 | 565 | 1025 | 498 | 219 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1502 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7217 | 394 | 882 | 2517 | 315 | 2026-03-23 22:25:09 |
| [hug](https://github.com/hugapi/hug) | 6903 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5604 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5530 | 471 | 1243 | 807 | 500 | 2026-03-26 16:50:23 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5217 | 1002 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4035 | 323 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4016 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3615 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 313 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2421 | 188 | 431 | 593 | 82 | 2026-03-26 23:12:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 904 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-23 17:46:41 |
| [pypy](https://github.com/pypy/pypy) | 1691 | 107 | 5187 | 191 | 766 | 2026-03-26 21:26:23 |
| [jython](https://github.com/jython/jython) | 1496 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-27T03:21:57*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
