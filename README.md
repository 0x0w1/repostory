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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193208 | 75150 | 41054 | 64355 | 2804 | 2026-01-06 02:19:04 |
| [transformers](https://github.com/huggingface/transformers) | 154623 | 31635 | 18395 | 24124 | 2167 | 2026-01-06 00:37:09 |
| [pytorch](https://github.com/pytorch/pytorch) | 96355 | 26421 | 56142 | 115119 | 17933 | 2026-01-06 02:21:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 93752 | 8474 | 3499 | 5073 | 207 | 2026-01-02 06:47:25 |
| [django](https://github.com/django/django) | 86370 | 33436 | 0 | 20433 | 380 | 2026-01-05 20:49:06 |
| [flask](https://github.com/pallets/flask) | 71013 | 16664 | 2708 | 2747 | 12 | 2026-01-05 16:50:56 |
| [cpython](https://github.com/python/cpython) | 70881 | 33833 | 74892 | 67582 | 9237 | 2026-01-06 01:25:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64488 | 26569 | 11872 | 19997 | 2118 | 2026-01-06 01:48:52 |
| [keras](https://github.com/keras-team/keras) | 63687 | 19670 | 12607 | 8584 | 238 | 2026-01-05 23:21:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47484 | 19472 | 28001 | 35515 | 3591 | 2026-01-06 01:17:43 |
| [ray](https://github.com/ray-project/ray) | 40622 | 7069 | 22100 | 37416 | 3262 | 2026-01-06 02:03:09 |
| [gym](https://github.com/openai/gym) | 36937 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33039 | 4633 | 5736 | 4076 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31159 | 11923 | 13728 | 16791 | 2393 | 2026-01-06 00:03:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29794 | 7049 | 3946 | 4897 | 82 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27828 | 4927 | 5180 | 3761 | 758 | 2026-01-05 22:46:44 |
| [dash](https://github.com/plotly/dash) | 24376 | 2245 | 2039 | 1400 | 557 | 2026-01-01 21:48:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22413 | 5545 | 1862 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22186 | 8170 | 11097 | 19792 | 1541 | 2026-01-04 06:14:22 |
| [RustPython](https://github.com/RustPython/RustPython) | 21612 | 1398 | 1274 | 5322 | 372 | 2026-01-06 02:17:33 |
| [micropython](https://github.com/micropython/micropython) | 21303 | 8626 | 5920 | 7467 | 1819 | 2026-01-05 19:06:20 |
| [sanic](https://github.com/sanic-org/sanic) | 18608 | 1585 | 1457 | 1661 | 107 | 2025-12-31 19:42:35 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18145 | 2767 | 3310 | 1997 | 762 | 2026-01-05 14:52:03 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16181 | 2170 | 3168 | 8454 | 267 | 2026-01-05 10:50:23 |
| [httpx](https://github.com/encode/httpx) | 14878 | 999 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14314 | 5574 | 11225 | 13040 | 1750 | 2026-01-05 18:27:35 |
| [dask](https://github.com/dask/dask) | 13690 | 1832 | 5481 | 6439 | 1208 | 2026-01-02 16:10:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13656 | 2072 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11817 | 1095 | 760 | 1757 | 53 | 2026-01-02 08:04:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11564 | 596 | 400 | 301 | 154 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11358 | 1614 | 8136 | 1018 | 209 | 2026-01-02 21:32:53 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8827 | 552 | 988 | 479 | 195 | 2026-01-04 16:26:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8724 | 1491 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7090 | 377 | 877 | 2486 | 312 | 2026-01-05 22:28:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5437 | 445 | 1213 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5134 | 981 | 883 | 275 | 179 | 2026-01-02 13:34:26 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3868 | 305 | 1173 | 207 | 118 | 2026-01-05 19:27:08 |
| [quart](https://github.com/pallets/quart) | 3572 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2722 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2347 | 181 | 421 | 562 | 75 | 2025-12-31 01:53:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1623 | 94 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1468 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-06T02:21:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
