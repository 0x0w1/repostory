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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191542 | 74819 | 40776 | 57107 | 1581 | 2025-09-09 01:51:09 |
| [transformers](https://github.com/huggingface/transformers) | 149325 | 30312 | 17894 | 22289 | 1978 | 2025-09-08 21:08:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 93038 | 25194 | 53596 | 108404 | 17064 | 2025-09-09 01:49:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 89290 | 7846 | 3466 | 4698 | 238 | 2025-09-08 19:12:47 |
| [django](https://github.com/django/django) | 84923 | 32913 | 0 | 19771 | 366 | 2025-09-08 15:14:03 |
| [flask](https://github.com/pallets/flask) | 70314 | 16521 | 2694 | 2696 | 6 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68745 | 32794 | 73528 | 64246 | 9333 | 2025-09-09 00:51:08 |
| [keras](https://github.com/keras-team/keras) | 63398 | 19625 | 12539 | 8319 | 271 | 2025-09-08 21:20:16 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63277 | 26209 | 11691 | 19314 | 2166 | 2025-09-08 18:21:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 46516 | 18881 | 27697 | 34554 | 3681 | 2025-09-08 20:58:22 |
| [ray](https://github.com/ray-project/ray) | 38843 | 6778 | 21057 | 34958 | 3062 | 2025-09-09 01:38:52 |
| [gym](https://github.com/openai/gym) | 36475 | 8692 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32442 | 4579 | 5720 | 4069 | 203 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30361 | 11324 | 13530 | 16127 | 2366 | 2025-09-08 20:47:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29445 | 7001 | 3945 | 4831 | 101 | 2025-09-08 19:44:29 |
| [celery](https://github.com/celery/celery) | 27157 | 4840 | 5159 | 3650 | 751 | 2025-09-07 15:41:52 |
| [dash](https://github.com/plotly/dash) | 24021 | 2198 | 1986 | 1326 | 558 | 2025-09-08 20:59:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22155 | 5536 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21676 | 7989 | 10970 | 19522 | 1641 | 2025-09-08 20:26:14 |
| [micropython](https://github.com/micropython/micropython) | 20796 | 8414 | 5805 | 7164 | 1786 | 2025-09-09 01:00:44 |
| [RustPython](https://github.com/RustPython/RustPython) | 20481 | 1342 | 1217 | 4860 | 441 | 2025-09-08 13:25:33 |
| [sanic](https://github.com/sanic-org/sanic) | 18492 | 1581 | 1449 | 1625 | 143 | 2025-09-08 03:48:03 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17704 | 2706 | 3250 | 1947 | 723 | 2025-08-29 20:22:39 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15973 | 2121 | 3144 | 8045 | 269 | 2025-09-08 11:53:06 |
| [httpx](https://github.com/encode/httpx) | 14533 | 951 | 917 | 1723 | 105 | 2025-09-05 15:15:17 |
| [scipy](https://github.com/scipy/scipy) | 13995 | 5469 | 11014 | 12553 | 1770 | 2025-09-07 14:17:21 |
| [dask](https://github.com/dask/dask) | 13470 | 1796 | 5434 | 6340 | 1200 | 2025-09-08 22:03:31 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13420 | 2031 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11439 | 1032 | 751 | 1692 | 48 | 2025-09-06 10:49:37 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11246 | 571 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10861 | 1578 | 8076 | 979 | 227 | 2025-09-07 13:28:02 |
| [falcon](https://github.com/falconry/falcon) | 9713 | 959 | 1098 | 1367 | 158 | 2025-09-08 14:42:41 |
| [bottle](https://github.com/bottlepy/bottle) | 8658 | 1487 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8520 | 520 | 939 | 434 | 408 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6893 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6840 | 367 | 866 | 2448 | 310 | 2025-09-08 21:32:26 |
| [eve](https://github.com/pyeve/eve) | 6732 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5633 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5276 | 436 | 1190 | 713 | 499 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4972 | 937 | 867 | 258 | 162 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4046 | 890 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3580 | 291 | 1156 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3445 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2682 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2307 | 131 | 426 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2198 | 163 | 400 | 504 | 68 | 2025-09-08 17:45:22 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 908 | 1077 | 1458 | 369 | 2025-09-07 03:45:02 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 261 | 2025-09-08 17:38:35 |
| [pypy](https://github.com/pypy/pypy) | 1495 | 85 | 5143 | 168 | 736 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1431 | 219 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-09T01:57:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
