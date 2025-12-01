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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192633 | 75010 | 41044 | 62245 | 2657 | 2025-11-30 23:23:16 |
| [transformers](https://github.com/huggingface/transformers) | 153198 | 31275 | 18246 | 23651 | 2126 | 2025-11-29 11:20:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 95497 | 26053 | 55601 | 113179 | 17803 | 2025-12-01 02:25:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 92504 | 8299 | 3477 | 4914 | 226 | 2025-11-30 14:48:25 |
| [django](https://github.com/django/django) | 85986 | 33276 | 0 | 20282 | 368 | 2025-11-30 07:31:42 |
| [flask](https://github.com/pallets/flask) | 70860 | 16640 | 2704 | 2729 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70074 | 33546 | 74501 | 66649 | 9183 | 2025-12-01 02:19:48 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64165 | 26476 | 11830 | 19855 | 2111 | 2025-11-30 15:46:50 |
| [keras](https://github.com/keras-team/keras) | 63617 | 19653 | 12598 | 8490 | 269 | 2025-11-27 15:12:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 47220 | 19356 | 27915 | 35266 | 3612 | 2025-11-30 18:17:26 |
| [ray](https://github.com/ray-project/ray) | 40078 | 6956 | 21949 | 36782 | 3269 | 2025-12-01 00:08:17 |
| [gym](https://github.com/openai/gym) | 36825 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32888 | 4633 | 5732 | 4074 | 182 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30933 | 11769 | 13672 | 16600 | 2364 | 2025-12-01 00:06:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29702 | 7038 | 3946 | 4876 | 92 | 2025-11-29 13:36:58 |
| [celery](https://github.com/celery/celery) | 27641 | 4906 | 5176 | 3732 | 753 | 2025-11-30 17:40:27 |
| [dash](https://github.com/plotly/dash) | 24294 | 2239 | 2030 | 1382 | 562 | 2025-11-27 17:51:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22376 | 5546 | 1856 | 1677 | 207 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22073 | 8133 | 11061 | 19695 | 1604 | 2025-11-29 21:39:24 |
| [micropython](https://github.com/micropython/micropython) | 21153 | 8560 | 5884 | 7391 | 1792 | 2025-11-30 12:12:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 20855 | 1364 | 1240 | 5012 | 449 | 2025-11-30 07:58:08 |
| [sanic](https://github.com/sanic-org/sanic) | 18587 | 1584 | 1453 | 1635 | 133 | 2025-11-30 19:21:39 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18036 | 2754 | 3301 | 1985 | 751 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16119 | 2160 | 3163 | 8311 | 286 | 2025-11-28 17:34:03 |
| [httpx](https://github.com/encode/httpx) | 14808 | 980 | 923 | 1757 | 115 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14229 | 5553 | 11163 | 12906 | 1768 | 2025-12-01 01:58:31 |
| [dask](https://github.com/dask/dask) | 13631 | 1826 | 5470 | 6408 | 1198 | 2025-11-25 14:34:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13593 | 2054 | 2636 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11707 | 1088 | 760 | 1745 | 52 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11465 | 586 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11195 | 1604 | 8123 | 1008 | 215 | 2025-11-30 21:59:33 |
| [falcon](https://github.com/falconry/falcon) | 9766 | 971 | 1113 | 1403 | 163 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8741 | 540 | 978 | 456 | 180 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8701 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7035 | 372 | 875 | 2472 | 312 | 2025-11-26 14:29:48 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 746 | 979 | 577 | 33 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5625 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5394 | 446 | 1200 | 722 | 506 | 2025-11-27 05:19:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5102 | 971 | 879 | 263 | 174 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4067 | 887 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4025 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3787 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3553 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2717 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2328 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2309 | 178 | 417 | 553 | 71 | 2025-11-29 16:20:27 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 371 | 1784 | 266 | 265 | 2025-11-24 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1582 | 90 | 5164 | 172 | 748 | 2025-11-24 21:06:55 |
| [jython](https://github.com/jython/jython) | 1461 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-01T02:32:17*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
