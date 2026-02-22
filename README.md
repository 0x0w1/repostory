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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193880 | 75231 | 41166 | 67554 | 3554 | 2026-02-22 02:08:01 |
| [transformers](https://github.com/huggingface/transformers) | 156788 | 32151 | 18604 | 24999 | 2286 | 2026-02-22 01:40:14 |
| [pytorch](https://github.com/pytorch/pytorch) | 97662 | 26940 | 56893 | 118073 | 17943 | 2026-02-22 02:23:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 95423 | 8720 | 3503 | 5326 | 150 | 2026-02-21 17:25:35 |
| [django](https://github.com/django/django) | 86903 | 33660 | 0 | 20681 | 421 | 2026-02-21 14:57:50 |
| [cpython](https://github.com/python/cpython) | 71658 | 34107 | 75319 | 68774 | 9248 | 2026-02-21 21:31:23 |
| [flask](https://github.com/pallets/flask) | 71250 | 16725 | 2721 | 2779 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65189 | 26718 | 11957 | 20250 | 2147 | 2026-02-21 11:57:35 |
| [keras](https://github.com/keras-team/keras) | 63865 | 19705 | 12640 | 8817 | 292 | 2026-02-21 03:15:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 47939 | 19692 | 28129 | 36077 | 3661 | 2026-02-21 18:13:27 |
| [ray](https://github.com/ray-project/ray) | 41420 | 7245 | 22354 | 38525 | 3391 | 2026-02-21 18:30:12 |
| [gym](https://github.com/openai/gym) | 37059 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33228 | 4637 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31481 | 12071 | 13796 | 16998 | 2311 | 2026-02-20 20:41:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29882 | 7069 | 3946 | 4925 | 83 | 2026-02-21 13:18:05 |
| [celery](https://github.com/celery/celery) | 28122 | 4955 | 5196 | 3815 | 776 | 2026-02-21 16:01:21 |
| [dash](https://github.com/plotly/dash) | 24508 | 2256 | 2058 | 1439 | 560 | 2026-02-20 16:45:58 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22471 | 8212 | 11161 | 19978 | 1543 | 2026-02-20 19:55:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22442 | 5546 | 1863 | 1702 | 216 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21810 | 1401 | 1302 | 5827 | 377 | 2026-02-21 15:30:56 |
| [micropython](https://github.com/micropython/micropython) | 21481 | 8720 | 5962 | 7582 | 1863 | 2026-02-14 08:06:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1464 | 1671 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18273 | 2776 | 3324 | 2042 | 778 | 2026-02-20 18:16:17 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16357 | 2198 | 3178 | 8630 | 275 | 2026-02-22 01:12:28 |
| [httpx](https://github.com/encode/httpx) | 15095 | 1042 | 925 | 1797 | 141 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14475 | 5621 | 11319 | 13305 | 1771 | 2026-02-21 23:10:19 |
| [dask](https://github.com/dask/dask) | 13746 | 1846 | 5508 | 6495 | 1230 | 2026-02-19 18:37:15 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13739 | 2079 | 2646 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11945 | 1119 | 763 | 1806 | 50 | 2026-02-21 09:22:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11655 | 601 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11620 | 1637 | 8157 | 1035 | 214 | 2026-02-19 17:53:52 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 979 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8913 | 558 | 1014 | 487 | 216 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8757 | 1497 | 861 | 630 | 283 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7173 | 387 | 880 | 2506 | 316 | 2026-02-18 16:15:26 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6754 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5612 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5502 | 459 | 1231 | 779 | 483 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5193 | 1000 | 905 | 291 | 197 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 893 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3970 | 315 | 1181 | 212 | 118 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3599 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2729 | 309 | 659 | 1278 | 307 | 2026-02-22 02:29:07 |
| [anyio](https://github.com/agronholm/anyio) | 2394 | 183 | 426 | 576 | 82 | 2026-02-21 12:49:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-02-16 17:43:15 |
| [pypy](https://github.com/pypy/pypy) | 1655 | 99 | 5176 | 179 | 757 | 2026-02-19 08:17:00 |
| [jython](https://github.com/jython/jython) | 1483 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-22T02:53:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
