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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191191 | 74768 | 40723 | 56259 | 1528 | 2025-08-16 01:29:23 |
| [transformers](https://github.com/huggingface/transformers) | 148379 | 30038 | 17774 | 21864 | 1968 | 2025-08-15 21:16:55 |
| [pytorch](https://github.com/pytorch/pytorch) | 92400 | 24965 | 53128 | 107221 | 16806 | 2025-08-16 02:02:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 88418 | 7731 | 3466 | 4660 | 288 | 2025-08-15 22:01:22 |
| [django](https://github.com/django/django) | 84586 | 32827 | 0 | 19667 | 355 | 2025-08-15 08:45:02 |
| [flask](https://github.com/pallets/flask) | 70179 | 16522 | 2692 | 2686 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68382 | 32594 | 73289 | 63621 | 9290 | 2025-08-15 21:19:23 |
| [keras](https://github.com/keras-team/keras) | 63333 | 19613 | 12524 | 8282 | 301 | 2025-08-14 20:13:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63032 | 26138 | 11645 | 19185 | 2161 | 2025-08-14 08:52:01 |
| [pandas](https://github.com/pandas-dev/pandas) | 46309 | 18815 | 27654 | 34425 | 3693 | 2025-08-15 18:59:11 |
| [ray](https://github.com/ray-project/ray) | 38489 | 6708 | 20892 | 34435 | 2987 | 2025-08-16 01:55:54 |
| [gym](https://github.com/openai/gym) | 36383 | 8685 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32183 | 4563 | 5716 | 4064 | 197 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30156 | 11202 | 13487 | 16016 | 2343 | 2025-08-14 22:07:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29372 | 6995 | 3945 | 4826 | 98 | 2025-08-15 11:28:26 |
| [celery](https://github.com/celery/celery) | 27007 | 4825 | 5156 | 3639 | 760 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23937 | 2188 | 1974 | 1312 | 548 | 2025-08-15 19:59:33 |
| [tornado](https://github.com/tornadoweb/tornado) | 22100 | 5537 | 1851 | 1670 | 206 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21557 | 7957 | 10941 | 19451 | 1654 | 2025-08-15 22:25:29 |
| [micropython](https://github.com/micropython/micropython) | 20728 | 8363 | 5782 | 7112 | 1772 | 2025-08-15 02:46:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 20408 | 1339 | 1207 | 4824 | 444 | 2025-08-11 21:28:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18469 | 1578 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17601 | 2699 | 3240 | 1944 | 720 | 2025-08-14 15:14:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15915 | 2111 | 3142 | 7994 | 262 | 2025-08-15 10:57:27 |
| [httpx](https://github.com/encode/httpx) | 14463 | 942 | 913 | 1707 | 101 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13919 | 5441 | 10970 | 12484 | 1758 | 2025-08-15 19:12:15 |
| [dask](https://github.com/dask/dask) | 13409 | 1791 | 5422 | 6333 | 1191 | 2025-08-12 06:36:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13366 | 2028 | 2622 | 1147 | 186 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11349 | 1028 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11140 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10780 | 1573 | 8066 | 975 | 237 | 2025-08-14 14:48:11 |
| [falcon](https://github.com/falconry/falcon) | 9703 | 959 | 1093 | 1359 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8646 | 1487 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8452 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6893 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6698 | 362 | 863 | 2441 | 312 | 2025-08-12 16:35:03 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5245 | 435 | 1183 | 708 | 492 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4941 | 925 | 861 | 258 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4040 | 891 | 1060 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3935 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3524 | 288 | 1152 | 194 | 116 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3395 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2675 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2296 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2174 | 163 | 399 | 498 | 68 | 2025-08-13 13:44:30 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1779 | 264 | 260 | 2025-08-11 17:55:35 |
| [pypy](https://github.com/pypy/pypy) | 1470 | 83 | 5139 | 168 | 733 | 2025-08-14 05:35:41 |
| [jython](https://github.com/jython/jython) | 1420 | 216 | 279 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-16T02:05:40*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
