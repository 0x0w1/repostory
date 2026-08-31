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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198082 | 76209 | 41730 | 81140 | 3003 | 2026-08-31 05:13:20 |
| [transformers](https://github.com/huggingface/transformers) | 164644 | 34401 | 19392 | 28271 | 2405 | 2026-08-31 03:02:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 102695 | 29048 | 60628 | 134121 | 17485 | 2026-08-31 05:12:06 |
| [fastapi](https://github.com/fastapi/fastapi) | 101943 | 9835 | 3548 | 6293 | 88 | 2026-08-26 17:54:56 |
| [django](https://github.com/django/django) | 89292 | 34213 | 0 | 21736 | 482 | 2026-08-29 17:52:42 |
| [cpython](https://github.com/python/cpython) | 75298 | 35312 | 77886 | 76452 | 9611 | 2026-08-30 22:10:27 |
| [flask](https://github.com/pallets/flask) | 72154 | 16953 | 2764 | 2898 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67108 | 27336 | 12257 | 21398 | 2139 | 2026-08-28 21:28:28 |
| [keras](https://github.com/keras-team/keras) | 64270 | 19772 | 12890 | 9776 | 235 | 2026-08-30 17:39:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 49604 | 20311 | 28501 | 38394 | 2740 | 2026-08-30 20:43:51 |
| [ray](https://github.com/ray-project/ray) | 43662 | 7983 | 22998 | 42390 | 3547 | 2026-08-31 02:58:02 |
| [gym](https://github.com/openai/gym) | 37243 | 8680 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33864 | 4722 | 5770 | 4118 | 237 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32635 | 12695 | 14073 | 18295 | 2340 | 2026-08-30 08:37:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30149 | 7080 | 3966 | 5049 | 59 | 2026-08-25 19:14:08 |
| [celery](https://github.com/celery/celery) | 28841 | 5144 | 5296 | 4275 | 761 | 2026-08-29 13:37:56 |
| [dash](https://github.com/plotly/dash) | 24387 | 2319 | 2146 | 1690 | 535 | 2026-08-28 22:53:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23130 | 8463 | 11408 | 20794 | 1473 | 2026-08-31 03:54:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 22315 | 1481 | 1422 | 7124 | 398 | 2026-08-30 14:35:08 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5554 | 1878 | 1808 | 253 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22030 | 8945 | 6119 | 8074 | 1529 | 2026-08-31 04:24:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18764 | 2837 | 3378 | 2146 | 750 | 2026-08-27 16:46:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18646 | 1600 | 1471 | 1704 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16534 | 2390 | 3242 | 9990 | 224 | 2026-08-31 03:21:12 |
| [httpx](https://github.com/encode/httpx) | 15459 | 1265 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14970 | 5899 | 11617 | 14415 | 1833 | 2026-08-29 13:30:33 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14008 | 2126 | 2659 | 1213 | 227 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13907 | 1942 | 5552 | 6712 | 1320 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12580 | 1281 | 780 | 2069 | 60 | 2026-08-30 13:22:00 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12119 | 1764 | 8280 | 1199 | 206 | 2026-08-30 18:14:04 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11894 | 611 | 419 | 328 | 157 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1031 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9178 | 610 | 1043 | 540 | 221 | 2026-08-30 17:48:51 |
| [bottle](https://github.com/bottlepy/bottle) | 8777 | 1502 | 865 | 645 | 289 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7308 | 418 | 899 | 2593 | 323 | 2026-08-27 03:44:56 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5620 | 500 | 1266 | 891 | 543 | 2026-08-24 16:57:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5371 | 1037 | 932 | 320 | 199 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4355 | 368 | 1199 | 246 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3659 | 205 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 316 | 675 | 1338 | 314 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 251 | 472 | 752 | 104 | 2026-08-30 11:23:00 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 368 | 1786 | 272 | 270 | 2026-08-24 17:57:48 |
| [pypy](https://github.com/pypy/pypy) | 1785 | 125 | 5255 | 297 | 726 | 2026-08-30 20:58:45 |
| [jython](https://github.com/jython/jython) | 1536 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-31T05:15:03*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
