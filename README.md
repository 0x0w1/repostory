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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196653 | 75765 | 41648 | 79304 | 2958 | 2026-08-02 03:04:22 |
| [transformers](https://github.com/huggingface/transformers) | 163232 | 34085 | 19258 | 27708 | 2316 | 2026-08-01 17:06:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 102116 | 28637 | 60133 | 131074 | 18379 | 2026-08-02 03:35:31 |
| [fastapi](https://github.com/fastapi/fastapi) | 101139 | 9718 | 3542 | 6182 | 79 | 2026-08-01 12:29:20 |
| [django](https://github.com/django/django) | 88254 | 34061 | 0 | 21599 | 449 | 2026-07-31 20:47:42 |
| [cpython](https://github.com/python/cpython) | 74007 | 35085 | 77498 | 75219 | 9519 | 2026-08-01 20:22:24 |
| [flask](https://github.com/pallets/flask) | 72017 | 16923 | 2758 | 2882 | 7 | 2026-07-30 17:29:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66851 | 27250 | 12214 | 21227 | 2112 | 2026-08-01 14:27:12 |
| [keras](https://github.com/keras-team/keras) | 64210 | 19746 | 12856 | 9650 | 208 | 2026-08-01 11:15:08 |
| [pandas](https://github.com/pandas-dev/pandas) | 49393 | 20217 | 28447 | 38039 | 2913 | 2026-08-02 01:51:40 |
| [ray](https://github.com/ray-project/ray) | 43409 | 7869 | 22890 | 41867 | 3496 | 2026-08-01 22:37:13 |
| [gym](https://github.com/openai/gym) | 37247 | 8686 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33794 | 4700 | 5768 | 4106 | 230 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32470 | 12612 | 14031 | 18045 | 2320 | 2026-08-01 12:57:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30115 | 7074 | 3965 | 5036 | 68 | 2026-07-31 18:52:20 |
| [celery](https://github.com/celery/celery) | 28750 | 5121 | 5289 | 4209 | 796 | 2026-07-31 22:13:52 |
| [dash](https://github.com/plotly/dash) | 24362 | 2311 | 2136 | 1671 | 541 | 2026-08-01 00:54:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23057 | 8423 | 11384 | 20710 | 1475 | 2026-08-01 19:16:30 |
| [RustPython](https://github.com/RustPython/RustPython) | 22236 | 1469 | 1406 | 6947 | 401 | 2026-08-01 15:25:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22192 | 5548 | 1876 | 1800 | 249 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21950 | 8913 | 6111 | 8006 | 1560 | 2026-08-01 08:22:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18703 | 2831 | 3376 | 2126 | 773 | 2026-08-01 12:45:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1594 | 1471 | 1700 | 143 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16506 | 2361 | 3228 | 9716 | 220 | 2026-07-31 15:24:15 |
| [httpx](https://github.com/encode/httpx) | 15385 | 1231 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14876 | 5839 | 11553 | 14185 | 1844 | 2026-08-01 20:46:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13984 | 2128 | 2655 | 1207 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13878 | 1922 | 5546 | 6678 | 1286 | 2026-07-28 14:48:11 |
| [starlette](https://github.com/Kludex/starlette) | 12510 | 1254 | 772 | 1993 | 77 | 2026-08-01 19:17:40 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12043 | 1735 | 8253 | 1163 | 211 | 2026-07-28 21:16:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11874 | 613 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 1020 | 1139 | 1493 | 157 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9157 | 602 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1500 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7305 | 411 | 898 | 2585 | 326 | 2026-08-01 11:05:56 |
| [hug](https://github.com/hugapi/hug) | 6885 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5606 | 501 | 1265 | 880 | 539 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5339 | 1030 | 924 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4292 | 357 | 1190 | 237 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4092 | 891 | 1065 | 2739 | 89 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 203 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2518 | 234 | 462 | 721 | 100 | 2026-08-01 14:38:38 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1084 | 1581 | 357 | 2026-07-29 16:59:19 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-27 17:48:12 |
| [pypy](https://github.com/pypy/pypy) | 1778 | 121 | 5244 | 282 | 727 | 2026-07-31 19:42:29 |
| [jython](https://github.com/jython/jython) | 1529 | 230 | 299 | 148 | 106 | 2026-07-26 19:12:04 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-02T03:39:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
