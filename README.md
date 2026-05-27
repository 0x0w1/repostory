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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195272 | 75339 | 41472 | 74531 | 5678 | 2026-05-27 04:39:32 |
| [transformers](https://github.com/huggingface/transformers) | 160968 | 33323 | 19002 | 26519 | 2386 | 2026-05-26 20:04:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 100188 | 27890 | 58919 | 125809 | 18256 | 2026-05-27 04:39:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 98521 | 9349 | 3529 | 5806 | 98 | 2026-05-26 08:48:55 |
| [django](https://github.com/django/django) | 87558 | 33959 | 0 | 21299 | 447 | 2026-05-26 18:36:37 |
| [cpython](https://github.com/python/cpython) | 72871 | 34682 | 76512 | 71669 | 9329 | 2026-05-26 21:16:16 |
| [flask](https://github.com/pallets/flask) | 71571 | 16854 | 2739 | 2832 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66180 | 27049 | 12110 | 20844 | 2029 | 2026-05-26 13:08:03 |
| [keras](https://github.com/keras-team/keras) | 64061 | 19776 | 12767 | 9367 | 196 | 2026-05-27 02:47:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 48855 | 19978 | 28295 | 37352 | 3269 | 2026-05-26 18:33:45 |
| [ray](https://github.com/ray-project/ray) | 42660 | 7615 | 22697 | 40573 | 3448 | 2026-05-27 04:12:29 |
| [gym](https://github.com/openai/gym) | 37206 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33612 | 4685 | 5756 | 4093 | 206 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32094 | 12388 | 13928 | 17509 | 2386 | 2026-05-27 01:44:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30031 | 7066 | 3967 | 5006 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28510 | 5050 | 5280 | 4123 | 783 | 2026-05-25 05:31:20 |
| [dash](https://github.com/plotly/dash) | 24216 | 2284 | 2102 | 1570 | 555 | 2026-05-26 22:53:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22840 | 8341 | 11285 | 20408 | 1483 | 2026-05-26 15:05:08 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5541 | 1872 | 1735 | 220 | 2026-05-21 18:10:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 22078 | 1442 | 1347 | 6564 | 381 | 2026-05-26 14:12:55 |
| [micropython](https://github.com/micropython/micropython) | 21743 | 8843 | 6059 | 7827 | 1730 | 2026-05-27 03:22:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1590 | 1466 | 1686 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18556 | 2806 | 3345 | 2088 | 757 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16431 | 2277 | 3205 | 9165 | 246 | 2026-05-27 02:18:39 |
| [httpx](https://github.com/encode/httpx) | 15274 | 1148 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14722 | 5735 | 11450 | 13755 | 1790 | 2026-05-26 20:46:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13890 | 2115 | 2653 | 1183 | 223 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13845 | 1875 | 5529 | 6583 | 1241 | 2026-05-26 22:31:28 |
| [starlette](https://github.com/Kludex/starlette) | 12334 | 1180 | 769 | 1916 | 63 | 2026-05-26 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11863 | 1688 | 8217 | 1093 | 213 | 2026-05-26 19:43:50 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11791 | 607 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 998 | 1125 | 1449 | 158 | 2026-05-21 04:48:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9069 | 580 | 1036 | 514 | 212 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8766 | 1501 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7274 | 397 | 892 | 2547 | 321 | 2026-05-25 21:57:42 |
| [hug](https://github.com/hugapi/hug) | 6887 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5570 | 483 | 1257 | 839 | 512 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5266 | 1015 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4158 | 334 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4085 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3635 | 198 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 664 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2472 | 206 | 439 | 641 | 86 | 2026-05-25 19:39:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1522 | 366 | 2026-05-25 20:08:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-05-25 17:51:18 |
| [pypy](https://github.com/pypy/pypy) | 1742 | 113 | 5214 | 250 | 740 | 2026-05-26 08:31:27 |
| [jython](https://github.com/jython/jython) | 1509 | 230 | 295 | 132 | 108 | 2026-05-26 09:38:18 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-27T04:40:35*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
