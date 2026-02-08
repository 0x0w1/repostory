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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193653 | 75213 | 41150 | 66668 | 3320 | 2026-02-07 20:03:28 |
| [transformers](https://github.com/huggingface/transformers) | 156202 | 31992 | 18540 | 24684 | 2226 | 2026-02-07 22:13:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 97233 | 26783 | 56723 | 117304 | 17999 | 2026-02-08 03:25:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 94885 | 8653 | 3502 | 5256 | 175 | 2026-02-07 23:37:32 |
| [django](https://github.com/django/django) | 86705 | 33632 | 0 | 20585 | 402 | 2026-02-06 21:19:49 |
| [cpython](https://github.com/python/cpython) | 71404 | 34036 | 75194 | 68375 | 9200 | 2026-02-07 23:14:18 |
| [flask](https://github.com/pallets/flask) | 71141 | 16697 | 2713 | 2764 | 2 | 2026-02-06 21:23:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64940 | 26670 | 11928 | 20167 | 2129 | 2026-02-06 14:50:17 |
| [keras](https://github.com/keras-team/keras) | 63757 | 19687 | 12625 | 8705 | 257 | 2026-02-07 01:14:31 |
| [pandas](https://github.com/pandas-dev/pandas) | 47827 | 19625 | 28086 | 35920 | 3645 | 2026-02-06 21:29:52 |
| [ray](https://github.com/ray-project/ray) | 41175 | 7194 | 22286 | 38205 | 3357 | 2026-02-08 03:17:02 |
| [gym](https://github.com/openai/gym) | 37021 | 8711 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33173 | 4638 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31399 | 12029 | 13782 | 16954 | 2304 | 2026-02-05 19:16:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29861 | 7064 | 3946 | 4919 | 89 | 2026-02-07 13:26:13 |
| [celery](https://github.com/celery/celery) | 27980 | 4940 | 5189 | 3789 | 766 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24460 | 2254 | 2053 | 1430 | 558 | 2026-02-07 17:40:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22441 | 5544 | 1863 | 1699 | 214 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22316 | 8181 | 11137 | 19934 | 1528 | 2026-02-07 01:33:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 21765 | 1401 | 1295 | 5681 | 371 | 2026-02-08 01:00:50 |
| [micropython](https://github.com/micropython/micropython) | 21444 | 8699 | 5950 | 7545 | 1840 | 2026-02-07 08:00:48 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1584 | 1465 | 1664 | 116 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18241 | 2777 | 3320 | 2024 | 773 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16254 | 2188 | 3176 | 8554 | 280 | 2026-02-07 20:26:55 |
| [httpx](https://github.com/encode/httpx) | 14973 | 1030 | 925 | 1787 | 133 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14434 | 5610 | 11292 | 13230 | 1760 | 2026-02-07 22:26:13 |
| [dask](https://github.com/dask/dask) | 13733 | 1842 | 5504 | 6485 | 1226 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13708 | 2079 | 2645 | 1160 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11901 | 1109 | 763 | 1784 | 53 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11636 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11475 | 1634 | 8151 | 1028 | 208 | 2026-02-06 15:06:53 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 979 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8888 | 556 | 1005 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8743 | 1492 | 860 | 627 | 282 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7157 | 382 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5476 | 454 | 1223 | 752 | 502 | 2026-02-07 23:01:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5181 | 999 | 900 | 289 | 190 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3942 | 310 | 1181 | 208 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3591 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 657 | 1270 | 312 | 2026-02-08 01:14:02 |
| [anyio](https://github.com/agronholm/anyio) | 2380 | 179 | 423 | 566 | 75 | 2026-02-04 20:13:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1933 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1647 | 97 | 5175 | 179 | 758 | 2026-02-06 10:46:06 |
| [jython](https://github.com/jython/jython) | 1478 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-08T03:26:48*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
