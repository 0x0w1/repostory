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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201137 | 79760 | 41905 | 83781 | 3437 | 2026-10-19 04:21:02 |
| [transformers](https://github.com/huggingface/transformers) | 167831 | 34902 | 19652 | 29277 | 2330 | 2026-10-19 04:18:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 104872 | 32809 | 61829 | 138877 | 17663 | 2026-10-19 04:21:18 |
| [fastapi](https://github.com/fastapi/fastapi) | 103229 | 10055 | 3556 | 6453 | 78 | 2026-10-18 22:49:57 |
| [django](https://github.com/django/django) | 91470 | 37553 | 0 | 22086 | 539 | 2026-10-15 06:51:05 |
| [cpython](https://github.com/python/cpython) | 77714 | 38671 | 78762 | 78544 | 9847 | 2026-10-18 16:25:24 |
| [flask](https://github.com/pallets/flask) | 74956 | 17099 | 2768 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67789 | 27544 | 12334 | 21633 | 2158 | 2026-10-18 16:03:44 |
| [keras](https://github.com/keras-team/keras) | 64372 | 19798 | 13019 | 10100 | 233 | 2026-10-19 01:43:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 50186 | 20547 | 28630 | 39515 | 2127 | 2026-10-18 23:51:45 |
| [ray](https://github.com/ray-project/ray) | 44063 | 8174 | 23204 | 43511 | 3607 | 2026-10-18 15:45:43 |
| [gym](https://github.com/openai/gym) | 37240 | 8666 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33971 | 4736 | 5776 | 4131 | 252 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33047 | 12937 | 14140 | 18848 | 2238 | 2026-10-18 22:56:33 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30210 | 7092 | 3966 | 5092 | 57 | 2026-10-14 22:32:27 |
| [celery](https://github.com/celery/celery) | 29007 | 5227 | 5339 | 4589 | 726 | 2026-10-18 08:52:37 |
| [dash](https://github.com/plotly/dash) | 24457 | 2326 | 2167 | 1773 | 433 | 2026-10-15 19:38:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23380 | 8518 | 11439 | 20994 | 1474 | 2026-10-19 02:22:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 22406 | 1500 | 1439 | 7654 | 290 | 2026-10-18 14:00:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5582 | 1888 | 1873 | 231 | 2026-10-16 15:30:44 |
| [micropython](https://github.com/micropython/micropython) | 22134 | 9011 | 6144 | 8141 | 1535 | 2026-10-19 03:10:08 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18847 | 2876 | 3391 | 2240 | 734 | 2026-10-16 17:21:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1612 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16579 | 2460 | 3263 | 10419 | 237 | 2026-10-16 10:57:59 |
| [httpx](https://github.com/encode/httpx) | 15641 | 4333 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15125 | 6018 | 11704 | 14711 | 1867 | 2026-10-18 19:35:32 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14076 | 2148 | 2667 | 1242 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13933 | 1987 | 5569 | 6766 | 1373 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12674 | 1380 | 787 | 2222 | 39 | 2026-10-18 21:09:43 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12247 | 1823 | 8350 | 1234 | 217 | 2026-10-18 16:34:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11911 | 619 | 426 | 343 | 172 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1039 | 1147 | 1547 | 157 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9214 | 619 | 1054 | 569 | 235 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8796 | 1518 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7349 | 456 | 904 | 2637 | 336 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 531 | 1287 | 949 | 559 | 2026-10-17 02:36:57 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5428 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4452 | 386 | 1207 | 257 | 120 | 2026-10-15 21:56:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3677 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1363 | 265 | 2026-10-18 20:57:47 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 317 | 490 | 856 | 131 | 2026-10-18 11:23:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1603 | 356 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1814 | 131 | 5284 | 360 | 717 | 2026-10-18 19:26:43 |
| [jython](https://github.com/jython/jython) | 1549 | 231 | 303 | 155 | 102 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-19T04:22:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
