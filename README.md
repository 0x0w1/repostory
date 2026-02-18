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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193769 | 75230 | 41162 | 67319 | 3592 | 2026-02-18 02:48:58 |
| [transformers](https://github.com/huggingface/transformers) | 156589 | 32120 | 18591 | 24925 | 2282 | 2026-02-17 21:29:44 |
| [pytorch](https://github.com/pytorch/pytorch) | 97474 | 26893 | 56851 | 117858 | 18037 | 2026-02-18 02:51:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 95192 | 8693 | 3503 | 5305 | 140 | 2026-02-17 09:59:37 |
| [django](https://github.com/django/django) | 86786 | 33643 | 0 | 20654 | 415 | 2026-02-16 19:37:49 |
| [cpython](https://github.com/python/cpython) | 71528 | 34088 | 75273 | 68669 | 9240 | 2026-02-17 22:03:22 |
| [flask](https://github.com/pallets/flask) | 71163 | 16715 | 2717 | 2770 | 3 | 2026-02-12 21:59:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65059 | 26701 | 11942 | 20218 | 2132 | 2026-02-17 13:41:44 |
| [keras](https://github.com/keras-team/keras) | 63769 | 19696 | 12635 | 8772 | 279 | 2026-02-18 02:35:37 |
| [pandas](https://github.com/pandas-dev/pandas) | 47902 | 19664 | 28108 | 36038 | 3658 | 2026-02-17 23:57:45 |
| [ray](https://github.com/ray-project/ray) | 41290 | 7230 | 22339 | 38439 | 3372 | 2026-02-18 02:49:43 |
| [gym](https://github.com/openai/gym) | 37042 | 8711 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33215 | 4635 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31454 | 12063 | 13793 | 16986 | 2316 | 2026-02-17 22:45:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29876 | 7066 | 3946 | 4923 | 88 | 2026-02-17 19:39:03 |
| [celery](https://github.com/celery/celery) | 28029 | 4948 | 5195 | 3806 | 771 | 2026-02-17 13:46:34 |
| [dash](https://github.com/plotly/dash) | 24494 | 2255 | 2055 | 1439 | 561 | 2026-02-18 02:38:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22440 | 5545 | 1863 | 1699 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22439 | 8195 | 11154 | 19971 | 1540 | 2026-02-17 18:59:14 |
| [RustPython](https://github.com/RustPython/RustPython) | 21799 | 1401 | 1301 | 5819 | 376 | 2026-02-17 23:21:27 |
| [micropython](https://github.com/micropython/micropython) | 21473 | 8714 | 5957 | 7568 | 1859 | 2026-02-14 08:06:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1583 | 1464 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18257 | 2774 | 3324 | 2036 | 780 | 2026-02-17 19:30:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16263 | 2193 | 3177 | 8600 | 278 | 2026-02-17 20:10:45 |
| [httpx](https://github.com/encode/httpx) | 15005 | 1036 | 925 | 1791 | 136 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14461 | 5618 | 11314 | 13285 | 1775 | 2026-02-17 22:02:48 |
| [dask](https://github.com/dask/dask) | 13743 | 1842 | 5504 | 6489 | 1222 | 2026-02-16 22:55:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13726 | 2079 | 2646 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11927 | 1117 | 763 | 1803 | 49 | 2026-02-15 13:37:42 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11647 | 600 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11518 | 1639 | 8154 | 1031 | 209 | 2026-02-16 15:27:59 |
| [falcon](https://github.com/falconry/falcon) | 9802 | 979 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8901 | 559 | 1014 | 487 | 216 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8758 | 1496 | 861 | 629 | 282 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7169 | 386 | 879 | 2502 | 315 | 2026-02-16 21:37:51 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5496 | 460 | 1230 | 778 | 482 | 2026-02-17 09:08:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5190 | 1000 | 904 | 290 | 195 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4072 | 891 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3961 | 313 | 1181 | 210 | 116 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3598 | 192 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2726 | 309 | 658 | 1276 | 311 | 2026-02-17 14:39:19 |
| [anyio](https://github.com/agronholm/anyio) | 2388 | 182 | 426 | 572 | 78 | 2026-02-15 00:48:12 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1936 | 367 | 1785 | 266 | 266 | 2026-02-16 17:43:15 |
| [pypy](https://github.com/pypy/pypy) | 1651 | 99 | 5176 | 179 | 758 | 2026-02-11 08:06:08 |
| [jython](https://github.com/jython/jython) | 1482 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-18T02:52:40*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
