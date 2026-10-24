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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201203 | 79288 | 41916 | 83974 | 3379 | 2026-10-24 04:16:41 |
| [transformers](https://github.com/huggingface/transformers) | 168050 | 34956 | 19686 | 29457 | 992 | 2026-10-24 00:49:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 105022 | 32412 | 61966 | 139263 | 17773 | 2026-10-24 04:05:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 104064 | 10112 | 3556 | 6526 | 60 | 2026-10-23 23:46:14 |
| [django](https://github.com/django/django) | 91575 | 37092 | 0 | 22111 | 535 | 2026-10-23 23:30:30 |
| [cpython](https://github.com/python/cpython) | 77750 | 38217 | 78869 | 79158 | 9321 | 2026-10-24 03:33:21 |
| [flask](https://github.com/pallets/flask) | 75030 | 17110 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67883 | 27570 | 12346 | 21677 | 2170 | 2026-10-23 13:36:07 |
| [keras](https://github.com/keras-team/keras) | 64379 | 19793 | 13036 | 10149 | 260 | 2026-10-23 22:31:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 50259 | 20577 | 28644 | 39661 | 2134 | 2026-10-23 20:11:32 |
| [ray](https://github.com/ray-project/ray) | 44111 | 8191 | 23237 | 43682 | 3612 | 2026-10-24 00:01:07 |
| [gym](https://github.com/openai/gym) | 37236 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33986 | 4735 | 5776 | 4134 | 254 | 2026-10-23 13:47:36 |
| [numpy](https://github.com/numpy/numpy) | 33113 | 12954 | 14149 | 18886 | 2234 | 2026-10-23 23:40:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30214 | 7093 | 3966 | 5096 | 61 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29049 | 5239 | 5349 | 4625 | 744 | 2026-10-24 03:52:49 |
| [dash](https://github.com/plotly/dash) | 24467 | 2331 | 2168 | 1788 | 433 | 2026-10-23 16:35:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23386 | 8526 | 11452 | 21015 | 1475 | 2026-10-23 19:17:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 22417 | 1505 | 1446 | 7790 | 291 | 2026-10-24 02:31:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5589 | 1888 | 1891 | 227 | 2026-10-21 17:27:04 |
| [micropython](https://github.com/micropython/micropython) | 22150 | 9012 | 6151 | 8155 | 1550 | 2026-10-23 06:06:21 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18852 | 2881 | 3397 | 2252 | 742 | 2026-10-23 23:43:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1614 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16588 | 2483 | 3266 | 10470 | 262 | 2026-10-23 11:23:34 |
| [httpx](https://github.com/encode/httpx) | 15736 | 3899 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15144 | 6032 | 11712 | 14743 | 1877 | 2026-10-23 17:19:53 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14086 | 2150 | 2667 | 1246 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13937 | 1998 | 5577 | 6782 | 1396 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12684 | 1401 | 794 | 2253 | 36 | 2026-10-23 23:17:22 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12262 | 1831 | 8359 | 1241 | 212 | 2026-10-23 14:28:12 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11912 | 619 | 426 | 344 | 171 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1046 | 1148 | 1554 | 161 | 2026-10-23 07:17:46 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9218 | 621 | 1054 | 577 | 243 | 2026-10-20 09:48:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1517 | 867 | 655 | 289 | 2026-10-23 15:12:18 |
| [trio](https://github.com/python-trio/trio) | 7352 | 462 | 905 | 2648 | 340 | 2026-10-24 04:06:40 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 534 | 1289 | 957 | 543 | 2026-10-24 03:21:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5431 | 1051 | 937 | 326 | 205 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4456 | 388 | 1209 | 257 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 317 | 677 | 1378 | 266 | 2026-10-23 23:48:15 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 329 | 493 | 870 | 141 | 2026-10-23 22:28:10 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2357 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1603 | 355 | 2026-10-22 16:55:34 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1817 | 131 | 5286 | 379 | 722 | 2026-10-23 19:06:03 |
| [jython](https://github.com/jython/jython) | 1550 | 231 | 305 | 155 | 104 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-24T04:19:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
