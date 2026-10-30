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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201212 | 78733 | 41927 | 84187 | 3445 | 2026-10-30 05:10:40 |
| [transformers](https://github.com/huggingface/transformers) | 168338 | 35033 | 19728 | 29614 | 1027 | 2026-10-30 05:23:58 |
| [pytorch](https://github.com/pytorch/pytorch) | 105005 | 31864 | 62111 | 139899 | 17878 | 2026-10-30 05:20:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 104269 | 10147 | 3556 | 6533 | 56 | 2026-10-27 04:56:28 |
| [django](https://github.com/django/django) | 91444 | 36541 | 0 | 22136 | 537 | 2026-10-30 01:28:27 |
| [cpython](https://github.com/python/cpython) | 77696 | 37703 | 78961 | 79458 | 9217 | 2026-10-30 04:19:09 |
| [flask](https://github.com/pallets/flask) | 74922 | 17213 | 2770 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67918 | 27597 | 12353 | 21711 | 2160 | 2026-10-29 23:49:06 |
| [keras](https://github.com/keras-team/keras) | 64398 | 19807 | 13049 | 10172 | 273 | 2026-10-30 03:04:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 50256 | 20672 | 28661 | 39739 | 2078 | 2026-10-30 01:43:27 |
| [ray](https://github.com/ray-project/ray) | 44158 | 8224 | 23268 | 43863 | 3665 | 2026-10-30 03:55:03 |
| [gym](https://github.com/openai/gym) | 37233 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34004 | 4738 | 5781 | 4138 | 260 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33198 | 13043 | 14157 | 18923 | 2231 | 2026-10-30 00:11:29 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30219 | 7094 | 3966 | 5102 | 65 | 2026-10-28 07:03:26 |
| [celery](https://github.com/celery/celery) | 29091 | 5252 | 5356 | 4665 | 742 | 2026-10-28 22:12:57 |
| [dash](https://github.com/plotly/dash) | 24473 | 2332 | 2170 | 1803 | 433 | 2026-10-29 20:22:21 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23400 | 8535 | 11455 | 21036 | 1482 | 2026-10-29 23:03:31 |
| [RustPython](https://github.com/RustPython/RustPython) | 22433 | 1507 | 1446 | 7925 | 308 | 2026-10-29 13:49:23 |
| [micropython](https://github.com/micropython/micropython) | 22169 | 9028 | 6152 | 8172 | 1551 | 2026-10-30 03:37:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5594 | 1888 | 1903 | 234 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18862 | 2882 | 3399 | 2258 | 745 | 2026-10-28 16:35:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16596 | 2495 | 3269 | 10562 | 264 | 2026-10-29 18:10:25 |
| [httpx](https://github.com/encode/httpx) | 15698 | 3245 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15167 | 6045 | 11734 | 14799 | 1892 | 2026-10-29 23:24:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14093 | 2151 | 2667 | 1247 | 257 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13937 | 2008 | 5580 | 6793 | 1410 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12696 | 1422 | 795 | 2288 | 57 | 2026-10-29 12:47:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12272 | 1838 | 8368 | 1253 | 218 | 2026-10-29 16:01:18 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11921 | 621 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9810 | 1050 | 1148 | 1559 | 160 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9228 | 622 | 1054 | 588 | 229 | 2026-10-29 17:21:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1516 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7356 | 464 | 906 | 2654 | 343 | 2026-10-29 06:09:20 |
| [hug](https://github.com/hugapi/hug) | 6873 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5639 | 538 | 1300 | 973 | 556 | 2026-10-29 23:19:31 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5438 | 1053 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4458 | 390 | 1210 | 259 | 118 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 276 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3679 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 677 | 1385 | 264 | 2026-10-29 22:14:08 |
| [anyio](https://github.com/agronholm/anyio) | 2565 | 339 | 493 | 874 | 143 | 2026-10-29 21:57:59 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1607 | 355 | 2026-10-29 16:43:15 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 371 | 1791 | 278 | 279 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1822 | 130 | 5290 | 392 | 721 | 2026-10-29 20:04:19 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 155 | 101 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-30T05:30:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
