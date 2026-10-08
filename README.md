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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200735 | 78562 | 41844 | 83180 | 3275 | 2026-10-08 05:37:01 |
| [transformers](https://github.com/huggingface/transformers) | 167045 | 34766 | 19581 | 29034 | 2357 | 2026-10-08 03:11:12 |
| [pytorch](https://github.com/pytorch/pytorch) | 103869 | 31610 | 61561 | 137996 | 17720 | 2026-10-08 05:44:26 |
| [fastapi](https://github.com/fastapi/fastapi) | 102868 | 10003 | 3556 | 6417 | 87 | 2026-10-07 21:21:56 |
| [django](https://github.com/django/django) | 91354 | 36478 | 0 | 22019 | 533 | 2026-10-07 16:48:53 |
| [cpython](https://github.com/python/cpython) | 77555 | 37548 | 78579 | 78059 | 9837 | 2026-10-08 01:26:20 |
| [flask](https://github.com/pallets/flask) | 74933 | 17060 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67491 | 27486 | 12314 | 21589 | 2157 | 2026-10-07 15:49:47 |
| [keras](https://github.com/keras-team/keras) | 64351 | 19804 | 12984 | 10014 | 240 | 2026-10-08 04:08:03 |
| [pandas](https://github.com/pandas-dev/pandas) | 49928 | 20473 | 28587 | 39264 | 2374 | 2026-10-07 21:56:35 |
| [ray](https://github.com/ray-project/ray) | 43982 | 8123 | 23129 | 43269 | 3561 | 2026-10-08 03:19:53 |
| [gym](https://github.com/openai/gym) | 37245 | 8670 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33949 | 4731 | 5774 | 4129 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33047 | 12896 | 14124 | 18722 | 2252 | 2026-10-07 23:54:54 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30199 | 7092 | 3966 | 5087 | 55 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28935 | 5207 | 5328 | 4527 | 729 | 2026-10-08 02:49:52 |
| [dash](https://github.com/plotly/dash) | 24443 | 2329 | 2166 | 1760 | 439 | 2026-10-07 18:04:36 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23336 | 8503 | 11432 | 20948 | 1490 | 2026-10-08 03:27:45 |
| [RustPython](https://github.com/RustPython/RustPython) | 22383 | 1497 | 1437 | 7464 | 289 | 2026-10-08 05:01:52 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5566 | 1885 | 1869 | 213 | 2026-10-07 21:34:52 |
| [micropython](https://github.com/micropython/micropython) | 22110 | 8991 | 6135 | 8121 | 1535 | 2026-10-03 07:13:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18827 | 2862 | 3387 | 2214 | 727 | 2026-10-08 00:59:00 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1608 | 1470 | 1684 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16568 | 2441 | 3262 | 10370 | 217 | 2026-10-07 11:41:48 |
| [httpx](https://github.com/encode/httpx) | 15531 | 3203 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15090 | 5998 | 11680 | 14652 | 1858 | 2026-10-07 14:32:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14060 | 2143 | 2663 | 1229 | 239 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13932 | 1972 | 5563 | 6746 | 1352 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12655 | 1363 | 786 | 2195 | 56 | 2026-10-06 20:18:56 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12206 | 1805 | 8334 | 1221 | 212 | 2026-10-07 17:33:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11909 | 615 | 425 | 337 | 166 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1036 | 1146 | 1533 | 158 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9204 | 614 | 1048 | 558 | 223 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1514 | 867 | 651 | 289 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7347 | 444 | 902 | 2628 | 332 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5632 | 520 | 1271 | 918 | 525 | 2026-10-07 04:44:53 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5414 | 1046 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4435 | 382 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 892 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3986 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3669 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 676 | 1355 | 290 | 2026-10-08 01:04:56 |
| [anyio](https://github.com/agronholm/anyio) | 2553 | 299 | 488 | 830 | 139 | 2026-10-06 20:50:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 356 | 2026-10-07 13:20:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1810 | 128 | 5275 | 331 | 724 | 2026-10-07 20:43:48 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 116 | 77 | 2026-10-05 17:39:10 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-08T05:46:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
