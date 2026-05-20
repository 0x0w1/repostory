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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195189 | 75317 | 41454 | 73969 | 5424 | 2026-05-20 04:14:02 |
| [transformers](https://github.com/huggingface/transformers) | 160787 | 33274 | 18968 | 26423 | 2350 | 2026-05-20 03:07:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 100025 | 27824 | 58808 | 125084 | 18458 | 2026-05-20 04:18:00 |
| [fastapi](https://github.com/fastapi/fastapi) | 98357 | 9321 | 3527 | 5773 | 189 | 2026-05-19 23:00:33 |
| [django](https://github.com/django/django) | 87513 | 33933 | 0 | 21263 | 444 | 2026-05-19 04:38:07 |
| [cpython](https://github.com/python/cpython) | 72763 | 34664 | 76426 | 71400 | 9313 | 2026-05-20 03:33:22 |
| [flask](https://github.com/pallets/flask) | 71563 | 16852 | 2738 | 2826 | 4 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66123 | 27032 | 12092 | 20793 | 2018 | 2026-05-19 15:17:52 |
| [keras](https://github.com/keras-team/keras) | 64077 | 19778 | 12762 | 9341 | 192 | 2026-05-20 03:02:25 |
| [pandas](https://github.com/pandas-dev/pandas) | 48803 | 19967 | 28288 | 37313 | 3256 | 2026-05-20 02:44:57 |
| [ray](https://github.com/ray-project/ray) | 42597 | 7591 | 22684 | 40465 | 3468 | 2026-05-20 03:22:59 |
| [gym](https://github.com/openai/gym) | 37209 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33589 | 4684 | 5756 | 4092 | 205 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32060 | 12371 | 13921 | 17471 | 2374 | 2026-05-20 02:12:33 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30023 | 7066 | 3967 | 5005 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28502 | 5045 | 5277 | 4114 | 777 | 2026-05-18 16:52:21 |
| [dash](https://github.com/plotly/dash) | 24204 | 2282 | 2100 | 1565 | 556 | 2026-05-19 18:38:23 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22818 | 8340 | 11275 | 20380 | 1482 | 2026-05-19 19:52:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5543 | 1872 | 1735 | 223 | 2026-05-19 22:54:07 |
| [RustPython](https://github.com/RustPython/RustPython) | 22057 | 1439 | 1345 | 6512 | 375 | 2026-05-19 23:59:59 |
| [micropython](https://github.com/micropython/micropython) | 21719 | 8837 | 6056 | 7812 | 1765 | 2026-05-15 09:37:52 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1590 | 1466 | 1684 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18541 | 2808 | 3345 | 2088 | 760 | 2026-05-19 16:56:06 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16442 | 2269 | 3205 | 9120 | 239 | 2026-05-20 00:52:08 |
| [httpx](https://github.com/encode/httpx) | 15274 | 1144 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14708 | 5732 | 11446 | 13713 | 1790 | 2026-05-19 20:13:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13880 | 2113 | 2653 | 1180 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13840 | 1872 | 5528 | 6569 | 1243 | 2026-05-14 21:18:18 |
| [starlette](https://github.com/Kludex/starlette) | 12322 | 1172 | 768 | 1896 | 60 | 2026-05-20 04:13:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11871 | 1685 | 8213 | 1086 | 219 | 2026-05-19 21:40:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11786 | 606 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 998 | 1125 | 1449 | 160 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9059 | 579 | 1035 | 512 | 209 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7269 | 394 | 892 | 2544 | 319 | 2026-05-18 01:23:55 |
| [hug](https://github.com/hugapi/hug) | 6891 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5568 | 481 | 1255 | 835 | 507 | 2026-05-19 21:38:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5259 | 1016 | 913 | 299 | 210 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4143 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2746 | 311 | 663 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2469 | 207 | 439 | 637 | 85 | 2026-05-19 20:06:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 428 | 398 | 28 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1509 | 363 | 2026-05-18 17:53:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-18 17:55:16 |
| [pypy](https://github.com/pypy/pypy) | 1736 | 113 | 5212 | 249 | 741 | 2026-05-19 20:09:45 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 131 | 111 | 2026-05-19 13:32:09 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-18 17:13:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-20T04:18:23*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
