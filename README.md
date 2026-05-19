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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195154 | 75308 | 41454 | 73833 | 5359 | 2026-05-19 04:15:59 |
| [transformers](https://github.com/huggingface/transformers) | 160749 | 33254 | 18965 | 26395 | 2346 | 2026-05-19 03:04:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 99996 | 27812 | 58774 | 124961 | 18519 | 2026-05-19 04:15:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 98319 | 9314 | 3527 | 5760 | 184 | 2026-05-18 16:50:32 |
| [django](https://github.com/django/django) | 87501 | 33922 | 0 | 21253 | 440 | 2026-05-18 21:06:15 |
| [cpython](https://github.com/python/cpython) | 72753 | 34663 | 76405 | 71336 | 9317 | 2026-05-19 01:19:07 |
| [flask](https://github.com/pallets/flask) | 71554 | 16848 | 2738 | 2823 | 4 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66113 | 27029 | 12090 | 20783 | 2029 | 2026-05-18 18:26:09 |
| [keras](https://github.com/keras-team/keras) | 64072 | 19777 | 12760 | 9335 | 192 | 2026-05-19 01:32:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 48797 | 19966 | 28283 | 37312 | 3259 | 2026-05-18 21:26:21 |
| [ray](https://github.com/ray-project/ray) | 42585 | 7586 | 22678 | 40430 | 3465 | 2026-05-19 04:14:06 |
| [gym](https://github.com/openai/gym) | 37208 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33587 | 4683 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 32055 | 12371 | 13921 | 17471 | 2379 | 2026-05-19 03:24:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30024 | 7066 | 3967 | 5005 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28501 | 5042 | 5276 | 4111 | 774 | 2026-05-18 16:52:21 |
| [dash](https://github.com/plotly/dash) | 24199 | 2284 | 2099 | 1564 | 555 | 2026-05-19 02:37:23 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22814 | 8340 | 11274 | 20369 | 1479 | 2026-05-17 23:16:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5543 | 1871 | 1733 | 220 | 2026-05-12 15:07:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 22056 | 1439 | 1345 | 6505 | 390 | 2026-05-18 23:23:18 |
| [micropython](https://github.com/micropython/micropython) | 21721 | 8837 | 6056 | 7809 | 1765 | 2026-05-15 09:37:52 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18540 | 2810 | 3344 | 2088 | 762 | 2026-05-18 18:07:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2269 | 3203 | 9104 | 252 | 2026-05-19 03:12:01 |
| [httpx](https://github.com/encode/httpx) | 15273 | 1144 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14703 | 5729 | 11444 | 13706 | 1790 | 2026-05-18 21:32:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13880 | 2113 | 2653 | 1180 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13836 | 1871 | 5528 | 6568 | 1242 | 2026-05-14 21:18:18 |
| [starlette](https://github.com/Kludex/starlette) | 12319 | 1171 | 766 | 1895 | 59 | 2026-05-16 16:04:35 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11867 | 1683 | 8208 | 1081 | 217 | 2026-05-18 16:31:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11784 | 606 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9056 | 580 | 1034 | 512 | 209 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8765 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7268 | 394 | 892 | 2544 | 319 | 2026-05-18 01:23:55 |
| [hug](https://github.com/hugapi/hug) | 6891 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5568 | 482 | 1253 | 833 | 504 | 2026-05-15 10:42:23 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5258 | 1016 | 912 | 299 | 209 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4142 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3634 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2745 | 311 | 663 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2467 | 206 | 439 | 636 | 86 | 2026-05-18 21:38:25 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 397 | 26 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1505 | 359 | 2026-05-18 17:53:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-18 17:55:16 |
| [pypy](https://github.com/pypy/pypy) | 1734 | 113 | 5210 | 248 | 739 | 2026-05-18 21:27:42 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 130 | 112 | 2026-05-18 19:40:14 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-18 17:13:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-19T04:17:33*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
