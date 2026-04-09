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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194581 | 75256 | 41292 | 70728 | 4237 | 2026-04-09 03:11:56 |
| [transformers](https://github.com/huggingface/transformers) | 159053 | 32801 | 18842 | 25846 | 2388 | 2026-04-09 01:50:17 |
| [pytorch](https://github.com/pytorch/pytorch) | 98936 | 27441 | 57727 | 121531 | 18253 | 2026-04-09 03:15:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 96983 | 9038 | 3513 | 5564 | 167 | 2026-04-08 20:54:23 |
| [django](https://github.com/django/django) | 87215 | 33810 | 0 | 21007 | 425 | 2026-04-08 21:30:06 |
| [cpython](https://github.com/python/cpython) | 72221 | 34370 | 75876 | 70117 | 9332 | 2026-04-08 23:34:46 |
| [flask](https://github.com/pallets/flask) | 71388 | 16775 | 2728 | 2799 | 3 | 2026-04-05 19:32:20 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65712 | 26908 | 12025 | 20523 | 2052 | 2026-04-08 13:29:03 |
| [keras](https://github.com/keras-team/keras) | 63944 | 19740 | 12727 | 9128 | 264 | 2026-04-09 01:10:16 |
| [pandas](https://github.com/pandas-dev/pandas) | 48416 | 19859 | 28234 | 36814 | 3477 | 2026-04-07 17:21:35 |
| [ray](https://github.com/ray-project/ray) | 42033 | 7420 | 22548 | 39549 | 3580 | 2026-04-09 03:10:49 |
| [gym](https://github.com/openai/gym) | 37147 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33427 | 4669 | 5750 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31772 | 12275 | 13866 | 17248 | 2343 | 2026-04-09 01:51:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29955 | 7069 | 3968 | 4997 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28315 | 5005 | 5266 | 4064 | 781 | 2026-04-07 12:54:55 |
| [dash](https://github.com/plotly/dash) | 24444 | 2272 | 2086 | 1522 | 545 | 2026-04-08 23:44:06 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22694 | 8314 | 11235 | 20188 | 1535 | 2026-04-08 21:04:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22387 | 5544 | 1869 | 1727 | 215 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21988 | 1423 | 1327 | 6172 | 373 | 2026-04-06 14:30:16 |
| [micropython](https://github.com/micropython/micropython) | 21616 | 8785 | 6015 | 7702 | 1864 | 2026-04-09 01:53:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1465 | 1679 | 130 | 2026-04-08 17:22:24 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18432 | 2794 | 3339 | 2065 | 773 | 2026-04-07 20:15:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16386 | 2242 | 3187 | 8826 | 279 | 2026-04-08 21:34:51 |
| [httpx](https://github.com/encode/httpx) | 15166 | 1106 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14588 | 5686 | 11407 | 13563 | 1792 | 2026-04-07 21:08:23 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13797 | 2095 | 2650 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13793 | 1861 | 5521 | 6523 | 1243 | 2026-04-07 15:43:50 |
| [starlette](https://github.com/Kludex/starlette) | 12184 | 1153 | 766 | 1859 | 55 | 2026-04-08 22:52:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11741 | 607 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11716 | 1667 | 8186 | 1054 | 214 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 987 | 1120 | 1429 | 163 | 2026-04-07 15:03:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8992 | 566 | 1026 | 500 | 220 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7234 | 396 | 889 | 2528 | 319 | 2026-04-08 14:07:02 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5602 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5542 | 473 | 1247 | 820 | 506 | 2026-04-08 23:00:49 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5229 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4058 | 328 | 1181 | 216 | 115 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4009 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3619 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2735 | 311 | 664 | 1306 | 305 | 2026-04-03 22:07:14 |
| [anyio](https://github.com/agronholm/anyio) | 2433 | 193 | 432 | 604 | 88 | 2026-04-07 22:16:53 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 367 | 1785 | 267 | 267 | 2026-04-06 17:51:41 |
| [pypy](https://github.com/pypy/pypy) | 1700 | 109 | 5190 | 203 | 752 | 2026-04-08 20:46:42 |
| [jython](https://github.com/jython/jython) | 1500 | 228 | 294 | 123 | 109 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-09T03:18:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
