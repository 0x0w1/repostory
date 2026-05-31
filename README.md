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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195316 | 75331 | 41473 | 74825 | 2977 | 2026-05-31 04:32:15 |
| [transformers](https://github.com/huggingface/transformers) | 161084 | 33371 | 19015 | 26581 | 2380 | 2026-05-31 03:52:24 |
| [pytorch](https://github.com/pytorch/pytorch) | 100283 | 27896 | 58990 | 126149 | 18359 | 2026-05-31 04:36:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 98687 | 9355 | 3529 | 5829 | 91 | 2026-05-30 17:18:40 |
| [django](https://github.com/django/django) | 87588 | 33968 | 0 | 21314 | 447 | 2026-05-29 15:46:53 |
| [cpython](https://github.com/python/cpython) | 72920 | 34693 | 76547 | 71778 | 9316 | 2026-05-31 04:22:18 |
| [flask](https://github.com/pallets/flask) | 71581 | 16838 | 2738 | 2831 | 3 | 2026-05-18 23:35:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66204 | 27042 | 12117 | 20861 | 2036 | 2026-05-29 15:59:40 |
| [keras](https://github.com/keras-team/keras) | 64075 | 19750 | 12771 | 9384 | 177 | 2026-05-29 23:07:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 48878 | 19965 | 28296 | 37373 | 3233 | 2026-05-30 22:52:04 |
| [ray](https://github.com/ray-project/ray) | 42718 | 7616 | 22704 | 40652 | 3459 | 2026-05-30 23:17:02 |
| [gym](https://github.com/openai/gym) | 37205 | 8700 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33618 | 4687 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32113 | 12401 | 13930 | 17532 | 2383 | 2026-05-30 02:36:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30039 | 7065 | 3967 | 5007 | 76 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28535 | 5056 | 5280 | 4125 | 783 | 2026-05-30 08:13:32 |
| [dash](https://github.com/plotly/dash) | 24222 | 2285 | 2103 | 1574 | 549 | 2026-05-29 17:03:25 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22847 | 8349 | 11292 | 20439 | 1481 | 2026-05-30 18:51:37 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5540 | 1872 | 1739 | 219 | 2026-05-29 19:53:03 |
| [RustPython](https://github.com/RustPython/RustPython) | 22086 | 1441 | 1348 | 6576 | 380 | 2026-05-30 11:16:49 |
| [micropython](https://github.com/micropython/micropython) | 21761 | 8845 | 6064 | 7833 | 1710 | 2026-05-29 08:50:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1590 | 1467 | 1686 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18564 | 2806 | 3347 | 2089 | 758 | 2026-05-21 04:07:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16432 | 2281 | 3209 | 9198 | 246 | 2026-05-30 20:51:38 |
| [httpx](https://github.com/encode/httpx) | 15280 | 1157 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14723 | 5744 | 11454 | 13789 | 1794 | 2026-05-31 04:04:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13896 | 2117 | 2653 | 1183 | 223 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1875 | 5533 | 6588 | 1239 | 2026-05-29 17:07:12 |
| [starlette](https://github.com/Kludex/starlette) | 12349 | 1186 | 769 | 1924 | 58 | 2026-05-31 01:07:04 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11872 | 1692 | 8219 | 1097 | 210 | 2026-05-30 14:13:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11802 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 997 | 1126 | 1451 | 159 | 2026-05-29 20:52:08 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9072 | 581 | 1036 | 515 | 212 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1504 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7272 | 398 | 892 | 2548 | 321 | 2026-05-25 21:57:42 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5597 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5572 | 485 | 1257 | 842 | 515 | 2026-05-20 14:48:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5269 | 1017 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4166 | 334 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3637 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2473 | 206 | 440 | 643 | 82 | 2026-05-30 20:54:50 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1527 | 371 | 2026-05-25 20:08:57 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-05-25 17:51:18 |
| [pypy](https://github.com/pypy/pypy) | 1741 | 113 | 5215 | 253 | 738 | 2026-05-29 15:35:23 |
| [jython](https://github.com/jython/jython) | 1512 | 230 | 296 | 132 | 108 | 2026-05-27 06:12:49 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2026-05-24 21:15:00 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-31T04:42:50*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
