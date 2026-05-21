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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195208 | 75313 | 41455 | 74108 | 5510 | 2026-05-21 04:25:49 |
| [transformers](https://github.com/huggingface/transformers) | 160817 | 33280 | 18975 | 26453 | 2369 | 2026-05-20 14:02:23 |
| [pytorch](https://github.com/pytorch/pytorch) | 100041 | 27832 | 58839 | 125223 | 18492 | 2026-05-21 04:26:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 98379 | 9322 | 3528 | 5775 | 189 | 2026-05-20 20:37:19 |
| [django](https://github.com/django/django) | 87512 | 33933 | 0 | 21272 | 443 | 2026-05-20 20:17:41 |
| [cpython](https://github.com/python/cpython) | 72782 | 34673 | 76433 | 71422 | 9312 | 2026-05-20 20:10:21 |
| [flask](https://github.com/pallets/flask) | 71567 | 16850 | 2738 | 2826 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66124 | 27026 | 12097 | 20800 | 2020 | 2026-05-20 14:42:15 |
| [keras](https://github.com/keras-team/keras) | 64074 | 19773 | 12762 | 9343 | 191 | 2026-05-20 16:40:08 |
| [pandas](https://github.com/pandas-dev/pandas) | 48812 | 19968 | 28288 | 37320 | 3259 | 2026-05-20 21:22:11 |
| [ray](https://github.com/ray-project/ray) | 42614 | 7594 | 22687 | 40492 | 3461 | 2026-05-21 01:36:17 |
| [gym](https://github.com/openai/gym) | 37207 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33592 | 4684 | 5756 | 4093 | 206 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32067 | 12373 | 13923 | 17478 | 2377 | 2026-05-20 22:05:04 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30023 | 7066 | 3967 | 5005 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28508 | 5045 | 5278 | 4114 | 776 | 2026-05-20 12:26:36 |
| [dash](https://github.com/plotly/dash) | 24202 | 2283 | 2101 | 1565 | 556 | 2026-05-20 21:19:31 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22822 | 8339 | 11276 | 20384 | 1479 | 2026-05-19 19:52:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5542 | 1872 | 1735 | 222 | 2026-05-20 17:34:31 |
| [RustPython](https://github.com/RustPython/RustPython) | 22058 | 1440 | 1346 | 6523 | 376 | 2026-05-21 00:59:41 |
| [micropython](https://github.com/micropython/micropython) | 21719 | 8838 | 6056 | 7815 | 1755 | 2026-05-20 14:41:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1590 | 1466 | 1684 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18545 | 2808 | 3345 | 2088 | 759 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2270 | 3205 | 9131 | 239 | 2026-05-20 18:31:23 |
| [httpx](https://github.com/encode/httpx) | 15279 | 1145 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14709 | 5732 | 11446 | 13719 | 1794 | 2026-05-20 14:22:41 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13882 | 2113 | 2653 | 1180 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13842 | 1872 | 5528 | 6570 | 1244 | 2026-05-14 21:18:18 |
| [starlette](https://github.com/Kludex/starlette) | 12321 | 1172 | 768 | 1896 | 59 | 2026-05-20 06:12:32 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11872 | 1687 | 8216 | 1089 | 214 | 2026-05-20 21:02:50 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11787 | 607 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 998 | 1125 | 1449 | 160 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9062 | 580 | 1035 | 512 | 209 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8765 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7269 | 395 | 892 | 2544 | 319 | 2026-05-18 01:23:55 |
| [hug](https://github.com/hugapi/hug) | 6891 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5569 | 483 | 1256 | 836 | 508 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5261 | 1016 | 913 | 299 | 210 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4145 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2746 | 311 | 663 | 1316 | 306 | 2026-05-15 23:21:12 |
| [anyio](https://github.com/agronholm/anyio) | 2468 | 207 | 439 | 637 | 85 | 2026-05-19 20:06:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 428 | 399 | 29 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1512 | 366 | 2026-05-18 17:53:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-18 17:55:16 |
| [pypy](https://github.com/pypy/pypy) | 1736 | 113 | 5213 | 249 | 741 | 2026-05-21 03:47:42 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 131 | 111 | 2026-05-19 13:32:09 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-18 17:13:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-21T04:26:38*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
