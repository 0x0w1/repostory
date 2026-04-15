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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194724 | 75276 | 41308 | 71158 | 4402 | 2026-04-15 03:29:49 |
| [transformers](https://github.com/huggingface/transformers) | 159383 | 32871 | 18861 | 25934 | 2355 | 2026-04-15 01:07:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 99127 | 27490 | 58004 | 121891 | 18524 | 2026-04-15 03:29:41 |
| [fastapi](https://github.com/fastapi/fastapi) | 97209 | 9074 | 3517 | 5581 | 172 | 2026-04-14 14:14:07 |
| [django](https://github.com/django/django) | 87266 | 33807 | 0 | 21041 | 431 | 2026-04-14 11:32:08 |
| [cpython](https://github.com/python/cpython) | 72330 | 34423 | 75965 | 70336 | 9328 | 2026-04-15 00:15:27 |
| [flask](https://github.com/pallets/flask) | 71419 | 16787 | 2731 | 2803 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65823 | 26942 | 12035 | 20552 | 2047 | 2026-04-14 14:26:18 |
| [keras](https://github.com/keras-team/keras) | 63992 | 19737 | 12727 | 9148 | 268 | 2026-04-15 03:08:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 48503 | 19867 | 28247 | 36922 | 3458 | 2026-04-14 21:52:21 |
| [ray](https://github.com/ray-project/ray) | 42124 | 7441 | 22565 | 39703 | 3580 | 2026-04-15 03:23:46 |
| [gym](https://github.com/openai/gym) | 37161 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33469 | 4671 | 5753 | 4089 | 199 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31851 | 12305 | 13874 | 17298 | 2345 | 2026-04-14 23:18:17 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29969 | 7066 | 3968 | 4997 | 76 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28360 | 5008 | 5267 | 4074 | 785 | 2026-04-14 17:05:24 |
| [dash](https://github.com/plotly/dash) | 24204 | 2274 | 2089 | 1530 | 544 | 2026-04-14 18:32:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22714 | 8317 | 11242 | 20203 | 1504 | 2026-04-13 20:51:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22270 | 5544 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22000 | 1425 | 1332 | 6208 | 388 | 2026-04-14 12:05:48 |
| [micropython](https://github.com/micropython/micropython) | 21621 | 8794 | 6025 | 7726 | 1892 | 2026-04-15 00:08:36 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1587 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18453 | 2797 | 3339 | 2072 | 768 | 2026-04-14 16:49:03 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16399 | 2242 | 3188 | 8858 | 275 | 2026-04-14 13:00:37 |
| [httpx](https://github.com/encode/httpx) | 15196 | 1109 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14602 | 5691 | 11413 | 13580 | 1791 | 2026-04-14 12:48:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13808 | 2096 | 2652 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1864 | 5521 | 6527 | 1243 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12206 | 1153 | 766 | 1864 | 53 | 2026-04-14 02:36:01 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11752 | 1667 | 8190 | 1055 | 214 | 2026-04-14 19:28:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11750 | 604 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 987 | 1121 | 1432 | 164 | 2026-04-12 14:11:25 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9007 | 569 | 1027 | 502 | 222 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8754 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7239 | 394 | 889 | 2531 | 318 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5547 | 474 | 1249 | 822 | 508 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5236 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4069 | 328 | 1183 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4007 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3624 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2436 | 193 | 434 | 608 | 86 | 2026-04-14 21:58:21 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 366 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1704 | 110 | 5197 | 220 | 747 | 2026-04-14 21:18:38 |
| [jython](https://github.com/jython/jython) | 1500 | 228 | 294 | 125 | 111 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-15T03:30:38*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
