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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193865 | 75233 | 41162 | 67447 | 3592 | 2026-02-20 02:36:24 |
| [transformers](https://github.com/huggingface/transformers) | 156731 | 32135 | 18596 | 24964 | 2282 | 2026-02-19 21:04:43 |
| [pytorch](https://github.com/pytorch/pytorch) | 97603 | 26914 | 56876 | 118002 | 17980 | 2026-02-20 02:45:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 95356 | 8709 | 3503 | 5313 | 145 | 2026-02-19 13:16:40 |
| [django](https://github.com/django/django) | 86891 | 33652 | 0 | 20673 | 424 | 2026-02-19 16:33:48 |
| [cpython](https://github.com/python/cpython) | 71643 | 34102 | 75297 | 68735 | 9245 | 2026-02-19 23:45:28 |
| [flask](https://github.com/pallets/flask) | 71240 | 16726 | 2717 | 2776 | 3 | 2026-02-19 16:42:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65180 | 26709 | 11953 | 20236 | 2137 | 2026-02-19 16:19:59 |
| [keras](https://github.com/keras-team/keras) | 63858 | 19701 | 12638 | 8791 | 279 | 2026-02-20 01:14:24 |
| [pandas](https://github.com/pandas-dev/pandas) | 47918 | 19682 | 28119 | 36060 | 3656 | 2026-02-19 23:04:58 |
| [ray](https://github.com/ray-project/ray) | 41403 | 7240 | 22343 | 38498 | 3378 | 2026-02-20 02:06:04 |
| [gym](https://github.com/openai/gym) | 37053 | 8711 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33221 | 4635 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31478 | 12069 | 13794 | 16993 | 2311 | 2026-02-19 13:39:10 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29879 | 7067 | 3946 | 4925 | 87 | 2026-02-19 13:00:10 |
| [celery](https://github.com/celery/celery) | 28115 | 4952 | 5196 | 3815 | 779 | 2026-02-19 22:13:40 |
| [dash](https://github.com/plotly/dash) | 24500 | 2256 | 2056 | 1439 | 562 | 2026-02-18 16:47:44 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22452 | 8199 | 11159 | 19974 | 1544 | 2026-02-18 08:43:13 |
| [tornado](https://github.com/tornadoweb/tornado) | 22441 | 5545 | 1863 | 1702 | 216 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21807 | 1401 | 1301 | 5822 | 374 | 2026-02-20 00:53:01 |
| [micropython](https://github.com/micropython/micropython) | 21475 | 8716 | 5959 | 7572 | 1865 | 2026-02-14 08:06:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1584 | 1464 | 1668 | 120 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18264 | 2776 | 3324 | 2038 | 777 | 2026-02-19 19:54:54 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16351 | 2197 | 3177 | 8610 | 280 | 2026-02-19 23:32:53 |
| [httpx](https://github.com/encode/httpx) | 15090 | 1041 | 925 | 1797 | 142 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14474 | 5621 | 11319 | 13293 | 1771 | 2026-02-20 00:56:56 |
| [dask](https://github.com/dask/dask) | 13745 | 1843 | 5507 | 6494 | 1228 | 2026-02-19 18:37:15 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13735 | 2078 | 2646 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11934 | 1119 | 763 | 1806 | 52 | 2026-02-15 13:37:42 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11652 | 600 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11612 | 1639 | 8157 | 1034 | 213 | 2026-02-19 17:53:52 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 979 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8908 | 558 | 1014 | 487 | 216 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8758 | 1497 | 861 | 630 | 283 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7170 | 386 | 880 | 2503 | 314 | 2026-02-18 16:15:26 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6753 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5613 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5498 | 460 | 1230 | 779 | 482 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5191 | 1000 | 905 | 291 | 197 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4072 | 893 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3966 | 314 | 1181 | 210 | 116 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3598 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2727 | 309 | 659 | 1276 | 310 | 2026-02-18 14:09:57 |
| [anyio](https://github.com/agronholm/anyio) | 2388 | 182 | 426 | 572 | 78 | 2026-02-15 00:48:12 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1936 | 367 | 1785 | 266 | 266 | 2026-02-16 17:43:15 |
| [pypy](https://github.com/pypy/pypy) | 1653 | 99 | 5176 | 179 | 757 | 2026-02-19 08:17:00 |
| [jython](https://github.com/jython/jython) | 1483 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-20T02:46:42*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
