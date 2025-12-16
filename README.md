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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192820 | 75094 | 41035 | 63143 | 2851 | 2025-12-16 02:08:24 |
| [transformers](https://github.com/huggingface/transformers) | 153905 | 31432 | 18330 | 23954 | 2165 | 2025-12-15 23:31:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 95924 | 26241 | 55863 | 114143 | 17857 | 2025-12-16 02:12:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 93092 | 8371 | 3499 | 4975 | 184 | 2025-12-15 11:04:46 |
| [django](https://github.com/django/django) | 86161 | 33358 | 0 | 20348 | 369 | 2025-12-15 22:00:21 |
| [flask](https://github.com/pallets/flask) | 70924 | 16652 | 2706 | 2732 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70325 | 33684 | 74689 | 67113 | 9245 | 2025-12-15 23:30:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64290 | 26507 | 11847 | 19919 | 2119 | 2025-12-15 14:11:13 |
| [keras](https://github.com/keras-team/keras) | 63639 | 19649 | 12605 | 8529 | 253 | 2025-12-16 00:10:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 47322 | 19402 | 27952 | 35361 | 3596 | 2025-12-15 21:49:03 |
| [ray](https://github.com/ray-project/ray) | 40340 | 7009 | 22018 | 37090 | 3179 | 2025-12-16 01:57:12 |
| [gym](https://github.com/openai/gym) | 36869 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32955 | 4635 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31019 | 11841 | 13696 | 16679 | 2387 | 2025-12-15 19:33:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29739 | 7041 | 3946 | 4885 | 77 | 2025-12-15 16:01:56 |
| [celery](https://github.com/celery/celery) | 27712 | 4913 | 5179 | 3742 | 755 | 2025-12-15 22:08:02 |
| [dash](https://github.com/plotly/dash) | 24342 | 2246 | 2035 | 1391 | 560 | 2025-12-15 23:02:52 |
| [tornado](https://github.com/tornadoweb/tornado) | 22384 | 5543 | 1860 | 1689 | 208 | 2025-12-15 19:22:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22123 | 8142 | 11077 | 19742 | 1572 | 2025-12-15 21:32:02 |
| [micropython](https://github.com/micropython/micropython) | 21215 | 8589 | 5897 | 7439 | 1812 | 2025-12-14 23:55:47 |
| [RustPython](https://github.com/RustPython/RustPython) | 20913 | 1368 | 1246 | 5134 | 446 | 2025-12-16 01:11:17 |
| [sanic](https://github.com/sanic-org/sanic) | 18598 | 1585 | 1455 | 1635 | 129 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18091 | 2761 | 3306 | 1992 | 754 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16145 | 2167 | 3167 | 8380 | 275 | 2025-12-15 11:34:17 |
| [httpx](https://github.com/encode/httpx) | 14844 | 993 | 924 | 1767 | 117 | 2025-12-10 15:17:09 |
| [scipy](https://github.com/scipy/scipy) | 14261 | 5558 | 11187 | 12958 | 1767 | 2025-12-14 00:23:06 |
| [dask](https://github.com/dask/dask) | 13656 | 1827 | 5476 | 6421 | 1202 | 2025-12-15 22:02:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13618 | 2066 | 2641 | 1150 | 200 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11757 | 1089 | 760 | 1747 | 53 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11523 | 590 | 397 | 298 | 148 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11266 | 1606 | 8128 | 1010 | 205 | 2025-12-14 03:37:47 |
| [falcon](https://github.com/falconry/falcon) | 9769 | 972 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8778 | 549 | 984 | 473 | 190 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8713 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7053 | 373 | 877 | 2482 | 314 | 2025-12-15 22:18:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 742 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5622 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5414 | 445 | 1207 | 730 | 512 | 2025-12-15 22:10:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5112 | 969 | 882 | 269 | 173 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3816 | 302 | 1169 | 203 | 119 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3561 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2718 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2334 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2325 | 180 | 420 | 558 | 75 | 2025-12-16 00:36:03 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-15 17:49:12 |
| [pypy](https://github.com/pypy/pypy) | 1603 | 91 | 5166 | 172 | 751 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 288 | 118 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-16T02:16:02*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
