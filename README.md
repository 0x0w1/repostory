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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193633 | 75212 | 41148 | 66629 | 3289 | 2026-02-07 02:40:40 |
| [transformers](https://github.com/huggingface/transformers) | 156166 | 31978 | 18534 | 24675 | 2212 | 2026-02-07 02:17:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 97210 | 26768 | 56723 | 117275 | 17989 | 2026-02-07 02:38:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 94856 | 8643 | 3502 | 5245 | 167 | 2026-02-06 19:04:48 |
| [django](https://github.com/django/django) | 86698 | 33629 | 0 | 20581 | 399 | 2026-02-06 21:19:49 |
| [cpython](https://github.com/python/cpython) | 71390 | 34032 | 75189 | 68351 | 9201 | 2026-02-06 21:26:45 |
| [flask](https://github.com/pallets/flask) | 71138 | 16697 | 2713 | 2764 | 2 | 2026-02-06 21:23:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64933 | 26672 | 11920 | 20166 | 2122 | 2026-02-06 14:50:17 |
| [keras](https://github.com/keras-team/keras) | 63754 | 19686 | 12625 | 8703 | 255 | 2026-02-07 01:14:31 |
| [pandas](https://github.com/pandas-dev/pandas) | 47814 | 19620 | 28083 | 35910 | 3635 | 2026-02-06 21:29:52 |
| [ray](https://github.com/ray-project/ray) | 41168 | 7192 | 22286 | 38181 | 3338 | 2026-02-07 01:58:25 |
| [gym](https://github.com/openai/gym) | 37022 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33169 | 4636 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31392 | 12022 | 13782 | 16951 | 2301 | 2026-02-05 19:16:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29860 | 7063 | 3946 | 4918 | 90 | 2026-02-05 15:11:44 |
| [celery](https://github.com/celery/celery) | 27976 | 4939 | 5188 | 3788 | 764 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24457 | 2253 | 2053 | 1429 | 557 | 2026-02-05 23:11:54 |
| [tornado](https://github.com/tornadoweb/tornado) | 22439 | 5543 | 1863 | 1698 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22314 | 8182 | 11133 | 19929 | 1522 | 2026-02-07 01:33:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 21759 | 1400 | 1295 | 5670 | 370 | 2026-02-06 11:46:51 |
| [micropython](https://github.com/micropython/micropython) | 21441 | 8698 | 5950 | 7544 | 1845 | 2026-02-06 14:14:48 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1583 | 1465 | 1663 | 115 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18240 | 2778 | 3320 | 2024 | 788 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16251 | 2186 | 3176 | 8552 | 279 | 2026-02-05 16:58:15 |
| [httpx](https://github.com/encode/httpx) | 14976 | 1029 | 925 | 1783 | 129 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14429 | 5609 | 11291 | 13225 | 1755 | 2026-02-07 01:40:47 |
| [dask](https://github.com/dask/dask) | 13730 | 1843 | 5504 | 6485 | 1229 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13706 | 2080 | 2645 | 1160 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11900 | 1107 | 763 | 1783 | 52 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11632 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11470 | 1634 | 8151 | 1028 | 208 | 2026-02-06 15:06:53 |
| [falcon](https://github.com/falconry/falcon) | 9793 | 978 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8887 | 556 | 1005 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8742 | 1492 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7155 | 382 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5476 | 453 | 1222 | 747 | 505 | 2026-02-06 02:29:41 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5180 | 1000 | 900 | 289 | 190 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3940 | 310 | 1181 | 208 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3591 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 657 | 1270 | 313 | 2026-02-06 05:16:53 |
| [anyio](https://github.com/agronholm/anyio) | 2380 | 179 | 423 | 566 | 75 | 2026-02-04 20:13:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1933 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1645 | 97 | 5175 | 179 | 758 | 2026-02-06 10:46:06 |
| [jython](https://github.com/jython/jython) | 1480 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-07T02:42:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
