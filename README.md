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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194936 | 75296 | 41342 | 72461 | 4783 | 2026-04-30 03:52:02 |
| [transformers](https://github.com/huggingface/transformers) | 160099 | 33057 | 18906 | 26146 | 2334 | 2026-04-30 03:10:53 |
| [pytorch](https://github.com/pytorch/pytorch) | 99539 | 27621 | 58337 | 123086 | 18530 | 2026-04-30 03:52:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 97767 | 9171 | 3523 | 5679 | 179 | 2026-04-29 12:22:44 |
| [django](https://github.com/django/django) | 87359 | 33856 | 0 | 21126 | 428 | 2026-04-29 20:42:29 |
| [cpython](https://github.com/python/cpython) | 72518 | 34513 | 76169 | 70701 | 9427 | 2026-04-30 02:39:29 |
| [flask](https://github.com/pallets/flask) | 71478 | 16827 | 2736 | 2813 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65953 | 26981 | 12063 | 20673 | 2062 | 2026-04-29 14:56:41 |
| [keras](https://github.com/keras-team/keras) | 64049 | 19761 | 12741 | 9257 | 245 | 2026-04-30 01:01:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 48622 | 19887 | 28263 | 37076 | 3392 | 2026-04-30 01:35:35 |
| [ray](https://github.com/ray-project/ray) | 42373 | 7512 | 22628 | 40045 | 3534 | 2026-04-30 02:43:37 |
| [gym](https://github.com/openai/gym) | 37176 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33528 | 4678 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31933 | 12325 | 13899 | 17389 | 2366 | 2026-04-29 18:59:11 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29983 | 7066 | 3967 | 5002 | 78 | 2026-04-28 07:27:54 |
| [celery](https://github.com/celery/celery) | 28417 | 5026 | 5272 | 4097 | 775 | 2026-04-29 14:03:56 |
| [dash](https://github.com/plotly/dash) | 24165 | 2276 | 2092 | 1546 | 543 | 2026-04-28 20:44:28 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22755 | 8325 | 11255 | 20277 | 1502 | 2026-04-29 20:32:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22218 | 5541 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22027 | 1432 | 1339 | 6329 | 376 | 2026-04-30 02:09:17 |
| [micropython](https://github.com/micropython/micropython) | 21664 | 8812 | 6042 | 7758 | 1890 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18491 | 2804 | 3340 | 2078 | 762 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16428 | 2260 | 3191 | 8915 | 281 | 2026-04-29 10:50:13 |
| [httpx](https://github.com/encode/httpx) | 15247 | 1135 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14649 | 5716 | 11426 | 13633 | 1789 | 2026-04-28 18:34:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13833 | 2104 | 2653 | 1173 | 216 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13812 | 1867 | 5522 | 6535 | 1246 | 2026-04-28 16:39:15 |
| [starlette](https://github.com/Kludex/starlette) | 12259 | 1165 | 766 | 1884 | 60 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11810 | 1674 | 8202 | 1065 | 215 | 2026-04-29 19:57:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11775 | 605 | 413 | 323 | 162 | 2026-04-28 20:38:57 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 996 | 1125 | 1443 | 157 | 2026-04-26 06:35:15 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9032 | 573 | 1033 | 509 | 206 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8757 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7249 | 393 | 891 | 2538 | 321 | 2026-04-29 10:11:16 |
| [hug](https://github.com/hugapi/hug) | 6893 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5562 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5249 | 1008 | 912 | 291 | 202 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4104 | 330 | 1183 | 218 | 113 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4006 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3627 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2448 | 201 | 436 | 620 | 86 | 2026-04-29 18:19:16 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 907 | 1084 | 1487 | 361 | 2026-04-29 16:54:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-27 17:52:32 |
| [pypy](https://github.com/pypy/pypy) | 1716 | 112 | 5202 | 233 | 739 | 2026-04-29 21:26:24 |
| [jython](https://github.com/jython/jython) | 1504 | 228 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-04-26 08:05:46 |

*Last Automatic Update: 2026-04-30T03:53:35*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
