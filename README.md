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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195573 | 75317 | 41513 | 75495 | 3205 | 2026-06-07 04:43:05 |
| [transformers](https://github.com/huggingface/transformers) | 161364 | 33437 | 19039 | 26721 | 2419 | 2026-06-06 19:44:57 |
| [pytorch](https://github.com/pytorch/pytorch) | 100557 | 27952 | 59080 | 126819 | 18329 | 2026-06-07 04:41:07 |
| [fastapi](https://github.com/fastapi/fastapi) | 98997 | 9406 | 3528 | 5870 | 95 | 2026-06-05 19:20:50 |
| [django](https://github.com/django/django) | 87778 | 33964 | 0 | 21354 | 447 | 2026-06-05 21:11:32 |
| [cpython](https://github.com/python/cpython) | 73117 | 34702 | 76635 | 72073 | 9307 | 2026-06-06 21:38:15 |
| [flask](https://github.com/pallets/flask) | 71641 | 16853 | 2741 | 2834 | 4 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66269 | 27051 | 12125 | 20900 | 2041 | 2026-06-05 07:30:53 |
| [keras](https://github.com/keras-team/keras) | 64088 | 19746 | 12776 | 9416 | 175 | 2026-06-05 21:31:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 48912 | 19995 | 28303 | 37426 | 3223 | 2026-06-06 16:09:55 |
| [ray](https://github.com/ray-project/ray) | 42797 | 7658 | 22722 | 40797 | 3445 | 2026-06-06 21:49:29 |
| [gym](https://github.com/openai/gym) | 37210 | 8703 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33635 | 4687 | 5757 | 4095 | 209 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32157 | 12429 | 13931 | 17567 | 2374 | 2026-06-06 21:00:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30056 | 7068 | 3967 | 5009 | 77 | 2026-06-06 13:20:03 |
| [celery](https://github.com/celery/celery) | 28563 | 5070 | 5280 | 4131 | 784 | 2026-06-03 07:47:09 |
| [dash](https://github.com/plotly/dash) | 24236 | 2290 | 2103 | 1580 | 538 | 2026-06-06 11:56:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22866 | 8349 | 11301 | 20493 | 1460 | 2026-06-06 02:08:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5538 | 1872 | 1741 | 217 | 2026-06-05 15:54:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 22099 | 1440 | 1353 | 6625 | 384 | 2026-06-04 20:20:35 |
| [micropython](https://github.com/micropython/micropython) | 21787 | 8860 | 6066 | 7856 | 1684 | 2026-06-04 13:18:58 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1590 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18583 | 2806 | 3351 | 2094 | 758 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2295 | 3211 | 9304 | 260 | 2026-06-07 03:09:26 |
| [httpx](https://github.com/encode/httpx) | 15279 | 1163 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14738 | 5750 | 11462 | 13831 | 1794 | 2026-06-06 21:08:06 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13900 | 2115 | 2653 | 1182 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13849 | 1880 | 5536 | 6602 | 1241 | 2026-06-06 20:15:44 |
| [starlette](https://github.com/Kludex/starlette) | 12367 | 1192 | 770 | 1936 | 58 | 2026-06-05 08:52:03 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11894 | 1695 | 8225 | 1106 | 212 | 2026-06-05 14:25:43 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11812 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 998 | 1127 | 1453 | 159 | 2026-06-01 11:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9081 | 596 | 1037 | 517 | 214 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7277 | 398 | 892 | 2550 | 320 | 2026-06-01 23:07:35 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5596 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5576 | 486 | 1257 | 848 | 516 | 2026-06-07 04:29:18 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5277 | 1018 | 914 | 300 | 212 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4181 | 337 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3639 | 200 | 283 | 128 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2748 | 311 | 666 | 1320 | 307 | 2026-06-06 13:02:09 |
| [anyio](https://github.com/agronholm/anyio) | 2478 | 207 | 441 | 647 | 83 | 2026-06-04 21:38:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 429 | 402 | 31 | 2026-06-07 01:27:55 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1536 | 360 | 2026-06-06 20:15:33 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-01 17:59:42 |
| [pypy](https://github.com/pypy/pypy) | 1747 | 113 | 5215 | 258 | 735 | 2026-06-06 18:47:23 |
| [jython](https://github.com/jython/jython) | 1515 | 230 | 297 | 135 | 110 | 2026-06-03 08:15:01 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 113 | 78 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-07T04:48:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
