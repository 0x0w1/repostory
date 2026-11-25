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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201775 | 77373 | 41991 | 85072 | 3530 | 2026-11-25 07:56:14 |
| [transformers](https://github.com/huggingface/transformers) | 169297 | 35290 | 19961 | 30386 | 1154 | 2026-11-25 08:08:44 |
| [pytorch](https://github.com/pytorch/pytorch) | 105715 | 30663 | 63054 | 142779 | 18593 | 2026-11-25 08:04:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 104992 | 10359 | 3556 | 6652 | 47 | 2026-11-24 11:14:37 |
| [django](https://github.com/django/django) | 91868 | 35062 | 0 | 22248 | 539 | 2026-11-23 18:39:57 |
| [cpython](https://github.com/python/cpython) | 78397 | 36522 | 79432 | 80751 | 9384 | 2026-11-25 05:06:47 |
| [flask](https://github.com/pallets/flask) | 75228 | 17297 | 2782 | 2911 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68322 | 27689 | 12404 | 21905 | 2156 | 2026-11-25 00:04:26 |
| [keras](https://github.com/keras-team/keras) | 64450 | 19803 | 13120 | 10339 | 273 | 2026-11-25 02:00:40 |
| [pandas](https://github.com/pandas-dev/pandas) | 50627 | 20718 | 28713 | 40174 | 1804 | 2026-11-24 20:15:36 |
| [ray](https://github.com/ray-project/ray) | 44377 | 8305 | 23373 | 44687 | 3866 | 2026-11-25 06:57:39 |
| [gym](https://github.com/openai/gym) | 37235 | 8662 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34094 | 4751 | 5785 | 4155 | 276 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33471 | 13066 | 14217 | 19119 | 2260 | 2026-11-25 03:18:47 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30256 | 7108 | 3966 | 5123 | 58 | 2026-11-25 07:37:05 |
| [celery](https://github.com/celery/celery) | 29264 | 5275 | 5408 | 4764 | 798 | 2026-11-25 03:21:32 |
| [dash](https://github.com/plotly/dash) | 24506 | 2348 | 2190 | 1867 | 445 | 2026-11-24 20:38:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23502 | 8579 | 11474 | 21116 | 1467 | 2026-11-25 06:23:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 22505 | 1509 | 1475 | 8440 | 328 | 2026-11-25 01:07:02 |
| [micropython](https://github.com/micropython/micropython) | 22231 | 9078 | 6192 | 8290 | 1606 | 2026-11-24 23:33:04 |
| [tornado](https://github.com/tornadoweb/tornado) | 22171 | 5618 | 1902 | 1967 | 171 | 2026-11-25 03:21:28 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18933 | 2910 | 3409 | 2304 | 738 | 2026-11-24 20:02:00 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1619 | 1475 | 1696 | 167 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16622 | 2543 | 3282 | 10797 | 344 | 2026-11-25 06:01:22 |
| [httpx](https://github.com/encode/httpx) | 15852 | 2009 | 925 | 1832 | 158 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15255 | 6128 | 11796 | 14989 | 1950 | 2026-11-24 18:05:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14123 | 2173 | 2669 | 1271 | 268 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13958 | 2035 | 5584 | 6897 | 1459 | 2026-11-24 23:36:38 |
| [starlette](https://github.com/Kludex/starlette) | 12766 | 1460 | 797 | 2306 | 37 | 2026-11-24 10:49:23 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12308 | 1958 | 8411 | 1264 | 219 | 2026-11-24 19:36:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11948 | 624 | 431 | 349 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9820 | 1055 | 1154 | 1585 | 161 | 2026-11-25 07:07:00 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9258 | 624 | 1062 | 623 | 167 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8804 | 1513 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 479 | 911 | 2677 | 343 | 2026-11-24 00:03:10 |
| [hug](https://github.com/hugapi/hug) | 6868 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 551 | 1311 | 998 | 562 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5461 | 1055 | 939 | 337 | 197 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4486 | 397 | 1212 | 259 | 116 | 2026-11-22 15:57:45 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2762 | 80 | 2026-11-25 06:02:52 |
| [databases](https://github.com/encode/databases) | 3984 | 366 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 215 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 683 | 1439 | 257 | 2026-11-25 02:55:37 |
| [anyio](https://github.com/agronholm/anyio) | 2575 | 363 | 507 | 919 | 169 | 2026-11-24 00:06:17 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1612 | 355 | 2026-11-23 17:40:38 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-23 18:08:22 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 134 | 5306 | 480 | 724 | 2026-11-24 20:59:06 |
| [jython](https://github.com/jython/jython) | 1549 | 238 | 307 | 166 | 111 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-25T08:09:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
