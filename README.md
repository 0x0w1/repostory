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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191201 | 74770 | 40725 | 56283 | 1535 | 2025-08-17 02:20:12 |
| [transformers](https://github.com/huggingface/transformers) | 148414 | 30056 | 17778 | 21871 | 1977 | 2025-08-16 21:21:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 92431 | 24974 | 53139 | 107237 | 16804 | 2025-08-17 02:21:01 |
| [fastapi](https://github.com/fastapi/fastapi) | 88447 | 7733 | 3466 | 4661 | 286 | 2025-08-15 22:01:22 |
| [django](https://github.com/django/django) | 84591 | 32827 | 0 | 19670 | 358 | 2025-08-15 08:45:02 |
| [flask](https://github.com/pallets/flask) | 70180 | 16522 | 2692 | 2686 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68395 | 32605 | 73300 | 63642 | 9297 | 2025-08-16 17:24:17 |
| [keras](https://github.com/keras-team/keras) | 63336 | 19612 | 12525 | 8282 | 297 | 2025-08-17 00:55:37 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63041 | 26140 | 11646 | 19187 | 2160 | 2025-08-16 14:39:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 46315 | 18820 | 27654 | 34429 | 3694 | 2025-08-15 18:59:11 |
| [ray](https://github.com/ray-project/ray) | 38495 | 6710 | 20896 | 34443 | 2990 | 2025-08-17 00:59:13 |
| [gym](https://github.com/openai/gym) | 36388 | 8685 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32186 | 4563 | 5716 | 4064 | 197 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30163 | 11208 | 13488 | 16019 | 2344 | 2025-08-16 12:20:52 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29376 | 6994 | 3945 | 4826 | 97 | 2025-08-16 07:10:06 |
| [celery](https://github.com/celery/celery) | 27014 | 4825 | 5156 | 3639 | 760 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23940 | 2188 | 1974 | 1312 | 548 | 2025-08-15 19:59:33 |
| [tornado](https://github.com/tornadoweb/tornado) | 22100 | 5538 | 1851 | 1670 | 206 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21560 | 7957 | 10945 | 19453 | 1656 | 2025-08-15 22:25:29 |
| [micropython](https://github.com/micropython/micropython) | 20729 | 8366 | 5783 | 7114 | 1772 | 2025-08-16 09:37:06 |
| [RustPython](https://github.com/RustPython/RustPython) | 20411 | 1339 | 1208 | 4824 | 445 | 2025-08-11 21:28:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18469 | 1578 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17601 | 2699 | 3240 | 1944 | 720 | 2025-08-14 15:14:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15918 | 2112 | 3142 | 7994 | 262 | 2025-08-15 10:57:27 |
| [httpx](https://github.com/encode/httpx) | 14464 | 943 | 913 | 1708 | 102 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13922 | 5441 | 10972 | 12486 | 1759 | 2025-08-17 00:58:02 |
| [dask](https://github.com/dask/dask) | 13415 | 1791 | 5422 | 6333 | 1191 | 2025-08-12 06:36:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13368 | 2028 | 2622 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11350 | 1028 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11141 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10784 | 1573 | 8066 | 975 | 236 | 2025-08-16 14:05:26 |
| [falcon](https://github.com/falconry/falcon) | 9703 | 959 | 1093 | 1359 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8647 | 1487 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8452 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6893 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6700 | 362 | 863 | 2441 | 312 | 2025-08-12 16:35:03 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5246 | 435 | 1184 | 708 | 493 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4940 | 925 | 861 | 258 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4040 | 891 | 1060 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3935 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3525 | 288 | 1152 | 194 | 116 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3397 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2675 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2297 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2175 | 163 | 399 | 498 | 68 | 2025-08-13 13:44:30 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 906 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1779 | 264 | 260 | 2025-08-11 17:55:35 |
| [pypy](https://github.com/pypy/pypy) | 1472 | 83 | 5139 | 168 | 733 | 2025-08-14 05:35:41 |
| [jython](https://github.com/jython/jython) | 1421 | 216 | 279 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-17T02:23:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
