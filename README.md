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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200088 | 76332 | 41778 | 82027 | 3169 | 2026-09-15 04:38:34 |
| [transformers](https://github.com/huggingface/transformers) | 166067 | 34580 | 19467 | 28576 | 2430 | 2026-09-15 04:37:55 |
| [pytorch](https://github.com/pytorch/pytorch) | 103011 | 29230 | 60959 | 135440 | 17610 | 2026-09-15 04:38:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 102340 | 9884 | 3552 | 6326 | 77 | 2026-09-14 18:49:48 |
| [django](https://github.com/django/django) | 91064 | 34253 | 0 | 21843 | 504 | 2026-09-14 15:22:13 |
| [cpython](https://github.com/python/cpython) | 77255 | 35385 | 78131 | 77050 | 9670 | 2026-09-15 03:41:55 |
| [flask](https://github.com/pallets/flask) | 74737 | 16986 | 2768 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67255 | 27402 | 12282 | 21487 | 2161 | 2026-09-14 23:49:53 |
| [keras](https://github.com/keras-team/keras) | 64321 | 19790 | 12905 | 9854 | 185 | 2026-09-15 00:14:31 |
| [pandas](https://github.com/pandas-dev/pandas) | 49732 | 20380 | 28546 | 38744 | 2719 | 2026-09-15 02:22:19 |
| [ray](https://github.com/ray-project/ray) | 43804 | 8036 | 23069 | 42685 | 3612 | 2026-09-15 04:36:27 |
| [gym](https://github.com/openai/gym) | 37238 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33899 | 4721 | 5772 | 4120 | 240 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32743 | 12784 | 14098 | 18430 | 2291 | 2026-09-15 02:57:35 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30179 | 7082 | 3966 | 5064 | 52 | 2026-09-14 14:07:14 |
| [celery](https://github.com/celery/celery) | 28886 | 5166 | 5300 | 4362 | 717 | 2026-09-15 04:13:59 |
| [dash](https://github.com/plotly/dash) | 24406 | 2313 | 2153 | 1701 | 480 | 2026-09-14 16:48:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23216 | 8482 | 11424 | 20861 | 1482 | 2026-09-13 18:57:29 |
| [RustPython](https://github.com/RustPython/RustPython) | 22344 | 1487 | 1424 | 7217 | 396 | 2026-09-15 00:48:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5555 | 1881 | 1821 | 261 | 2026-09-14 20:00:57 |
| [micropython](https://github.com/micropython/micropython) | 22064 | 8967 | 6124 | 8090 | 1525 | 2026-09-11 14:21:56 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18782 | 2843 | 3384 | 2166 | 705 | 2026-09-14 23:51:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1597 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16548 | 2408 | 3251 | 10106 | 219 | 2026-09-14 21:04:04 |
| [httpx](https://github.com/encode/httpx) | 15477 | 1295 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15014 | 5931 | 11643 | 14508 | 1836 | 2026-09-15 03:59:03 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14021 | 2134 | 2662 | 1223 | 234 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13917 | 1956 | 5558 | 6725 | 1334 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12617 | 1309 | 783 | 2114 | 47 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12159 | 1783 | 8298 | 1208 | 208 | 2026-09-14 20:38:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11899 | 615 | 420 | 330 | 160 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1034 | 1142 | 1518 | 160 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9188 | 613 | 1045 | 549 | 224 | 2026-09-14 13:10:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1510 | 867 | 650 | 292 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7327 | 428 | 901 | 2607 | 327 | 2026-09-14 22:29:41 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 739 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5630 | 515 | 1270 | 902 | 525 | 2026-09-15 00:44:58 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5388 | 1041 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4395 | 375 | 1202 | 249 | 118 | 2026-09-11 19:10:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3992 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 206 | 286 | 136 | 25 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2760 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2542 | 263 | 477 | 771 | 109 | 2026-09-14 23:44:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1794 | 125 | 5257 | 303 | 720 | 2026-09-14 19:53:27 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-15T04:39:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
