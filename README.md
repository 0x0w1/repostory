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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194917 | 75288 | 41335 | 72285 | 4759 | 2026-04-28 03:55:19 |
| [transformers](https://github.com/huggingface/transformers) | 160010 | 33035 | 18899 | 26119 | 2338 | 2026-04-28 02:56:25 |
| [pytorch](https://github.com/pytorch/pytorch) | 99490 | 27607 | 58300 | 122883 | 18549 | 2026-04-28 03:55:04 |
| [fastapi](https://github.com/fastapi/fastapi) | 97710 | 9164 | 3522 | 5671 | 174 | 2026-04-27 20:25:55 |
| [django](https://github.com/django/django) | 87345 | 33833 | 0 | 21115 | 434 | 2026-04-28 00:58:07 |
| [cpython](https://github.com/python/cpython) | 72489 | 34500 | 76134 | 70654 | 9429 | 2026-04-28 02:51:07 |
| [flask](https://github.com/pallets/flask) | 71454 | 16819 | 2735 | 2813 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65934 | 26979 | 12058 | 20650 | 2050 | 2026-04-27 16:52:36 |
| [keras](https://github.com/keras-team/keras) | 64048 | 19761 | 12741 | 9236 | 252 | 2026-04-28 02:32:11 |
| [pandas](https://github.com/pandas-dev/pandas) | 48593 | 19881 | 28262 | 37050 | 3427 | 2026-04-28 02:35:44 |
| [ray](https://github.com/ray-project/ray) | 42339 | 7508 | 22618 | 40010 | 3575 | 2026-04-28 02:31:54 |
| [gym](https://github.com/openai/gym) | 37176 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33519 | 4675 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31915 | 12318 | 13893 | 17379 | 2378 | 2026-04-27 23:12:52 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29991 | 7067 | 3968 | 5002 | 80 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28415 | 5024 | 5271 | 4096 | 778 | 2026-04-27 16:52:24 |
| [dash](https://github.com/plotly/dash) | 24153 | 2276 | 2092 | 1545 | 544 | 2026-04-27 21:02:43 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22744 | 8325 | 11253 | 20266 | 1499 | 2026-04-25 05:28:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22222 | 5540 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22024 | 1430 | 1335 | 6303 | 379 | 2026-04-28 02:22:32 |
| [micropython](https://github.com/micropython/micropython) | 21662 | 8810 | 6041 | 7756 | 1888 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18483 | 2803 | 3340 | 2078 | 763 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16423 | 2260 | 3191 | 8910 | 280 | 2026-04-28 00:43:55 |
| [httpx](https://github.com/encode/httpx) | 15243 | 1135 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14645 | 5714 | 11425 | 13630 | 1787 | 2026-04-25 06:20:56 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13829 | 2103 | 2653 | 1172 | 215 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13809 | 1867 | 5522 | 6533 | 1248 | 2026-04-28 00:58:06 |
| [starlette](https://github.com/Kludex/starlette) | 12247 | 1162 | 766 | 1884 | 60 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11800 | 1677 | 8200 | 1064 | 214 | 2026-04-24 21:39:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11775 | 604 | 413 | 323 | 167 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 996 | 1125 | 1443 | 158 | 2026-04-26 06:35:15 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9030 | 571 | 1032 | 506 | 203 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8754 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7249 | 393 | 890 | 2537 | 320 | 2026-04-27 22:22:52 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5563 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5248 | 1008 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4099 | 330 | 1183 | 218 | 113 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3627 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2447 | 201 | 436 | 619 | 87 | 2026-04-27 18:00:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 905 | 1083 | 1479 | 364 | 2026-04-28 03:10:21 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-27 17:52:32 |
| [pypy](https://github.com/pypy/pypy) | 1714 | 112 | 5201 | 228 | 743 | 2026-04-27 19:35:48 |
| [jython](https://github.com/jython/jython) | 1504 | 228 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-04-26 08:05:46 |

*Last Automatic Update: 2026-04-28T03:55:38*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
