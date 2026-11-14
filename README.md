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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201592 | 77960 | 41977 | 84731 | 3436 | 2026-11-14 05:55:22 |
| [transformers](https://github.com/huggingface/transformers) | 168955 | 35193 | 19870 | 30038 | 1125 | 2026-11-14 00:53:09 |
| [pytorch](https://github.com/pytorch/pytorch) | 105472 | 30712 | 62597 | 141565 | 18209 | 2026-11-14 05:56:02 |
| [fastapi](https://github.com/fastapi/fastapi) | 104693 | 10248 | 3555 | 6610 | 53 | 2026-11-13 17:46:18 |
| [django](https://github.com/django/django) | 91730 | 35215 | 0 | 22202 | 529 | 2026-11-13 17:06:51 |
| [cpython](https://github.com/python/cpython) | 78204 | 36590 | 79272 | 80295 | 9286 | 2026-11-14 05:50:11 |
| [flask](https://github.com/pallets/flask) | 75114 | 17324 | 2780 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68166 | 27676 | 12381 | 21810 | 2168 | 2026-11-13 12:58:16 |
| [keras](https://github.com/keras-team/keras) | 64426 | 19818 | 13085 | 10264 | 237 | 2026-11-13 23:49:20 |
| [pandas](https://github.com/pandas-dev/pandas) | 50512 | 20737 | 28692 | 39984 | 1867 | 2026-11-13 22:53:04 |
| [ray](https://github.com/ray-project/ray) | 44285 | 8283 | 23321 | 44354 | 3779 | 2026-11-14 03:02:24 |
| [gym](https://github.com/openai/gym) | 37235 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34051 | 4739 | 5784 | 4148 | 270 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33363 | 13100 | 14186 | 19034 | 2243 | 2026-11-13 22:55:48 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30232 | 7101 | 3966 | 5114 | 65 | 2026-11-12 10:27:24 |
| [celery](https://github.com/celery/celery) | 29194 | 5262 | 5392 | 4731 | 801 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24489 | 2347 | 2182 | 1835 | 437 | 2026-11-13 15:25:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23455 | 8549 | 11460 | 21066 | 1474 | 2026-11-13 21:25:06 |
| [RustPython](https://github.com/RustPython/RustPython) | 22482 | 1510 | 1463 | 8264 | 308 | 2026-11-14 02:49:49 |
| [micropython](https://github.com/micropython/micropython) | 22197 | 9063 | 6180 | 8253 | 1602 | 2026-11-12 12:22:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5607 | 1895 | 1931 | 222 | 2026-11-13 20:46:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18899 | 2893 | 3402 | 2281 | 752 | 2026-11-13 07:35:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1618 | 1474 | 1690 | 164 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16606 | 2522 | 3275 | 10715 | 303 | 2026-11-13 19:33:14 |
| [httpx](https://github.com/encode/httpx) | 15786 | 1872 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15216 | 6084 | 11766 | 14900 | 1910 | 2026-11-13 23:28:02 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14111 | 2161 | 2668 | 1255 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13949 | 2027 | 5583 | 6837 | 1434 | 2026-11-13 16:55:52 |
| [starlette](https://github.com/Kludex/starlette) | 12719 | 1444 | 798 | 2303 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12281 | 1848 | 8393 | 1264 | 207 | 2026-11-13 16:45:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11937 | 621 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9814 | 1056 | 1152 | 1576 | 163 | 2026-11-11 09:13:34 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9245 | 627 | 1057 | 617 | 159 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1512 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7362 | 476 | 911 | 2671 | 342 | 2026-11-13 19:20:22 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5642 | 546 | 1308 | 991 | 557 | 2026-11-12 09:12:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5451 | 1054 | 938 | 334 | 201 | 2026-11-14 03:23:07 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4477 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 320 | 682 | 1417 | 258 | 2026-11-12 22:25:01 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 500 | 893 | 147 | 2026-11-13 20:51:47 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 281 | 279 | 2026-11-09 18:05:48 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 133 | 5302 | 430 | 721 | 2026-11-13 16:10:40 |
| [jython](https://github.com/jython/jython) | 1551 | 236 | 306 | 163 | 108 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-14T06:00:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
