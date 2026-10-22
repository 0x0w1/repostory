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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201177 | 79396 | 41913 | 83909 | 3450 | 2026-10-22 04:18:34 |
| [transformers](https://github.com/huggingface/transformers) | 167968 | 34947 | 19669 | 29375 | 947 | 2026-10-22 01:14:57 |
| [pytorch](https://github.com/pytorch/pytorch) | 104977 | 32518 | 61903 | 139097 | 17689 | 2026-10-22 04:17:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 103363 | 10075 | 3555 | 6511 | 57 | 2026-10-21 20:59:13 |
| [django](https://github.com/django/django) | 91483 | 37226 | 0 | 22104 | 541 | 2026-10-22 00:29:33 |
| [cpython](https://github.com/python/cpython) | 77730 | 38319 | 78784 | 78861 | 9441 | 2026-10-22 04:19:12 |
| [flask](https://github.com/pallets/flask) | 74950 | 17126 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67857 | 27576 | 12343 | 21657 | 2166 | 2026-10-21 20:18:26 |
| [keras](https://github.com/keras-team/keras) | 64377 | 19805 | 13034 | 10139 | 267 | 2026-10-21 23:42:46 |
| [pandas](https://github.com/pandas-dev/pandas) | 50240 | 20590 | 28639 | 39622 | 2147 | 2026-10-21 19:48:42 |
| [ray](https://github.com/ray-project/ray) | 44102 | 8185 | 23224 | 43604 | 3585 | 2026-10-22 02:32:38 |
| [gym](https://github.com/openai/gym) | 37236 | 8666 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33982 | 4735 | 5776 | 4133 | 254 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33087 | 12971 | 14144 | 18870 | 2237 | 2026-10-22 02:32:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30212 | 7091 | 3966 | 5093 | 58 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29032 | 5234 | 5347 | 4612 | 749 | 2026-10-20 22:12:54 |
| [dash](https://github.com/plotly/dash) | 24465 | 2328 | 2167 | 1780 | 433 | 2026-10-21 19:45:02 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23386 | 8520 | 11447 | 21001 | 1474 | 2026-10-21 19:42:37 |
| [RustPython](https://github.com/RustPython/RustPython) | 22412 | 1502 | 1446 | 7742 | 298 | 2026-10-22 02:21:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22168 | 5584 | 1888 | 1888 | 225 | 2026-10-21 17:27:04 |
| [micropython](https://github.com/micropython/micropython) | 22145 | 9011 | 6148 | 8149 | 1547 | 2026-10-19 03:10:08 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18853 | 2877 | 3396 | 2243 | 738 | 2026-10-22 01:59:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1614 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16585 | 2473 | 3266 | 10450 | 246 | 2026-10-21 11:47:18 |
| [httpx](https://github.com/encode/httpx) | 15664 | 3998 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15139 | 6026 | 11709 | 14734 | 1874 | 2026-10-21 21:23:38 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14083 | 2151 | 2667 | 1245 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13935 | 1993 | 5571 | 6774 | 1382 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12681 | 1397 | 793 | 2237 | 58 | 2026-10-21 13:57:51 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12254 | 1836 | 8356 | 1239 | 210 | 2026-10-21 16:25:41 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 619 | 426 | 344 | 171 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1045 | 1147 | 1552 | 162 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9218 | 620 | 1054 | 571 | 237 | 2026-10-20 09:48:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7351 | 459 | 905 | 2640 | 339 | 2026-10-19 23:00:19 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5640 | 531 | 1289 | 954 | 555 | 2026-10-21 18:40:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5428 | 1050 | 936 | 325 | 204 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4456 | 386 | 1209 | 257 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 289 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 317 | 677 | 1369 | 264 | 2026-10-21 23:15:11 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 321 | 492 | 863 | 135 | 2026-10-20 07:08:23 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 917 | 1085 | 1603 | 356 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1816 | 131 | 5286 | 370 | 717 | 2026-10-21 20:10:28 |
| [jython](https://github.com/jython/jython) | 1549 | 231 | 304 | 155 | 103 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-22T04:24:15*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
