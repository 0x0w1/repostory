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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193688 | 75225 | 41151 | 66848 | 3390 | 2026-02-11 03:11:04 |
| [transformers](https://github.com/huggingface/transformers) | 156340 | 32031 | 18561 | 24739 | 2209 | 2026-02-10 21:36:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 97312 | 26818 | 56753 | 117483 | 18025 | 2026-02-11 03:16:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 94989 | 8671 | 3503 | 5270 | 158 | 2026-02-11 03:00:57 |
| [django](https://github.com/django/django) | 86730 | 33634 | 0 | 20604 | 400 | 2026-02-10 22:59:02 |
| [cpython](https://github.com/python/cpython) | 71450 | 34055 | 75223 | 68478 | 9204 | 2026-02-10 23:09:08 |
| [flask](https://github.com/pallets/flask) | 71147 | 16707 | 2714 | 2766 | 2 | 2026-02-06 21:23:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64981 | 26675 | 11931 | 20185 | 2129 | 2026-02-10 15:16:28 |
| [keras](https://github.com/keras-team/keras) | 63763 | 19691 | 12630 | 8728 | 281 | 2026-02-10 04:38:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 47852 | 19644 | 28089 | 35956 | 3639 | 2026-02-10 22:52:47 |
| [ray](https://github.com/ray-project/ray) | 41217 | 7204 | 22311 | 38295 | 3365 | 2026-02-11 02:52:52 |
| [gym](https://github.com/openai/gym) | 37032 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33184 | 4639 | 5739 | 4078 | 187 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31414 | 12042 | 13786 | 16964 | 2313 | 2026-02-11 02:11:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29868 | 7066 | 3946 | 4921 | 90 | 2026-02-10 14:31:29 |
| [celery](https://github.com/celery/celery) | 27997 | 4944 | 5193 | 3792 | 773 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24462 | 2254 | 2053 | 1431 | 559 | 2026-02-07 17:40:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22445 | 5547 | 1863 | 1699 | 214 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22321 | 8185 | 11144 | 19943 | 1537 | 2026-02-11 00:33:19 |
| [RustPython](https://github.com/RustPython/RustPython) | 21777 | 1400 | 1297 | 5713 | 368 | 2026-02-11 02:10:12 |
| [micropython](https://github.com/micropython/micropython) | 21452 | 8699 | 5952 | 7550 | 1839 | 2026-02-11 00:35:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1465 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18243 | 2773 | 3322 | 2026 | 775 | 2026-02-10 19:15:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16259 | 2188 | 3177 | 8567 | 287 | 2026-02-11 02:43:16 |
| [httpx](https://github.com/encode/httpx) | 14978 | 1029 | 925 | 1789 | 135 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14444 | 5613 | 11300 | 13244 | 1767 | 2026-02-10 23:45:57 |
| [dask](https://github.com/dask/dask) | 13737 | 1842 | 5504 | 6486 | 1224 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13718 | 2078 | 2646 | 1160 | 204 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11911 | 1115 | 763 | 1787 | 56 | 2026-02-11 02:32:47 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11639 | 601 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11492 | 1636 | 8152 | 1030 | 207 | 2026-02-09 14:28:51 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 979 | 1119 | 1413 | 163 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8893 | 557 | 1006 | 483 | 206 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8749 | 1493 | 860 | 628 | 282 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7161 | 385 | 878 | 2498 | 317 | 2026-02-10 22:42:45 |
| [hug](https://github.com/hugapi/hug) | 6906 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 584 | 38 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5489 | 458 | 1224 | 767 | 484 | 2026-02-11 02:58:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5183 | 999 | 901 | 289 | 191 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3952 | 310 | 1181 | 209 | 115 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3593 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2726 | 308 | 658 | 1270 | 313 | 2026-02-08 01:14:02 |
| [anyio](https://github.com/agronholm/anyio) | 2382 | 180 | 423 | 569 | 74 | 2026-02-09 18:37:13 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1934 | 367 | 1785 | 266 | 266 | 2026-02-09 18:28:59 |
| [pypy](https://github.com/pypy/pypy) | 1650 | 98 | 5175 | 179 | 757 | 2026-02-09 08:46:09 |
| [jython](https://github.com/jython/jython) | 1479 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-11T03:17:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
