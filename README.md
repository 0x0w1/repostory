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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192688 | 75027 | 41024 | 62618 | 2713 | 2025-12-06 01:55:41 |
| [transformers](https://github.com/huggingface/transformers) | 153509 | 31326 | 18282 | 23785 | 2126 | 2025-12-05 20:05:04 |
| [pytorch](https://github.com/pytorch/pytorch) | 95631 | 26106 | 55684 | 113562 | 17819 | 2025-12-06 02:01:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 92734 | 8329 | 3483 | 4941 | 194 | 2025-12-05 21:27:18 |
| [django](https://github.com/django/django) | 86054 | 33292 | 0 | 20311 | 364 | 2025-12-05 15:30:06 |
| [flask](https://github.com/pallets/flask) | 70880 | 16645 | 2704 | 2729 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70137 | 33588 | 74555 | 66800 | 9221 | 2025-12-05 23:27:16 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64202 | 26483 | 11836 | 19876 | 2113 | 2025-12-05 16:59:36 |
| [keras](https://github.com/keras-team/keras) | 63628 | 19653 | 12601 | 8507 | 265 | 2025-12-05 22:17:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 47264 | 19363 | 27934 | 35288 | 3569 | 2025-12-05 17:43:27 |
| [ray](https://github.com/ray-project/ray) | 40165 | 6977 | 21972 | 36889 | 3195 | 2025-12-06 01:41:59 |
| [gym](https://github.com/openai/gym) | 36843 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32914 | 4636 | 5732 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30954 | 11800 | 13686 | 16636 | 2380 | 2025-12-05 19:26:52 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29710 | 7038 | 3946 | 4879 | 81 | 2025-12-05 12:11:42 |
| [celery](https://github.com/celery/celery) | 27681 | 4908 | 5177 | 3736 | 750 | 2025-12-05 12:28:43 |
| [dash](https://github.com/plotly/dash) | 24316 | 2242 | 2034 | 1386 | 557 | 2025-12-05 17:17:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22381 | 5543 | 1857 | 1677 | 206 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22088 | 8137 | 11064 | 19701 | 1599 | 2025-12-04 21:12:22 |
| [micropython](https://github.com/micropython/micropython) | 21174 | 8570 | 5887 | 7407 | 1789 | 2025-12-03 14:00:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 20874 | 1365 | 1240 | 5028 | 442 | 2025-12-06 01:02:46 |
| [sanic](https://github.com/sanic-org/sanic) | 18592 | 1585 | 1454 | 1635 | 128 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18050 | 2756 | 3302 | 1988 | 751 | 2025-12-05 23:04:44 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16132 | 2163 | 3164 | 8341 | 271 | 2025-12-05 16:11:50 |
| [httpx](https://github.com/encode/httpx) | 14814 | 983 | 923 | 1759 | 117 | 2025-12-01 17:39:25 |
| [scipy](https://github.com/scipy/scipy) | 14245 | 5553 | 11171 | 12919 | 1762 | 2025-12-05 23:57:06 |
| [dask](https://github.com/dask/dask) | 13640 | 1825 | 5472 | 6412 | 1199 | 2025-12-05 11:49:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13600 | 2058 | 2637 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11732 | 1087 | 760 | 1746 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11494 | 588 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11222 | 1604 | 8128 | 1009 | 213 | 2025-12-05 22:47:12 |
| [falcon](https://github.com/falconry/falcon) | 9768 | 971 | 1114 | 1403 | 164 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8757 | 545 | 980 | 464 | 180 | 2025-12-04 11:35:16 |
| [bottle](https://github.com/bottlepy/bottle) | 8708 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7043 | 370 | 876 | 2478 | 313 | 2025-12-06 01:51:15 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 744 | 979 | 581 | 35 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5404 | 445 | 1203 | 725 | 511 | 2025-11-27 05:19:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5106 | 971 | 879 | 264 | 174 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 887 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3803 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3555 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2715 | 305 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2330 | 135 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2316 | 179 | 418 | 554 | 72 | 2025-12-01 20:04:08 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-01 17:53:21 |
| [pypy](https://github.com/pypy/pypy) | 1591 | 90 | 5165 | 172 | 749 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-06T02:01:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
