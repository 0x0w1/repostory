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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201192 | 79381 | 41914 | 83930 | 3419 | 2026-10-23 04:11:08 |
| [transformers](https://github.com/huggingface/transformers) | 168006 | 34944 | 19677 | 29420 | 960 | 2026-10-23 03:42:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 104989 | 32516 | 61946 | 139167 | 17747 | 2026-10-23 04:13:52 |
| [fastapi](https://github.com/fastapi/fastapi) | 103867 | 10093 | 3556 | 6518 | 57 | 2026-10-22 22:21:50 |
| [django](https://github.com/django/django) | 91563 | 37211 | 0 | 22109 | 540 | 2026-10-22 17:46:07 |
| [cpython](https://github.com/python/cpython) | 77748 | 38311 | 78834 | 79043 | 9416 | 2026-10-23 03:13:31 |
| [flask](https://github.com/pallets/flask) | 75014 | 17108 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67871 | 27564 | 12343 | 21666 | 2171 | 2026-10-22 13:18:29 |
| [keras](https://github.com/keras-team/keras) | 64376 | 19795 | 13036 | 10143 | 260 | 2026-10-23 02:02:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 50244 | 20567 | 28643 | 39639 | 2128 | 2026-10-22 22:43:47 |
| [ray](https://github.com/ray-project/ray) | 44106 | 8192 | 23232 | 43643 | 3602 | 2026-10-23 01:31:23 |
| [gym](https://github.com/openai/gym) | 37236 | 8666 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33987 | 4735 | 5776 | 4133 | 254 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33102 | 12948 | 14146 | 18874 | 2236 | 2026-10-22 21:46:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30215 | 7093 | 3966 | 5095 | 60 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29039 | 5237 | 5348 | 4621 | 744 | 2026-10-22 22:13:03 |
| [dash](https://github.com/plotly/dash) | 24468 | 2328 | 2167 | 1785 | 431 | 2026-10-22 20:56:07 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23386 | 8522 | 11452 | 21010 | 1477 | 2026-10-23 04:01:20 |
| [RustPython](https://github.com/RustPython/RustPython) | 22415 | 1503 | 1446 | 7771 | 304 | 2026-10-22 18:58:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5587 | 1888 | 1890 | 227 | 2026-10-21 17:27:04 |
| [micropython](https://github.com/micropython/micropython) | 22146 | 9012 | 6150 | 8154 | 1554 | 2026-10-19 03:10:08 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18854 | 2879 | 3397 | 2248 | 741 | 2026-10-22 15:58:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1614 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16588 | 2479 | 3266 | 10456 | 251 | 2026-10-22 11:04:29 |
| [httpx](https://github.com/encode/httpx) | 15719 | 4016 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15144 | 6029 | 11711 | 14737 | 1877 | 2026-10-21 21:23:38 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14085 | 2150 | 2667 | 1246 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13935 | 1994 | 5571 | 6777 | 1385 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12681 | 1399 | 794 | 2244 | 62 | 2026-10-22 23:41:16 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12256 | 1829 | 8357 | 1239 | 210 | 2026-10-22 20:14:20 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 619 | 426 | 344 | 171 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9808 | 1046 | 1147 | 1554 | 163 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9218 | 620 | 1054 | 572 | 238 | 2026-10-20 09:48:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7351 | 460 | 905 | 2646 | 340 | 2026-10-23 04:26:03 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5640 | 532 | 1289 | 955 | 553 | 2026-10-22 13:52:07 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5429 | 1051 | 937 | 326 | 205 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4456 | 387 | 1209 | 257 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4104 | 895 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 289 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 317 | 677 | 1372 | 266 | 2026-10-23 04:09:01 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 324 | 493 | 865 | 137 | 2026-10-20 07:08:23 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1603 | 355 | 2026-10-22 16:55:34 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1816 | 131 | 5286 | 374 | 721 | 2026-10-22 10:42:20 |
| [jython](https://github.com/jython/jython) | 1550 | 231 | 305 | 155 | 104 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-23T04:29:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
