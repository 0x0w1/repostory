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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191675 | 74841 | 40795 | 57630 | 1651 | 2025-09-18 01:51:10 |
| [transformers](https://github.com/huggingface/transformers) | 149928 | 30442 | 17935 | 22443 | 1997 | 2025-09-17 19:52:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 93246 | 25327 | 53805 | 108976 | 17128 | 2025-09-18 01:46:51 |
| [fastapi](https://github.com/fastapi/fastapi) | 89567 | 7889 | 3468 | 4718 | 244 | 2025-09-16 18:28:51 |
| [django](https://github.com/django/django) | 85015 | 32971 | 0 | 19814 | 367 | 2025-09-17 20:25:07 |
| [flask](https://github.com/pallets/flask) | 70371 | 16528 | 2696 | 2702 | 9 | 2025-09-12 21:52:55 |
| [cpython](https://github.com/python/cpython) | 68907 | 32893 | 73634 | 64533 | 9309 | 2025-09-18 01:17:04 |
| [keras](https://github.com/keras-team/keras) | 63411 | 19619 | 12549 | 8341 | 268 | 2025-09-17 21:39:41 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63366 | 26239 | 11716 | 19369 | 2175 | 2025-09-17 19:00:16 |
| [pandas](https://github.com/pandas-dev/pandas) | 46598 | 18963 | 27719 | 34600 | 3660 | 2025-09-17 20:34:44 |
| [ray](https://github.com/ray-project/ray) | 38978 | 6805 | 21170 | 35174 | 3191 | 2025-09-18 01:45:55 |
| [gym](https://github.com/openai/gym) | 36532 | 8692 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32489 | 4576 | 5722 | 4068 | 204 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30415 | 11431 | 13544 | 16159 | 2352 | 2025-09-17 19:13:09 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29472 | 7004 | 3945 | 4835 | 104 | 2025-09-15 19:45:43 |
| [celery](https://github.com/celery/celery) | 27208 | 4845 | 5162 | 3655 | 757 | 2025-09-16 04:08:45 |
| [dash](https://github.com/plotly/dash) | 24067 | 2200 | 1995 | 1330 | 562 | 2025-09-16 15:30:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5536 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21701 | 8028 | 10987 | 19547 | 1623 | 2025-09-17 07:58:44 |
| [micropython](https://github.com/micropython/micropython) | 20830 | 8426 | 5814 | 7190 | 1787 | 2025-09-16 03:31:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 20522 | 1345 | 1220 | 4872 | 438 | 2025-09-17 00:11:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18492 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17741 | 2710 | 3251 | 1951 | 720 | 2025-09-17 21:41:28 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15992 | 2125 | 3145 | 8079 | 272 | 2025-09-17 22:29:49 |
| [httpx](https://github.com/encode/httpx) | 14564 | 956 | 918 | 1728 | 99 | 2025-09-16 21:45:32 |
| [scipy](https://github.com/scipy/scipy) | 14031 | 5478 | 11027 | 12591 | 1761 | 2025-09-17 15:54:30 |
| [dask](https://github.com/dask/dask) | 13487 | 1796 | 5437 | 6345 | 1198 | 2025-09-16 14:21:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13441 | 2034 | 2627 | 1148 | 188 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11463 | 1038 | 753 | 1704 | 49 | 2025-09-13 10:21:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11257 | 574 | 388 | 289 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10904 | 1579 | 8087 | 982 | 234 | 2025-09-15 21:56:02 |
| [falcon](https://github.com/falconry/falcon) | 9719 | 959 | 1099 | 1369 | 158 | 2025-09-10 04:12:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8659 | 1486 | 855 | 622 | 284 | 2025-09-13 12:31:44 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8544 | 523 | 944 | 434 | 410 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6895 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6860 | 367 | 869 | 2451 | 312 | 2025-09-15 21:35:35 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5292 | 437 | 1192 | 713 | 500 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4998 | 939 | 870 | 260 | 167 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4047 | 889 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3613 | 291 | 1157 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3452 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2686 | 304 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2308 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2213 | 163 | 401 | 510 | 67 | 2025-09-16 10:30:58 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-09-15 17:40:35 |
| [pypy](https://github.com/pypy/pypy) | 1497 | 86 | 5143 | 168 | 734 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1432 | 220 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-18T01:53:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
