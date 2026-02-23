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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193886 | 75228 | 41167 | 67584 | 3575 | 2026-02-23 02:34:29 |
| [transformers](https://github.com/huggingface/transformers) | 156826 | 32164 | 18607 | 25009 | 2297 | 2026-02-23 01:20:14 |
| [pytorch](https://github.com/pytorch/pytorch) | 97685 | 26950 | 56897 | 118096 | 17933 | 2026-02-23 02:22:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 95461 | 8725 | 3503 | 5331 | 150 | 2026-02-22 18:22:03 |
| [django](https://github.com/django/django) | 86910 | 33667 | 0 | 20686 | 422 | 2026-02-21 14:57:50 |
| [cpython](https://github.com/python/cpython) | 71672 | 34120 | 75336 | 68799 | 9266 | 2026-02-23 01:59:41 |
| [flask](https://github.com/pallets/flask) | 71253 | 16726 | 2721 | 2779 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65201 | 26722 | 11958 | 20260 | 2141 | 2026-02-22 17:07:00 |
| [keras](https://github.com/keras-team/keras) | 63866 | 19703 | 12641 | 8824 | 288 | 2026-02-22 21:35:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 47954 | 19688 | 28130 | 36084 | 3667 | 2026-02-22 15:45:41 |
| [ray](https://github.com/ray-project/ray) | 41430 | 7245 | 22355 | 38537 | 3401 | 2026-02-23 01:31:42 |
| [gym](https://github.com/openai/gym) | 37058 | 8708 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33233 | 4638 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31492 | 12072 | 13797 | 17000 | 2312 | 2026-02-23 00:47:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29885 | 7067 | 3946 | 4926 | 84 | 2026-02-21 13:18:05 |
| [celery](https://github.com/celery/celery) | 28131 | 4961 | 5196 | 3818 | 775 | 2026-02-22 11:31:39 |
| [dash](https://github.com/plotly/dash) | 24509 | 2256 | 2058 | 1439 | 560 | 2026-02-20 16:45:58 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22478 | 8212 | 11161 | 19979 | 1544 | 2026-02-20 19:55:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22443 | 5546 | 1863 | 1702 | 216 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21813 | 1402 | 1303 | 5832 | 378 | 2026-02-22 23:48:18 |
| [micropython](https://github.com/micropython/micropython) | 21485 | 8721 | 5962 | 7582 | 1853 | 2026-02-23 02:35:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1464 | 1671 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18281 | 2775 | 3324 | 2042 | 778 | 2026-02-20 18:16:17 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16359 | 2198 | 3178 | 8641 | 269 | 2026-02-22 17:11:52 |
| [httpx](https://github.com/encode/httpx) | 15096 | 1042 | 925 | 1798 | 142 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14477 | 5622 | 11322 | 13311 | 1775 | 2026-02-23 02:48:06 |
| [dask](https://github.com/dask/dask) | 13746 | 1844 | 5508 | 6496 | 1230 | 2026-02-22 23:28:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13741 | 2079 | 2647 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11948 | 1119 | 763 | 1806 | 47 | 2026-02-22 13:27:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11655 | 601 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11623 | 1639 | 8158 | 1035 | 215 | 2026-02-19 17:53:52 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 979 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8916 | 558 | 1015 | 487 | 217 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8758 | 1497 | 861 | 630 | 283 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7175 | 387 | 880 | 2506 | 316 | 2026-02-18 16:15:26 |
| [hug](https://github.com/hugapi/hug) | 6909 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6754 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5611 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5503 | 460 | 1232 | 779 | 484 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5193 | 1000 | 906 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 893 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3970 | 316 | 1180 | 213 | 118 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3599 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2729 | 309 | 660 | 1280 | 308 | 2026-02-23 02:49:11 |
| [anyio](https://github.com/agronholm/anyio) | 2394 | 183 | 426 | 576 | 82 | 2026-02-21 12:49:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-02-16 17:43:15 |
| [pypy](https://github.com/pypy/pypy) | 1656 | 99 | 5176 | 179 | 757 | 2026-02-19 08:17:00 |
| [jython](https://github.com/jython/jython) | 1483 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-23T02:53:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
