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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200232 | 77038 | 41787 | 82417 | 3251 | 2026-09-22 04:29:43 |
| [transformers](https://github.com/huggingface/transformers) | 166494 | 34658 | 19501 | 28714 | 2404 | 2026-09-22 04:17:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 103159 | 30012 | 61124 | 136313 | 17559 | 2026-09-22 04:32:06 |
| [fastapi](https://github.com/fastapi/fastapi) | 102516 | 9925 | 3552 | 6348 | 82 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91148 | 34999 | 0 | 21882 | 505 | 2026-09-20 17:42:44 |
| [cpython](https://github.com/python/cpython) | 77238 | 36068 | 78220 | 77354 | 9708 | 2026-09-22 02:49:16 |
| [flask](https://github.com/pallets/flask) | 74760 | 16993 | 2767 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67335 | 27431 | 12290 | 21527 | 2153 | 2026-09-21 14:56:13 |
| [keras](https://github.com/keras-team/keras) | 64327 | 19801 | 12929 | 9907 | 224 | 2026-09-22 04:21:25 |
| [pandas](https://github.com/pandas-dev/pandas) | 49777 | 20413 | 28553 | 38865 | 2658 | 2026-09-22 04:08:28 |
| [ray](https://github.com/ray-project/ray) | 43887 | 8069 | 23089 | 42852 | 3613 | 2026-09-22 02:09:06 |
| [gym](https://github.com/openai/gym) | 37236 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33912 | 4724 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32800 | 12831 | 14106 | 18544 | 2281 | 2026-09-22 03:40:40 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30190 | 7085 | 3966 | 5069 | 52 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28909 | 5173 | 5303 | 4414 | 726 | 2026-09-22 02:33:09 |
| [dash](https://github.com/plotly/dash) | 24423 | 2319 | 2152 | 1721 | 439 | 2026-09-21 23:22:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23246 | 8492 | 11425 | 20887 | 1486 | 2026-09-22 00:25:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 22354 | 1485 | 1428 | 7281 | 402 | 2026-09-22 01:49:51 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5558 | 1883 | 1834 | 259 | 2026-09-22 03:01:36 |
| [micropython](https://github.com/micropython/micropython) | 22077 | 8976 | 6132 | 8099 | 1525 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18797 | 2850 | 3385 | 2191 | 715 | 2026-09-22 02:02:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1601 | 1468 | 1678 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16556 | 2418 | 3256 | 10165 | 228 | 2026-09-21 14:00:51 |
| [httpx](https://github.com/encode/httpx) | 15500 | 1773 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15031 | 5958 | 11651 | 14545 | 1836 | 2026-09-21 18:35:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14033 | 2137 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13923 | 1961 | 5559 | 6728 | 1337 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12624 | 1319 | 782 | 2132 | 55 | 2026-09-20 10:07:50 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12171 | 1795 | 8301 | 1213 | 209 | 2026-09-21 17:07:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11898 | 615 | 421 | 331 | 162 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1036 | 1144 | 1526 | 160 | 2026-09-21 17:56:24 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9194 | 612 | 1046 | 550 | 222 | 2026-09-19 05:35:44 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7333 | 432 | 902 | 2613 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 517 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5402 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4408 | 376 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4101 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3672 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2546 | 272 | 477 | 783 | 115 | 2026-09-21 18:00:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1794 | 125 | 5260 | 303 | 714 | 2026-09-22 03:46:01 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-22T04:34:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
