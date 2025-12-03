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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192655 | 75019 | 41007 | 62407 | 2710 | 2025-12-03 02:02:38 |
| [transformers](https://github.com/huggingface/transformers) | 153322 | 31294 | 18259 | 23708 | 2119 | 2025-12-02 20:03:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 95543 | 26080 | 55631 | 113316 | 17837 | 2025-12-03 02:07:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 92568 | 8306 | 3478 | 4926 | 188 | 2025-12-02 22:27:54 |
| [django](https://github.com/django/django) | 86009 | 33279 | 0 | 20297 | 368 | 2025-12-02 20:40:21 |
| [flask](https://github.com/pallets/flask) | 70865 | 16644 | 2704 | 2729 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70099 | 33569 | 74519 | 66711 | 9198 | 2025-12-02 20:33:40 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64179 | 26482 | 11831 | 19863 | 2108 | 2025-12-02 15:14:53 |
| [keras](https://github.com/keras-team/keras) | 63621 | 19656 | 12599 | 8495 | 269 | 2025-12-02 21:14:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 47238 | 19359 | 27921 | 35274 | 3582 | 2025-12-02 22:09:02 |
| [ray](https://github.com/ray-project/ray) | 40105 | 6967 | 21957 | 36818 | 3211 | 2025-12-03 02:04:52 |
| [gym](https://github.com/openai/gym) | 36834 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32897 | 4633 | 5732 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30940 | 11782 | 13680 | 16616 | 2376 | 2025-12-03 00:02:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29704 | 7039 | 3946 | 4876 | 87 | 2025-12-02 16:32:17 |
| [celery](https://github.com/celery/celery) | 27663 | 4907 | 5177 | 3734 | 756 | 2025-12-01 16:54:26 |
| [dash](https://github.com/plotly/dash) | 24302 | 2239 | 2032 | 1383 | 558 | 2025-12-02 22:55:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22375 | 5545 | 1857 | 1677 | 207 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22078 | 8134 | 11063 | 19697 | 1603 | 2025-12-01 21:41:58 |
| [micropython](https://github.com/micropython/micropython) | 21157 | 8564 | 5887 | 7398 | 1787 | 2025-12-01 13:47:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 20861 | 1364 | 1240 | 5021 | 449 | 2025-12-02 22:07:33 |
| [sanic](https://github.com/sanic-org/sanic) | 18588 | 1584 | 1454 | 1635 | 133 | 2025-11-30 19:21:39 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18042 | 2755 | 3302 | 1986 | 753 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16123 | 2163 | 3164 | 8329 | 270 | 2025-12-02 17:10:12 |
| [httpx](https://github.com/encode/httpx) | 14814 | 983 | 923 | 1758 | 116 | 2025-12-01 17:39:25 |
| [scipy](https://github.com/scipy/scipy) | 14235 | 5553 | 11167 | 12909 | 1763 | 2025-12-02 21:00:04 |
| [dask](https://github.com/dask/dask) | 13635 | 1826 | 5471 | 6408 | 1199 | 2025-11-25 14:34:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13595 | 2057 | 2637 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11718 | 1088 | 760 | 1746 | 53 | 2025-12-01 21:33:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11470 | 587 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11203 | 1605 | 8127 | 1008 | 215 | 2025-12-03 01:07:25 |
| [falcon](https://github.com/falconry/falcon) | 9766 | 971 | 1113 | 1403 | 163 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8749 | 542 | 979 | 458 | 178 | 2025-12-02 07:59:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8703 | 1488 | 856 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7037 | 372 | 875 | 2475 | 312 | 2025-12-02 21:01:29 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 746 | 979 | 580 | 34 | 2025-12-02 15:18:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5399 | 446 | 1200 | 724 | 508 | 2025-11-27 05:19:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5105 | 972 | 879 | 264 | 175 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4067 | 886 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3791 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3554 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2716 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2330 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2313 | 179 | 418 | 554 | 72 | 2025-12-01 20:04:08 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 370 | 1784 | 266 | 265 | 2025-12-01 17:53:21 |
| [pypy](https://github.com/pypy/pypy) | 1584 | 90 | 5165 | 172 | 749 | 2025-12-02 21:00:34 |
| [jython](https://github.com/jython/jython) | 1461 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-03T02:07:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
