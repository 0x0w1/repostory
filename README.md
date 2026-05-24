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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195256 | 75327 | 41462 | 74362 | 5568 | 2026-05-24 04:15:06 |
| [transformers](https://github.com/huggingface/transformers) | 160911 | 33302 | 18986 | 26482 | 2389 | 2026-05-22 19:58:10 |
| [pytorch](https://github.com/pytorch/pytorch) | 100144 | 27858 | 58878 | 125568 | 18537 | 2026-05-24 04:16:50 |
| [fastapi](https://github.com/fastapi/fastapi) | 98468 | 9340 | 3528 | 5788 | 134 | 2026-05-23 18:52:32 |
| [django](https://github.com/django/django) | 87566 | 33943 | 0 | 21281 | 446 | 2026-05-22 22:41:09 |
| [cpython](https://github.com/python/cpython) | 72873 | 34680 | 76465 | 71542 | 9324 | 2026-05-23 19:27:28 |
| [flask](https://github.com/pallets/flask) | 71571 | 16856 | 2739 | 2828 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66169 | 27038 | 12106 | 20820 | 2028 | 2026-05-23 01:35:43 |
| [keras](https://github.com/keras-team/keras) | 64087 | 19774 | 12764 | 9356 | 192 | 2026-05-22 21:17:15 |
| [pandas](https://github.com/pandas-dev/pandas) | 48833 | 19974 | 28291 | 37334 | 3271 | 2026-05-23 17:26:56 |
| [ray](https://github.com/ray-project/ray) | 42644 | 7604 | 22694 | 40532 | 3440 | 2026-05-24 03:44:19 |
| [gym](https://github.com/openai/gym) | 37212 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33607 | 4685 | 5756 | 4093 | 206 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32085 | 12378 | 13926 | 17487 | 2379 | 2026-05-22 16:16:32 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30028 | 7068 | 3967 | 5006 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28522 | 5048 | 5280 | 4118 | 782 | 2026-05-20 12:26:36 |
| [dash](https://github.com/plotly/dash) | 24211 | 2284 | 2102 | 1568 | 556 | 2026-05-22 07:08:24 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22829 | 8340 | 11281 | 20399 | 1481 | 2026-05-23 07:11:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5541 | 1872 | 1735 | 220 | 2026-05-21 18:10:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 22071 | 1440 | 1347 | 6543 | 387 | 2026-05-23 12:20:58 |
| [micropython](https://github.com/micropython/micropython) | 21731 | 8840 | 6057 | 7825 | 1757 | 2026-05-21 09:25:59 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1591 | 1466 | 1686 | 136 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18548 | 2808 | 3345 | 2088 | 759 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2274 | 3205 | 9149 | 242 | 2026-05-22 13:00:52 |
| [httpx](https://github.com/encode/httpx) | 15288 | 1146 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14717 | 5732 | 11448 | 13731 | 1792 | 2026-05-23 06:28:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13887 | 2115 | 2653 | 1181 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13845 | 1874 | 5529 | 6579 | 1244 | 2026-05-22 23:37:08 |
| [starlette](https://github.com/Kludex/starlette) | 12328 | 1178 | 768 | 1911 | 62 | 2026-05-23 16:54:32 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11873 | 1687 | 8216 | 1092 | 216 | 2026-05-23 01:32:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11792 | 607 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 999 | 1125 | 1449 | 158 | 2026-05-21 04:48:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9068 | 580 | 1035 | 512 | 209 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8766 | 1500 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7271 | 395 | 892 | 2545 | 320 | 2026-05-22 23:22:51 |
| [hug](https://github.com/hugapi/hug) | 6890 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5570 | 483 | 1256 | 838 | 510 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5263 | 1016 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4150 | 333 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4085 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 197 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2746 | 311 | 663 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2470 | 208 | 439 | 639 | 86 | 2026-05-23 20:34:19 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 428 | 399 | 29 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1519 | 364 | 2026-05-21 15:39:48 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 267 | 2026-05-18 17:55:16 |
| [pypy](https://github.com/pypy/pypy) | 1740 | 113 | 5213 | 250 | 740 | 2026-05-21 13:16:48 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 131 | 109 | 2026-05-23 16:06:46 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-18 17:13:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-24T04:19:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
