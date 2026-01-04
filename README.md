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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193175 | 75151 | 41051 | 64252 | 2761 | 2026-01-04 02:27:11 |
| [transformers](https://github.com/huggingface/transformers) | 154548 | 31615 | 18389 | 24100 | 2179 | 2026-01-01 13:51:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 96308 | 26410 | 56116 | 115040 | 17904 | 2026-01-04 02:26:26 |
| [fastapi](https://github.com/fastapi/fastapi) | 93695 | 8461 | 3499 | 5068 | 204 | 2026-01-02 06:47:25 |
| [django](https://github.com/django/django) | 86355 | 33434 | 0 | 20426 | 377 | 2026-01-03 18:42:02 |
| [flask](https://github.com/pallets/flask) | 71013 | 16664 | 2707 | 2745 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70596 | 33806 | 74872 | 67552 | 9234 | 2026-01-03 23:54:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64467 | 26558 | 11868 | 19986 | 2126 | 2026-01-02 19:34:41 |
| [keras](https://github.com/keras-team/keras) | 63685 | 19666 | 12607 | 8577 | 241 | 2026-01-03 01:27:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 47470 | 19467 | 27997 | 35501 | 3610 | 2026-01-03 11:52:57 |
| [ray](https://github.com/ray-project/ray) | 40594 | 7060 | 22092 | 37386 | 3262 | 2026-01-04 02:07:03 |
| [gym](https://github.com/openai/gym) | 36926 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33026 | 4632 | 5736 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31137 | 11914 | 13725 | 16779 | 2390 | 2026-01-03 21:26:05 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29783 | 7049 | 3946 | 4897 | 84 | 2026-01-02 17:57:10 |
| [celery](https://github.com/celery/celery) | 27822 | 4925 | 5180 | 3756 | 759 | 2025-12-29 21:48:53 |
| [dash](https://github.com/plotly/dash) | 24376 | 2245 | 2039 | 1400 | 557 | 2026-01-01 21:48:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22412 | 5545 | 1862 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22179 | 8168 | 11095 | 19788 | 1538 | 2026-01-03 23:38:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 21604 | 1397 | 1271 | 5304 | 383 | 2026-01-04 02:07:58 |
| [micropython](https://github.com/micropython/micropython) | 21289 | 8623 | 5912 | 7466 | 1821 | 2026-01-04 01:23:33 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1585 | 1457 | 1661 | 107 | 2025-12-31 19:42:35 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18141 | 2767 | 3310 | 1997 | 762 | 2026-01-02 16:29:47 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16172 | 2170 | 3168 | 8448 | 266 | 2026-01-03 17:56:31 |
| [httpx](https://github.com/encode/httpx) | 14877 | 999 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14306 | 5573 | 11219 | 13031 | 1745 | 2026-01-03 19:18:42 |
| [dask](https://github.com/dask/dask) | 13685 | 1832 | 5481 | 6437 | 1207 | 2026-01-02 16:10:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13652 | 2072 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11814 | 1095 | 760 | 1757 | 53 | 2026-01-02 08:04:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11561 | 596 | 400 | 301 | 154 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11345 | 1612 | 8135 | 1017 | 207 | 2026-01-02 21:32:53 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8823 | 552 | 988 | 478 | 195 | 2026-01-01 20:11:23 |
| [bottle](https://github.com/bottlepy/bottle) | 8721 | 1491 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7088 | 377 | 877 | 2484 | 313 | 2026-01-01 00:06:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5433 | 444 | 1213 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5130 | 980 | 883 | 274 | 178 | 2026-01-02 13:34:26 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3863 | 305 | 1172 | 207 | 118 | 2026-01-02 21:34:03 |
| [quart](https://github.com/pallets/quart) | 3570 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2721 | 307 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2344 | 181 | 421 | 562 | 75 | 2025-12-31 01:53:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1621 | 94 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1465 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-04T02:32:59*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
