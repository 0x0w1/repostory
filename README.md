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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200601 | 77890 | 41815 | 82833 | 3353 | 2026-09-29 05:17:36 |
| [transformers](https://github.com/huggingface/transformers) | 166783 | 34709 | 19530 | 28853 | 2396 | 2026-09-29 04:49:07 |
| [pytorch](https://github.com/pytorch/pytorch) | 103483 | 30892 | 61299 | 136994 | 17602 | 2026-09-29 05:27:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 102708 | 9966 | 3553 | 6362 | 83 | 2026-09-28 19:48:59 |
| [django](https://github.com/django/django) | 91228 | 35815 | 0 | 21963 | 524 | 2026-09-28 15:21:59 |
| [cpython](https://github.com/python/cpython) | 77337 | 36902 | 78328 | 77684 | 9760 | 2026-09-29 04:32:37 |
| [flask](https://github.com/pallets/flask) | 74801 | 17010 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67416 | 27460 | 12299 | 21548 | 2159 | 2026-09-24 17:11:32 |
| [keras](https://github.com/keras-team/keras) | 64342 | 19805 | 12959 | 9947 | 267 | 2026-09-29 00:21:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 49861 | 20447 | 28568 | 39038 | 2508 | 2026-09-29 04:05:42 |
| [ray](https://github.com/ray-project/ray) | 43939 | 8093 | 23111 | 43035 | 3564 | 2026-09-29 04:49:15 |
| [gym](https://github.com/openai/gym) | 37238 | 8672 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33928 | 4729 | 5774 | 4127 | 249 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32870 | 12853 | 14115 | 18602 | 2269 | 2026-09-29 02:34:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30193 | 7084 | 3966 | 5073 | 49 | 2026-09-24 10:51:51 |
| [celery](https://github.com/celery/celery) | 28922 | 5186 | 5311 | 4455 | 731 | 2026-09-28 22:13:45 |
| [dash](https://github.com/plotly/dash) | 24441 | 2325 | 2158 | 1735 | 427 | 2026-09-29 00:40:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23299 | 8496 | 11429 | 20912 | 1491 | 2026-09-28 19:19:49 |
| [RustPython](https://github.com/RustPython/RustPython) | 22371 | 1489 | 1431 | 7389 | 400 | 2026-09-29 02:49:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5561 | 1884 | 1839 | 248 | 2026-09-25 19:17:31 |
| [micropython](https://github.com/micropython/micropython) | 22103 | 8982 | 6132 | 8110 | 1532 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18811 | 2856 | 3386 | 2201 | 720 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1604 | 1468 | 1679 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16565 | 2435 | 3257 | 10237 | 229 | 2026-09-29 03:23:36 |
| [httpx](https://github.com/encode/httpx) | 15520 | 2539 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15049 | 5978 | 11669 | 14601 | 1846 | 2026-09-28 15:37:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14047 | 2143 | 2663 | 1225 | 237 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13927 | 1968 | 5562 | 6735 | 1346 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12640 | 1343 | 784 | 2155 | 63 | 2026-09-28 18:49:23 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12189 | 1796 | 8308 | 1214 | 210 | 2026-09-28 19:16:50 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11908 | 617 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1038 | 1145 | 1530 | 155 | 2026-09-28 19:57:01 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9200 | 613 | 1047 | 554 | 222 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1512 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7340 | 436 | 902 | 2615 | 331 | 2026-09-28 22:58:04 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5632 | 519 | 1271 | 906 | 521 | 2026-09-27 09:32:15 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5411 | 1042 | 934 | 324 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4420 | 379 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3989 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 208 | 289 | 136 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1341 | 312 | 2026-09-29 01:02:21 |
| [anyio](https://github.com/agronholm/anyio) | 2551 | 285 | 482 | 801 | 122 | 2026-09-29 00:07:07 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 275 | 272 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1803 | 127 | 5266 | 315 | 718 | 2026-09-29 02:55:59 |
| [jython](https://github.com/jython/jython) | 1544 | 231 | 303 | 152 | 100 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-29T05:29:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
