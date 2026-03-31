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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194395 | 75254 | 41290 | 70136 | 4066 | 2026-03-31 03:04:45 |
| [transformers](https://github.com/huggingface/transformers) | 158568 | 32689 | 18798 | 25703 | 2324 | 2026-03-31 03:01:21 |
| [pytorch](https://github.com/pytorch/pytorch) | 98666 | 27354 | 57564 | 120761 | 18166 | 2026-03-31 03:12:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 96690 | 8966 | 3517 | 5539 | 170 | 2026-03-30 19:51:47 |
| [django](https://github.com/django/django) | 87124 | 33811 | 0 | 20969 | 423 | 2026-03-30 19:56:52 |
| [cpython](https://github.com/python/cpython) | 72126 | 34334 | 75749 | 69844 | 9323 | 2026-03-30 21:03:47 |
| [flask](https://github.com/pallets/flask) | 71360 | 16760 | 2726 | 2795 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65561 | 26864 | 12019 | 20485 | 2129 | 2026-03-30 15:45:03 |
| [keras](https://github.com/keras-team/keras) | 63924 | 19746 | 12718 | 9068 | 302 | 2026-03-30 20:41:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 48295 | 19804 | 28214 | 36652 | 3529 | 2026-03-31 00:24:28 |
| [ray](https://github.com/ray-project/ray) | 41884 | 7397 | 22510 | 39359 | 3572 | 2026-03-31 02:14:54 |
| [gym](https://github.com/openai/gym) | 37120 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33395 | 4665 | 5750 | 4087 | 194 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31697 | 12216 | 13857 | 17183 | 2339 | 2026-03-31 00:13:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29941 | 7074 | 3947 | 4952 | 77 | 2026-03-29 09:57:51 |
| [celery](https://github.com/celery/celery) | 28273 | 4997 | 5209 | 3881 | 764 | 2026-03-30 11:10:48 |
| [dash](https://github.com/plotly/dash) | 24428 | 2269 | 2082 | 1503 | 599 | 2026-03-30 18:33:10 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22651 | 8298 | 11223 | 20153 | 1528 | 2026-03-31 02:41:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22385 | 5546 | 1865 | 1724 | 211 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21929 | 1416 | 1325 | 6152 | 369 | 2026-03-30 16:38:03 |
| [micropython](https://github.com/micropython/micropython) | 21588 | 8767 | 6003 | 7674 | 1858 | 2026-03-31 01:39:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18402 | 2791 | 3334 | 2063 | 771 | 2026-03-30 19:12:25 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16358 | 2233 | 3184 | 8794 | 276 | 2026-03-31 00:48:16 |
| [httpx](https://github.com/encode/httpx) | 15131 | 1095 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14575 | 5676 | 11394 | 13533 | 1786 | 2026-03-30 23:30:27 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13785 | 2091 | 2651 | 1168 | 213 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13776 | 1858 | 5517 | 6512 | 1234 | 2026-03-30 22:35:39 |
| [starlette](https://github.com/Kludex/starlette) | 12151 | 1146 | 766 | 1846 | 50 | 2026-03-30 19:51:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11731 | 607 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11684 | 1662 | 8181 | 1053 | 215 | 2026-03-29 17:10:26 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 982 | 1119 | 1422 | 162 | 2026-03-28 18:33:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8981 | 567 | 1025 | 498 | 219 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8767 | 1501 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7218 | 394 | 882 | 2519 | 316 | 2026-03-30 22:03:16 |
| [hug](https://github.com/hugapi/hug) | 6899 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5602 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5534 | 470 | 1243 | 811 | 501 | 2026-03-30 19:56:27 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5221 | 1004 | 909 | 291 | 200 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2735 | 85 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4043 | 325 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4011 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3614 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2737 | 311 | 664 | 1304 | 307 | 2026-03-30 12:47:05 |
| [anyio](https://github.com/agronholm/anyio) | 2425 | 189 | 431 | 596 | 82 | 2026-03-30 19:08:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 367 | 1785 | 267 | 267 | 2026-03-30 17:40:37 |
| [pypy](https://github.com/pypy/pypy) | 1695 | 109 | 5189 | 191 | 764 | 2026-03-30 20:29:49 |
| [jython](https://github.com/jython/jython) | 1498 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-31T03:20:46*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
