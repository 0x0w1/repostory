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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195347 | 75333 | 41474 | 74870 | 3022 | 2026-06-01 05:02:47 |
| [transformers](https://github.com/huggingface/transformers) | 161140 | 33376 | 19017 | 26588 | 2387 | 2026-06-01 04:58:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 100303 | 27899 | 58993 | 126192 | 18331 | 2026-06-01 04:47:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 98731 | 9360 | 3529 | 5840 | 90 | 2026-06-01 04:41:44 |
| [django](https://github.com/django/django) | 87609 | 33986 | 0 | 21333 | 453 | 2026-05-29 15:46:53 |
| [cpython](https://github.com/python/cpython) | 72934 | 34691 | 76554 | 71818 | 9311 | 2026-05-31 20:13:21 |
| [flask](https://github.com/pallets/flask) | 71597 | 16843 | 2738 | 2834 | 3 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66208 | 27044 | 12117 | 20862 | 2033 | 2026-05-31 15:38:21 |
| [keras](https://github.com/keras-team/keras) | 64077 | 19747 | 12771 | 9388 | 180 | 2026-05-29 23:07:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 48885 | 19966 | 28297 | 37377 | 3236 | 2026-05-31 18:37:26 |
| [ray](https://github.com/ray-project/ray) | 42728 | 7621 | 22705 | 40665 | 3469 | 2026-05-31 23:57:58 |
| [gym](https://github.com/openai/gym) | 37206 | 8702 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33622 | 4687 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32119 | 12404 | 13930 | 17536 | 2385 | 2026-05-30 02:36:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30042 | 7065 | 3967 | 5007 | 76 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28539 | 5056 | 5280 | 4126 | 784 | 2026-05-30 08:13:32 |
| [dash](https://github.com/plotly/dash) | 24224 | 2285 | 2103 | 1574 | 549 | 2026-06-01 01:25:29 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22851 | 8349 | 11296 | 20442 | 1487 | 2026-05-30 18:51:37 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5541 | 1872 | 1739 | 218 | 2026-06-01 01:34:16 |
| [RustPython](https://github.com/RustPython/RustPython) | 22088 | 1443 | 1348 | 6577 | 377 | 2026-05-31 15:08:40 |
| [micropython](https://github.com/micropython/micropython) | 21765 | 8846 | 6066 | 7835 | 1711 | 2026-05-29 08:50:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1590 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18570 | 2806 | 3347 | 2089 | 758 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16435 | 2280 | 3209 | 9207 | 234 | 2026-06-01 00:41:46 |
| [httpx](https://github.com/encode/httpx) | 15283 | 1158 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14725 | 5743 | 11456 | 13793 | 1785 | 2026-06-01 01:54:44 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13897 | 2116 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13848 | 1877 | 5533 | 6590 | 1241 | 2026-05-29 17:07:12 |
| [starlette](https://github.com/Kludex/starlette) | 12353 | 1189 | 770 | 1928 | 58 | 2026-05-31 11:24:20 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11872 | 1692 | 8219 | 1097 | 210 | 2026-05-30 14:13:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11803 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 997 | 1126 | 1451 | 159 | 2026-05-29 20:52:08 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9073 | 585 | 1036 | 516 | 213 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1504 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7274 | 397 | 892 | 2548 | 320 | 2026-06-01 05:04:30 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5573 | 485 | 1257 | 843 | 514 | 2026-05-31 15:57:06 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5270 | 1017 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4167 | 336 | 1184 | 223 | 114 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3637 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2474 | 206 | 440 | 643 | 82 | 2026-05-31 08:54:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1529 | 373 | 2026-05-25 20:08:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-05-25 17:51:18 |
| [pypy](https://github.com/pypy/pypy) | 1741 | 113 | 5215 | 254 | 738 | 2026-05-31 10:10:39 |
| [jython](https://github.com/jython/jython) | 1513 | 230 | 296 | 134 | 110 | 2026-05-27 06:12:49 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-01T05:05:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
