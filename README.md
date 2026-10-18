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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201078 | 79637 | 41904 | 83738 | 3397 | 2026-10-18 04:10:34 |
| [transformers](https://github.com/huggingface/transformers) | 167799 | 34889 | 19650 | 29269 | 2327 | 2026-10-18 00:34:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 104837 | 32724 | 61795 | 138843 | 17645 | 2026-10-18 04:04:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 103184 | 10050 | 3556 | 6446 | 83 | 2026-10-17 18:19:21 |
| [django](https://github.com/django/django) | 91419 | 37466 | 0 | 22083 | 545 | 2026-10-15 06:51:05 |
| [cpython](https://github.com/python/cpython) | 77668 | 38574 | 78750 | 78522 | 9852 | 2026-10-18 04:12:51 |
| [flask](https://github.com/pallets/flask) | 74923 | 17079 | 2767 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67734 | 27541 | 12333 | 21632 | 2161 | 2026-10-16 17:21:46 |
| [keras](https://github.com/keras-team/keras) | 64376 | 19798 | 13019 | 10099 | 235 | 2026-10-16 22:56:12 |
| [pandas](https://github.com/pandas-dev/pandas) | 50149 | 20532 | 28627 | 39500 | 2137 | 2026-10-18 02:33:59 |
| [ray](https://github.com/ray-project/ray) | 44057 | 8169 | 23201 | 43497 | 3595 | 2026-10-18 00:22:21 |
| [gym](https://github.com/openai/gym) | 37240 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33967 | 4736 | 5776 | 4130 | 251 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33036 | 12925 | 14136 | 18841 | 2240 | 2026-10-17 20:57:47 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30211 | 7092 | 3966 | 5092 | 57 | 2026-10-14 22:32:27 |
| [celery](https://github.com/celery/celery) | 28996 | 5220 | 5336 | 4579 | 717 | 2026-10-17 15:55:10 |
| [dash](https://github.com/plotly/dash) | 24456 | 2327 | 2167 | 1773 | 433 | 2026-10-15 19:38:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23380 | 8517 | 11439 | 20993 | 1475 | 2026-10-17 19:32:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22405 | 1500 | 1439 | 7639 | 287 | 2026-10-18 02:06:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5581 | 1888 | 1873 | 231 | 2026-10-16 15:30:44 |
| [micropython](https://github.com/micropython/micropython) | 22134 | 9008 | 6144 | 8140 | 1536 | 2026-10-17 00:21:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18847 | 2875 | 3391 | 2238 | 732 | 2026-10-16 17:21:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1611 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16576 | 2459 | 3263 | 10418 | 236 | 2026-10-16 10:57:59 |
| [httpx](https://github.com/encode/httpx) | 15615 | 4261 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15123 | 6018 | 11702 | 14703 | 1863 | 2026-10-18 00:48:26 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14075 | 2148 | 2667 | 1242 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1984 | 5569 | 6762 | 1369 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12673 | 1377 | 787 | 2216 | 45 | 2026-10-17 18:12:35 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12244 | 1819 | 8349 | 1232 | 218 | 2026-10-16 20:52:53 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11910 | 617 | 426 | 341 | 170 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9808 | 1039 | 1147 | 1547 | 157 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9213 | 619 | 1050 | 565 | 227 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8796 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7346 | 456 | 904 | 2637 | 336 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5636 | 530 | 1283 | 945 | 551 | 2026-10-17 02:36:57 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5428 | 1049 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4452 | 384 | 1207 | 257 | 120 | 2026-10-15 21:56:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 894 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3677 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1362 | 266 | 2026-10-17 21:44:36 |
| [anyio](https://github.com/agronholm/anyio) | 2558 | 317 | 490 | 856 | 134 | 2026-10-17 23:09:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1603 | 356 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1814 | 130 | 5284 | 359 | 716 | 2026-10-17 19:14:44 |
| [jython](https://github.com/jython/jython) | 1549 | 231 | 303 | 155 | 102 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-18T04:13:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
