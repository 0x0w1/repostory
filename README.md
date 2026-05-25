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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195258 | 75338 | 41464 | 74376 | 5577 | 2026-05-25 04:25:42 |
| [transformers](https://github.com/huggingface/transformers) | 160934 | 33309 | 18991 | 26490 | 2396 | 2026-05-25 04:41:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 100165 | 27862 | 58883 | 125622 | 18546 | 2026-05-25 04:39:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 98488 | 9341 | 3528 | 5798 | 102 | 2026-05-24 13:06:13 |
| [django](https://github.com/django/django) | 87572 | 33952 | 0 | 21289 | 444 | 2026-05-25 00:58:38 |
| [cpython](https://github.com/python/cpython) | 72877 | 34677 | 76472 | 71577 | 9315 | 2026-05-24 19:31:20 |
| [flask](https://github.com/pallets/flask) | 71575 | 16852 | 2739 | 2830 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66181 | 27045 | 12106 | 20824 | 2029 | 2026-05-24 18:21:52 |
| [keras](https://github.com/keras-team/keras) | 64086 | 19776 | 12765 | 9361 | 198 | 2026-05-22 21:17:15 |
| [pandas](https://github.com/pandas-dev/pandas) | 48838 | 19976 | 28291 | 37341 | 3269 | 2026-05-25 02:17:25 |
| [ray](https://github.com/ray-project/ray) | 42656 | 7606 | 22695 | 40533 | 3434 | 2026-05-24 20:46:30 |
| [gym](https://github.com/openai/gym) | 37210 | 8702 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33608 | 4685 | 5756 | 4093 | 206 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32088 | 12381 | 13926 | 17495 | 2381 | 2026-05-24 22:25:18 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30029 | 7067 | 3967 | 5006 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28526 | 5049 | 5280 | 4119 | 783 | 2026-05-20 12:26:36 |
| [dash](https://github.com/plotly/dash) | 24211 | 2285 | 2102 | 1568 | 556 | 2026-05-22 07:08:24 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22832 | 8340 | 11282 | 20401 | 1480 | 2026-05-24 21:34:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5541 | 1872 | 1735 | 220 | 2026-05-21 18:10:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 22075 | 1441 | 1347 | 6547 | 383 | 2026-05-24 11:00:32 |
| [micropython](https://github.com/micropython/micropython) | 21737 | 8838 | 6057 | 7825 | 1729 | 2026-05-25 03:19:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1590 | 1466 | 1686 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18551 | 2808 | 3345 | 2088 | 759 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16442 | 2273 | 3205 | 9151 | 244 | 2026-05-22 13:00:52 |
| [httpx](https://github.com/encode/httpx) | 15288 | 1147 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14717 | 5737 | 11450 | 13749 | 1793 | 2026-05-25 01:45:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13887 | 2117 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13842 | 1874 | 5529 | 6579 | 1244 | 2026-05-22 23:37:08 |
| [starlette](https://github.com/Kludex/starlette) | 12329 | 1178 | 768 | 1911 | 62 | 2026-05-23 16:54:32 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11877 | 1685 | 8216 | 1092 | 214 | 2026-05-24 19:21:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11791 | 607 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 999 | 1125 | 1449 | 158 | 2026-05-21 04:48:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9068 | 579 | 1036 | 513 | 211 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8767 | 1500 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7272 | 397 | 892 | 2546 | 320 | 2026-05-24 18:55:32 |
| [hug](https://github.com/hugapi/hug) | 6888 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5570 | 484 | 1256 | 838 | 510 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5263 | 1016 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4152 | 333 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 198 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 664 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2471 | 208 | 439 | 640 | 86 | 2026-05-24 14:46:47 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1520 | 365 | 2026-05-21 15:39:48 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 268 | 266 | 2026-05-18 17:55:16 |
| [pypy](https://github.com/pypy/pypy) | 1740 | 113 | 5214 | 250 | 740 | 2026-05-24 17:43:24 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 131 | 109 | 2026-05-23 16:06:46 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-18 17:13:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-25T04:42:19*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
