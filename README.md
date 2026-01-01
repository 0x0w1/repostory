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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193133 | 75153 | 41051 | 64124 | 2668 | 2025-12-31 20:25:50 |
| [transformers](https://github.com/huggingface/transformers) | 154473 | 31591 | 18383 | 24089 | 2167 | 2025-12-24 15:30:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 96258 | 26402 | 56103 | 114989 | 17922 | 2026-01-01 02:22:04 |
| [fastapi](https://github.com/fastapi/fastapi) | 93599 | 8451 | 3499 | 5059 | 198 | 2025-12-29 18:54:44 |
| [django](https://github.com/django/django) | 86321 | 33424 | 0 | 20417 | 372 | 2025-12-31 15:48:14 |
| [flask](https://github.com/pallets/flask) | 70996 | 16667 | 2707 | 2742 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70541 | 33783 | 74849 | 67489 | 9242 | 2025-12-31 20:51:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64431 | 26546 | 11865 | 19972 | 2121 | 2025-12-31 15:19:54 |
| [keras](https://github.com/keras-team/keras) | 63677 | 19662 | 12607 | 8567 | 240 | 2025-12-30 00:48:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 47455 | 19461 | 27991 | 35472 | 3596 | 2025-12-31 19:15:09 |
| [ray](https://github.com/ray-project/ray) | 40562 | 7059 | 22087 | 37355 | 3268 | 2026-01-01 00:07:35 |
| [gym](https://github.com/openai/gym) | 36917 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33016 | 4632 | 5736 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31122 | 11901 | 13723 | 16768 | 2387 | 2025-12-31 18:08:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29774 | 7048 | 3946 | 4895 | 83 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27805 | 4926 | 5180 | 3755 | 760 | 2025-12-29 21:48:53 |
| [dash](https://github.com/plotly/dash) | 24375 | 2245 | 2039 | 1398 | 556 | 2025-12-31 13:46:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22408 | 5545 | 1862 | 1690 | 210 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22171 | 8162 | 11095 | 19778 | 1545 | 2025-12-30 18:46:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21580 | 1394 | 1271 | 5283 | 393 | 2025-12-31 23:58:59 |
| [micropython](https://github.com/micropython/micropython) | 21266 | 8615 | 5911 | 7462 | 1822 | 2025-12-30 13:40:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18611 | 1585 | 1457 | 1661 | 107 | 2025-12-31 19:42:35 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18131 | 2768 | 3309 | 1996 | 760 | 2025-12-31 20:57:58 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16166 | 2170 | 3168 | 8407 | 267 | 2025-12-30 10:34:11 |
| [httpx](https://github.com/encode/httpx) | 14876 | 999 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14300 | 5569 | 11219 | 13024 | 1760 | 2025-12-31 17:12:51 |
| [dask](https://github.com/dask/dask) | 13679 | 1831 | 5481 | 6432 | 1206 | 2025-12-31 17:00:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13649 | 2071 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11806 | 1094 | 760 | 1754 | 52 | 2025-12-31 08:43:47 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11553 | 594 | 399 | 299 | 151 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11332 | 1611 | 8134 | 1017 | 210 | 2025-12-31 16:22:43 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8820 | 551 | 987 | 475 | 192 | 2025-12-26 14:55:26 |
| [bottle](https://github.com/bottlepy/bottle) | 8719 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7086 | 376 | 877 | 2484 | 313 | 2026-01-01 00:06:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5428 | 444 | 1213 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5130 | 980 | 882 | 273 | 177 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4019 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3858 | 305 | 1172 | 207 | 119 | 2025-12-26 20:05:52 |
| [quart](https://github.com/pallets/quart) | 3568 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2721 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2342 | 181 | 421 | 562 | 75 | 2025-12-31 01:53:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1928 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1618 | 93 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1464 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-01T02:31:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
