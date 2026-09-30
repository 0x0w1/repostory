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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200627 | 77976 | 41817 | 82894 | 3280 | 2026-09-30 05:11:03 |
| [transformers](https://github.com/huggingface/transformers) | 166834 | 34729 | 19538 | 28873 | 2394 | 2026-09-30 02:48:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 103536 | 31008 | 61330 | 137091 | 17585 | 2026-09-30 05:11:38 |
| [fastapi](https://github.com/fastapi/fastapi) | 102719 | 9973 | 3553 | 6369 | 82 | 2026-09-29 22:36:03 |
| [django](https://github.com/django/django) | 91231 | 35912 | 0 | 21972 | 525 | 2026-09-29 19:29:30 |
| [cpython](https://github.com/python/cpython) | 77360 | 37019 | 78348 | 77762 | 9744 | 2026-09-30 03:31:36 |
| [flask](https://github.com/pallets/flask) | 74800 | 17010 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67431 | 27464 | 12303 | 21549 | 2160 | 2026-09-29 16:42:42 |
| [keras](https://github.com/keras-team/keras) | 64346 | 19805 | 12964 | 9959 | 248 | 2026-09-30 04:16:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 49874 | 20448 | 28572 | 39044 | 2477 | 2026-09-30 00:40:08 |
| [ray](https://github.com/ray-project/ray) | 43955 | 8102 | 23113 | 43059 | 3561 | 2026-09-30 04:42:04 |
| [gym](https://github.com/openai/gym) | 37237 | 8672 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33930 | 4731 | 5774 | 4127 | 249 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32884 | 12857 | 14118 | 18616 | 2264 | 2026-09-30 00:21:57 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30195 | 7085 | 3966 | 5074 | 50 | 2026-09-29 19:13:32 |
| [celery](https://github.com/celery/celery) | 28925 | 5189 | 5312 | 4465 | 726 | 2026-09-30 03:26:23 |
| [dash](https://github.com/plotly/dash) | 24446 | 2325 | 2158 | 1736 | 422 | 2026-09-29 16:59:45 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23307 | 8496 | 11430 | 20913 | 1493 | 2026-09-30 03:22:33 |
| [RustPython](https://github.com/RustPython/RustPython) | 22374 | 1489 | 1433 | 7401 | 404 | 2026-09-29 17:16:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5560 | 1884 | 1840 | 249 | 2026-09-25 19:17:31 |
| [micropython](https://github.com/micropython/micropython) | 22108 | 8982 | 6133 | 8111 | 1526 | 2026-09-30 05:06:49 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18817 | 2858 | 3386 | 2205 | 724 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1603 | 1468 | 1679 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16567 | 2436 | 3258 | 10254 | 231 | 2026-09-29 21:14:37 |
| [httpx](https://github.com/encode/httpx) | 15525 | 2656 | 925 | 1805 | 139 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15060 | 5980 | 11671 | 14610 | 1852 | 2026-09-29 11:06:26 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14052 | 2143 | 2663 | 1225 | 237 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13928 | 1970 | 5562 | 6735 | 1345 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12643 | 1346 | 784 | 2158 | 59 | 2026-09-29 07:31:18 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12192 | 1798 | 8311 | 1214 | 211 | 2026-09-29 17:27:17 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11911 | 616 | 422 | 332 | 164 | 2026-09-30 02:54:35 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1037 | 1145 | 1530 | 155 | 2026-09-28 19:57:01 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9202 | 614 | 1047 | 555 | 223 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8795 | 1511 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7342 | 437 | 902 | 2617 | 330 | 2026-09-30 03:18:48 |
| [hug](https://github.com/hugapi/hug) | 6880 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 521 | 1271 | 908 | 523 | 2026-09-27 09:32:15 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5412 | 1042 | 934 | 324 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4423 | 380 | 1202 | 251 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3674 | 208 | 289 | 136 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 675 | 1341 | 311 | 2026-09-30 02:01:55 |
| [anyio](https://github.com/agronholm/anyio) | 2551 | 288 | 484 | 805 | 126 | 2026-09-29 18:41:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1599 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1786 | 276 | 273 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1804 | 127 | 5267 | 316 | 716 | 2026-09-29 20:24:37 |
| [jython](https://github.com/jython/jython) | 1544 | 231 | 303 | 152 | 100 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-30T05:18:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
