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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192533 | 74998 | 41017 | 61921 | 2529 | 2025-11-25 02:00:46 |
| [transformers](https://github.com/huggingface/transformers) | 152953 | 31213 | 18220 | 23549 | 2108 | 2025-11-24 21:57:48 |
| [pytorch](https://github.com/pytorch/pytorch) | 95333 | 25996 | 55534 | 113005 | 17679 | 2025-11-25 01:59:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 92250 | 8269 | 3477 | 4902 | 223 | 2025-11-24 19:17:19 |
| [django](https://github.com/django/django) | 85915 | 33257 | 0 | 20253 | 364 | 2025-11-24 21:35:17 |
| [flask](https://github.com/pallets/flask) | 70830 | 16633 | 2704 | 2723 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69984 | 33500 | 74437 | 66525 | 9190 | 2025-11-25 01:32:55 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64125 | 26469 | 11824 | 19826 | 2118 | 2025-11-24 13:13:38 |
| [keras](https://github.com/keras-team/keras) | 63596 | 19659 | 12595 | 8482 | 270 | 2025-11-25 01:45:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 47179 | 19329 | 27903 | 35235 | 3645 | 2025-11-24 08:05:19 |
| [ray](https://github.com/ray-project/ray) | 39990 | 6937 | 21910 | 36697 | 3240 | 2025-11-25 01:54:41 |
| [gym](https://github.com/openai/gym) | 36803 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32862 | 4629 | 5732 | 4074 | 183 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30892 | 11739 | 13666 | 16567 | 2366 | 2025-11-24 23:44:34 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29687 | 7040 | 3946 | 4873 | 93 | 2025-11-24 19:36:51 |
| [celery](https://github.com/celery/celery) | 27615 | 4902 | 5176 | 3730 | 753 | 2025-11-24 16:54:38 |
| [dash](https://github.com/plotly/dash) | 24271 | 2238 | 2028 | 1379 | 580 | 2025-11-24 21:18:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22359 | 5544 | 1854 | 1676 | 204 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22039 | 8128 | 11053 | 19685 | 1618 | 2025-11-24 21:42:25 |
| [micropython](https://github.com/micropython/micropython) | 21124 | 8543 | 5881 | 7379 | 1800 | 2025-11-25 01:25:07 |
| [RustPython](https://github.com/RustPython/RustPython) | 20833 | 1360 | 1237 | 4993 | 444 | 2025-11-24 21:14:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18577 | 1585 | 1453 | 1630 | 151 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18012 | 2749 | 3295 | 1984 | 746 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16106 | 2157 | 3163 | 8308 | 288 | 2025-11-24 16:26:04 |
| [httpx](https://github.com/encode/httpx) | 14771 | 981 | 922 | 1756 | 113 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14206 | 5546 | 11154 | 12885 | 1774 | 2025-11-24 17:33:19 |
| [dask](https://github.com/dask/dask) | 13615 | 1826 | 5466 | 6407 | 1194 | 2025-11-24 22:09:31 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13578 | 2052 | 2634 | 1149 | 194 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11688 | 1083 | 760 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11443 | 586 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11168 | 1600 | 8120 | 1006 | 211 | 2025-11-21 21:17:16 |
| [falcon](https://github.com/falconry/falcon) | 9760 | 972 | 1113 | 1403 | 163 | 2025-11-22 17:38:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8730 | 539 | 970 | 454 | 176 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8699 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7011 | 372 | 874 | 2471 | 313 | 2025-11-24 22:19:44 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 979 | 577 | 33 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5626 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5392 | 446 | 1200 | 719 | 505 | 2025-11-25 02:03:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5094 | 970 | 877 | 263 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4063 | 887 | 1062 | 2722 | 90 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 3930 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3776 | 302 | 1168 | 201 | 115 | 2025-11-20 22:26:20 |
| [quart](https://github.com/pallets/quart) | 3548 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2710 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2302 | 177 | 415 | 551 | 74 | 2025-11-25 00:03:59 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 372 | 1784 | 266 | 265 | 2025-11-24 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1574 | 89 | 5164 | 172 | 748 | 2025-11-24 21:06:55 |
| [jython](https://github.com/jython/jython) | 1459 | 225 | 286 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-25T02:05:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
