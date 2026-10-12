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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200874 | 79188 | 41864 | 83466 | 3411 | 2026-10-12 05:39:05 |
| [transformers](https://github.com/huggingface/transformers) | 167534 | 34843 | 19606 | 29106 | 2338 | 2026-10-12 03:18:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 104609 | 32169 | 61647 | 138253 | 17711 | 2026-10-12 05:15:27 |
| [fastapi](https://github.com/fastapi/fastapi) | 103025 | 10022 | 3555 | 6421 | 88 | 2026-10-08 12:29:28 |
| [django](https://github.com/django/django) | 91384 | 37000 | 0 | 22052 | 541 | 2026-10-11 14:28:36 |
| [cpython](https://github.com/python/cpython) | 77613 | 38094 | 78641 | 78203 | 9728 | 2026-10-12 04:07:05 |
| [flask](https://github.com/pallets/flask) | 75010 | 17062 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67553 | 27505 | 12321 | 21609 | 2168 | 2026-10-10 08:33:16 |
| [keras](https://github.com/keras-team/keras) | 64362 | 19798 | 12998 | 10049 | 249 | 2026-10-11 04:57:46 |
| [pandas](https://github.com/pandas-dev/pandas) | 50024 | 20486 | 28597 | 39390 | 2286 | 2026-10-12 03:02:58 |
| [ray](https://github.com/ray-project/ray) | 44007 | 8127 | 23154 | 43339 | 3562 | 2026-10-11 11:34:21 |
| [gym](https://github.com/openai/gym) | 37245 | 8668 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33951 | 4731 | 5774 | 4129 | 250 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33068 | 12900 | 14125 | 18747 | 2241 | 2026-10-12 05:38:07 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30202 | 7095 | 3966 | 5090 | 56 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28947 | 5215 | 5331 | 4551 | 750 | 2026-10-10 08:55:44 |
| [dash](https://github.com/plotly/dash) | 24446 | 2329 | 2166 | 1759 | 434 | 2026-10-09 21:04:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23354 | 8502 | 11435 | 20961 | 1495 | 2026-10-11 19:22:47 |
| [RustPython](https://github.com/RustPython/RustPython) | 22393 | 1501 | 1438 | 7545 | 301 | 2026-10-12 04:38:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5570 | 1888 | 1879 | 223 | 2026-10-10 21:27:46 |
| [micropython](https://github.com/micropython/micropython) | 22115 | 9000 | 6140 | 8123 | 1533 | 2026-10-12 04:11:53 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18832 | 2869 | 3389 | 2226 | 730 | 2026-10-09 16:12:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1610 | 1470 | 1684 | 156 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16574 | 2452 | 3263 | 10395 | 226 | 2026-10-11 20:10:03 |
| [httpx](https://github.com/encode/httpx) | 15619 | 3799 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15103 | 6003 | 11683 | 14670 | 1862 | 2026-10-11 07:52:47 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14061 | 2146 | 2663 | 1234 | 244 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1976 | 5563 | 6753 | 1357 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12659 | 1370 | 787 | 2205 | 57 | 2026-10-09 14:25:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12228 | 1810 | 8337 | 1225 | 215 | 2026-10-09 16:52:33 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11911 | 616 | 426 | 338 | 168 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 1038 | 1147 | 1542 | 163 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9209 | 615 | 1050 | 559 | 226 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8794 | 1515 | 867 | 654 | 288 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7345 | 450 | 903 | 2630 | 334 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5632 | 525 | 1275 | 925 | 532 | 2026-10-11 14:57:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5422 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4445 | 384 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 210 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 317 | 677 | 1357 | 277 | 2026-10-11 18:39:23 |
| [anyio](https://github.com/agronholm/anyio) | 2556 | 306 | 489 | 844 | 133 | 2026-10-11 09:11:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1811 | 129 | 5280 | 342 | 714 | 2026-10-12 05:26:16 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-10-11 22:49:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-12T05:40:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
