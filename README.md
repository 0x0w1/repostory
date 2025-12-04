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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192667 | 75023 | 41009 | 62470 | 2714 | 2025-12-04 02:04:38 |
| [transformers](https://github.com/huggingface/transformers) | 153392 | 31309 | 18268 | 23731 | 2121 | 2025-12-03 20:21:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 95575 | 26089 | 55647 | 113392 | 17824 | 2025-12-04 02:04:18 |
| [fastapi](https://github.com/fastapi/fastapi) | 92603 | 8312 | 3479 | 4933 | 194 | 2025-12-04 01:54:43 |
| [django](https://github.com/django/django) | 86027 | 33283 | 0 | 20304 | 366 | 2025-12-03 21:04:22 |
| [flask](https://github.com/pallets/flask) | 70872 | 16647 | 2704 | 2729 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70111 | 33576 | 74530 | 66741 | 9213 | 2025-12-04 00:16:37 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64179 | 26480 | 11832 | 19866 | 2111 | 2025-12-02 15:14:53 |
| [keras](https://github.com/keras-team/keras) | 63624 | 19654 | 12600 | 8499 | 269 | 2025-12-04 01:44:02 |
| [pandas](https://github.com/pandas-dev/pandas) | 47247 | 19357 | 27923 | 35277 | 3586 | 2025-12-03 16:20:43 |
| [ray](https://github.com/ray-project/ray) | 40120 | 6971 | 21967 | 36846 | 3209 | 2025-12-04 01:34:04 |
| [gym](https://github.com/openai/gym) | 36837 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32904 | 4633 | 5732 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30943 | 11791 | 13683 | 16622 | 2378 | 2025-12-03 21:35:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29706 | 7037 | 3946 | 4876 | 86 | 2025-12-03 10:22:25 |
| [celery](https://github.com/celery/celery) | 27669 | 4904 | 5177 | 3734 | 753 | 2025-12-03 10:17:40 |
| [dash](https://github.com/plotly/dash) | 24306 | 2241 | 2033 | 1384 | 558 | 2025-12-03 23:45:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22378 | 5544 | 1858 | 1677 | 206 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22082 | 8136 | 11063 | 19697 | 1601 | 2025-12-01 21:41:58 |
| [micropython](https://github.com/micropython/micropython) | 21164 | 8565 | 5887 | 7403 | 1785 | 2025-12-03 14:00:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 20869 | 1365 | 1240 | 5022 | 447 | 2025-12-04 00:17:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18590 | 1584 | 1454 | 1635 | 130 | 2025-12-03 21:06:21 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18043 | 2756 | 3302 | 1987 | 752 | 2025-12-03 18:15:47 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16126 | 2164 | 3164 | 8337 | 275 | 2025-12-03 20:56:27 |
| [httpx](https://github.com/encode/httpx) | 14815 | 983 | 923 | 1758 | 116 | 2025-12-01 17:39:25 |
| [scipy](https://github.com/scipy/scipy) | 14240 | 5554 | 11169 | 12912 | 1767 | 2025-12-03 11:19:26 |
| [dask](https://github.com/dask/dask) | 13636 | 1825 | 5471 | 6410 | 1201 | 2025-11-25 14:34:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13598 | 2058 | 2637 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11723 | 1087 | 760 | 1746 | 53 | 2025-12-01 21:33:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11485 | 587 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11213 | 1604 | 8128 | 1008 | 213 | 2025-12-03 19:17:32 |
| [falcon](https://github.com/falconry/falcon) | 9766 | 971 | 1114 | 1403 | 164 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8755 | 542 | 979 | 459 | 178 | 2025-12-03 19:26:24 |
| [bottle](https://github.com/bottlepy/bottle) | 8706 | 1488 | 856 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7038 | 372 | 876 | 2475 | 313 | 2025-12-02 21:01:29 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 744 | 979 | 580 | 34 | 2025-12-02 15:18:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5400 | 445 | 1201 | 724 | 509 | 2025-11-27 05:19:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5105 | 971 | 879 | 264 | 175 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 886 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3795 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3555 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2716 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2330 | 135 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2314 | 179 | 418 | 554 | 72 | 2025-12-01 20:04:08 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-01 17:53:21 |
| [pypy](https://github.com/pypy/pypy) | 1587 | 90 | 5165 | 172 | 749 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1461 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-04T02:08:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
