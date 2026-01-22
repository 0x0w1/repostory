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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193431 | 75186 | 41105 | 65391 | 2813 | 2026-01-22 02:20:31 |
| [transformers](https://github.com/huggingface/transformers) | 155505 | 31816 | 18447 | 24351 | 2184 | 2026-01-21 18:19:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 96795 | 26566 | 56400 | 116123 | 17910 | 2026-01-22 02:25:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 94331 | 8563 | 3500 | 5159 | 209 | 2026-01-21 17:58:09 |
| [django](https://github.com/django/django) | 86534 | 33526 | 0 | 20503 | 387 | 2026-01-20 16:54:07 |
| [cpython](https://github.com/python/cpython) | 71176 | 33938 | 75071 | 68071 | 9265 | 2026-01-21 22:31:58 |
| [flask](https://github.com/pallets/flask) | 71077 | 16679 | 2709 | 2754 | 12 | 2026-01-05 16:50:56 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64728 | 26617 | 11898 | 20082 | 2123 | 2026-01-21 18:30:05 |
| [keras](https://github.com/keras-team/keras) | 63734 | 19677 | 12615 | 8632 | 251 | 2026-01-21 20:16:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47654 | 19542 | 28038 | 35700 | 3631 | 2026-01-21 20:43:10 |
| [ray](https://github.com/ray-project/ray) | 40920 | 7140 | 22192 | 37852 | 3317 | 2026-01-22 01:45:24 |
| [gym](https://github.com/openai/gym) | 36968 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33092 | 4633 | 5737 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31302 | 11981 | 13756 | 16887 | 2304 | 2026-01-21 23:33:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29814 | 7055 | 3946 | 4904 | 86 | 2026-01-13 22:15:14 |
| [celery](https://github.com/celery/celery) | 27897 | 4931 | 5184 | 3769 | 758 | 2026-01-17 05:57:45 |
| [dash](https://github.com/plotly/dash) | 24412 | 2248 | 2046 | 1420 | 559 | 2026-01-21 23:12:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22432 | 5543 | 1862 | 1695 | 210 | 2026-01-20 14:26:57 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22256 | 8170 | 11112 | 19854 | 1529 | 2026-01-22 01:15:50 |
| [RustPython](https://github.com/RustPython/RustPython) | 21706 | 1401 | 1293 | 5472 | 367 | 2026-01-22 00:31:21 |
| [micropython](https://github.com/micropython/micropython) | 21369 | 8660 | 5938 | 7492 | 1836 | 2026-01-16 08:10:24 |
| [sanic](https://github.com/sanic-org/sanic) | 18627 | 1583 | 1463 | 1662 | 113 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18199 | 2773 | 3315 | 2005 | 766 | 2026-01-14 21:23:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16217 | 2181 | 3171 | 8500 | 270 | 2026-01-21 18:43:40 |
| [httpx](https://github.com/encode/httpx) | 14928 | 1012 | 925 | 1779 | 126 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14380 | 5593 | 11262 | 13139 | 1754 | 2026-01-22 00:56:46 |
| [dask](https://github.com/dask/dask) | 13725 | 1836 | 5491 | 6450 | 1216 | 2026-01-16 12:34:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13693 | 2081 | 2644 | 1156 | 203 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11857 | 1098 | 762 | 1770 | 47 | 2026-01-18 13:59:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11599 | 601 | 403 | 309 | 152 | 2026-01-19 17:03:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11415 | 1626 | 8142 | 1023 | 205 | 2026-01-21 21:38:16 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 976 | 1119 | 1410 | 164 | 2026-01-21 18:48:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8855 | 556 | 997 | 480 | 199 | 2026-01-13 18:26:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8730 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7107 | 379 | 878 | 2490 | 314 | 2026-01-20 02:39:49 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5619 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5452 | 447 | 1220 | 736 | 511 | 2026-01-14 06:28:04 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5160 | 991 | 890 | 282 | 183 | 2026-01-15 16:36:40 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 889 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4023 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3905 | 307 | 1177 | 207 | 118 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3576 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2363 | 180 | 423 | 564 | 76 | 2026-01-19 18:01:42 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 368 | 1785 | 266 | 266 | 2026-01-19 17:53:24 |
| [pypy](https://github.com/pypy/pypy) | 1635 | 96 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1472 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-22T02:27:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
