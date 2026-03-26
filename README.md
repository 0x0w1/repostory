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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194344 | 75247 | 41280 | 69844 | 3989 | 2026-03-26 03:14:14 |
| [transformers](https://github.com/huggingface/transformers) | 158416 | 32608 | 18775 | 25599 | 2286 | 2026-03-25 20:34:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 98575 | 27306 | 57494 | 120454 | 18117 | 2026-03-26 03:17:51 |
| [fastapi](https://github.com/fastapi/fastapi) | 96564 | 8938 | 3514 | 5513 | 164 | 2026-03-24 16:39:59 |
| [django](https://github.com/django/django) | 87121 | 33787 | 0 | 20928 | 424 | 2026-03-25 16:20:58 |
| [cpython](https://github.com/python/cpython) | 72105 | 34309 | 75710 | 69714 | 9325 | 2026-03-26 00:42:27 |
| [flask](https://github.com/pallets/flask) | 71380 | 16758 | 2725 | 2793 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65524 | 26842 | 12017 | 20460 | 2155 | 2026-03-25 18:03:08 |
| [keras](https://github.com/keras-team/keras) | 63928 | 19736 | 12696 | 9026 | 288 | 2026-03-25 23:51:01 |
| [pandas](https://github.com/pandas-dev/pandas) | 48245 | 19780 | 28206 | 36597 | 3613 | 2026-03-26 03:09:37 |
| [ray](https://github.com/ray-project/ray) | 41859 | 7383 | 22493 | 39225 | 3520 | 2026-03-26 02:35:49 |
| [gym](https://github.com/openai/gym) | 37115 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33386 | 4661 | 5747 | 4085 | 191 | 2026-03-23 17:48:01 |
| [numpy](https://github.com/numpy/numpy) | 31659 | 12200 | 13846 | 17159 | 2334 | 2026-03-25 21:20:11 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29941 | 7076 | 3947 | 4951 | 78 | 2026-03-24 16:57:27 |
| [celery](https://github.com/celery/celery) | 28284 | 4997 | 5209 | 3875 | 770 | 2026-03-25 14:23:39 |
| [dash](https://github.com/plotly/dash) | 24486 | 2269 | 2082 | 1498 | 598 | 2026-03-25 22:32:41 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22635 | 8284 | 11215 | 20122 | 1549 | 2026-03-26 02:38:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5548 | 1865 | 1722 | 211 | 2026-03-23 17:29:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 21915 | 1415 | 1317 | 6116 | 362 | 2026-03-25 23:28:53 |
| [micropython](https://github.com/micropython/micropython) | 21578 | 8758 | 5996 | 7662 | 1842 | 2026-03-25 13:05:26 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18385 | 2790 | 3330 | 2059 | 769 | 2026-03-25 18:43:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16384 | 2229 | 3182 | 8773 | 277 | 2026-03-26 02:53:55 |
| [httpx](https://github.com/encode/httpx) | 15150 | 1089 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14561 | 5672 | 11385 | 13503 | 1776 | 2026-03-26 02:35:19 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13782 | 2092 | 2649 | 1168 | 211 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13774 | 1858 | 5517 | 6511 | 1233 | 2026-03-24 00:04:43 |
| [starlette](https://github.com/Kludex/starlette) | 12120 | 1148 | 766 | 1843 | 49 | 2026-03-22 18:27:00 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11721 | 606 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11702 | 1658 | 8174 | 1050 | 209 | 2026-03-24 19:50:39 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 982 | 1119 | 1422 | 164 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8967 | 564 | 1025 | 497 | 218 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1501 | 863 | 632 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7218 | 393 | 882 | 2517 | 315 | 2026-03-23 22:25:09 |
| [hug](https://github.com/hugapi/hug) | 6903 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5604 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5526 | 470 | 1243 | 805 | 498 | 2026-03-21 22:19:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5216 | 1002 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4033 | 323 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4016 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3615 | 194 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 313 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2420 | 188 | 431 | 593 | 82 | 2026-03-25 20:00:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 904 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-23 17:46:41 |
| [pypy](https://github.com/pypy/pypy) | 1690 | 107 | 5187 | 191 | 766 | 2026-03-25 08:29:15 |
| [jython](https://github.com/jython/jython) | 1496 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-26T03:18:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
