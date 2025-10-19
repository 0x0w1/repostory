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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192085 | 74915 | 40874 | 59621 | 1551 | 2025-10-19 01:42:02 |
| [transformers](https://github.com/huggingface/transformers) | 151282 | 30844 | 18070 | 23063 | 2058 | 2025-10-18 18:31:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 94043 | 25598 | 54372 | 110998 | 16954 | 2025-10-19 02:09:47 |
| [fastapi](https://github.com/fastapi/fastapi) | 90879 | 8066 | 3470 | 4782 | 202 | 2025-10-13 17:40:45 |
| [django](https://github.com/django/django) | 85449 | 33115 | 0 | 19909 | 347 | 2025-10-18 19:04:11 |
| [flask](https://github.com/pallets/flask) | 70581 | 16592 | 2699 | 2709 | 11 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69403 | 33139 | 74000 | 65383 | 9210 | 2025-10-18 23:20:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63722 | 26342 | 11773 | 19629 | 2148 | 2025-10-18 13:01:57 |
| [keras](https://github.com/keras-team/keras) | 63476 | 19623 | 12567 | 8404 | 255 | 2025-10-19 00:13:52 |
| [pandas](https://github.com/pandas-dev/pandas) | 46866 | 19145 | 27801 | 34888 | 3618 | 2025-10-19 00:39:16 |
| [ray](https://github.com/ray-project/ray) | 39374 | 6784 | 21598 | 35939 | 3179 | 2025-10-19 01:48:33 |
| [gym](https://github.com/openai/gym) | 36689 | 8710 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32670 | 4601 | 5726 | 4071 | 210 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30599 | 11586 | 13595 | 16364 | 2345 | 2025-10-18 17:27:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29581 | 7022 | 3945 | 4846 | 94 | 2025-10-14 06:22:47 |
| [celery](https://github.com/celery/celery) | 27370 | 4863 | 5173 | 3695 | 753 | 2025-10-18 19:50:26 |
| [dash](https://github.com/plotly/dash) | 24170 | 2220 | 2012 | 1354 | 571 | 2025-10-17 20:26:15 |
| [tornado](https://github.com/tornadoweb/tornado) | 22311 | 5534 | 1853 | 1674 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21844 | 8069 | 11012 | 19605 | 1630 | 2025-10-17 00:10:16 |
| [micropython](https://github.com/micropython/micropython) | 20960 | 8493 | 5850 | 7287 | 1780 | 2025-10-17 03:42:53 |
| [RustPython](https://github.com/RustPython/RustPython) | 20659 | 1350 | 1221 | 4909 | 451 | 2025-10-13 13:59:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18523 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17855 | 2729 | 3266 | 1966 | 715 | 2025-10-17 14:53:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16044 | 2138 | 3153 | 8235 | 257 | 2025-10-18 19:45:35 |
| [httpx](https://github.com/encode/httpx) | 14642 | 963 | 919 | 1746 | 101 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14097 | 5507 | 11082 | 12711 | 1781 | 2025-10-18 15:32:39 |
| [dask](https://github.com/dask/dask) | 13539 | 1805 | 5441 | 6365 | 1194 | 2025-10-15 06:34:30 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13506 | 2034 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11563 | 1047 | 755 | 1725 | 52 | 2025-10-16 17:17:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11346 | 579 | 395 | 296 | 146 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11021 | 1586 | 8103 | 992 | 217 | 2025-10-18 20:06:23 |
| [falcon](https://github.com/falconry/falcon) | 9737 | 968 | 1107 | 1381 | 166 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8674 | 1487 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8633 | 528 | 957 | 446 | 168 | 2025-10-17 11:15:24 |
| [trio](https://github.com/python-trio/trio) | 6906 | 369 | 872 | 2460 | 312 | 2025-10-13 21:56:58 |
| [hug](https://github.com/hugapi/hug) | 6901 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5333 | 439 | 1196 | 713 | 501 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5037 | 950 | 874 | 262 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4053 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3692 | 292 | 1163 | 196 | 118 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3500 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2696 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2315 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2254 | 166 | 406 | 529 | 72 | 2025-10-18 17:10:46 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 909 | 1077 | 1462 | 369 | 2025-10-14 17:45:08 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1925 | 369 | 1780 | 264 | 260 | 2025-10-13 17:45:09 |
| [pypy](https://github.com/pypy/pypy) | 1535 | 87 | 5151 | 171 | 739 | 2025-10-10 06:55:50 |
| [jython](https://github.com/jython/jython) | 1442 | 224 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-19T02:10:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
