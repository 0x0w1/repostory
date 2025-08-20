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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191240 | 74788 | 40730 | 56381 | 1520 | 2025-08-20 01:48:04 |
| [transformers](https://github.com/huggingface/transformers) | 148526 | 30092 | 17803 | 21923 | 1963 | 2025-08-19 20:10:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 92515 | 25021 | 53199 | 107372 | 16832 | 2025-08-20 01:56:09 |
| [fastapi](https://github.com/fastapi/fastapi) | 88557 | 7747 | 3466 | 4663 | 283 | 2025-08-19 14:28:48 |
| [django](https://github.com/django/django) | 84628 | 32833 | 0 | 19687 | 364 | 2025-08-19 15:44:07 |
| [flask](https://github.com/pallets/flask) | 70198 | 16523 | 2692 | 2688 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68446 | 32634 | 73333 | 63710 | 9294 | 2025-08-19 21:31:00 |
| [keras](https://github.com/keras-team/keras) | 63350 | 19613 | 12526 | 8287 | 297 | 2025-08-19 22:21:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63073 | 26160 | 11650 | 19198 | 2161 | 2025-08-19 12:27:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 46340 | 18832 | 27661 | 34439 | 3702 | 2025-08-19 18:12:59 |
| [ray](https://github.com/ray-project/ray) | 38549 | 6725 | 20907 | 34508 | 2989 | 2025-08-20 01:58:02 |
| [gym](https://github.com/openai/gym) | 36405 | 8687 | 1838 | 1464 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32206 | 4564 | 5716 | 4064 | 197 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30185 | 11227 | 13492 | 16036 | 2344 | 2025-08-19 18:29:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29386 | 6993 | 3945 | 4827 | 98 | 2025-08-16 07:10:06 |
| [celery](https://github.com/celery/celery) | 27039 | 4828 | 5156 | 3639 | 760 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23959 | 2190 | 1976 | 1313 | 551 | 2025-08-19 23:35:06 |
| [tornado](https://github.com/tornadoweb/tornado) | 22104 | 5539 | 1851 | 1669 | 206 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21573 | 7964 | 10946 | 19459 | 1655 | 2025-08-19 16:45:19 |
| [micropython](https://github.com/micropython/micropython) | 20740 | 8370 | 5787 | 7122 | 1767 | 2025-08-19 12:06:34 |
| [RustPython](https://github.com/RustPython/RustPython) | 20420 | 1342 | 1208 | 4828 | 449 | 2025-08-18 09:15:45 |
| [sanic](https://github.com/sanic-org/sanic) | 18474 | 1578 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17620 | 2701 | 3241 | 1944 | 721 | 2025-08-19 14:08:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15925 | 2113 | 3143 | 8001 | 265 | 2025-08-19 18:34:46 |
| [httpx](https://github.com/encode/httpx) | 14477 | 945 | 914 | 1708 | 103 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13932 | 5447 | 10975 | 12491 | 1761 | 2025-08-18 22:57:00 |
| [dask](https://github.com/dask/dask) | 13418 | 1792 | 5423 | 6333 | 1190 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13373 | 2028 | 2623 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11362 | 1031 | 750 | 1680 | 48 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11152 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10792 | 1575 | 8068 | 977 | 237 | 2025-08-19 17:26:41 |
| [falcon](https://github.com/falconry/falcon) | 9704 | 959 | 1093 | 1359 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8649 | 1488 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8455 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6727 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6712 | 362 | 863 | 2442 | 312 | 2025-08-18 22:06:52 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5249 | 435 | 1184 | 710 | 495 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4947 | 925 | 863 | 257 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1060 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3934 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3532 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3402 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2676 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2178 | 163 | 399 | 499 | 68 | 2025-08-18 17:55:01 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 906 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-18 17:39:32 |
| [pypy](https://github.com/pypy/pypy) | 1474 | 83 | 5140 | 168 | 734 | 2025-08-19 15:10:36 |
| [jython](https://github.com/jython/jython) | 1425 | 217 | 280 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-20T02:02:13*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
