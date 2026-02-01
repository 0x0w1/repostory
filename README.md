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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193572 | 75209 | 41132 | 66044 | 3012 | 2026-02-01 03:18:31 |
| [transformers](https://github.com/huggingface/transformers) | 155998 | 31920 | 18502 | 24559 | 2213 | 2026-01-31 22:25:07 |
| [pytorch](https://github.com/pytorch/pytorch) | 97086 | 26704 | 56609 | 116883 | 17990 | 2026-02-01 02:23:02 |
| [fastapi](https://github.com/fastapi/fastapi) | 94675 | 8613 | 3501 | 5189 | 220 | 2026-01-31 19:23:04 |
| [django](https://github.com/django/django) | 86635 | 33577 | 0 | 20557 | 398 | 2026-01-31 16:48:59 |
| [cpython](https://github.com/python/cpython) | 71296 | 33994 | 75146 | 68213 | 9222 | 2026-01-31 04:37:52 |
| [flask](https://github.com/pallets/flask) | 71124 | 16684 | 2713 | 2762 | 2 | 2026-01-28 15:43:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64851 | 26649 | 11907 | 20113 | 2113 | 2026-01-30 09:11:43 |
| [keras](https://github.com/keras-team/keras) | 63754 | 19681 | 12624 | 8673 | 252 | 2026-02-01 02:13:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 47754 | 19595 | 28065 | 35840 | 3628 | 2026-01-31 21:29:01 |
| [ray](https://github.com/ray-project/ray) | 41066 | 7172 | 22259 | 38029 | 3327 | 2026-01-31 19:42:17 |
| [gym](https://github.com/openai/gym) | 36999 | 8711 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33147 | 4636 | 5738 | 4077 | 185 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31364 | 12010 | 13768 | 16926 | 2293 | 2026-01-31 23:31:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29848 | 7062 | 3946 | 4911 | 89 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27942 | 4934 | 5185 | 3778 | 761 | 2026-01-29 12:37:15 |
| [dash](https://github.com/plotly/dash) | 24429 | 2252 | 2051 | 1424 | 560 | 2026-01-27 22:05:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22436 | 5543 | 1863 | 1697 | 212 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22299 | 8175 | 11117 | 19887 | 1529 | 2026-01-30 00:47:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 21740 | 1400 | 1295 | 5567 | 374 | 2026-02-01 03:13:05 |
| [micropython](https://github.com/micropython/micropython) | 21407 | 8687 | 5946 | 7527 | 1844 | 2026-01-31 11:46:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1583 | 1464 | 1663 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18227 | 2776 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16239 | 2184 | 3175 | 8531 | 277 | 2026-01-30 16:29:02 |
| [httpx](https://github.com/encode/httpx) | 14958 | 1026 | 925 | 1782 | 129 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14414 | 5606 | 11277 | 13184 | 1749 | 2026-02-01 00:48:28 |
| [dask](https://github.com/dask/dask) | 13726 | 1838 | 5499 | 6460 | 1217 | 2026-01-30 20:59:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13698 | 2080 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11885 | 1100 | 763 | 1776 | 48 | 2026-01-27 08:14:03 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11622 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11451 | 1634 | 8146 | 1027 | 206 | 2026-01-30 19:09:56 |
| [falcon](https://github.com/falconry/falcon) | 9785 | 977 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8877 | 556 | 1000 | 482 | 200 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8736 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7127 | 380 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5615 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5469 | 452 | 1221 | 742 | 507 | 2026-01-31 08:15:18 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5172 | 998 | 896 | 285 | 188 | 2026-01-27 13:50:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3928 | 308 | 1180 | 207 | 114 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3585 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 657 | 1263 | 314 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2372 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1644 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1477 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-01T03:21:18*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
