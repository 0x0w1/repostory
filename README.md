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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193317 | 75152 | 41078 | 64928 | 2790 | 2026-01-13 02:19:24 |
| [transformers](https://github.com/huggingface/transformers) | 154975 | 31712 | 18412 | 24226 | 2158 | 2026-01-13 01:11:49 |
| [pytorch](https://github.com/pytorch/pytorch) | 96568 | 26486 | 56259 | 115530 | 17842 | 2026-01-13 02:19:30 |
| [fastapi](https://github.com/fastapi/fastapi) | 94014 | 8513 | 3500 | 5122 | 204 | 2026-01-12 10:13:31 |
| [django](https://github.com/django/django) | 86444 | 33473 | 0 | 20464 | 379 | 2026-01-12 21:38:32 |
| [cpython](https://github.com/python/cpython) | 71039 | 33879 | 74962 | 67816 | 9220 | 2026-01-13 00:25:56 |
| [flask](https://github.com/pallets/flask) | 71038 | 16676 | 2708 | 2748 | 12 | 2026-01-05 16:50:56 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64608 | 26599 | 11885 | 20036 | 2124 | 2026-01-12 09:18:03 |
| [keras](https://github.com/keras-team/keras) | 63708 | 19673 | 12608 | 8598 | 239 | 2026-01-12 23:51:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 47562 | 19504 | 28012 | 35584 | 3610 | 2026-01-12 23:22:31 |
| [ray](https://github.com/ray-project/ray) | 40731 | 7102 | 22139 | 37590 | 3275 | 2026-01-13 02:16:30 |
| [gym](https://github.com/openai/gym) | 36948 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33066 | 4631 | 5736 | 4077 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31209 | 11953 | 13741 | 16839 | 2338 | 2026-01-13 01:15:42 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29802 | 7049 | 3946 | 4899 | 84 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27859 | 4929 | 5182 | 3766 | 756 | 2026-01-10 18:43:35 |
| [dash](https://github.com/plotly/dash) | 24397 | 2248 | 2041 | 1411 | 557 | 2026-01-12 20:29:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22416 | 5544 | 1862 | 1691 | 209 | 2026-01-12 18:40:23 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22214 | 8172 | 11101 | 19808 | 1531 | 2026-01-12 23:55:59 |
| [RustPython](https://github.com/RustPython/RustPython) | 21653 | 1400 | 1283 | 5367 | 371 | 2026-01-13 01:47:37 |
| [micropython](https://github.com/micropython/micropython) | 21334 | 8648 | 5935 | 7476 | 1828 | 2026-01-13 02:15:09 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1584 | 1460 | 1662 | 110 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18176 | 2773 | 3313 | 1999 | 765 | 2026-01-09 17:00:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16196 | 2177 | 3171 | 8486 | 270 | 2026-01-12 18:49:20 |
| [httpx](https://github.com/encode/httpx) | 14894 | 1007 | 925 | 1776 | 124 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14338 | 5587 | 11245 | 13091 | 1755 | 2026-01-12 23:48:19 |
| [dask](https://github.com/dask/dask) | 13707 | 1837 | 5483 | 6446 | 1209 | 2026-01-08 16:18:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13679 | 2081 | 2644 | 1156 | 203 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11833 | 1098 | 761 | 1765 | 51 | 2026-01-11 21:47:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11578 | 597 | 400 | 303 | 150 | 2026-01-12 21:16:53 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11374 | 1621 | 8139 | 1020 | 210 | 2026-01-11 02:02:35 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 974 | 1115 | 1406 | 162 | 2026-01-10 11:15:16 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8836 | 555 | 996 | 480 | 200 | 2026-01-10 20:01:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8728 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7097 | 378 | 877 | 2487 | 312 | 2026-01-12 21:58:36 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5620 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5445 | 445 | 1217 | 735 | 511 | 2026-01-12 06:20:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5150 | 988 | 884 | 279 | 178 | 2026-01-07 13:28:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4024 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3882 | 305 | 1174 | 207 | 117 | 2026-01-12 21:25:37 |
| [quart](https://github.com/pallets/quart) | 3573 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2355 | 180 | 421 | 563 | 74 | 2026-01-12 17:50:45 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1784 | 266 | 265 | 2026-01-12 17:44:15 |
| [pypy](https://github.com/pypy/pypy) | 1627 | 95 | 5169 | 177 | 754 | 2026-01-12 22:21:27 |
| [jython](https://github.com/jython/jython) | 1469 | 225 | 289 | 120 | 106 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-13T02:19:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
