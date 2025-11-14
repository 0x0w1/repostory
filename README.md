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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192426 | 74991 | 40988 | 61254 | 2264 | 2025-11-14 02:00:55 |
| [transformers](https://github.com/huggingface/transformers) | 152487 | 31135 | 18183 | 23415 | 2120 | 2025-11-14 00:47:43 |
| [pytorch](https://github.com/pytorch/pytorch) | 95046 | 25897 | 54837 | 112465 | 17052 | 2025-11-14 02:03:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 91900 | 8225 | 3477 | 4872 | 216 | 2025-11-13 17:05:28 |
| [django](https://github.com/django/django) | 85780 | 33224 | 0 | 20030 | 356 | 2025-11-13 16:22:44 |
| [flask](https://github.com/pallets/flask) | 70776 | 16620 | 2701 | 2724 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69848 | 33404 | 74337 | 66258 | 9201 | 2025-11-13 21:26:58 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64024 | 26435 | 11809 | 19764 | 2114 | 2025-11-13 14:05:30 |
| [keras](https://github.com/keras-team/keras) | 63557 | 19648 | 12590 | 8470 | 268 | 2025-11-13 19:35:54 |
| [pandas](https://github.com/pandas-dev/pandas) | 47101 | 19290 | 27877 | 35178 | 3614 | 2025-11-13 21:14:17 |
| [ray](https://github.com/ray-project/ray) | 39815 | 6900 | 21813 | 36453 | 3203 | 2025-11-14 02:02:35 |
| [gym](https://github.com/openai/gym) | 36765 | 8709 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32813 | 4621 | 5730 | 4072 | 196 | 2025-11-13 13:25:50 |
| [numpy](https://github.com/numpy/numpy) | 30819 | 11693 | 13644 | 16501 | 2351 | 2025-11-13 18:55:45 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29662 | 7035 | 3946 | 4867 | 87 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27546 | 4890 | 5176 | 3722 | 754 | 2025-11-14 00:23:26 |
| [dash](https://github.com/plotly/dash) | 24248 | 2230 | 2024 | 1369 | 580 | 2025-11-13 23:49:08 |
| [tornado](https://github.com/tornadoweb/tornado) | 22344 | 5544 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21981 | 8113 | 11044 | 19661 | 1624 | 2025-11-13 20:19:41 |
| [micropython](https://github.com/micropython/micropython) | 21090 | 8528 | 5872 | 7344 | 1801 | 2025-11-13 03:40:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 20794 | 1358 | 1227 | 4961 | 447 | 2025-11-14 01:31:47 |
| [sanic](https://github.com/sanic-org/sanic) | 18558 | 1582 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17965 | 2746 | 3292 | 1977 | 748 | 2025-11-13 23:21:30 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16089 | 2155 | 3161 | 8298 | 282 | 2025-11-13 10:33:58 |
| [httpx](https://github.com/encode/httpx) | 14735 | 975 | 921 | 1754 | 110 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14187 | 5537 | 11134 | 12832 | 1794 | 2025-11-14 00:36:39 |
| [dask](https://github.com/dask/dask) | 13588 | 1821 | 5458 | 6399 | 1193 | 2025-11-12 10:53:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13556 | 2044 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11655 | 1077 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11420 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11124 | 1597 | 8116 | 1000 | 211 | 2025-11-12 23:07:42 |
| [falcon](https://github.com/falconry/falcon) | 9756 | 974 | 1110 | 1400 | 162 | 2025-11-13 20:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8706 | 536 | 967 | 452 | 176 | 2025-11-13 17:57:30 |
| [bottle](https://github.com/bottlepy/bottle) | 8688 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6995 | 371 | 873 | 2469 | 313 | 2025-11-11 03:51:31 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5373 | 444 | 1197 | 715 | 503 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5079 | 963 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 888 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3934 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3752 | 300 | 1166 | 200 | 117 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3538 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2707 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2294 | 176 | 414 | 546 | 76 | 2025-11-13 19:39:09 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 371 | 1782 | 265 | 262 | 2025-11-10 17:52:34 |
| [pypy](https://github.com/pypy/pypy) | 1567 | 89 | 5162 | 171 | 748 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-11-10 17:11:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-14T02:04:52*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
