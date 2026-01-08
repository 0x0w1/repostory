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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193270 | 75145 | 41062 | 64563 | 2821 | 2026-01-08 02:17:26 |
| [transformers](https://github.com/huggingface/transformers) | 154706 | 31655 | 18399 | 24158 | 2173 | 2026-01-08 00:41:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 96419 | 26451 | 56179 | 115271 | 17892 | 2026-01-08 02:21:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 93840 | 8484 | 3501 | 5079 | 214 | 2026-01-07 22:23:35 |
| [django](https://github.com/django/django) | 86402 | 33444 | 0 | 20444 | 385 | 2026-01-07 21:56:03 |
| [flask](https://github.com/pallets/flask) | 71019 | 16663 | 2710 | 2747 | 12 | 2026-01-05 16:50:56 |
| [cpython](https://github.com/python/cpython) | 70982 | 33853 | 74906 | 67640 | 9214 | 2026-01-07 22:56:14 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64548 | 26585 | 11874 | 20010 | 2114 | 2026-01-07 16:23:05 |
| [keras](https://github.com/keras-team/keras) | 63694 | 19671 | 12608 | 8589 | 243 | 2026-01-05 23:21:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47506 | 19478 | 28005 | 35537 | 3594 | 2026-01-07 17:31:20 |
| [ray](https://github.com/ray-project/ray) | 40658 | 7082 | 22122 | 37484 | 3267 | 2026-01-08 02:12:32 |
| [gym](https://github.com/openai/gym) | 36943 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33048 | 4630 | 5736 | 4076 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31173 | 11926 | 13736 | 16807 | 2390 | 2026-01-08 00:23:38 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29797 | 7049 | 3946 | 4897 | 82 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27844 | 4926 | 5181 | 3764 | 761 | 2026-01-06 22:10:42 |
| [dash](https://github.com/plotly/dash) | 24383 | 2246 | 2039 | 1406 | 557 | 2026-01-07 22:52:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22412 | 5545 | 1862 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22194 | 8169 | 11098 | 19798 | 1543 | 2026-01-07 16:08:36 |
| [RustPython](https://github.com/RustPython/RustPython) | 21629 | 1399 | 1276 | 5332 | 367 | 2026-01-07 03:53:44 |
| [micropython](https://github.com/micropython/micropython) | 21313 | 8634 | 5929 | 7470 | 1825 | 2026-01-07 00:28:51 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1584 | 1459 | 1662 | 109 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18153 | 2770 | 3310 | 1997 | 761 | 2026-01-07 16:23:38 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16186 | 2170 | 3169 | 8460 | 269 | 2026-01-07 22:22:07 |
| [httpx](https://github.com/encode/httpx) | 14885 | 1003 | 925 | 1776 | 124 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14321 | 5579 | 11230 | 13049 | 1748 | 2026-01-07 18:13:45 |
| [dask](https://github.com/dask/dask) | 13695 | 1833 | 5482 | 6444 | 1208 | 2026-01-07 21:22:12 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13659 | 2075 | 2643 | 1154 | 200 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11826 | 1096 | 761 | 1758 | 54 | 2026-01-02 08:04:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11566 | 597 | 400 | 302 | 155 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11360 | 1617 | 8137 | 1019 | 208 | 2026-01-07 12:53:03 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8834 | 552 | 988 | 479 | 194 | 2026-01-04 16:26:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8725 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7093 | 378 | 877 | 2486 | 312 | 2026-01-05 22:28:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5620 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5442 | 444 | 1215 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5140 | 981 | 884 | 278 | 180 | 2026-01-07 13:28:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4023 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3876 | 305 | 1173 | 207 | 118 | 2026-01-05 19:27:08 |
| [quart](https://github.com/pallets/quart) | 3572 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2355 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2349 | 180 | 421 | 562 | 73 | 2026-01-06 11:46:43 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1623 | 94 | 5169 | 173 | 754 | 2026-01-06 13:46:04 |
| [jython](https://github.com/jython/jython) | 1468 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-08T02:22:04*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
