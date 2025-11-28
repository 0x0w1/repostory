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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192591 | 75002 | 41032 | 62140 | 2587 | 2025-11-28 00:11:34 |
| [transformers](https://github.com/huggingface/transformers) | 153116 | 31245 | 18239 | 23625 | 2123 | 2025-11-27 20:25:39 |
| [pytorch](https://github.com/pytorch/pytorch) | 95424 | 26032 | 55582 | 113123 | 17784 | 2025-11-28 02:00:46 |
| [fastapi](https://github.com/fastapi/fastapi) | 92428 | 8289 | 3477 | 4909 | 228 | 2025-11-24 19:17:19 |
| [django](https://github.com/django/django) | 85957 | 33269 | 0 | 20270 | 361 | 2025-11-27 16:15:31 |
| [flask](https://github.com/pallets/flask) | 70845 | 16634 | 2704 | 2725 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 70032 | 33521 | 74471 | 66585 | 9198 | 2025-11-27 22:22:21 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64150 | 26476 | 11828 | 19844 | 2109 | 2025-11-27 16:02:35 |
| [keras](https://github.com/keras-team/keras) | 63610 | 19654 | 12596 | 8486 | 265 | 2025-11-27 15:12:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 47203 | 19345 | 27911 | 35255 | 3609 | 2025-11-27 10:22:38 |
| [ray](https://github.com/ray-project/ray) | 40040 | 6952 | 21939 | 36764 | 3259 | 2025-11-28 01:30:24 |
| [gym](https://github.com/openai/gym) | 36823 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32878 | 4634 | 5732 | 4074 | 182 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30916 | 11762 | 13672 | 16582 | 2366 | 2025-11-27 16:26:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29698 | 7042 | 3946 | 4876 | 95 | 2025-11-25 11:07:20 |
| [celery](https://github.com/celery/celery) | 27629 | 4907 | 5176 | 3730 | 753 | 2025-11-24 16:54:38 |
| [dash](https://github.com/plotly/dash) | 24281 | 2237 | 2030 | 1381 | 568 | 2025-11-27 17:51:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22373 | 5545 | 1855 | 1677 | 206 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22063 | 8132 | 11057 | 19691 | 1608 | 2025-11-27 17:15:50 |
| [micropython](https://github.com/micropython/micropython) | 21145 | 8548 | 5884 | 7384 | 1793 | 2025-11-27 07:49:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 20844 | 1361 | 1238 | 4998 | 445 | 2025-11-27 23:41:22 |
| [sanic](https://github.com/sanic-org/sanic) | 18590 | 1585 | 1453 | 1630 | 151 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18024 | 2748 | 3301 | 1985 | 751 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16114 | 2157 | 3163 | 8309 | 288 | 2025-11-24 16:26:04 |
| [httpx](https://github.com/encode/httpx) | 14794 | 980 | 923 | 1756 | 114 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14219 | 5551 | 11159 | 12898 | 1778 | 2025-11-27 20:42:17 |
| [dask](https://github.com/dask/dask) | 13627 | 1827 | 5469 | 6408 | 1197 | 2025-11-25 14:34:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13590 | 2052 | 2636 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11698 | 1086 | 760 | 1745 | 52 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11462 | 586 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11182 | 1601 | 8123 | 1006 | 214 | 2025-11-27 17:26:40 |
| [falcon](https://github.com/falconry/falcon) | 9769 | 972 | 1113 | 1403 | 163 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8735 | 539 | 976 | 454 | 179 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8701 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7030 | 372 | 875 | 2472 | 312 | 2025-11-26 14:29:48 |
| [hug](https://github.com/hugapi/hug) | 6913 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 746 | 979 | 577 | 33 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5625 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5393 | 446 | 1200 | 719 | 503 | 2025-11-27 05:19:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5100 | 971 | 877 | 263 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4066 | 887 | 1062 | 2722 | 90 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4038 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3781 | 302 | 1168 | 202 | 116 | 2025-11-20 22:26:20 |
| [quart](https://github.com/pallets/quart) | 3550 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2719 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2330 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2304 | 177 | 416 | 551 | 74 | 2025-11-25 00:03:59 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 372 | 1784 | 266 | 265 | 2025-11-24 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1578 | 90 | 5164 | 172 | 748 | 2025-11-24 21:06:55 |
| [jython](https://github.com/jython/jython) | 1460 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-28T02:03:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
