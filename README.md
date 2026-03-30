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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194382 | 75253 | 41288 | 70050 | 4059 | 2026-03-30 03:07:02 |
| [transformers](https://github.com/huggingface/transformers) | 158533 | 32673 | 18795 | 25679 | 2328 | 2026-03-28 10:24:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 98637 | 27339 | 57538 | 120667 | 18115 | 2026-03-30 02:57:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 96666 | 8965 | 3517 | 5537 | 171 | 2026-03-29 04:27:55 |
| [django](https://github.com/django/django) | 87129 | 33808 | 0 | 20955 | 425 | 2026-03-28 17:40:50 |
| [cpython](https://github.com/python/cpython) | 72114 | 34329 | 75742 | 69827 | 9342 | 2026-03-30 03:08:19 |
| [flask](https://github.com/pallets/flask) | 71355 | 16757 | 2726 | 2795 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65544 | 26861 | 12019 | 20479 | 2133 | 2026-03-27 17:18:05 |
| [keras](https://github.com/keras-team/keras) | 63917 | 19744 | 12718 | 9067 | 315 | 2026-03-29 17:05:31 |
| [pandas](https://github.com/pandas-dev/pandas) | 48275 | 19792 | 28213 | 36629 | 3542 | 2026-03-29 18:18:19 |
| [ray](https://github.com/ray-project/ray) | 41868 | 7394 | 22505 | 39313 | 3541 | 2026-03-30 00:59:27 |
| [gym](https://github.com/openai/gym) | 37117 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33396 | 4665 | 5749 | 4087 | 193 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31682 | 12213 | 13856 | 17180 | 2341 | 2026-03-29 19:54:34 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29941 | 7075 | 3947 | 4952 | 77 | 2026-03-29 09:57:51 |
| [celery](https://github.com/celery/celery) | 28267 | 4997 | 5209 | 3880 | 765 | 2026-03-28 10:18:19 |
| [dash](https://github.com/plotly/dash) | 24493 | 2269 | 2082 | 1502 | 599 | 2026-03-27 15:27:58 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22651 | 8299 | 11223 | 20152 | 1538 | 2026-03-29 16:32:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22410 | 5546 | 1865 | 1723 | 211 | 2026-03-26 17:59:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 21922 | 1415 | 1324 | 6138 | 367 | 2026-03-30 00:49:26 |
| [micropython](https://github.com/micropython/micropython) | 21587 | 8763 | 6001 | 7668 | 1851 | 2026-03-26 19:16:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18398 | 2790 | 3333 | 2063 | 774 | 2026-03-27 21:03:58 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16356 | 2233 | 3183 | 8791 | 278 | 2026-03-30 00:18:55 |
| [httpx](https://github.com/encode/httpx) | 15132 | 1093 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14572 | 5677 | 11393 | 13527 | 1787 | 2026-03-29 21:18:47 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13784 | 2091 | 2650 | 1168 | 212 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13779 | 1858 | 5517 | 6511 | 1233 | 2026-03-24 00:04:43 |
| [starlette](https://github.com/Kludex/starlette) | 12143 | 1147 | 766 | 1845 | 49 | 2026-03-29 06:31:20 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11729 | 607 | 411 | 319 | 162 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11683 | 1662 | 8180 | 1053 | 214 | 2026-03-29 17:10:26 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 982 | 1119 | 1422 | 162 | 2026-03-28 18:33:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8980 | 567 | 1025 | 498 | 219 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1501 | 863 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7219 | 394 | 882 | 2518 | 316 | 2026-03-23 22:25:09 |
| [hug](https://github.com/hugapi/hug) | 6901 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5603 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5534 | 470 | 1243 | 810 | 500 | 2026-03-28 08:03:42 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5221 | 1004 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2735 | 85 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4038 | 325 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4012 | 258 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3614 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 312 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2424 | 189 | 431 | 595 | 82 | 2026-03-29 10:12:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 367 | 1785 | 267 | 267 | 2026-03-23 17:46:41 |
| [pypy](https://github.com/pypy/pypy) | 1695 | 109 | 5188 | 191 | 763 | 2026-03-30 02:51:16 |
| [jython](https://github.com/jython/jython) | 1497 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-30T03:29:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
