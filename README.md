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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195008 | 75275 | 41359 | 72880 | 4923 | 2026-05-06 03:50:20 |
| [transformers](https://github.com/huggingface/transformers) | 160287 | 33118 | 18929 | 26216 | 2347 | 2026-05-05 21:41:15 |
| [pytorch](https://github.com/pytorch/pytorch) | 99670 | 27678 | 58522 | 123554 | 18559 | 2026-05-06 03:51:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 97917 | 9208 | 3524 | 5704 | 185 | 2026-05-05 11:43:18 |
| [django](https://github.com/django/django) | 87410 | 33837 | 0 | 21165 | 431 | 2026-05-06 00:13:40 |
| [cpython](https://github.com/python/cpython) | 72589 | 34552 | 76248 | 70893 | 9279 | 2026-05-06 03:48:00 |
| [flask](https://github.com/pallets/flask) | 71494 | 16831 | 2736 | 2817 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65987 | 26988 | 12065 | 20697 | 2029 | 2026-05-06 00:45:39 |
| [keras](https://github.com/keras-team/keras) | 64059 | 19765 | 12748 | 9291 | 226 | 2026-05-06 03:26:46 |
| [pandas](https://github.com/pandas-dev/pandas) | 48667 | 19908 | 28270 | 37124 | 3389 | 2026-05-06 00:46:17 |
| [ray](https://github.com/ray-project/ray) | 42432 | 7526 | 22646 | 40149 | 3560 | 2026-05-06 03:07:07 |
| [gym](https://github.com/openai/gym) | 37175 | 8704 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33543 | 4680 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31979 | 12341 | 13904 | 17415 | 2369 | 2026-05-05 19:02:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29996 | 7068 | 3967 | 5004 | 78 | 2026-04-28 07:27:54 |
| [celery](https://github.com/celery/celery) | 28433 | 5030 | 5272 | 4104 | 777 | 2026-05-05 22:12:58 |
| [dash](https://github.com/plotly/dash) | 24149 | 2277 | 2092 | 1547 | 540 | 2026-05-05 19:38:30 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22773 | 8327 | 11260 | 20305 | 1493 | 2026-05-05 12:04:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22184 | 5541 | 1871 | 1728 | 218 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22034 | 1435 | 1340 | 6378 | 371 | 2026-05-05 17:06:51 |
| [micropython](https://github.com/micropython/micropython) | 21678 | 8814 | 6047 | 7776 | 1815 | 2026-05-05 05:25:11 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18497 | 2803 | 3344 | 2082 | 766 | 2026-05-04 22:49:02 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16426 | 2262 | 3191 | 8940 | 260 | 2026-05-05 12:37:20 |
| [httpx](https://github.com/encode/httpx) | 15261 | 1139 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14665 | 5718 | 11431 | 13647 | 1781 | 2026-05-05 22:15:47 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13842 | 2108 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13820 | 1868 | 5523 | 6541 | 1244 | 2026-05-05 14:00:47 |
| [starlette](https://github.com/Kludex/starlette) | 12284 | 1168 | 766 | 1886 | 56 | 2026-05-03 06:45:09 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11825 | 1677 | 8202 | 1074 | 217 | 2026-05-05 19:03:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11781 | 605 | 413 | 323 | 153 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 998 | 1125 | 1446 | 158 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9039 | 575 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8761 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7259 | 393 | 891 | 2540 | 320 | 2026-05-01 17:34:53 |
| [hug](https://github.com/hugapi/hug) | 6893 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5566 | 480 | 1248 | 825 | 504 | 2026-05-05 12:07:41 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5250 | 1010 | 912 | 293 | 204 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4122 | 331 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3631 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2741 | 311 | 663 | 1310 | 306 | 2026-05-04 22:07:07 |
| [anyio](https://github.com/agronholm/anyio) | 2458 | 202 | 437 | 622 | 85 | 2026-05-03 20:13:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 908 | 1084 | 1493 | 360 | 2026-05-05 17:01:07 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1720 | 112 | 5205 | 238 | 739 | 2026-05-05 20:24:29 |
| [jython](https://github.com/jython/jython) | 1507 | 229 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-06T03:54:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
