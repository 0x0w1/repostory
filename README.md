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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193396 | 75176 | 41092 | 65258 | 2836 | 2026-01-18 18:43:33 |
| [transformers](https://github.com/huggingface/transformers) | 155366 | 31776 | 18432 | 24305 | 2167 | 2026-01-18 17:31:59 |
| [pytorch](https://github.com/pytorch/pytorch) | 96721 | 26543 | 56349 | 115892 | 17874 | 2026-01-19 02:24:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 94210 | 8544 | 3500 | 5140 | 205 | 2026-01-18 20:32:39 |
| [django](https://github.com/django/django) | 86499 | 33507 | 0 | 20492 | 388 | 2026-01-18 20:26:56 |
| [cpython](https://github.com/python/cpython) | 71135 | 33922 | 75041 | 67989 | 9255 | 2026-01-18 22:28:38 |
| [flask](https://github.com/pallets/flask) | 71057 | 16674 | 2709 | 2751 | 12 | 2026-01-05 16:50:56 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64674 | 26606 | 11891 | 20072 | 2119 | 2026-01-18 23:19:19 |
| [keras](https://github.com/keras-team/keras) | 63714 | 19678 | 12611 | 8623 | 253 | 2026-01-16 22:34:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 47616 | 19527 | 28029 | 35655 | 3629 | 2026-01-18 23:54:29 |
| [ray](https://github.com/ray-project/ray) | 40846 | 7128 | 22175 | 37756 | 3297 | 2026-01-19 02:18:01 |
| [gym](https://github.com/openai/gym) | 36959 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33083 | 4633 | 5737 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31265 | 11972 | 13749 | 16856 | 2324 | 2026-01-16 23:12:59 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29811 | 7053 | 3946 | 4903 | 85 | 2026-01-13 22:15:14 |
| [celery](https://github.com/celery/celery) | 27879 | 4929 | 5184 | 3768 | 757 | 2026-01-17 05:57:45 |
| [dash](https://github.com/plotly/dash) | 24403 | 2248 | 2041 | 1412 | 556 | 2026-01-16 23:21:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22434 | 5543 | 1862 | 1695 | 211 | 2026-01-13 20:42:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22245 | 8175 | 11107 | 19840 | 1527 | 2026-01-18 19:57:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 21683 | 1401 | 1292 | 5436 | 367 | 2026-01-19 01:01:11 |
| [micropython](https://github.com/micropython/micropython) | 21354 | 8654 | 5937 | 7491 | 1834 | 2026-01-16 08:10:24 |
| [sanic](https://github.com/sanic-org/sanic) | 18617 | 1584 | 1462 | 1662 | 112 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18190 | 2772 | 3314 | 2004 | 764 | 2026-01-14 21:23:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16209 | 2180 | 3171 | 8493 | 270 | 2026-01-17 22:43:46 |
| [httpx](https://github.com/encode/httpx) | 14916 | 1008 | 925 | 1779 | 126 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14360 | 5589 | 11256 | 13126 | 1756 | 2026-01-19 01:31:24 |
| [dask](https://github.com/dask/dask) | 13719 | 1836 | 5488 | 6449 | 1213 | 2026-01-16 12:34:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13689 | 2080 | 2644 | 1156 | 203 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11852 | 1098 | 761 | 1769 | 46 | 2026-01-18 13:59:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11596 | 600 | 403 | 306 | 152 | 2026-01-15 19:26:30 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11397 | 1625 | 8142 | 1022 | 207 | 2026-01-17 16:48:43 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 974 | 1118 | 1408 | 164 | 2026-01-18 16:19:15 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8844 | 556 | 996 | 480 | 199 | 2026-01-13 18:26:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8730 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7105 | 379 | 878 | 2488 | 314 | 2026-01-12 21:58:36 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5618 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5446 | 446 | 1219 | 735 | 509 | 2026-01-14 06:28:04 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5158 | 990 | 886 | 281 | 179 | 2026-01-15 16:36:40 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4024 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3900 | 307 | 1177 | 207 | 118 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3575 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2722 | 307 | 655 | 1261 | 310 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2361 | 179 | 421 | 563 | 74 | 2026-01-12 17:50:45 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1785 | 266 | 266 | 2026-01-12 17:44:15 |
| [pypy](https://github.com/pypy/pypy) | 1633 | 96 | 5172 | 177 | 755 | 2026-01-16 09:43:20 |
| [jython](https://github.com/jython/jython) | 1469 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-19T02:28:23*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
