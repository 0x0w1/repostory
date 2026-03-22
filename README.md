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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194301 | 75253 | 41250 | 69528 | 3836 | 2026-03-22 02:54:21 |
| [transformers](https://github.com/huggingface/transformers) | 158212 | 32561 | 18750 | 25541 | 2299 | 2026-03-21 20:56:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 98477 | 27265 | 57426 | 120137 | 18060 | 2026-03-22 02:24:59 |
| [fastapi](https://github.com/fastapi/fastapi) | 96462 | 8897 | 3513 | 5491 | 163 | 2026-03-20 17:07:26 |
| [django](https://github.com/django/django) | 87123 | 33775 | 0 | 20894 | 432 | 2026-03-21 14:50:19 |
| [cpython](https://github.com/python/cpython) | 72076 | 34271 | 75655 | 69605 | 9331 | 2026-03-21 18:41:50 |
| [flask](https://github.com/pallets/flask) | 71397 | 16755 | 2724 | 2788 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65493 | 26828 | 12009 | 20428 | 2152 | 2026-03-20 10:42:57 |
| [keras](https://github.com/keras-team/keras) | 63948 | 19739 | 12675 | 8989 | 265 | 2026-03-21 20:39:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 48209 | 19768 | 28197 | 36505 | 3641 | 2026-03-22 00:19:09 |
| [ray](https://github.com/ray-project/ray) | 41829 | 7372 | 22478 | 39119 | 3499 | 2026-03-22 02:43:30 |
| [gym](https://github.com/openai/gym) | 37112 | 8705 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33366 | 4659 | 5746 | 4084 | 196 | 2026-03-21 17:23:03 |
| [numpy](https://github.com/numpy/numpy) | 31636 | 12182 | 13842 | 17136 | 2338 | 2026-03-21 08:39:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29933 | 7078 | 3947 | 4948 | 80 | 2026-03-19 14:26:11 |
| [celery](https://github.com/celery/celery) | 28288 | 4995 | 5209 | 3872 | 772 | 2026-03-20 22:13:14 |
| [dash](https://github.com/plotly/dash) | 24476 | 2268 | 2078 | 1481 | 592 | 2026-03-20 20:04:42 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22610 | 8273 | 11212 | 20086 | 1540 | 2026-03-20 22:59:08 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5548 | 1865 | 1721 | 213 | 2026-03-20 11:40:59 |
| [RustPython](https://github.com/RustPython/RustPython) | 21894 | 1411 | 1318 | 6091 | 363 | 2026-03-21 13:49:28 |
| [micropython](https://github.com/micropython/micropython) | 21566 | 8752 | 5992 | 7645 | 1837 | 2026-03-21 13:04:38 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18368 | 2787 | 3330 | 2058 | 774 | 2026-03-20 15:31:47 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16394 | 2219 | 3184 | 8764 | 277 | 2026-03-19 11:01:01 |
| [httpx](https://github.com/encode/httpx) | 15164 | 1081 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14551 | 5665 | 11383 | 13483 | 1782 | 2026-03-21 22:50:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13776 | 2089 | 2648 | 1165 | 210 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13774 | 1861 | 5518 | 6509 | 1231 | 2026-03-19 09:37:28 |
| [starlette](https://github.com/Kludex/starlette) | 12035 | 1141 | 767 | 1836 | 50 | 2026-03-16 05:35:30 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11707 | 1655 | 8173 | 1050 | 210 | 2026-03-20 20:37:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11704 | 604 | 410 | 318 | 160 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 983 | 1119 | 1422 | 164 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8958 | 565 | 1025 | 497 | 218 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8767 | 1503 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7211 | 392 | 882 | 2516 | 315 | 2026-03-21 21:37:53 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 734 | 979 | 587 | 26 | 2026-03-19 09:45:14 |
| [vibora](https://github.com/vibora-io/vibora) | 5606 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5526 | 468 | 1244 | 805 | 499 | 2026-03-21 22:19:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5214 | 1002 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4078 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4024 | 322 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4018 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3610 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 313 | 664 | 1304 | 309 | 2026-03-22 01:46:51 |
| [anyio](https://github.com/agronholm/anyio) | 2414 | 189 | 431 | 589 | 87 | 2026-03-16 20:33:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-16 17:53:47 |
| [pypy](https://github.com/pypy/pypy) | 1685 | 106 | 5185 | 190 | 764 | 2026-03-21 18:19:26 |
| [jython](https://github.com/jython/jython) | 1491 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-22T02:56:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
