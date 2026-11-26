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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201841 | 77373 | 42004 | 85098 | 3408 | 2026-11-26 07:36:33 |
| [transformers](https://github.com/huggingface/transformers) | 169349 | 35305 | 19968 | 30445 | 1162 | 2026-11-26 07:51:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 105771 | 30658 | 63072 | 142905 | 18608 | 2026-11-26 07:57:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 105049 | 10363 | 3556 | 6656 | 48 | 2026-11-24 11:14:37 |
| [django](https://github.com/django/django) | 91916 | 35058 | 0 | 22252 | 539 | 2026-11-25 12:49:52 |
| [cpython](https://github.com/python/cpython) | 78460 | 36522 | 79452 | 80789 | 9380 | 2026-11-26 07:51:45 |
| [flask](https://github.com/pallets/flask) | 75287 | 17302 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68336 | 27696 | 12405 | 21920 | 2164 | 2026-11-26 07:44:16 |
| [keras](https://github.com/keras-team/keras) | 64451 | 19803 | 13120 | 10347 | 271 | 2026-11-26 05:31:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 50644 | 20724 | 28715 | 40185 | 1811 | 2026-11-25 17:15:39 |
| [ray](https://github.com/ray-project/ray) | 44386 | 8309 | 23377 | 44725 | 3892 | 2026-11-26 06:28:17 |
| [gym](https://github.com/openai/gym) | 37237 | 8662 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34095 | 4753 | 5785 | 4155 | 276 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33481 | 13075 | 14224 | 19130 | 2262 | 2026-11-26 01:15:00 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30260 | 7109 | 3966 | 5123 | 58 | 2026-11-25 07:37:05 |
| [celery](https://github.com/celery/celery) | 29270 | 5275 | 5408 | 4764 | 794 | 2026-11-25 15:53:42 |
| [dash](https://github.com/plotly/dash) | 24507 | 2351 | 2192 | 1878 | 421 | 2026-11-25 21:46:25 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23503 | 8584 | 11474 | 21123 | 1464 | 2026-11-26 04:26:23 |
| [RustPython](https://github.com/RustPython/RustPython) | 22509 | 1510 | 1475 | 8451 | 330 | 2026-11-26 07:55:43 |
| [micropython](https://github.com/micropython/micropython) | 22234 | 9080 | 6193 | 8297 | 1611 | 2026-11-26 03:26:54 |
| [tornado](https://github.com/tornadoweb/tornado) | 22171 | 5619 | 1902 | 1974 | 171 | 2026-11-25 20:27:47 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18941 | 2910 | 3409 | 2305 | 737 | 2026-11-25 17:58:41 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1620 | 1475 | 1697 | 168 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16623 | 2545 | 3282 | 10810 | 338 | 2026-11-26 06:55:30 |
| [httpx](https://github.com/encode/httpx) | 15860 | 2007 | 925 | 1832 | 158 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15258 | 6131 | 11798 | 14996 | 1946 | 2026-11-25 23:11:32 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14123 | 2174 | 2669 | 1272 | 269 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13958 | 2036 | 5584 | 6901 | 1455 | 2026-11-25 18:00:25 |
| [starlette](https://github.com/Kludex/starlette) | 12770 | 1461 | 797 | 2306 | 37 | 2026-11-24 10:49:23 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12312 | 1958 | 8411 | 1265 | 219 | 2026-11-24 19:36:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11948 | 624 | 431 | 349 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9823 | 1055 | 1154 | 1585 | 161 | 2026-11-25 07:07:00 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9259 | 624 | 1062 | 623 | 167 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8803 | 1512 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 479 | 911 | 2677 | 343 | 2026-11-24 00:03:10 |
| [hug](https://github.com/hugapi/hug) | 6869 | 391 | 466 | 466 | 190 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5644 | 553 | 1311 | 1000 | 564 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5461 | 1055 | 940 | 337 | 197 | 2026-11-25 09:36:21 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4486 | 397 | 1212 | 259 | 116 | 2026-11-22 15:57:45 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2762 | 80 | 2026-11-25 06:02:52 |
| [databases](https://github.com/encode/databases) | 3983 | 367 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 216 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 683 | 1440 | 257 | 2026-11-25 23:08:01 |
| [anyio](https://github.com/agronholm/anyio) | 2575 | 367 | 507 | 924 | 171 | 2026-11-25 16:36:31 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1086 | 1612 | 356 | 2026-11-23 17:40:38 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-23 18:08:22 |
| [pypy](https://github.com/pypy/pypy) | 1828 | 133 | 5307 | 483 | 723 | 2026-11-26 06:00:03 |
| [jython](https://github.com/jython/jython) | 1549 | 238 | 307 | 166 | 111 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-26T07:58:22*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
