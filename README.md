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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194834 | 75278 | 41320 | 71827 | 4677 | 2026-04-23 03:35:14 |
| [transformers](https://github.com/huggingface/transformers) | 159772 | 32980 | 18889 | 26052 | 2345 | 2026-04-23 01:50:52 |
| [pytorch](https://github.com/pytorch/pytorch) | 99359 | 27568 | 58182 | 122504 | 18519 | 2026-04-23 03:34:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 97537 | 9132 | 3518 | 5646 | 169 | 2026-04-22 13:11:12 |
| [django](https://github.com/django/django) | 87311 | 33824 | 0 | 21088 | 432 | 2026-04-23 02:22:55 |
| [cpython](https://github.com/python/cpython) | 72417 | 34470 | 76070 | 70536 | 9414 | 2026-04-23 03:06:56 |
| [flask](https://github.com/pallets/flask) | 71436 | 16805 | 2735 | 2810 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65890 | 26970 | 12047 | 20623 | 2066 | 2026-04-22 22:44:06 |
| [keras](https://github.com/keras-team/keras) | 64026 | 19761 | 12739 | 9215 | 292 | 2026-04-23 01:16:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 48551 | 19873 | 28253 | 37007 | 3404 | 2026-04-22 16:28:22 |
| [ray](https://github.com/ray-project/ray) | 42263 | 7485 | 22602 | 39909 | 3581 | 2026-04-23 01:48:04 |
| [gym](https://github.com/openai/gym) | 37173 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33501 | 4676 | 5754 | 4091 | 202 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31873 | 12309 | 13890 | 17350 | 2369 | 2026-04-23 01:12:09 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29984 | 7067 | 3968 | 5001 | 79 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28400 | 5016 | 5270 | 4086 | 781 | 2026-04-22 22:14:02 |
| [dash](https://github.com/plotly/dash) | 24137 | 2277 | 2091 | 1542 | 544 | 2026-04-22 22:05:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22730 | 8325 | 11247 | 20249 | 1495 | 2026-04-23 03:08:28 |
| [tornado](https://github.com/tornadoweb/tornado) | 22221 | 5542 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22027 | 1428 | 1335 | 6252 | 377 | 2026-04-23 02:11:03 |
| [micropython](https://github.com/micropython/micropython) | 21644 | 8803 | 6035 | 7745 | 1876 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18470 | 2803 | 3338 | 2078 | 762 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16411 | 2256 | 3191 | 8896 | 281 | 2026-04-22 14:51:37 |
| [httpx](https://github.com/encode/httpx) | 15217 | 1120 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14627 | 5708 | 11421 | 13621 | 1786 | 2026-04-22 07:06:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13826 | 2103 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13805 | 1867 | 5521 | 6531 | 1246 | 2026-04-22 10:20:36 |
| [starlette](https://github.com/Kludex/starlette) | 12225 | 1158 | 766 | 1877 | 57 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11785 | 1673 | 8198 | 1062 | 218 | 2026-04-22 13:01:43 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11763 | 605 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 988 | 1121 | 1433 | 155 | 2026-04-20 21:43:28 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9023 | 569 | 1031 | 505 | 201 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8753 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7246 | 392 | 890 | 2536 | 320 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6894 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 733 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5556 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5242 | 1007 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4083 | 330 | 1183 | 218 | 116 | 2026-04-20 21:11:28 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3625 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2737 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2442 | 198 | 434 | 613 | 84 | 2026-04-21 12:21:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 904 | 1082 | 1471 | 366 | 2026-04-22 18:18:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1712 | 111 | 5200 | 226 | 747 | 2026-04-22 19:01:39 |
| [jython](https://github.com/jython/jython) | 1500 | 228 | 294 | 126 | 111 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-23T03:35:57*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
