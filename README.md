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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192833 | 75107 | 41038 | 63240 | 2885 | 2025-12-17 02:04:45 |
| [transformers](https://github.com/huggingface/transformers) | 153937 | 31447 | 18339 | 23972 | 2154 | 2025-12-17 00:21:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 95959 | 26252 | 55891 | 114246 | 17892 | 2025-12-17 02:04:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 93132 | 8377 | 3499 | 4998 | 193 | 2025-12-16 23:56:11 |
| [django](https://github.com/django/django) | 86175 | 33388 | 0 | 20351 | 367 | 2025-12-16 22:47:36 |
| [flask](https://github.com/pallets/flask) | 70928 | 16656 | 2706 | 2732 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70341 | 33691 | 74706 | 67167 | 9236 | 2025-12-17 00:12:32 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64304 | 26506 | 11850 | 19926 | 2126 | 2025-12-16 09:55:35 |
| [keras](https://github.com/keras-team/keras) | 63644 | 19652 | 12605 | 8532 | 246 | 2025-12-17 01:40:35 |
| [pandas](https://github.com/pandas-dev/pandas) | 47328 | 19408 | 27959 | 35369 | 3598 | 2025-12-16 21:10:53 |
| [ray](https://github.com/ray-project/ray) | 40359 | 7012 | 22021 | 37119 | 3189 | 2025-12-17 01:24:23 |
| [gym](https://github.com/openai/gym) | 36869 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32955 | 4634 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31026 | 11849 | 13699 | 16688 | 2391 | 2025-12-16 20:27:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29743 | 7041 | 3946 | 4887 | 78 | 2025-12-15 16:01:56 |
| [celery](https://github.com/celery/celery) | 27721 | 4915 | 5179 | 3744 | 752 | 2025-12-16 15:05:43 |
| [dash](https://github.com/plotly/dash) | 24344 | 2247 | 2035 | 1394 | 561 | 2025-12-17 00:04:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22387 | 5543 | 1861 | 1690 | 210 | 2025-12-16 22:45:34 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22126 | 8146 | 11079 | 19747 | 1567 | 2025-12-16 23:47:13 |
| [micropython](https://github.com/micropython/micropython) | 21220 | 8592 | 5898 | 7441 | 1809 | 2025-12-16 13:16:45 |
| [RustPython](https://github.com/RustPython/RustPython) | 20917 | 1369 | 1247 | 5141 | 439 | 2025-12-16 23:15:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18599 | 1585 | 1455 | 1635 | 129 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18095 | 2761 | 3307 | 1992 | 755 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16149 | 2167 | 3167 | 8384 | 275 | 2025-12-16 10:51:09 |
| [httpx](https://github.com/encode/httpx) | 14846 | 993 | 924 | 1767 | 117 | 2025-12-10 15:17:09 |
| [scipy](https://github.com/scipy/scipy) | 14261 | 5556 | 11190 | 12965 | 1768 | 2025-12-17 00:32:32 |
| [dask](https://github.com/dask/dask) | 13653 | 1827 | 5478 | 6425 | 1204 | 2025-12-16 21:06:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13622 | 2067 | 2641 | 1150 | 200 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11761 | 1091 | 760 | 1748 | 53 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11524 | 590 | 397 | 298 | 148 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11274 | 1607 | 8128 | 1012 | 205 | 2025-12-16 20:12:56 |
| [falcon](https://github.com/falconry/falcon) | 9769 | 974 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8781 | 550 | 984 | 474 | 191 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8713 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7053 | 373 | 877 | 2482 | 314 | 2025-12-15 22:18:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 741 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5622 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5416 | 445 | 1208 | 730 | 510 | 2025-12-16 09:05:24 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5114 | 971 | 882 | 269 | 173 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3819 | 302 | 1169 | 203 | 118 | 2025-12-16 17:47:34 |
| [quart](https://github.com/pallets/quart) | 3562 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2719 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2325 | 180 | 420 | 558 | 75 | 2025-12-16 12:21:58 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-15 17:49:12 |
| [pypy](https://github.com/pypy/pypy) | 1606 | 91 | 5167 | 172 | 752 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1463 | 225 | 288 | 118 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-17T02:07:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
