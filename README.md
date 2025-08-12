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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191141 | 74765 | 40708 | 55963 | 1555 | 2025-08-12 02:00:39 |
| [transformers](https://github.com/huggingface/transformers) | 148199 | 29984 | 17743 | 21772 | 1971 | 2025-08-11 23:00:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 92290 | 24920 | 53018 | 106918 | 16778 | 2025-08-12 02:04:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 88255 | 7716 | 3466 | 4656 | 299 | 2025-08-11 17:45:34 |
| [django](https://github.com/django/django) | 84549 | 32781 | 0 | 19656 | 356 | 2025-08-11 08:22:59 |
| [flask](https://github.com/pallets/flask) | 70151 | 16517 | 2692 | 2686 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68297 | 32540 | 73225 | 63507 | 9287 | 2025-08-12 02:05:13 |
| [keras](https://github.com/keras-team/keras) | 63300 | 19607 | 12519 | 8270 | 290 | 2025-08-11 22:48:28 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 62967 | 26125 | 11641 | 19163 | 2156 | 2025-08-11 23:24:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 46253 | 18778 | 27642 | 34398 | 3693 | 2025-08-11 20:59:00 |
| [ray](https://github.com/ray-project/ray) | 38422 | 6693 | 20863 | 34302 | 3006 | 2025-08-12 02:01:51 |
| [gym](https://github.com/openai/gym) | 36357 | 8687 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32152 | 4558 | 5715 | 4064 | 196 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30133 | 11187 | 13476 | 15998 | 2330 | 2025-08-12 01:44:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29364 | 6991 | 3945 | 4821 | 98 | 2025-08-10 17:06:47 |
| [celery](https://github.com/celery/celery) | 26983 | 4822 | 5153 | 3633 | 755 | 2025-08-11 16:51:12 |
| [dash](https://github.com/plotly/dash) | 23914 | 2186 | 1971 | 1311 | 546 | 2025-08-11 17:01:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22094 | 5537 | 1851 | 1668 | 206 | 2025-08-11 13:39:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21536 | 7954 | 10934 | 19440 | 1652 | 2025-08-11 21:57:27 |
| [micropython](https://github.com/micropython/micropython) | 20713 | 8349 | 5774 | 7091 | 1765 | 2025-08-11 12:33:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 20392 | 1336 | 1205 | 4819 | 437 | 2025-08-11 21:28:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18464 | 1576 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17582 | 2691 | 3234 | 1938 | 713 | 2025-08-07 21:42:57 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15907 | 2111 | 3141 | 7974 | 260 | 2025-08-11 23:01:44 |
| [httpx](https://github.com/encode/httpx) | 14450 | 937 | 911 | 1704 | 97 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13909 | 5439 | 10964 | 12477 | 1752 | 2025-08-11 12:56:38 |
| [dask](https://github.com/dask/dask) | 13396 | 1791 | 5418 | 6331 | 1186 | 2025-08-04 17:59:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13356 | 2027 | 2621 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11330 | 1028 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11125 | 567 | 387 | 287 | 140 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10759 | 1572 | 8063 | 975 | 235 | 2025-08-11 14:25:32 |
| [falcon](https://github.com/falconry/falcon) | 9700 | 959 | 1092 | 1355 | 161 | 2025-08-09 11:43:51 |
| [bottle](https://github.com/bottlepy/bottle) | 8647 | 1486 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8440 | 517 | 936 | 429 | 404 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6894 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6691 | 361 | 863 | 2440 | 312 | 2025-08-11 22:21:07 |
| [vibora](https://github.com/vibora-io/vibora) | 5636 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5242 | 435 | 1183 | 708 | 492 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4935 | 923 | 861 | 258 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1060 | 2712 | 82 | 2025-02-23 16:39:21 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3515 | 286 | 1150 | 193 | 114 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3391 | 185 | 277 | 120 | 62 | 2025-07-29 15:07:12 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2676 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2296 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2166 | 163 | 399 | 497 | 67 | 2025-08-11 20:17:34 |
| [web2py](https://github.com/web2py/web2py) | 2150 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1920 | 369 | 1779 | 264 | 260 | 2025-08-11 17:55:35 |
| [pypy](https://github.com/pypy/pypy) | 1466 | 83 | 5138 | 166 | 732 | 2025-08-11 19:30:46 |
| [jython](https://github.com/jython/jython) | 1419 | 216 | 278 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-12T02:08:38*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
