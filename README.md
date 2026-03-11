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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194148 | 75220 | 41205 | 68750 | 3656 | 2026-03-11 02:41:22 |
| [transformers](https://github.com/huggingface/transformers) | 157715 | 32360 | 18691 | 25285 | 2266 | 2026-03-10 22:53:08 |
| [pytorch](https://github.com/pytorch/pytorch) | 98186 | 27138 | 57242 | 119348 | 18142 | 2026-03-11 02:39:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 96135 | 8814 | 3507 | 5415 | 150 | 2026-03-10 12:50:47 |
| [django](https://github.com/django/django) | 87084 | 33730 | 0 | 20817 | 433 | 2026-03-10 15:32:39 |
| [cpython](https://github.com/python/cpython) | 71984 | 34209 | 75509 | 69275 | 9292 | 2026-03-11 00:50:36 |
| [flask](https://github.com/pallets/flask) | 71403 | 16741 | 2723 | 2781 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65397 | 26756 | 11985 | 20370 | 2142 | 2026-03-10 17:10:10 |
| [keras](https://github.com/keras-team/keras) | 63975 | 19714 | 12659 | 8938 | 271 | 2026-03-11 02:36:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 48104 | 19721 | 28163 | 36284 | 3676 | 2026-03-10 18:23:32 |
| [ray](https://github.com/ray-project/ray) | 41739 | 7308 | 22434 | 38856 | 3441 | 2026-03-11 02:06:28 |
| [gym](https://github.com/openai/gym) | 37081 | 8707 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33292 | 4644 | 5742 | 4083 | 194 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31582 | 12148 | 13825 | 17099 | 2327 | 2026-03-10 17:03:41 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29934 | 7080 | 3946 | 4942 | 79 | 2026-03-10 09:58:39 |
| [celery](https://github.com/celery/celery) | 28262 | 4988 | 5202 | 3858 | 771 | 2026-03-10 15:04:28 |
| [dash](https://github.com/plotly/dash) | 24453 | 2262 | 2069 | 1456 | 572 | 2026-03-06 19:02:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22550 | 8252 | 11194 | 20032 | 1539 | 2026-03-11 00:40:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22406 | 5545 | 1864 | 1710 | 218 | 2026-03-11 01:59:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 21871 | 1404 | 1314 | 6014 | 360 | 2026-03-10 06:39:55 |
| [micropython](https://github.com/micropython/micropython) | 21526 | 8736 | 5972 | 7610 | 1843 | 2026-03-11 00:31:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18320 | 2781 | 3327 | 2054 | 776 | 2026-03-10 22:29:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16439 | 2210 | 3181 | 8735 | 276 | 2026-03-10 22:14:05 |
| [httpx](https://github.com/encode/httpx) | 15205 | 1059 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14517 | 5649 | 11359 | 13409 | 1790 | 2026-03-10 21:24:19 |
| [dask](https://github.com/dask/dask) | 13764 | 1853 | 5513 | 6504 | 1228 | 2026-03-05 10:51:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13763 | 2079 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12016 | 1131 | 764 | 1824 | 47 | 2026-03-07 11:57:25 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11727 | 1650 | 8164 | 1043 | 213 | 2026-03-09 22:58:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11681 | 601 | 406 | 314 | 153 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1418 | 163 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8937 | 562 | 1020 | 492 | 218 | 2026-03-06 14:12:06 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7196 | 391 | 880 | 2512 | 319 | 2026-03-10 00:05:15 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5513 | 465 | 1238 | 795 | 493 | 2026-03-08 17:01:54 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5204 | 1000 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1063 | 2731 | 80 | 2026-03-11 01:36:54 |
| [databases](https://github.com/encode/databases) | 4019 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4003 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3605 | 193 | 280 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 311 | 660 | 1286 | 308 | 2026-03-09 23:12:29 |
| [anyio](https://github.com/agronholm/anyio) | 2406 | 184 | 429 | 581 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1080 | 1464 | 368 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1678 | 103 | 5178 | 184 | 759 | 2026-03-11 02:40:33 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-11T02:41:57*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
