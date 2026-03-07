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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194018 | 75220 | 41197 | 68497 | 3666 | 2026-03-07 02:13:17 |
| [transformers](https://github.com/huggingface/transformers) | 157502 | 32312 | 18673 | 25227 | 2284 | 2026-03-06 22:28:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 98008 | 27096 | 57162 | 119096 | 18089 | 2026-03-07 02:33:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 95961 | 8795 | 3506 | 5406 | 145 | 2026-03-06 17:54:41 |
| [django](https://github.com/django/django) | 86994 | 33717 | 0 | 20781 | 424 | 2026-03-06 22:32:33 |
| [cpython](https://github.com/python/cpython) | 71868 | 34192 | 75463 | 69149 | 9295 | 2026-03-06 22:24:21 |
| [flask](https://github.com/pallets/flask) | 71331 | 16742 | 2723 | 2780 | 3 | 2026-03-04 15:36:26 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65316 | 26748 | 11982 | 20336 | 2136 | 2026-03-06 09:47:39 |
| [keras](https://github.com/keras-team/keras) | 63913 | 19714 | 12653 | 8925 | 283 | 2026-03-06 20:03:04 |
| [pandas](https://github.com/pandas-dev/pandas) | 48071 | 19720 | 28157 | 36212 | 3691 | 2026-03-07 02:29:22 |
| [ray](https://github.com/ray-project/ray) | 41620 | 7296 | 22417 | 38779 | 3436 | 2026-03-07 02:28:47 |
| [gym](https://github.com/openai/gym) | 37077 | 8707 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33285 | 4641 | 5742 | 4081 | 192 | 2026-03-03 08:56:07 |
| [numpy](https://github.com/numpy/numpy) | 31568 | 12124 | 13822 | 17071 | 2321 | 2026-03-06 14:16:54 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29926 | 7076 | 3946 | 4939 | 78 | 2026-03-04 15:27:11 |
| [celery](https://github.com/celery/celery) | 28198 | 4982 | 5201 | 3852 | 779 | 2026-03-05 15:27:55 |
| [dash](https://github.com/plotly/dash) | 24436 | 2262 | 2069 | 1456 | 572 | 2026-03-06 19:02:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22532 | 8234 | 11187 | 20016 | 1534 | 2026-03-06 21:09:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22402 | 5545 | 1863 | 1703 | 217 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21860 | 1405 | 1312 | 5992 | 372 | 2026-03-07 00:55:47 |
| [micropython](https://github.com/micropython/micropython) | 21514 | 8727 | 5971 | 7603 | 1846 | 2026-03-04 13:08:15 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18311 | 2781 | 3326 | 2053 | 777 | 2026-03-06 19:04:59 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16377 | 2209 | 3181 | 8711 | 273 | 2026-03-06 11:41:11 |
| [httpx](https://github.com/encode/httpx) | 15140 | 1055 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14508 | 5642 | 11350 | 13389 | 1780 | 2026-03-06 20:52:58 |
| [dask](https://github.com/dask/dask) | 13757 | 1850 | 5509 | 6503 | 1225 | 2026-03-05 10:51:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13757 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12003 | 1131 | 763 | 1822 | 46 | 2026-03-05 12:56:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11678 | 600 | 405 | 314 | 153 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11671 | 1650 | 8164 | 1041 | 212 | 2026-03-06 21:58:36 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 980 | 1119 | 1417 | 163 | 2026-03-06 07:42:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8933 | 560 | 1019 | 492 | 219 | 2026-03-06 14:12:06 |
| [bottle](https://github.com/bottlepy/bottle) | 8761 | 1499 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7190 | 387 | 880 | 2511 | 319 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5514 | 465 | 1236 | 792 | 489 | 2026-03-05 07:19:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5203 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4076 | 895 | 1063 | 2731 | 81 | 2026-03-05 21:21:24 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3992 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3606 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2733 | 311 | 660 | 1285 | 308 | 2026-03-06 21:26:00 |
| [anyio](https://github.com/agronholm/anyio) | 2405 | 184 | 429 | 580 | 83 | 2026-03-04 20:45:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1464 | 367 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-03-02 18:13:20 |
| [pypy](https://github.com/pypy/pypy) | 1665 | 100 | 5177 | 182 | 758 | 2026-03-06 11:02:10 |
| [jython](https://github.com/jython/jython) | 1489 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-07T02:36:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
