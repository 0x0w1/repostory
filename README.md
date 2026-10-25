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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201231 | 79117 | 41916 | 83993 | 3397 | 2026-10-25 04:01:13 |
| [transformers](https://github.com/huggingface/transformers) | 168109 | 34975 | 19689 | 29469 | 1002 | 2026-10-25 01:22:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 105049 | 32181 | 61975 | 139295 | 17781 | 2026-10-25 03:55:59 |
| [fastapi](https://github.com/fastapi/fastapi) | 104100 | 10117 | 3556 | 6527 | 61 | 2026-10-23 23:46:14 |
| [django](https://github.com/django/django) | 91582 | 36948 | 0 | 22113 | 536 | 2026-10-23 23:30:30 |
| [cpython](https://github.com/python/cpython) | 77761 | 37997 | 78880 | 79215 | 9306 | 2026-10-25 04:08:51 |
| [flask](https://github.com/pallets/flask) | 75031 | 17117 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67898 | 27576 | 12346 | 21680 | 2171 | 2026-10-24 21:40:06 |
| [keras](https://github.com/keras-team/keras) | 64386 | 19797 | 13037 | 10154 | 266 | 2026-10-23 22:31:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 50268 | 20586 | 28648 | 39673 | 2130 | 2026-10-25 00:04:46 |
| [ray](https://github.com/ray-project/ray) | 44119 | 8196 | 23245 | 43697 | 3627 | 2026-10-25 01:37:06 |
| [gym](https://github.com/openai/gym) | 37235 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33992 | 4735 | 5778 | 4135 | 257 | 2026-10-23 13:47:36 |
| [numpy](https://github.com/numpy/numpy) | 33126 | 12960 | 14150 | 18890 | 2236 | 2026-10-24 20:41:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30216 | 7095 | 3966 | 5098 | 63 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29056 | 5243 | 5349 | 4630 | 737 | 2026-10-24 16:18:16 |
| [dash](https://github.com/plotly/dash) | 24469 | 2331 | 2168 | 1788 | 433 | 2026-10-23 16:35:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23390 | 8528 | 11452 | 21018 | 1478 | 2026-10-23 19:17:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 22422 | 1507 | 1446 | 7797 | 295 | 2026-10-24 05:57:37 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5590 | 1888 | 1892 | 228 | 2026-10-25 03:27:54 |
| [micropython](https://github.com/micropython/micropython) | 22152 | 9014 | 6151 | 8157 | 1552 | 2026-10-23 06:06:21 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18853 | 2882 | 3397 | 2253 | 743 | 2026-10-23 23:43:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1614 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16591 | 2483 | 3266 | 10471 | 262 | 2026-10-23 11:23:34 |
| [httpx](https://github.com/encode/httpx) | 15747 | 3673 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15150 | 6036 | 11716 | 14750 | 1874 | 2026-10-24 21:37:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14086 | 2150 | 2667 | 1246 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13938 | 2000 | 5577 | 6785 | 1399 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12682 | 1406 | 794 | 2261 | 40 | 2026-10-24 17:17:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12262 | 1831 | 8359 | 1241 | 212 | 2026-10-23 14:28:12 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 619 | 426 | 344 | 171 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1047 | 1148 | 1554 | 157 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9218 | 621 | 1054 | 578 | 244 | 2026-10-20 09:48:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1517 | 867 | 655 | 289 | 2026-10-23 15:12:18 |
| [trio](https://github.com/python-trio/trio) | 7352 | 462 | 905 | 2648 | 339 | 2026-10-24 14:32:28 |
| [hug](https://github.com/hugapi/hug) | 6874 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5636 | 535 | 1300 | 969 | 558 | 2026-10-25 03:52:22 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5432 | 1050 | 937 | 326 | 204 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4455 | 388 | 1209 | 257 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 677 | 1378 | 264 | 2026-10-24 15:22:24 |
| [anyio](https://github.com/agronholm/anyio) | 2559 | 330 | 493 | 870 | 141 | 2026-10-25 00:15:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2357 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1603 | 355 | 2026-10-22 16:55:34 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1819 | 131 | 5286 | 379 | 718 | 2026-10-24 16:55:51 |
| [jython](https://github.com/jython/jython) | 1551 | 231 | 305 | 155 | 104 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-25T04:23:17*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
