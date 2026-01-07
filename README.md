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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193240 | 75147 | 41055 | 64483 | 2854 | 2026-01-07 02:20:52 |
| [transformers](https://github.com/huggingface/transformers) | 154668 | 31648 | 18396 | 24139 | 2165 | 2026-01-07 02:14:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 96384 | 26433 | 56156 | 115186 | 17892 | 2026-01-07 02:21:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 93793 | 8479 | 3499 | 5078 | 212 | 2026-01-06 22:11:20 |
| [django](https://github.com/django/django) | 86393 | 33442 | 0 | 20437 | 381 | 2026-01-06 20:15:56 |
| [flask](https://github.com/pallets/flask) | 71018 | 16662 | 2708 | 2747 | 12 | 2026-01-05 16:50:56 |
| [cpython](https://github.com/python/cpython) | 70956 | 33851 | 74897 | 67620 | 9220 | 2026-01-06 23:51:12 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64511 | 26578 | 11872 | 20004 | 2117 | 2026-01-06 14:26:20 |
| [keras](https://github.com/keras-team/keras) | 63692 | 19671 | 12607 | 8586 | 240 | 2026-01-05 23:21:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47495 | 19476 | 28003 | 35532 | 3593 | 2026-01-06 22:12:54 |
| [ray](https://github.com/ray-project/ray) | 40639 | 7076 | 22113 | 37447 | 3272 | 2026-01-07 02:11:20 |
| [gym](https://github.com/openai/gym) | 36941 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33042 | 4630 | 5736 | 4076 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31169 | 11927 | 13734 | 16800 | 2399 | 2026-01-06 20:05:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29794 | 7050 | 3946 | 4897 | 82 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27836 | 4927 | 5180 | 3763 | 759 | 2026-01-06 22:10:42 |
| [dash](https://github.com/plotly/dash) | 24378 | 2246 | 2039 | 1404 | 555 | 2026-01-06 23:55:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22411 | 5545 | 1862 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22189 | 8171 | 11097 | 19793 | 1542 | 2026-01-04 06:14:22 |
| [RustPython](https://github.com/RustPython/RustPython) | 21620 | 1399 | 1276 | 5331 | 368 | 2026-01-07 01:30:11 |
| [micropython](https://github.com/micropython/micropython) | 21308 | 8630 | 5923 | 7469 | 1820 | 2026-01-07 00:28:51 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1584 | 1458 | 1662 | 108 | 2026-01-06 21:21:41 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18149 | 2769 | 3310 | 1997 | 762 | 2026-01-05 14:52:03 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16182 | 2170 | 3168 | 8456 | 268 | 2026-01-06 10:31:42 |
| [httpx](https://github.com/encode/httpx) | 14881 | 1001 | 925 | 1775 | 123 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14318 | 5576 | 11228 | 13044 | 1750 | 2026-01-06 23:22:26 |
| [dask](https://github.com/dask/dask) | 13692 | 1832 | 5481 | 6443 | 1210 | 2026-01-06 18:13:27 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13659 | 2073 | 2643 | 1154 | 200 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11821 | 1095 | 760 | 1757 | 53 | 2026-01-02 08:04:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11566 | 596 | 400 | 301 | 154 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11360 | 1616 | 8137 | 1019 | 209 | 2026-01-07 00:10:06 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8832 | 552 | 988 | 479 | 195 | 2026-01-04 16:26:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8725 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7091 | 377 | 877 | 2486 | 312 | 2026-01-05 22:28:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5620 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5438 | 444 | 1213 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5138 | 981 | 883 | 277 | 179 | 2026-01-06 10:31:06 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3873 | 305 | 1173 | 207 | 118 | 2026-01-05 19:27:08 |
| [quart](https://github.com/pallets/quart) | 3572 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2349 | 180 | 421 | 562 | 73 | 2026-01-06 11:46:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2341 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1623 | 94 | 5169 | 173 | 754 | 2026-01-06 13:46:04 |
| [jython](https://github.com/jython/jython) | 1468 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-07T02:21:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
