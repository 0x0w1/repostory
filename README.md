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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200121 | 76501 | 41776 | 82096 | 3152 | 2026-09-16 04:11:39 |
| [transformers](https://github.com/huggingface/transformers) | 166220 | 34589 | 19474 | 28602 | 2432 | 2026-09-16 03:48:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 103036 | 29403 | 60995 | 135529 | 17617 | 2026-09-16 04:32:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 102356 | 9890 | 3551 | 6330 | 79 | 2026-09-14 18:49:48 |
| [django](https://github.com/django/django) | 91066 | 34419 | 0 | 21845 | 502 | 2026-09-15 17:37:20 |
| [cpython](https://github.com/python/cpython) | 77183 | 35533 | 78146 | 77101 | 9644 | 2026-09-16 02:13:12 |
| [flask](https://github.com/pallets/flask) | 74742 | 16987 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67264 | 27405 | 12281 | 21491 | 2163 | 2026-09-14 23:49:53 |
| [keras](https://github.com/keras-team/keras) | 64318 | 19792 | 12906 | 9865 | 192 | 2026-09-16 01:20:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 49731 | 20384 | 28545 | 38750 | 2692 | 2026-09-15 22:45:31 |
| [ray](https://github.com/ray-project/ray) | 43821 | 8038 | 23072 | 42708 | 3595 | 2026-09-16 01:59:04 |
| [gym](https://github.com/openai/gym) | 37239 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33901 | 4718 | 5772 | 4120 | 240 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32749 | 12799 | 14097 | 18448 | 2285 | 2026-09-15 19:56:15 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30183 | 7082 | 3966 | 5067 | 50 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28891 | 5165 | 5300 | 4370 | 726 | 2026-09-15 22:13:04 |
| [dash](https://github.com/plotly/dash) | 24408 | 2313 | 2152 | 1701 | 476 | 2026-09-15 19:59:18 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23219 | 8482 | 11424 | 20864 | 1484 | 2026-09-16 00:16:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22347 | 1487 | 1424 | 7221 | 394 | 2026-09-16 02:10:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5554 | 1882 | 1823 | 258 | 2026-09-15 16:51:11 |
| [micropython](https://github.com/micropython/micropython) | 22067 | 8970 | 6127 | 8092 | 1526 | 2026-09-16 00:09:28 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18785 | 2844 | 3384 | 2182 | 711 | 2026-09-15 21:35:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1597 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16547 | 2409 | 3252 | 10127 | 220 | 2026-09-16 02:35:25 |
| [httpx](https://github.com/encode/httpx) | 15483 | 1297 | 925 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15016 | 5934 | 11645 | 14513 | 1840 | 2026-09-15 12:46:34 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14022 | 2133 | 2662 | 1223 | 234 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13919 | 1956 | 5558 | 6726 | 1335 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12618 | 1309 | 782 | 2115 | 47 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12158 | 1783 | 8299 | 1208 | 208 | 2026-09-15 21:07:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11900 | 615 | 420 | 330 | 160 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 1033 | 1142 | 1518 | 160 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9191 | 613 | 1045 | 549 | 224 | 2026-09-14 13:10:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1510 | 868 | 651 | 292 | 2026-09-15 07:20:39 |
| [trio](https://github.com/python-trio/trio) | 7328 | 428 | 901 | 2607 | 327 | 2026-09-14 22:29:41 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 739 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5630 | 516 | 1270 | 903 | 525 | 2026-09-15 14:26:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5391 | 1041 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4397 | 376 | 1202 | 250 | 119 | 2026-09-11 19:10:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3991 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3669 | 206 | 286 | 136 | 25 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2760 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2543 | 264 | 477 | 772 | 109 | 2026-09-15 17:39:30 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 136 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1795 | 125 | 5257 | 303 | 711 | 2026-09-15 19:06:49 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-16T04:34:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
