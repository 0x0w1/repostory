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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200704 | 78339 | 41840 | 83045 | 3278 | 2026-10-05 04:54:41 |
| [transformers](https://github.com/huggingface/transformers) | 166962 | 34749 | 19562 | 28954 | 2374 | 2026-10-05 05:15:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 103766 | 31390 | 61481 | 137563 | 17589 | 2026-10-05 05:18:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 102814 | 9990 | 3557 | 6404 | 86 | 2026-10-02 11:36:38 |
| [django](https://github.com/django/django) | 91312 | 36251 | 0 | 21993 | 531 | 2026-10-03 15:23:24 |
| [cpython](https://github.com/python/cpython) | 77493 | 37352 | 78514 | 77944 | 9773 | 2026-10-05 03:09:26 |
| [flask](https://github.com/pallets/flask) | 74889 | 17038 | 2769 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67472 | 27477 | 12310 | 21569 | 2161 | 2026-10-03 14:29:24 |
| [keras](https://github.com/keras-team/keras) | 64353 | 19805 | 12974 | 9993 | 265 | 2026-10-02 22:17:14 |
| [pandas](https://github.com/pandas-dev/pandas) | 49915 | 20462 | 28582 | 39174 | 2413 | 2026-10-05 04:19:04 |
| [ray](https://github.com/ray-project/ray) | 43970 | 8120 | 23118 | 43172 | 3559 | 2026-10-05 05:17:31 |
| [gym](https://github.com/openai/gym) | 37243 | 8670 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33938 | 4734 | 5774 | 4128 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 32995 | 12880 | 14123 | 18653 | 2251 | 2026-10-04 23:35:35 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30202 | 7087 | 3966 | 5076 | 50 | 2026-09-30 06:38:50 |
| [celery](https://github.com/celery/celery) | 28935 | 5203 | 5326 | 4509 | 736 | 2026-10-05 05:15:55 |
| [dash](https://github.com/plotly/dash) | 24441 | 2328 | 2165 | 1748 | 432 | 2026-10-02 15:22:38 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23325 | 8504 | 11433 | 20938 | 1499 | 2026-10-04 14:30:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 22376 | 1494 | 1434 | 7428 | 404 | 2026-10-05 00:43:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22170 | 5564 | 1885 | 1851 | 215 | 2026-10-04 21:50:53 |
| [micropython](https://github.com/micropython/micropython) | 22108 | 8984 | 6135 | 8119 | 1533 | 2026-10-03 07:13:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18822 | 2858 | 3386 | 2207 | 728 | 2026-10-01 07:39:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1608 | 1470 | 1684 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16570 | 2440 | 3261 | 10326 | 217 | 2026-10-05 00:15:59 |
| [httpx](https://github.com/encode/httpx) | 15524 | 3015 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15076 | 5989 | 11680 | 14633 | 1860 | 2026-10-04 23:09:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14057 | 2142 | 2663 | 1227 | 238 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13933 | 1972 | 5563 | 6743 | 1351 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12651 | 1359 | 785 | 2177 | 49 | 2026-10-04 20:29:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12199 | 1804 | 8328 | 1218 | 217 | 2026-10-03 18:37:23 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11907 | 616 | 422 | 335 | 163 | 2026-10-01 15:38:19 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1037 | 1145 | 1533 | 157 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9208 | 614 | 1047 | 558 | 224 | 2026-10-04 11:29:42 |
| [bottle](https://github.com/bottlepy/bottle) | 8793 | 1514 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7341 | 441 | 902 | 2624 | 330 | 2026-10-01 07:30:18 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 520 | 1270 | 909 | 520 | 2026-10-03 15:26:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5414 | 1045 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4427 | 384 | 1204 | 253 | 121 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3988 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3672 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 676 | 1348 | 300 | 2026-10-05 02:55:17 |
| [anyio](https://github.com/agronholm/anyio) | 2551 | 298 | 484 | 818 | 131 | 2026-10-04 21:16:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 917 | 1085 | 1601 | 357 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1786 | 276 | 273 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1807 | 128 | 5274 | 325 | 722 | 2026-10-05 04:01:41 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-10-05T05:19:18*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
