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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195307 | 75321 | 41473 | 74797 | 2957 | 2026-05-30 03:41:56 |
| [transformers](https://github.com/huggingface/transformers) | 161054 | 33358 | 19010 | 26575 | 2371 | 2026-05-30 02:54:14 |
| [pytorch](https://github.com/pytorch/pytorch) | 100267 | 27887 | 58985 | 126105 | 18345 | 2026-05-30 04:06:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 98655 | 9348 | 3529 | 5823 | 89 | 2026-05-28 10:49:02 |
| [django](https://github.com/django/django) | 87582 | 33954 | 0 | 21310 | 446 | 2026-05-29 15:46:53 |
| [cpython](https://github.com/python/cpython) | 72905 | 34686 | 76535 | 71740 | 9318 | 2026-05-29 21:48:10 |
| [flask](https://github.com/pallets/flask) | 71585 | 16837 | 2739 | 2832 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66204 | 27042 | 12117 | 20861 | 2037 | 2026-05-29 15:59:40 |
| [keras](https://github.com/keras-team/keras) | 64073 | 19751 | 12771 | 9382 | 175 | 2026-05-29 23:07:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 48872 | 19961 | 28296 | 37367 | 3227 | 2026-05-29 21:26:56 |
| [ray](https://github.com/ray-project/ray) | 42709 | 7612 | 22704 | 40649 | 3456 | 2026-05-30 03:03:41 |
| [gym](https://github.com/openai/gym) | 37205 | 8699 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33620 | 4688 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32110 | 12398 | 13929 | 17530 | 2381 | 2026-05-30 02:36:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30037 | 7065 | 3967 | 5007 | 76 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28532 | 5056 | 5280 | 4125 | 785 | 2026-05-25 05:31:20 |
| [dash](https://github.com/plotly/dash) | 24220 | 2285 | 2102 | 1573 | 547 | 2026-05-29 17:03:25 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22845 | 8347 | 11289 | 20436 | 1482 | 2026-05-30 03:59:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5540 | 1872 | 1739 | 219 | 2026-05-29 19:53:03 |
| [RustPython](https://github.com/RustPython/RustPython) | 22085 | 1441 | 1348 | 6573 | 379 | 2026-05-28 06:37:44 |
| [micropython](https://github.com/micropython/micropython) | 21753 | 8846 | 6062 | 7831 | 1708 | 2026-05-29 08:50:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1590 | 1467 | 1686 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18562 | 2806 | 3347 | 2089 | 758 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16432 | 2278 | 3207 | 9189 | 248 | 2026-05-29 19:59:49 |
| [httpx](https://github.com/encode/httpx) | 15276 | 1156 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14725 | 5743 | 11452 | 13780 | 1794 | 2026-05-29 18:50:00 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13893 | 2115 | 2653 | 1183 | 223 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1875 | 5533 | 6588 | 1239 | 2026-05-29 17:07:12 |
| [starlette](https://github.com/Kludex/starlette) | 12348 | 1184 | 769 | 1920 | 64 | 2026-05-28 11:40:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11871 | 1692 | 8219 | 1096 | 211 | 2026-05-28 16:37:17 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11797 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 998 | 1126 | 1451 | 158 | 2026-05-29 20:52:08 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9073 | 582 | 1036 | 515 | 212 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1504 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7273 | 397 | 892 | 2547 | 321 | 2026-05-25 21:57:42 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5572 | 484 | 1257 | 841 | 514 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5269 | 1017 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4165 | 334 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3637 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2473 | 206 | 439 | 642 | 81 | 2026-05-27 16:04:06 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1524 | 368 | 2026-05-25 20:08:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-05-25 17:51:18 |
| [pypy](https://github.com/pypy/pypy) | 1741 | 113 | 5214 | 252 | 739 | 2026-05-29 15:35:23 |
| [jython](https://github.com/jython/jython) | 1511 | 230 | 296 | 132 | 108 | 2026-05-27 06:12:49 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-30T04:08:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
