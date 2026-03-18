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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194175 | 75260 | 41238 | 69235 | 3767 | 2026-03-18 02:53:29 |
| [transformers](https://github.com/huggingface/transformers) | 157975 | 32519 | 18727 | 25467 | 2329 | 2026-03-18 00:10:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 98335 | 27236 | 57354 | 119840 | 18078 | 2026-03-18 02:53:12 |
| [fastapi](https://github.com/fastapi/fastapi) | 96289 | 8875 | 3512 | 5450 | 165 | 2026-03-17 20:22:08 |
| [django](https://github.com/django/django) | 87063 | 33759 | 0 | 20865 | 432 | 2026-03-17 21:08:18 |
| [cpython](https://github.com/python/cpython) | 71997 | 34248 | 75613 | 69476 | 9321 | 2026-03-17 20:59:26 |
| [flask](https://github.com/pallets/flask) | 71344 | 16748 | 2724 | 2787 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65404 | 26806 | 12000 | 20412 | 2140 | 2026-03-17 17:04:44 |
| [keras](https://github.com/keras-team/keras) | 63907 | 19740 | 12673 | 8972 | 273 | 2026-03-13 23:34:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 48165 | 19754 | 28182 | 36428 | 3670 | 2026-03-18 01:52:48 |
| [ray](https://github.com/ray-project/ray) | 41762 | 7355 | 22462 | 39007 | 3480 | 2026-03-18 02:16:14 |
| [gym](https://github.com/openai/gym) | 37098 | 8706 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33347 | 4661 | 5745 | 4083 | 195 | 2026-03-15 10:29:09 |
| [numpy](https://github.com/numpy/numpy) | 31615 | 12173 | 13835 | 17127 | 2339 | 2026-03-16 10:02:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29929 | 7077 | 3946 | 4945 | 78 | 2026-03-17 21:09:33 |
| [celery](https://github.com/celery/celery) | 28227 | 4993 | 5208 | 3867 | 767 | 2026-03-15 10:51:04 |
| [dash](https://github.com/plotly/dash) | 24467 | 2266 | 2074 | 1475 | 583 | 2026-03-16 17:39:59 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22589 | 8264 | 11203 | 20071 | 1547 | 2026-03-17 23:41:30 |
| [tornado](https://github.com/tornadoweb/tornado) | 22406 | 5545 | 1864 | 1714 | 215 | 2026-03-17 19:24:12 |
| [RustPython](https://github.com/RustPython/RustPython) | 21889 | 1408 | 1317 | 6073 | 370 | 2026-03-17 14:35:44 |
| [micropython](https://github.com/micropython/micropython) | 21554 | 8748 | 5978 | 7630 | 1851 | 2026-03-17 05:16:38 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18356 | 2787 | 3330 | 2057 | 777 | 2026-03-18 00:29:18 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16365 | 2212 | 3182 | 8754 | 272 | 2026-03-18 02:06:15 |
| [httpx](https://github.com/encode/httpx) | 15139 | 1074 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14540 | 5660 | 11377 | 13461 | 1791 | 2026-03-17 23:42:34 |
| [dask](https://github.com/dask/dask) | 13769 | 1858 | 5517 | 6508 | 1230 | 2026-03-16 22:03:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13769 | 2084 | 2648 | 1164 | 209 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12030 | 1135 | 764 | 1832 | 44 | 2026-03-16 05:35:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11687 | 602 | 408 | 317 | 158 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11661 | 1652 | 8168 | 1046 | 215 | 2026-03-17 15:35:43 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 980 | 1119 | 1420 | 163 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8951 | 565 | 1023 | 495 | 223 | 2026-03-13 12:05:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8765 | 1503 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7204 | 392 | 882 | 2514 | 318 | 2026-03-16 22:58:38 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5607 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5523 | 466 | 1241 | 801 | 492 | 2026-03-15 21:25:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5208 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4017 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4015 | 322 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3609 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2735 | 312 | 662 | 1301 | 309 | 2026-03-17 23:59:07 |
| [anyio](https://github.com/agronholm/anyio) | 2411 | 188 | 429 | 587 | 84 | 2026-03-16 20:33:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-16 17:53:47 |
| [pypy](https://github.com/pypy/pypy) | 1682 | 103 | 5180 | 185 | 758 | 2026-03-16 11:57:50 |
| [jython](https://github.com/jython/jython) | 1490 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-18T02:54:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
