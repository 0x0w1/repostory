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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191105 | 74764 | 40706 | 55840 | 1491 | 2025-08-09 01:17:04 |
| [transformers](https://github.com/huggingface/transformers) | 148102 | 29956 | 17730 | 21743 | 1963 | 2025-08-08 20:32:26 |
| [pytorch](https://github.com/pytorch/pytorch) | 92216 | 24898 | 52974 | 106807 | 16757 | 2025-08-09 01:38:33 |
| [fastapi](https://github.com/tiangolo/fastapi) | 88176 | 7704 | 3466 | 4653 | 301 | 2025-08-08 10:32:11 |
| [django](https://github.com/django/django) | 84520 | 32774 | 0 | 19650 | 355 | 2025-08-08 19:39:50 |
| [flask](https://github.com/pallets/flask) | 70142 | 16516 | 2692 | 2685 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68256 | 32522 | 73199 | 63454 | 9274 | 2025-08-08 19:07:15 |
| [keras](https://github.com/keras-team/keras) | 63296 | 19604 | 12519 | 8264 | 288 | 2025-08-08 23:06:18 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 62938 | 26119 | 11635 | 19146 | 2151 | 2025-08-08 16:17:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 46235 | 18771 | 27640 | 34389 | 3696 | 2025-08-08 19:54:59 |
| [ray](https://github.com/ray-project/ray) | 38389 | 6691 | 20842 | 34249 | 2994 | 2025-08-09 01:24:57 |
| [gym](https://github.com/openai/gym) | 36350 | 8687 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32130 | 4556 | 5715 | 4064 | 196 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30111 | 11178 | 13475 | 15990 | 2326 | 2025-08-08 23:55:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29357 | 6989 | 3945 | 4817 | 101 | 2025-08-08 18:18:02 |
| [celery](https://github.com/celery/celery) | 26965 | 4822 | 5153 | 3632 | 760 | 2025-08-06 08:30:26 |
| [dash](https://github.com/plotly/dash) | 23901 | 2184 | 1970 | 1311 | 545 | 2025-08-09 00:05:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22083 | 5537 | 1851 | 1666 | 206 | 2025-08-08 18:27:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21525 | 7949 | 10932 | 19436 | 1652 | 2025-08-07 21:18:23 |
| [micropython](https://github.com/micropython/micropython) | 20705 | 8339 | 5770 | 7074 | 1757 | 2025-08-07 07:02:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 20379 | 1335 | 1204 | 4815 | 432 | 2025-08-08 22:41:13 |
| [sanic](https://github.com/channelcat/sanic) | 18463 | 1576 | 1448 | 1625 | 142 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17574 | 2687 | 3232 | 1937 | 710 | 2025-08-07 21:42:57 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15900 | 2112 | 3140 | 7965 | 259 | 2025-08-08 16:28:50 |
| [httpx](https://github.com/encode/httpx) | 14439 | 936 | 911 | 1704 | 97 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13900 | 5437 | 10963 | 12472 | 1752 | 2025-08-07 04:02:43 |
| [dask](https://github.com/dask/dask) | 13390 | 1791 | 5417 | 6331 | 1185 | 2025-08-04 17:59:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13353 | 2024 | 2621 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11324 | 1029 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11122 | 567 | 387 | 287 | 140 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10751 | 1572 | 8063 | 975 | 237 | 2025-08-07 14:52:25 |
| [falcon](https://github.com/falconry/falcon) | 9698 | 960 | 1091 | 1352 | 158 | 2025-08-08 20:09:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8643 | 1486 | 853 | 621 | 283 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8436 | 517 | 933 | 428 | 412 | 2025-08-08 15:26:58 |
| [hug](https://github.com/timothycrosley/hug) | 6894 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 745 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6682 | 359 | 863 | 2438 | 311 | 2025-08-07 04:47:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5636 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5236 | 434 | 1183 | 705 | 490 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4934 | 922 | 860 | 258 | 156 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4039 | 890 | 1060 | 2712 | 82 | 2025-02-23 16:39:21 |
| [databases](https://github.com/encode/databases) | 3934 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3508 | 286 | 1150 | 193 | 114 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3388 | 184 | 277 | 120 | 62 | 2025-07-29 15:07:12 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2672 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2295 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2166 | 163 | 399 | 496 | 67 | 2025-08-04 18:10:59 |
| [web2py](https://github.com/web2py/web2py) | 2150 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1918 | 369 | 1779 | 264 | 260 | 2025-08-04 17:44:33 |
| [pypy](https://github.com/pypy/pypy) | 1463 | 83 | 5138 | 166 | 732 | 2025-08-08 13:06:27 |
| [jython](https://github.com/jython/jython) | 1416 | 216 | 278 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-09T10:56:34*
