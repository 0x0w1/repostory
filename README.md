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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195840 | 75186 | 41563 | 76683 | 3528 | 2026-06-23 04:11:28 |
| [transformers](https://github.com/huggingface/transformers) | 161823 | 33570 | 19096 | 27015 | 2437 | 2026-06-23 03:24:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 100963 | 28093 | 59364 | 127927 | 18323 | 2026-06-23 03:57:33 |
| [fastapi](https://github.com/fastapi/fastapi) | 99546 | 9468 | 3535 | 5959 | 98 | 2026-06-21 19:39:50 |
| [django](https://github.com/django/django) | 87943 | 33857 | 0 | 21459 | 454 | 2026-06-22 19:01:45 |
| [cpython](https://github.com/python/cpython) | 73370 | 34761 | 76843 | 72782 | 9384 | 2026-06-23 03:59:25 |
| [flask](https://github.com/pallets/flask) | 71702 | 16875 | 2751 | 2839 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66397 | 27090 | 12156 | 21030 | 2093 | 2026-06-22 16:32:24 |
| [keras](https://github.com/keras-team/keras) | 64100 | 19738 | 12805 | 9487 | 223 | 2026-06-18 23:13:32 |
| [pandas](https://github.com/pandas-dev/pandas) | 49038 | 20028 | 28332 | 37554 | 3203 | 2026-06-22 23:30:54 |
| [ray](https://github.com/ray-project/ray) | 42975 | 7714 | 22763 | 41116 | 3484 | 2026-06-23 03:04:42 |
| [gym](https://github.com/openai/gym) | 37225 | 8702 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33688 | 4689 | 5760 | 4098 | 215 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32238 | 12471 | 13952 | 17683 | 2392 | 2026-06-23 03:10:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30083 | 7071 | 3967 | 5021 | 85 | 2026-06-16 19:13:19 |
| [celery](https://github.com/celery/celery) | 28619 | 5081 | 5282 | 4156 | 791 | 2026-06-20 17:30:01 |
| [dash](https://github.com/plotly/dash) | 24268 | 2300 | 2117 | 1596 | 555 | 2026-06-22 17:49:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22918 | 8355 | 11326 | 20549 | 1463 | 2026-06-19 19:16:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22185 | 5531 | 1873 | 1754 | 216 | 2026-06-22 19:29:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22132 | 1448 | 1357 | 6722 | 390 | 2026-06-22 13:57:48 |
| [micropython](https://github.com/micropython/micropython) | 21826 | 8883 | 6071 | 7891 | 1634 | 2026-06-23 03:15:05 |
| [sanic](https://github.com/sanic-org/sanic) | 18624 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18620 | 2814 | 3364 | 2098 | 769 | 2026-06-22 22:58:40 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16461 | 2334 | 3215 | 9426 | 217 | 2026-06-23 01:53:39 |
| [httpx](https://github.com/encode/httpx) | 15312 | 1181 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14769 | 5772 | 11494 | 13954 | 1815 | 2026-06-22 16:23:31 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13923 | 2115 | 2655 | 1185 | 226 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13852 | 1892 | 5539 | 6625 | 1247 | 2026-06-23 01:44:36 |
| [starlette](https://github.com/Kludex/starlette) | 12415 | 1204 | 770 | 1952 | 46 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11941 | 1700 | 8233 | 1120 | 211 | 2026-06-22 23:28:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11831 | 609 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9793 | 1002 | 1130 | 1465 | 162 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9103 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1502 | 864 | 635 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7278 | 397 | 892 | 2554 | 319 | 2026-06-22 22:13:40 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6741 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5588 | 489 | 1259 | 859 | 519 | 2026-06-18 15:20:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5298 | 1023 | 914 | 307 | 208 | 2026-06-19 16:35:32 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4214 | 341 | 1185 | 226 | 118 | 2026-06-22 11:24:56 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 890 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 312 | 672 | 1334 | 308 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2485 | 212 | 446 | 663 | 88 | 2026-06-22 23:43:50 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1084 | 1548 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 268 | 266 | 2026-06-22 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1755 | 116 | 5226 | 263 | 735 | 2026-06-22 21:30:42 |
| [jython](https://github.com/jython/jython) | 1518 | 230 | 297 | 137 | 111 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-23T04:12:37*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
