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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194882 | 75281 | 41333 | 72134 | 4675 | 2026-04-26 03:41:32 |
| [transformers](https://github.com/huggingface/transformers) | 159925 | 33014 | 18896 | 26103 | 2359 | 2026-04-25 04:00:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 99440 | 27594 | 58246 | 122728 | 18570 | 2026-04-26 03:45:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 97648 | 9158 | 3522 | 5663 | 173 | 2026-04-26 01:23:24 |
| [django](https://github.com/django/django) | 87334 | 33831 | 0 | 21112 | 437 | 2026-04-25 14:52:10 |
| [cpython](https://github.com/python/cpython) | 72449 | 34495 | 76107 | 70603 | 9413 | 2026-04-25 23:02:51 |
| [flask](https://github.com/pallets/flask) | 71451 | 16814 | 2735 | 2813 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65922 | 26975 | 12052 | 20635 | 2039 | 2026-04-25 15:44:11 |
| [keras](https://github.com/keras-team/keras) | 64039 | 19761 | 12740 | 9233 | 257 | 2026-04-25 22:52:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 48576 | 19877 | 28257 | 37030 | 3413 | 2026-04-25 14:26:22 |
| [ray](https://github.com/ray-project/ray) | 42311 | 7501 | 22609 | 39981 | 3575 | 2026-04-26 01:10:25 |
| [gym](https://github.com/openai/gym) | 37174 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33512 | 4676 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31894 | 12315 | 13890 | 17369 | 2374 | 2026-04-25 21:34:26 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29990 | 7066 | 3968 | 5002 | 80 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28409 | 5021 | 5271 | 4089 | 776 | 2026-04-23 22:23:41 |
| [dash](https://github.com/plotly/dash) | 24149 | 2276 | 2092 | 1544 | 544 | 2026-04-24 20:51:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22734 | 8324 | 11251 | 20265 | 1496 | 2026-04-25 05:28:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22221 | 5541 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22025 | 1429 | 1335 | 6280 | 372 | 2026-04-26 03:33:35 |
| [micropython](https://github.com/micropython/micropython) | 21655 | 8806 | 6041 | 7754 | 1888 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18480 | 2803 | 3340 | 2078 | 763 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16420 | 2260 | 3191 | 8903 | 280 | 2026-04-24 10:57:52 |
| [httpx](https://github.com/encode/httpx) | 15234 | 1129 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14634 | 5710 | 11424 | 13627 | 1787 | 2026-04-25 06:20:56 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13828 | 2103 | 2653 | 1172 | 215 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13807 | 1867 | 5522 | 6532 | 1247 | 2026-04-22 10:20:36 |
| [starlette](https://github.com/Kludex/starlette) | 12237 | 1160 | 766 | 1883 | 59 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11794 | 1676 | 8199 | 1064 | 214 | 2026-04-24 21:39:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11772 | 605 | 413 | 323 | 167 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 991 | 1125 | 1438 | 159 | 2026-04-25 09:29:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9027 | 571 | 1032 | 506 | 203 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8753 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7248 | 393 | 890 | 2536 | 320 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5561 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5245 | 1008 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4094 | 330 | 1183 | 218 | 113 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3626 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2444 | 201 | 435 | 617 | 85 | 2026-04-24 10:56:29 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 904 | 1083 | 1478 | 365 | 2026-04-24 15:15:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1714 | 112 | 5200 | 227 | 744 | 2026-04-25 18:14:38 |
| [jython](https://github.com/jython/jython) | 1501 | 228 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-04-25 21:17:27 |

*Last Automatic Update: 2026-04-26T03:46:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
