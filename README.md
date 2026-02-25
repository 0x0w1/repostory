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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193902 | 75226 | 41170 | 67715 | 3520 | 2026-02-25 02:49:55 |
| [transformers](https://github.com/huggingface/transformers) | 156926 | 32188 | 18618 | 25046 | 2278 | 2026-02-24 22:12:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 97726 | 26978 | 56926 | 118263 | 17974 | 2026-02-25 02:46:12 |
| [fastapi](https://github.com/fastapi/fastapi) | 95538 | 8746 | 3505 | 5354 | 154 | 2026-02-24 21:29:01 |
| [django](https://github.com/django/django) | 86924 | 33682 | 0 | 20698 | 423 | 2026-02-24 23:41:17 |
| [cpython](https://github.com/python/cpython) | 71695 | 34128 | 75349 | 68847 | 9250 | 2026-02-25 00:53:01 |
| [flask](https://github.com/pallets/flask) | 71261 | 16734 | 2722 | 2779 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65212 | 26733 | 11969 | 20282 | 2153 | 2026-02-24 13:28:21 |
| [keras](https://github.com/keras-team/keras) | 63863 | 19706 | 12644 | 8838 | 278 | 2026-02-25 02:37:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 47968 | 19697 | 28134 | 36097 | 3671 | 2026-02-24 21:39:44 |
| [ray](https://github.com/ray-project/ray) | 41468 | 7251 | 22363 | 38583 | 3401 | 2026-02-25 02:35:46 |
| [gym](https://github.com/openai/gym) | 37054 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33240 | 4639 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31502 | 12078 | 13802 | 17010 | 2318 | 2026-02-24 21:40:32 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29896 | 7069 | 3946 | 4928 | 81 | 2026-02-24 14:23:59 |
| [celery](https://github.com/celery/celery) | 28145 | 4962 | 5196 | 3822 | 776 | 2026-02-23 18:02:54 |
| [dash](https://github.com/plotly/dash) | 24514 | 2258 | 2063 | 1444 | 566 | 2026-02-24 22:36:42 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22494 | 8215 | 11163 | 19986 | 1546 | 2026-02-23 21:41:41 |
| [tornado](https://github.com/tornadoweb/tornado) | 22445 | 5547 | 1863 | 1702 | 216 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21816 | 1403 | 1304 | 5848 | 381 | 2026-02-24 15:37:53 |
| [micropython](https://github.com/micropython/micropython) | 21487 | 8725 | 5962 | 7584 | 1845 | 2026-02-24 13:27:50 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18278 | 2778 | 3324 | 2046 | 779 | 2026-02-24 23:31:20 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16362 | 2204 | 3178 | 8653 | 269 | 2026-02-24 19:48:27 |
| [httpx](https://github.com/encode/httpx) | 15108 | 1045 | 925 | 1803 | 146 | 2026-02-23 10:40:42 |
| [scipy](https://github.com/scipy/scipy) | 14483 | 5625 | 11331 | 13329 | 1772 | 2026-02-24 21:19:38 |
| [dask](https://github.com/dask/dask) | 13746 | 1847 | 5508 | 6498 | 1232 | 2026-02-22 23:28:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13742 | 2080 | 2647 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11970 | 1121 | 763 | 1811 | 48 | 2026-02-23 22:17:04 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11659 | 602 | 403 | 314 | 151 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11634 | 1641 | 8158 | 1035 | 211 | 2026-02-24 16:47:01 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 980 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8920 | 558 | 1016 | 487 | 218 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8765 | 1498 | 861 | 631 | 284 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7176 | 387 | 880 | 2507 | 316 | 2026-02-23 22:21:21 |
| [hug](https://github.com/hugapi/hug) | 6909 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6754 | 737 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5610 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5506 | 461 | 1233 | 780 | 486 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5193 | 1001 | 907 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4074 | 893 | 1063 | 2728 | 80 | 2026-02-24 23:01:36 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3973 | 317 | 1180 | 213 | 114 | 2026-02-23 22:58:28 |
| [quart](https://github.com/pallets/quart) | 3600 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2730 | 310 | 660 | 1282 | 310 | 2026-02-24 02:46:22 |
| [anyio](https://github.com/agronholm/anyio) | 2398 | 183 | 426 | 577 | 81 | 2026-02-24 01:03:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 907 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-02-23 17:52:49 |
| [pypy](https://github.com/pypy/pypy) | 1657 | 99 | 5176 | 179 | 757 | 2026-02-19 08:17:00 |
| [jython](https://github.com/jython/jython) | 1486 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-25T02:51:31*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
