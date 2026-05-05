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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194990 | 75275 | 41354 | 72796 | 4915 | 2026-05-05 03:34:19 |
| [transformers](https://github.com/huggingface/transformers) | 160248 | 33106 | 18925 | 26198 | 2350 | 2026-05-04 15:48:04 |
| [pytorch](https://github.com/pytorch/pytorch) | 99610 | 27654 | 58423 | 123454 | 18538 | 2026-05-05 03:37:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 97890 | 9199 | 3524 | 5701 | 185 | 2026-05-04 18:58:41 |
| [django](https://github.com/django/django) | 87400 | 33845 | 0 | 21161 | 430 | 2026-05-04 21:09:21 |
| [cpython](https://github.com/python/cpython) | 72575 | 34547 | 76231 | 70859 | 9286 | 2026-05-05 03:30:03 |
| [flask](https://github.com/pallets/flask) | 71483 | 16827 | 2736 | 2817 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65970 | 26989 | 12065 | 20696 | 2041 | 2026-05-04 18:12:50 |
| [keras](https://github.com/keras-team/keras) | 64055 | 19761 | 12746 | 9279 | 238 | 2026-05-05 02:41:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 48656 | 19901 | 28267 | 37114 | 3389 | 2026-05-04 22:29:42 |
| [ray](https://github.com/ray-project/ray) | 42423 | 7524 | 22639 | 40122 | 3553 | 2026-05-05 02:36:13 |
| [gym](https://github.com/openai/gym) | 37176 | 8704 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33542 | 4680 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31967 | 12334 | 13903 | 17409 | 2371 | 2026-05-04 16:59:09 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29994 | 7068 | 3967 | 5004 | 78 | 2026-04-28 07:27:54 |
| [celery](https://github.com/celery/celery) | 28427 | 5028 | 5272 | 4100 | 775 | 2026-05-05 01:38:29 |
| [dash](https://github.com/plotly/dash) | 24168 | 2277 | 2092 | 1547 | 540 | 2026-05-04 23:04:32 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22769 | 8324 | 11260 | 20301 | 1491 | 2026-05-05 03:26:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22211 | 5541 | 1871 | 1728 | 218 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22032 | 1435 | 1340 | 6368 | 374 | 2026-05-04 20:26:17 |
| [micropython](https://github.com/micropython/micropython) | 21676 | 8815 | 6046 | 7773 | 1812 | 2026-05-01 12:38:24 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18497 | 2804 | 3343 | 2081 | 764 | 2026-05-04 22:49:02 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16428 | 2261 | 3191 | 8926 | 256 | 2026-05-04 19:00:32 |
| [httpx](https://github.com/encode/httpx) | 15257 | 1138 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14660 | 5716 | 11431 | 13644 | 1783 | 2026-05-04 20:57:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13838 | 2107 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13820 | 1868 | 5522 | 6536 | 1247 | 2026-04-28 16:39:15 |
| [starlette](https://github.com/Kludex/starlette) | 12275 | 1168 | 766 | 1886 | 56 | 2026-05-03 06:45:09 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11820 | 1675 | 8202 | 1072 | 216 | 2026-05-04 12:55:49 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11779 | 605 | 413 | 323 | 153 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 998 | 1125 | 1446 | 158 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9037 | 574 | 1033 | 510 | 207 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8759 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7257 | 393 | 891 | 2540 | 320 | 2026-05-01 17:34:53 |
| [hug](https://github.com/hugapi/hug) | 6892 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5565 | 480 | 1249 | 825 | 506 | 2026-05-01 04:21:03 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5249 | 1010 | 912 | 293 | 204 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4116 | 331 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3630 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 311 | 663 | 1309 | 305 | 2026-05-04 22:07:07 |
| [anyio](https://github.com/agronholm/anyio) | 2457 | 202 | 436 | 620 | 82 | 2026-05-03 20:13:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 908 | 1084 | 1492 | 362 | 2026-05-04 10:17:01 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1719 | 112 | 5205 | 237 | 740 | 2026-05-04 21:46:25 |
| [jython](https://github.com/jython/jython) | 1507 | 229 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-05T03:37:47*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
