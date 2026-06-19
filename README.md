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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195764 | 75196 | 41558 | 76479 | 3464 | 2026-06-19 05:07:57 |
| [transformers](https://github.com/huggingface/transformers) | 161711 | 33542 | 19091 | 26955 | 2449 | 2026-06-18 18:23:09 |
| [pytorch](https://github.com/pytorch/pytorch) | 100865 | 28049 | 59328 | 127768 | 18302 | 2026-06-19 05:10:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 99389 | 9453 | 3535 | 5933 | 88 | 2026-06-18 10:15:48 |
| [django](https://github.com/django/django) | 87907 | 33867 | 0 | 21449 | 453 | 2026-06-18 19:25:17 |
| [cpython](https://github.com/python/cpython) | 73314 | 34750 | 76778 | 72577 | 9325 | 2026-06-18 23:29:34 |
| [flask](https://github.com/pallets/flask) | 71680 | 16879 | 2751 | 2837 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66367 | 27078 | 12150 | 21004 | 2084 | 2026-06-18 12:52:58 |
| [keras](https://github.com/keras-team/keras) | 64096 | 19737 | 12795 | 9463 | 191 | 2026-06-18 23:13:32 |
| [pandas](https://github.com/pandas-dev/pandas) | 49008 | 20022 | 28329 | 37487 | 3180 | 2026-06-18 19:01:54 |
| [ray](https://github.com/ray-project/ray) | 42930 | 7700 | 22754 | 41080 | 3474 | 2026-06-19 03:44:51 |
| [gym](https://github.com/openai/gym) | 37224 | 8704 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33668 | 4688 | 5759 | 4098 | 214 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32215 | 12461 | 13949 | 17654 | 2395 | 2026-06-19 02:47:36 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30076 | 7070 | 3967 | 5016 | 81 | 2026-06-16 19:13:19 |
| [celery](https://github.com/celery/celery) | 28600 | 5080 | 5280 | 4149 | 782 | 2026-06-18 22:12:40 |
| [dash](https://github.com/plotly/dash) | 24265 | 2300 | 2114 | 1593 | 551 | 2026-06-18 23:35:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22904 | 8355 | 11318 | 20544 | 1460 | 2026-06-18 20:57:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22183 | 5531 | 1873 | 1751 | 225 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22126 | 1444 | 1357 | 6700 | 385 | 2026-06-18 20:10:46 |
| [micropython](https://github.com/micropython/micropython) | 21815 | 8877 | 6069 | 7883 | 1640 | 2026-06-18 19:14:43 |
| [sanic](https://github.com/sanic-org/sanic) | 18624 | 1588 | 1467 | 1689 | 132 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18611 | 2812 | 3361 | 2096 | 766 | 2026-06-18 22:37:14 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16444 | 2330 | 3215 | 9411 | 221 | 2026-06-19 02:16:48 |
| [httpx](https://github.com/encode/httpx) | 15302 | 1175 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14758 | 5765 | 11483 | 13904 | 1804 | 2026-06-19 03:04:02 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13919 | 2117 | 2654 | 1185 | 225 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1888 | 5539 | 6620 | 1245 | 2026-06-19 00:32:57 |
| [starlette](https://github.com/Kludex/starlette) | 12403 | 1203 | 770 | 1951 | 45 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11926 | 1698 | 8230 | 1118 | 209 | 2026-06-18 18:13:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11821 | 610 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1002 | 1129 | 1465 | 161 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9098 | 600 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1503 | 864 | 635 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7279 | 397 | 892 | 2553 | 319 | 2026-06-16 05:03:49 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 737 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5586 | 489 | 1258 | 856 | 515 | 2026-06-18 15:20:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5298 | 1022 | 914 | 305 | 208 | 2026-06-18 19:38:18 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4209 | 341 | 1185 | 225 | 117 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4001 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 312 | 671 | 1333 | 307 | 2026-06-19 01:02:00 |
| [anyio](https://github.com/agronholm/anyio) | 2484 | 210 | 446 | 659 | 87 | 2026-06-18 19:52:44 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1084 | 1546 | 363 | 2026-06-12 17:54:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-15 17:49:21 |
| [pypy](https://github.com/pypy/pypy) | 1752 | 114 | 5224 | 261 | 735 | 2026-06-19 03:35:43 |
| [jython](https://github.com/jython/jython) | 1516 | 230 | 297 | 136 | 110 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-19T05:10:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
