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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192068 | 74912 | 40868 | 59539 | 1522 | 2025-10-17 01:51:01 |
| [transformers](https://github.com/huggingface/transformers) | 151204 | 30813 | 18065 | 23019 | 2044 | 2025-10-17 01:03:33 |
| [pytorch](https://github.com/pytorch/pytorch) | 93984 | 25584 | 54332 | 110905 | 17013 | 2025-10-17 01:55:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 90812 | 8057 | 3469 | 4780 | 201 | 2025-10-13 17:40:45 |
| [django](https://github.com/django/django) | 85431 | 33100 | 0 | 19904 | 348 | 2025-10-16 19:01:18 |
| [flask](https://github.com/pallets/flask) | 70564 | 16589 | 2699 | 2709 | 11 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69380 | 33114 | 73974 | 65330 | 9183 | 2025-10-16 20:26:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63700 | 26331 | 11771 | 19615 | 2144 | 2025-10-16 15:17:49 |
| [keras](https://github.com/keras-team/keras) | 63471 | 19621 | 12567 | 8397 | 258 | 2025-10-17 00:19:47 |
| [pandas](https://github.com/pandas-dev/pandas) | 46846 | 19136 | 27793 | 34875 | 3622 | 2025-10-16 21:18:11 |
| [ray](https://github.com/ray-project/ray) | 39356 | 6781 | 21587 | 35895 | 3179 | 2025-10-17 01:53:11 |
| [gym](https://github.com/openai/gym) | 36683 | 8709 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32663 | 4598 | 5726 | 4071 | 210 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30589 | 11569 | 13593 | 16343 | 2343 | 2025-10-16 22:11:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29573 | 7021 | 3945 | 4846 | 102 | 2025-10-14 06:22:47 |
| [celery](https://github.com/celery/celery) | 27357 | 4860 | 5173 | 3694 | 757 | 2025-10-16 22:10:39 |
| [dash](https://github.com/plotly/dash) | 24163 | 2219 | 2012 | 1351 | 569 | 2025-10-16 16:47:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22307 | 5533 | 1853 | 1674 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21834 | 8065 | 11009 | 19602 | 1627 | 2025-10-17 00:10:16 |
| [micropython](https://github.com/micropython/micropython) | 20950 | 8489 | 5847 | 7284 | 1776 | 2025-10-15 13:10:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 20648 | 1351 | 1221 | 4908 | 450 | 2025-10-13 13:59:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18524 | 1576 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17846 | 2728 | 3266 | 1966 | 715 | 2025-10-09 18:25:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16040 | 2136 | 3152 | 8228 | 256 | 2025-10-16 18:11:48 |
| [httpx](https://github.com/encode/httpx) | 14635 | 961 | 919 | 1744 | 100 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14090 | 5504 | 11079 | 12699 | 1774 | 2025-10-16 21:33:37 |
| [dask](https://github.com/dask/dask) | 13535 | 1804 | 5441 | 6361 | 1190 | 2025-10-15 06:34:30 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13500 | 2035 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11558 | 1045 | 755 | 1725 | 52 | 2025-10-16 17:17:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11339 | 579 | 393 | 296 | 144 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11021 | 1587 | 8100 | 991 | 215 | 2025-10-16 00:55:31 |
| [falcon](https://github.com/falconry/falcon) | 9735 | 967 | 1107 | 1378 | 164 | 2025-10-15 19:45:12 |
| [bottle](https://github.com/bottlepy/bottle) | 8673 | 1486 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8626 | 527 | 954 | 446 | 165 | 2025-10-15 08:30:54 |
| [trio](https://github.com/python-trio/trio) | 6903 | 369 | 872 | 2459 | 311 | 2025-10-13 21:56:58 |
| [hug](https://github.com/hugapi/hug) | 6900 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5331 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5033 | 948 | 874 | 262 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4050 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3689 | 292 | 1163 | 196 | 118 | 2025-10-11 18:40:46 |
| [quart](https://github.com/pallets/quart) | 3499 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2694 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2314 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2251 | 166 | 406 | 526 | 69 | 2025-10-16 11:19:34 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 908 | 1077 | 1461 | 368 | 2025-10-14 17:45:08 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1925 | 368 | 1780 | 264 | 260 | 2025-10-13 17:45:09 |
| [pypy](https://github.com/pypy/pypy) | 1531 | 87 | 5151 | 171 | 739 | 2025-10-10 06:55:50 |
| [jython](https://github.com/jython/jython) | 1441 | 224 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-17T01:56:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
