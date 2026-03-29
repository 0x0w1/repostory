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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194368 | 75254 | 41288 | 70035 | 4050 | 2026-03-29 03:26:09 |
| [transformers](https://github.com/huggingface/transformers) | 158508 | 32656 | 18789 | 25669 | 2316 | 2026-03-28 10:24:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 98611 | 27331 | 57533 | 120649 | 18113 | 2026-03-29 03:20:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 96648 | 8958 | 3517 | 5535 | 168 | 2026-03-26 21:53:12 |
| [django](https://github.com/django/django) | 87122 | 33803 | 0 | 20951 | 423 | 2026-03-28 17:40:50 |
| [cpython](https://github.com/python/cpython) | 72104 | 34319 | 75755 | 69812 | 9334 | 2026-03-28 20:21:19 |
| [flask](https://github.com/pallets/flask) | 71353 | 16759 | 2726 | 2796 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65536 | 26853 | 12018 | 20477 | 2133 | 2026-03-27 17:18:05 |
| [keras](https://github.com/keras-team/keras) | 63912 | 19742 | 12718 | 9064 | 318 | 2026-03-28 19:35:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 48268 | 19791 | 28212 | 36627 | 3564 | 2026-03-28 18:27:55 |
| [ray](https://github.com/ray-project/ray) | 41861 | 7391 | 22504 | 39305 | 3537 | 2026-03-29 03:21:48 |
| [gym](https://github.com/openai/gym) | 37117 | 8707 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33392 | 4664 | 5749 | 4087 | 193 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31678 | 12211 | 13854 | 17169 | 2337 | 2026-03-29 00:29:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29941 | 7076 | 3947 | 4951 | 77 | 2026-03-24 16:57:27 |
| [celery](https://github.com/celery/celery) | 28265 | 4997 | 5209 | 3880 | 765 | 2026-03-28 10:18:19 |
| [dash](https://github.com/plotly/dash) | 24490 | 2269 | 2082 | 1502 | 599 | 2026-03-27 15:27:58 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22650 | 8296 | 11222 | 20148 | 1539 | 2026-03-28 22:14:17 |
| [tornado](https://github.com/tornadoweb/tornado) | 22410 | 5546 | 1865 | 1723 | 211 | 2026-03-26 17:59:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 21921 | 1416 | 1324 | 6133 | 367 | 2026-03-28 19:33:56 |
| [micropython](https://github.com/micropython/micropython) | 21590 | 8760 | 5999 | 7668 | 1850 | 2026-03-26 19:16:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18400 | 2791 | 3332 | 2063 | 773 | 2026-03-27 21:03:58 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16356 | 2233 | 3183 | 8790 | 279 | 2026-03-28 19:43:18 |
| [httpx](https://github.com/encode/httpx) | 15130 | 1094 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14569 | 5676 | 11391 | 13523 | 1785 | 2026-03-28 22:52:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13782 | 2091 | 2650 | 1168 | 212 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13777 | 1858 | 5517 | 6511 | 1233 | 2026-03-24 00:04:43 |
| [starlette](https://github.com/Kludex/starlette) | 12142 | 1147 | 766 | 1846 | 50 | 2026-03-28 22:14:05 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11727 | 607 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11679 | 1661 | 8178 | 1053 | 214 | 2026-03-28 21:27:35 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 982 | 1119 | 1422 | 162 | 2026-03-28 18:33:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8976 | 567 | 1025 | 498 | 219 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1501 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7217 | 394 | 882 | 2518 | 316 | 2026-03-23 22:25:09 |
| [hug](https://github.com/hugapi/hug) | 6901 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5603 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5533 | 470 | 1243 | 808 | 498 | 2026-03-28 08:03:42 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5219 | 1003 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4037 | 325 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4012 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3615 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 312 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2422 | 189 | 431 | 595 | 83 | 2026-03-28 13:51:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 367 | 1785 | 267 | 267 | 2026-03-23 17:46:41 |
| [pypy](https://github.com/pypy/pypy) | 1692 | 109 | 5188 | 191 | 763 | 2026-03-29 03:15:29 |
| [jython](https://github.com/jython/jython) | 1496 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-29T03:26:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
