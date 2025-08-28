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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191362 | 74801 | 40753 | 56691 | 1518 | 2025-08-28 01:51:08 |
| [transformers](https://github.com/huggingface/transformers) | 148900 | 30192 | 17850 | 22086 | 1987 | 2025-08-27 21:06:12 |
| [pytorch](https://github.com/pytorch/pytorch) | 92726 | 25104 | 53361 | 107857 | 17011 | 2025-08-28 01:50:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 88860 | 7784 | 3467 | 4671 | 283 | 2025-08-25 20:03:25 |
| [django](https://github.com/django/django) | 84798 | 32861 | 0 | 19720 | 361 | 2025-08-27 22:23:43 |
| [flask](https://github.com/pallets/flask) | 70228 | 16522 | 2692 | 2690 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68558 | 32689 | 73412 | 63869 | 9303 | 2025-08-27 23:41:32 |
| [keras](https://github.com/keras-team/keras) | 63368 | 19615 | 12530 | 8303 | 296 | 2025-08-27 20:11:07 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63156 | 26175 | 11660 | 19240 | 2165 | 2025-08-27 10:28:25 |
| [pandas](https://github.com/pandas-dev/pandas) | 46420 | 18854 | 27676 | 34478 | 3693 | 2025-08-27 16:40:07 |
| [ray](https://github.com/ray-project/ray) | 38675 | 6744 | 20984 | 34696 | 3039 | 2025-08-28 01:57:17 |
| [gym](https://github.com/openai/gym) | 36420 | 8691 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32335 | 4568 | 5718 | 4065 | 200 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30259 | 11263 | 13501 | 16067 | 2345 | 2025-08-27 23:14:41 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29405 | 7000 | 3945 | 4828 | 98 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27098 | 4831 | 5157 | 3647 | 757 | 2025-08-26 18:18:37 |
| [dash](https://github.com/plotly/dash) | 23979 | 2192 | 1980 | 1321 | 554 | 2025-08-27 14:32:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22118 | 5538 | 1851 | 1670 | 206 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21614 | 7972 | 10952 | 19484 | 1635 | 2025-08-28 00:43:12 |
| [micropython](https://github.com/micropython/micropython) | 20755 | 8383 | 5798 | 7136 | 1773 | 2025-08-28 01:32:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 20436 | 1342 | 1211 | 4837 | 441 | 2025-08-28 00:58:20 |
| [sanic](https://github.com/sanic-org/sanic) | 18483 | 1579 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17652 | 2706 | 3245 | 1945 | 719 | 2025-08-27 22:20:54 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15946 | 2117 | 3144 | 8012 | 265 | 2025-08-27 19:03:36 |
| [httpx](https://github.com/encode/httpx) | 14502 | 946 | 915 | 1709 | 104 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13959 | 5454 | 10986 | 12515 | 1769 | 2025-08-27 03:42:20 |
| [dask](https://github.com/dask/dask) | 13440 | 1794 | 5426 | 6337 | 1195 | 2025-08-27 20:54:53 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13390 | 2029 | 2624 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11389 | 1032 | 750 | 1683 | 49 | 2025-08-24 13:36:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11194 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10820 | 1578 | 8074 | 979 | 230 | 2025-08-27 00:53:51 |
| [falcon](https://github.com/falconry/falcon) | 9708 | 959 | 1094 | 1362 | 156 | 2025-08-27 21:26:23 |
| [bottle](https://github.com/bottlepy/bottle) | 8651 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8472 | 519 | 936 | 430 | 403 | 2025-08-27 11:10:14 |
| [hug](https://github.com/hugapi/hug) | 6892 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6757 | 365 | 864 | 2445 | 314 | 2025-08-23 20:10:19 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 575 | 30 | 2025-08-26 14:12:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5262 | 435 | 1188 | 711 | 495 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4963 | 929 | 864 | 257 | 158 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4042 | 891 | 1061 | 2718 | 88 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3556 | 288 | 1154 | 194 | 115 | 2025-08-27 18:15:28 |
| [quart](https://github.com/pallets/quart) | 3419 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2679 | 304 | 649 | 1261 | 307 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2186 | 165 | 399 | 501 | 67 | 2025-08-25 19:02:47 |
| [web2py](https://github.com/web2py/web2py) | 2155 | 908 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-25 17:35:48 |
| [pypy](https://github.com/pypy/pypy) | 1484 | 84 | 5142 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1428 | 218 | 280 | 113 | 99 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 100 | 36 | 15 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-28T01:58:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
