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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191332 | 74789 | 40746 | 56587 | 1512 | 2025-08-26 01:51:49 |
| [transformers](https://github.com/huggingface/transformers) | 148807 | 30167 | 17830 | 22038 | 1964 | 2025-08-25 21:17:59 |
| [pytorch](https://github.com/pytorch/pytorch) | 92670 | 25087 | 53305 | 107695 | 16938 | 2025-08-26 02:01:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 88771 | 7770 | 3467 | 4668 | 281 | 2025-08-25 20:03:25 |
| [django](https://github.com/django/django) | 84769 | 32854 | 0 | 19710 | 365 | 2025-08-25 13:51:11 |
| [flask](https://github.com/pallets/flask) | 70221 | 16518 | 2692 | 2688 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68531 | 32677 | 73392 | 63828 | 9298 | 2025-08-26 01:34:07 |
| [keras](https://github.com/keras-team/keras) | 63361 | 19613 | 12528 | 8300 | 296 | 2025-08-26 00:30:20 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63128 | 26174 | 11658 | 19226 | 2163 | 2025-08-25 12:51:14 |
| [pandas](https://github.com/pandas-dev/pandas) | 46396 | 18851 | 27671 | 34473 | 3708 | 2025-08-26 01:32:37 |
| [ray](https://github.com/ray-project/ray) | 38633 | 6737 | 20942 | 34630 | 3032 | 2025-08-26 01:52:27 |
| [gym](https://github.com/openai/gym) | 36410 | 8692 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32231 | 4567 | 5718 | 4065 | 200 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30244 | 11254 | 13499 | 16060 | 2342 | 2025-08-25 21:05:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29398 | 6996 | 3945 | 4828 | 98 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27086 | 4831 | 5157 | 3646 | 761 | 2025-08-26 01:00:58 |
| [dash](https://github.com/plotly/dash) | 23976 | 2190 | 1978 | 1319 | 552 | 2025-08-22 21:25:47 |
| [tornado](https://github.com/tornadoweb/tornado) | 22111 | 5537 | 1851 | 1670 | 206 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21607 | 7968 | 10950 | 19479 | 1636 | 2025-08-26 01:49:01 |
| [micropython](https://github.com/micropython/micropython) | 20753 | 8381 | 5795 | 7127 | 1771 | 2025-08-26 00:54:17 |
| [RustPython](https://github.com/RustPython/RustPython) | 20432 | 1341 | 1210 | 4833 | 442 | 2025-08-26 01:42:05 |
| [sanic](https://github.com/sanic-org/sanic) | 18485 | 1579 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17647 | 2705 | 3243 | 1945 | 721 | 2025-08-22 14:56:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15939 | 2114 | 3144 | 8008 | 264 | 2025-08-26 00:02:25 |
| [httpx](https://github.com/encode/httpx) | 14494 | 946 | 916 | 1708 | 104 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13955 | 5453 | 10979 | 12511 | 1765 | 2025-08-25 23:22:42 |
| [dask](https://github.com/dask/dask) | 13432 | 1794 | 5426 | 6334 | 1194 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13386 | 2029 | 2624 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11377 | 1032 | 750 | 1683 | 49 | 2025-08-24 13:36:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11173 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10812 | 1576 | 8071 | 978 | 233 | 2025-08-25 15:37:40 |
| [falcon](https://github.com/falconry/falcon) | 9704 | 959 | 1093 | 1361 | 156 | 2025-08-24 13:51:01 |
| [bottle](https://github.com/bottlepy/bottle) | 8649 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8462 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6753 | 364 | 864 | 2445 | 314 | 2025-08-23 20:10:19 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5259 | 435 | 1188 | 711 | 497 | 2025-08-24 10:55:31 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4955 | 928 | 864 | 257 | 158 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4042 | 891 | 1061 | 2718 | 88 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3547 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3411 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2678 | 304 | 649 | 1261 | 307 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2180 | 165 | 399 | 501 | 67 | 2025-08-25 19:02:47 |
| [web2py](https://github.com/web2py/web2py) | 2155 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-25 17:35:48 |
| [pypy](https://github.com/pypy/pypy) | 1482 | 84 | 5142 | 168 | 736 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1427 | 218 | 280 | 113 | 99 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 100 | 36 | 15 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-26T02:02:57*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
