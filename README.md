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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194194 | 75250 | 41229 | 69141 | 3752 | 2026-03-17 02:29:12 |
| [transformers](https://github.com/huggingface/transformers) | 157941 | 32504 | 18726 | 25443 | 2334 | 2026-03-16 21:11:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 98337 | 27226 | 57336 | 119753 | 18080 | 2026-03-17 02:37:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 96279 | 8868 | 3511 | 5440 | 159 | 2026-03-16 15:42:19 |
| [django](https://github.com/django/django) | 87079 | 33754 | 0 | 20861 | 432 | 2026-03-17 01:17:29 |
| [cpython](https://github.com/python/cpython) | 72001 | 34242 | 75589 | 69449 | 9300 | 2026-03-17 02:17:47 |
| [flask](https://github.com/pallets/flask) | 71375 | 16747 | 2724 | 2783 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65427 | 26802 | 11998 | 20405 | 2139 | 2026-03-16 10:47:43 |
| [keras](https://github.com/keras-team/keras) | 63935 | 19738 | 12671 | 8969 | 271 | 2026-03-13 23:34:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 48158 | 19749 | 28177 | 36402 | 3672 | 2026-03-17 02:20:38 |
| [ray](https://github.com/ray-project/ray) | 41777 | 7348 | 22454 | 38975 | 3473 | 2026-03-17 02:18:54 |
| [gym](https://github.com/openai/gym) | 37097 | 8706 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33339 | 4660 | 5744 | 4083 | 194 | 2026-03-15 10:29:09 |
| [numpy](https://github.com/numpy/numpy) | 31609 | 12171 | 13832 | 17125 | 2335 | 2026-03-16 10:02:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29930 | 7078 | 3946 | 4944 | 78 | 2026-03-16 18:52:08 |
| [celery](https://github.com/celery/celery) | 28242 | 4993 | 5208 | 3867 | 767 | 2026-03-15 10:51:04 |
| [dash](https://github.com/plotly/dash) | 24467 | 2266 | 2072 | 1473 | 580 | 2026-03-16 17:39:59 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22584 | 8262 | 11201 | 20068 | 1547 | 2026-03-17 00:02:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22410 | 5545 | 1864 | 1713 | 217 | 2026-03-16 19:36:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 21887 | 1409 | 1316 | 6063 | 368 | 2026-03-16 20:49:57 |
| [micropython](https://github.com/micropython/micropython) | 21548 | 8748 | 5976 | 7628 | 1851 | 2026-03-16 03:41:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18353 | 2786 | 3330 | 2056 | 779 | 2026-03-16 22:49:44 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16393 | 2212 | 3182 | 8752 | 273 | 2026-03-17 02:26:52 |
| [httpx](https://github.com/encode/httpx) | 15162 | 1071 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14536 | 5660 | 11376 | 13456 | 1798 | 2026-03-16 17:22:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13770 | 2084 | 2648 | 1164 | 209 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13767 | 1858 | 5516 | 6508 | 1229 | 2026-03-16 22:03:09 |
| [starlette](https://github.com/Kludex/starlette) | 12028 | 1135 | 764 | 1832 | 44 | 2026-03-16 05:35:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11686 | 602 | 408 | 316 | 157 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11674 | 1651 | 8167 | 1045 | 214 | 2026-03-16 20:20:38 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1419 | 162 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8952 | 565 | 1022 | 495 | 222 | 2026-03-13 12:05:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1503 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7205 | 392 | 880 | 2514 | 319 | 2026-03-16 22:58:38 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5607 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5520 | 466 | 1241 | 800 | 491 | 2026-03-15 21:25:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5211 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1064 | 2732 | 82 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4018 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4015 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3607 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 312 | 662 | 1300 | 308 | 2026-03-16 01:40:12 |
| [anyio](https://github.com/agronholm/anyio) | 2412 | 188 | 429 | 587 | 84 | 2026-03-16 20:33:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-16 17:53:47 |
| [pypy](https://github.com/pypy/pypy) | 1682 | 103 | 5180 | 185 | 758 | 2026-03-16 11:57:50 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-17T02:47:59*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
