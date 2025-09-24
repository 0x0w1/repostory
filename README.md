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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191770 | 74878 | 40812 | 58066 | 1688 | 2025-09-24 01:54:52 |
| [transformers](https://github.com/huggingface/transformers) | 150148 | 30489 | 17969 | 22563 | 1997 | 2025-09-23 23:20:01 |
| [pytorch](https://github.com/pytorch/pytorch) | 93405 | 25386 | 53925 | 109340 | 17136 | 2025-09-24 01:54:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 89758 | 7919 | 3468 | 4725 | 215 | 2025-09-23 12:44:04 |
| [django](https://github.com/django/django) | 85113 | 33004 | 0 | 19833 | 352 | 2025-09-23 16:36:49 |
| [flask](https://github.com/pallets/flask) | 70422 | 16544 | 2697 | 2703 | 8 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69006 | 32932 | 73689 | 64660 | 9291 | 2025-09-24 01:52:24 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63426 | 26267 | 11721 | 19410 | 2175 | 2025-09-23 14:01:47 |
| [keras](https://github.com/keras-team/keras) | 63424 | 19629 | 12551 | 8351 | 260 | 2025-09-23 18:29:06 |
| [pandas](https://github.com/pandas-dev/pandas) | 46642 | 19003 | 27724 | 34652 | 3645 | 2025-09-24 00:50:01 |
| [ray](https://github.com/ray-project/ray) | 39063 | 6819 | 21204 | 35314 | 3101 | 2025-09-24 01:24:09 |
| [gym](https://github.com/openai/gym) | 36572 | 8698 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32519 | 4579 | 5722 | 4068 | 204 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30443 | 11453 | 13548 | 16193 | 2357 | 2025-09-24 00:33:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29490 | 7009 | 3945 | 4839 | 104 | 2025-09-20 10:19:28 |
| [celery](https://github.com/celery/celery) | 27241 | 4849 | 5164 | 3664 | 752 | 2025-09-23 12:12:22 |
| [dash](https://github.com/plotly/dash) | 24088 | 2205 | 1997 | 1333 | 563 | 2025-09-23 00:45:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22218 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21722 | 8036 | 10991 | 19560 | 1627 | 2025-09-22 19:03:57 |
| [micropython](https://github.com/micropython/micropython) | 20870 | 8446 | 5822 | 7207 | 1788 | 2025-09-24 01:43:02 |
| [RustPython](https://github.com/RustPython/RustPython) | 20545 | 1348 | 1220 | 4890 | 446 | 2025-09-22 13:05:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18493 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17765 | 2719 | 3251 | 1953 | 722 | 2025-09-19 15:28:16 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16005 | 2126 | 3146 | 8094 | 273 | 2025-09-23 17:00:26 |
| [httpx](https://github.com/encode/httpx) | 14578 | 957 | 918 | 1731 | 98 | 2025-09-20 17:09:10 |
| [scipy](https://github.com/scipy/scipy) | 14045 | 5483 | 11037 | 12614 | 1761 | 2025-09-23 15:22:37 |
| [dask](https://github.com/dask/dask) | 13493 | 1798 | 5437 | 6348 | 1199 | 2025-09-23 15:16:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13453 | 2037 | 2627 | 1148 | 188 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11490 | 1044 | 754 | 1712 | 46 | 2025-09-20 21:43:28 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11277 | 574 | 388 | 289 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10932 | 1580 | 8089 | 983 | 223 | 2025-09-23 19:56:10 |
| [falcon](https://github.com/falconry/falcon) | 9722 | 959 | 1100 | 1370 | 156 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8664 | 1486 | 855 | 623 | 283 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8561 | 525 | 946 | 435 | 409 | 2025-09-21 09:38:28 |
| [hug](https://github.com/hugapi/hug) | 6895 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6865 | 366 | 870 | 2455 | 312 | 2025-09-22 22:36:12 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5299 | 438 | 1194 | 713 | 499 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5011 | 940 | 871 | 261 | 169 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 888 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3632 | 292 | 1158 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3466 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2688 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2306 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2217 | 163 | 401 | 513 | 62 | 2025-09-23 14:10:12 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1923 | 369 | 1780 | 264 | 261 | 2025-09-22 17:45:36 |
| [pypy](https://github.com/pypy/pypy) | 1502 | 86 | 5144 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1435 | 222 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-09-22 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-24T01:55:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
