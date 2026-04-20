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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194781 | 75279 | 41318 | 71500 | 4543 | 2026-04-20 03:13:26 |
| [transformers](https://github.com/huggingface/transformers) | 159629 | 32935 | 18874 | 25993 | 2360 | 2026-04-20 03:19:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 99273 | 27526 | 58088 | 122173 | 18467 | 2026-04-20 03:36:28 |
| [fastapi](https://github.com/fastapi/fastapi) | 97408 | 9100 | 3517 | 5619 | 182 | 2026-04-17 11:43:13 |
| [django](https://github.com/django/django) | 87282 | 33815 | 0 | 21077 | 432 | 2026-04-19 20:42:58 |
| [cpython](https://github.com/python/cpython) | 72388 | 34453 | 76031 | 70463 | 9388 | 2026-04-20 02:36:45 |
| [flask](https://github.com/pallets/flask) | 71425 | 16791 | 2735 | 2807 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65873 | 26961 | 12044 | 20590 | 2059 | 2026-04-18 13:24:56 |
| [keras](https://github.com/keras-team/keras) | 64016 | 19746 | 12738 | 9189 | 300 | 2026-04-18 01:50:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 48540 | 19867 | 28247 | 36976 | 3428 | 2026-04-19 19:59:00 |
| [ray](https://github.com/ray-project/ray) | 42208 | 7455 | 22587 | 39808 | 3588 | 2026-04-20 01:24:02 |
| [gym](https://github.com/openai/gym) | 37171 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33490 | 4673 | 5755 | 4090 | 202 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31864 | 12306 | 13881 | 17324 | 2363 | 2026-04-17 19:58:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29974 | 7066 | 3968 | 4998 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28379 | 5010 | 5269 | 4079 | 779 | 2026-04-18 09:17:31 |
| [dash](https://github.com/plotly/dash) | 24198 | 2278 | 2089 | 1538 | 547 | 2026-04-17 20:07:12 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22723 | 8320 | 11245 | 20232 | 1505 | 2026-04-18 10:56:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22260 | 5544 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22022 | 1426 | 1332 | 6229 | 375 | 2026-04-19 14:37:22 |
| [micropython](https://github.com/micropython/micropython) | 21640 | 8799 | 6032 | 7737 | 1876 | 2026-04-16 13:44:34 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18463 | 2800 | 3338 | 2075 | 763 | 2026-04-15 23:24:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16405 | 2250 | 3190 | 8877 | 278 | 2026-04-20 01:50:00 |
| [httpx](https://github.com/encode/httpx) | 15209 | 1116 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14620 | 5698 | 11418 | 13601 | 1789 | 2026-04-19 20:49:44 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13818 | 2100 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13804 | 1866 | 5521 | 6529 | 1245 | 2026-04-13 18:09:43 |
| [starlette](https://github.com/Kludex/starlette) | 12216 | 1157 | 766 | 1873 | 56 | 2026-04-16 07:31:36 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11767 | 1670 | 8192 | 1057 | 213 | 2026-04-18 14:00:41 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11758 | 604 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 987 | 1121 | 1432 | 156 | 2026-04-18 16:27:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9017 | 568 | 1028 | 504 | 199 | 2026-04-18 19:04:16 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1496 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7243 | 393 | 889 | 2533 | 317 | 2026-04-13 23:21:14 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5551 | 478 | 1249 | 823 | 509 | 2026-04-14 02:16:52 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5241 | 1006 | 910 | 291 | 200 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4079 | 330 | 1183 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4007 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3625 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2439 | 197 | 434 | 610 | 84 | 2026-04-17 21:43:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 904 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 365 | 1785 | 267 | 267 | 2026-04-13 17:43:03 |
| [pypy](https://github.com/pypy/pypy) | 1711 | 111 | 5199 | 226 | 748 | 2026-04-19 21:37:45 |
| [jython](https://github.com/jython/jython) | 1499 | 227 | 294 | 126 | 111 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-20T03:42:11*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
