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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193297 | 75157 | 41067 | 64851 | 2767 | 2026-01-12 01:51:53 |
| [transformers](https://github.com/huggingface/transformers) | 154925 | 31695 | 18409 | 24211 | 2176 | 2026-01-12 02:13:12 |
| [pytorch](https://github.com/pytorch/pytorch) | 96538 | 26485 | 56236 | 115453 | 17859 | 2026-01-12 02:23:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 93971 | 8504 | 3500 | 5119 | 217 | 2026-01-11 22:23:22 |
| [django](https://github.com/django/django) | 86430 | 33468 | 0 | 20461 | 383 | 2026-01-10 07:45:13 |
| [flask](https://github.com/pallets/flask) | 71037 | 16672 | 2708 | 2748 | 12 | 2026-01-05 16:50:56 |
| [cpython](https://github.com/python/cpython) | 71026 | 33871 | 74951 | 67774 | 9239 | 2026-01-11 20:42:55 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64595 | 26589 | 11883 | 20024 | 2115 | 2026-01-11 15:35:59 |
| [keras](https://github.com/keras-team/keras) | 63703 | 19672 | 12608 | 8596 | 241 | 2026-01-09 23:51:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47542 | 19496 | 28010 | 35572 | 3608 | 2026-01-11 20:16:43 |
| [ray](https://github.com/ray-project/ray) | 40714 | 7095 | 22133 | 37555 | 3275 | 2026-01-11 03:20:17 |
| [gym](https://github.com/openai/gym) | 36944 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33062 | 4631 | 5736 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31200 | 11945 | 13740 | 16833 | 2334 | 2026-01-11 21:42:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29798 | 7048 | 3946 | 4899 | 84 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27851 | 4929 | 5182 | 3766 | 757 | 2026-01-10 18:43:35 |
| [dash](https://github.com/plotly/dash) | 24395 | 2248 | 2041 | 1408 | 561 | 2026-01-08 15:55:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22415 | 5545 | 1862 | 1691 | 210 | 2026-01-08 06:35:07 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22212 | 8172 | 11100 | 19806 | 1532 | 2026-01-11 17:56:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 21645 | 1400 | 1283 | 5361 | 369 | 2026-01-12 01:52:16 |
| [micropython](https://github.com/micropython/micropython) | 21333 | 8646 | 5935 | 7475 | 1830 | 2026-01-09 04:23:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18609 | 1584 | 1460 | 1662 | 110 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18168 | 2772 | 3313 | 1998 | 764 | 2026-01-09 17:00:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16197 | 2171 | 3171 | 8481 | 272 | 2026-01-11 20:22:33 |
| [httpx](https://github.com/encode/httpx) | 14890 | 1006 | 925 | 1776 | 124 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14335 | 5581 | 11240 | 13084 | 1753 | 2026-01-11 22:18:13 |
| [dask](https://github.com/dask/dask) | 13705 | 1835 | 5483 | 6445 | 1208 | 2026-01-08 16:18:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13674 | 2080 | 2644 | 1156 | 203 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11831 | 1096 | 761 | 1764 | 50 | 2026-01-11 21:47:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11574 | 597 | 400 | 303 | 156 | 2026-01-12 00:58:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11376 | 1621 | 8138 | 1019 | 208 | 2026-01-11 02:02:35 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 975 | 1115 | 1406 | 162 | 2026-01-10 11:15:16 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8834 | 555 | 995 | 480 | 200 | 2026-01-10 20:01:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8727 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7097 | 378 | 877 | 2486 | 312 | 2026-01-05 22:28:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5619 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5441 | 445 | 1215 | 735 | 512 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5147 | 988 | 884 | 279 | 180 | 2026-01-07 13:28:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4024 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3879 | 305 | 1173 | 207 | 117 | 2026-01-09 21:22:57 |
| [quart](https://github.com/pallets/quart) | 3573 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2353 | 180 | 421 | 562 | 73 | 2026-01-06 11:46:43 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1627 | 95 | 5169 | 174 | 755 | 2026-01-08 21:11:28 |
| [jython](https://github.com/jython/jython) | 1469 | 225 | 289 | 120 | 106 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-12T02:28:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
