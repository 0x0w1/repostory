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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191223 | 74780 | 40727 | 56342 | 1527 | 2025-08-19 02:00:28 |
| [transformers](https://github.com/huggingface/transformers) | 148480 | 30080 | 17793 | 21893 | 1961 | 2025-08-18 20:35:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 92485 | 25009 | 53167 | 107314 | 16827 | 2025-08-19 01:55:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 88512 | 7747 | 3466 | 4664 | 285 | 2025-08-18 21:07:26 |
| [django](https://github.com/django/django) | 84616 | 32830 | 0 | 19680 | 361 | 2025-08-18 21:21:00 |
| [flask](https://github.com/pallets/flask) | 70191 | 16524 | 2692 | 2688 | 9 | 2025-08-18 18:44:59 |
| [cpython](https://github.com/python/cpython) | 68425 | 32628 | 73317 | 63681 | 9278 | 2025-08-18 21:21:55 |
| [keras](https://github.com/keras-team/keras) | 63344 | 19614 | 12525 | 8286 | 296 | 2025-08-19 01:31:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63058 | 26156 | 11647 | 19194 | 2159 | 2025-08-19 01:11:14 |
| [pandas](https://github.com/pandas-dev/pandas) | 46328 | 18831 | 27657 | 34435 | 3694 | 2025-08-18 15:50:35 |
| [ray](https://github.com/ray-project/ray) | 38527 | 6719 | 20900 | 34477 | 2978 | 2025-08-19 01:51:34 |
| [gym](https://github.com/openai/gym) | 36398 | 8687 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32195 | 4564 | 5716 | 4064 | 197 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30175 | 11220 | 13491 | 16028 | 2341 | 2025-08-18 23:43:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29380 | 6993 | 3945 | 4827 | 98 | 2025-08-16 07:10:06 |
| [celery](https://github.com/celery/celery) | 27028 | 4826 | 5156 | 3639 | 760 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23953 | 2190 | 1976 | 1312 | 550 | 2025-08-18 13:11:58 |
| [tornado](https://github.com/tornadoweb/tornado) | 22103 | 5539 | 1851 | 1670 | 206 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21567 | 7961 | 10945 | 19454 | 1653 | 2025-08-18 20:16:57 |
| [micropython](https://github.com/micropython/micropython) | 20733 | 8369 | 5787 | 7120 | 1774 | 2025-08-18 04:08:55 |
| [RustPython](https://github.com/RustPython/RustPython) | 20415 | 1342 | 1208 | 4828 | 449 | 2025-08-18 09:15:45 |
| [sanic](https://github.com/sanic-org/sanic) | 18474 | 1578 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17611 | 2700 | 3241 | 1944 | 721 | 2025-08-14 15:14:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15923 | 2113 | 3142 | 7998 | 262 | 2025-08-18 16:30:06 |
| [httpx](https://github.com/encode/httpx) | 14472 | 944 | 914 | 1708 | 103 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13928 | 5444 | 10974 | 12490 | 1758 | 2025-08-18 22:57:00 |
| [dask](https://github.com/dask/dask) | 13417 | 1791 | 5423 | 6333 | 1190 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13370 | 2028 | 2623 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11358 | 1029 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11150 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10787 | 1574 | 8068 | 977 | 238 | 2025-08-18 21:26:01 |
| [falcon](https://github.com/falconry/falcon) | 9704 | 959 | 1093 | 1359 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8648 | 1487 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8454 | 517 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6727 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6707 | 362 | 863 | 2442 | 312 | 2025-08-18 22:06:52 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5247 | 435 | 1184 | 709 | 494 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4943 | 925 | 861 | 258 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1060 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3935 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3531 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3401 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2676 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2175 | 163 | 399 | 499 | 68 | 2025-08-18 17:55:01 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 906 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1779 | 264 | 260 | 2025-08-18 17:39:32 |
| [pypy](https://github.com/pypy/pypy) | 1474 | 83 | 5140 | 168 | 734 | 2025-08-14 05:35:41 |
| [jython](https://github.com/jython/jython) | 1424 | 216 | 279 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-19T02:04:20*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
