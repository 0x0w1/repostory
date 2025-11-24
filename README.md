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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192525 | 74994 | 41016 | 61853 | 2526 | 2025-11-24 00:03:04 |
| [transformers](https://github.com/huggingface/transformers) | 152896 | 31208 | 18215 | 23529 | 2123 | 2025-11-23 10:25:50 |
| [pytorch](https://github.com/pytorch/pytorch) | 95307 | 25987 | 55502 | 112942 | 17657 | 2025-11-24 02:11:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 92203 | 8259 | 3476 | 4899 | 224 | 2025-11-23 20:10:06 |
| [django](https://github.com/django/django) | 85892 | 33251 | 0 | 20240 | 365 | 2025-11-22 16:06:51 |
| [flask](https://github.com/pallets/flask) | 70815 | 16631 | 2704 | 2723 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69975 | 33495 | 74429 | 66487 | 9200 | 2025-11-23 23:55:34 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64110 | 26459 | 11822 | 19812 | 2118 | 2025-11-23 08:45:38 |
| [keras](https://github.com/keras-team/keras) | 63589 | 19657 | 12594 | 8479 | 271 | 2025-11-21 02:04:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 47171 | 19328 | 27898 | 35227 | 3632 | 2025-11-24 01:11:26 |
| [ray](https://github.com/ray-project/ray) | 39974 | 6933 | 21904 | 36672 | 3237 | 2025-11-24 01:41:03 |
| [gym](https://github.com/openai/gym) | 36799 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32857 | 4628 | 5732 | 4073 | 182 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30885 | 11731 | 13665 | 16556 | 2363 | 2025-11-22 07:40:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29679 | 7039 | 3946 | 4871 | 91 | 2025-11-21 12:29:35 |
| [celery](https://github.com/celery/celery) | 27613 | 4899 | 5176 | 3729 | 753 | 2025-11-22 17:54:49 |
| [dash](https://github.com/plotly/dash) | 24271 | 2235 | 2027 | 1379 | 583 | 2025-11-21 18:12:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22358 | 5542 | 1854 | 1676 | 204 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22034 | 8127 | 11053 | 19681 | 1623 | 2025-11-21 15:59:36 |
| [micropython](https://github.com/micropython/micropython) | 21120 | 8540 | 5879 | 7375 | 1799 | 2025-11-24 01:42:59 |
| [RustPython](https://github.com/RustPython/RustPython) | 20830 | 1358 | 1237 | 4989 | 446 | 2025-11-23 15:04:43 |
| [sanic](https://github.com/sanic-org/sanic) | 18574 | 1584 | 1453 | 1630 | 151 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18010 | 2749 | 3295 | 1984 | 748 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16105 | 2157 | 3163 | 8308 | 288 | 2025-11-22 23:37:47 |
| [httpx](https://github.com/encode/httpx) | 14770 | 980 | 921 | 1756 | 112 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14208 | 5546 | 11154 | 12881 | 1774 | 2025-11-24 01:14:00 |
| [dask](https://github.com/dask/dask) | 13613 | 1825 | 5466 | 6406 | 1193 | 2025-11-22 15:50:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13575 | 2051 | 2634 | 1149 | 194 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11682 | 1082 | 760 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11441 | 586 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11163 | 1600 | 8120 | 1005 | 210 | 2025-11-21 21:17:16 |
| [falcon](https://github.com/falconry/falcon) | 9759 | 972 | 1112 | 1403 | 162 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8726 | 538 | 970 | 454 | 176 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8698 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7008 | 371 | 874 | 2470 | 314 | 2025-11-17 21:56:02 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 745 | 979 | 576 | 32 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5626 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5389 | 445 | 1200 | 718 | 507 | 2025-11-23 12:09:34 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5094 | 970 | 877 | 263 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4063 | 887 | 1062 | 2722 | 90 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3774 | 301 | 1168 | 201 | 115 | 2025-11-20 22:26:20 |
| [quart](https://github.com/pallets/quart) | 3546 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2709 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2301 | 176 | 415 | 549 | 72 | 2025-11-22 11:56:08 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1928 | 372 | 1784 | 266 | 265 | 2025-11-20 00:37:23 |
| [pypy](https://github.com/pypy/pypy) | 1574 | 89 | 5164 | 172 | 750 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1459 | 225 | 286 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-18 10:59:56 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-24T02:12:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
