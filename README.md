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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194003 | 75214 | 41191 | 68329 | 3593 | 2026-03-05 02:42:38 |
| [transformers](https://github.com/huggingface/transformers) | 157395 | 32288 | 18656 | 25184 | 2268 | 2026-03-04 22:59:26 |
| [pytorch](https://github.com/pytorch/pytorch) | 97970 | 27073 | 57122 | 118916 | 18082 | 2026-03-05 02:45:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 95884 | 8782 | 3506 | 5395 | 144 | 2026-03-04 12:53:14 |
| [django](https://github.com/django/django) | 86974 | 33713 | 0 | 20763 | 420 | 2026-03-04 21:15:49 |
| [cpython](https://github.com/python/cpython) | 71827 | 34172 | 75439 | 69075 | 9270 | 2026-03-05 00:07:47 |
| [flask](https://github.com/pallets/flask) | 71321 | 16740 | 2722 | 2782 | 3 | 2026-03-04 15:36:26 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65292 | 26748 | 11980 | 20325 | 2144 | 2026-03-03 23:55:33 |
| [keras](https://github.com/keras-team/keras) | 63910 | 19712 | 12653 | 8902 | 280 | 2026-03-05 02:33:06 |
| [pandas](https://github.com/pandas-dev/pandas) | 48049 | 19717 | 28153 | 36173 | 3693 | 2026-03-05 01:38:10 |
| [ray](https://github.com/ray-project/ray) | 41587 | 7286 | 22408 | 38747 | 3433 | 2026-03-05 02:37:24 |
| [gym](https://github.com/openai/gym) | 37071 | 8708 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33276 | 4640 | 5742 | 4080 | 191 | 2026-03-03 08:56:07 |
| [numpy](https://github.com/numpy/numpy) | 31557 | 12113 | 13820 | 17050 | 2324 | 2026-03-04 18:04:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29923 | 7076 | 3946 | 4939 | 79 | 2026-03-04 15:27:11 |
| [celery](https://github.com/celery/celery) | 28191 | 4979 | 5199 | 3846 | 771 | 2026-03-03 22:13:36 |
| [dash](https://github.com/plotly/dash) | 24434 | 2264 | 2068 | 1456 | 573 | 2026-03-04 23:58:34 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22522 | 8228 | 11184 | 20008 | 1545 | 2026-03-04 22:00:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22401 | 5543 | 1863 | 1703 | 217 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21856 | 1405 | 1310 | 5975 | 387 | 2026-03-05 01:21:44 |
| [micropython](https://github.com/micropython/micropython) | 21514 | 8725 | 5971 | 7601 | 1846 | 2026-03-04 13:08:15 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18303 | 2779 | 3326 | 2053 | 777 | 2026-03-04 15:38:03 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16373 | 2209 | 3181 | 8704 | 272 | 2026-03-04 18:55:07 |
| [httpx](https://github.com/encode/httpx) | 15133 | 1051 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14505 | 5639 | 11346 | 13376 | 1780 | 2026-03-04 22:28:14 |
| [dask](https://github.com/dask/dask) | 13756 | 1849 | 5509 | 6501 | 1225 | 2026-03-04 16:05:27 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13756 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11994 | 1127 | 763 | 1820 | 46 | 2026-03-01 20:46:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11674 | 601 | 404 | 314 | 152 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11657 | 1650 | 8162 | 1040 | 215 | 2026-03-03 22:14:24 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 980 | 1119 | 1417 | 165 | 2026-03-04 17:39:06 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8927 | 560 | 1018 | 491 | 219 | 2026-03-04 12:33:09 |
| [bottle](https://github.com/bottlepy/bottle) | 8759 | 1499 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7186 | 386 | 880 | 2510 | 318 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6910 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5609 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5516 | 465 | 1236 | 792 | 489 | 2026-03-04 07:17:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5199 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4075 | 894 | 1063 | 2730 | 80 | 2026-03-04 19:38:51 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3984 | 321 | 1181 | 214 | 115 | 2026-03-02 16:28:40 |
| [quart](https://github.com/pallets/quart) | 3607 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2731 | 310 | 660 | 1284 | 308 | 2026-03-04 02:34:39 |
| [anyio](https://github.com/agronholm/anyio) | 2402 | 183 | 429 | 580 | 83 | 2026-03-04 20:45:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1464 | 367 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-03-02 18:13:20 |
| [pypy](https://github.com/pypy/pypy) | 1663 | 100 | 5177 | 182 | 759 | 2026-03-02 18:40:57 |
| [jython](https://github.com/jython/jython) | 1488 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-05T02:46:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
