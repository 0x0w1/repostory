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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192016 | 74915 | 40859 | 59332 | 1960 | 2025-10-14 01:54:14 |
| [transformers](https://github.com/huggingface/transformers) | 151032 | 30753 | 18047 | 22917 | 2038 | 2025-10-13 16:41:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 93891 | 25546 | 54258 | 110653 | 17002 | 2025-10-14 01:48:13 |
| [fastapi](https://github.com/fastapi/fastapi) | 90698 | 8032 | 3469 | 4774 | 197 | 2025-10-13 17:40:45 |
| [django](https://github.com/django/django) | 85396 | 33088 | 0 | 19891 | 353 | 2025-10-13 21:34:26 |
| [flask](https://github.com/pallets/flask) | 70551 | 16585 | 2699 | 2708 | 11 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69333 | 33079 | 73928 | 65212 | 9179 | 2025-10-13 20:36:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63660 | 26318 | 11763 | 19600 | 2136 | 2025-10-13 15:45:19 |
| [keras](https://github.com/keras-team/keras) | 63468 | 19621 | 12565 | 8390 | 264 | 2025-10-11 04:36:53 |
| [pandas](https://github.com/pandas-dev/pandas) | 46823 | 19127 | 27780 | 34854 | 3630 | 2025-10-13 23:12:42 |
| [ray](https://github.com/ray-project/ray) | 39308 | 6771 | 21553 | 35783 | 3157 | 2025-10-14 01:28:42 |
| [gym](https://github.com/openai/gym) | 36671 | 8707 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32647 | 4595 | 5726 | 4071 | 210 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30565 | 11553 | 13589 | 16292 | 2364 | 2025-10-13 21:32:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29557 | 7015 | 3945 | 4843 | 102 | 2025-10-09 17:47:30 |
| [celery](https://github.com/celery/celery) | 27333 | 4858 | 5172 | 3688 | 755 | 2025-10-13 22:10:59 |
| [dash](https://github.com/plotly/dash) | 24157 | 2214 | 2011 | 1350 | 575 | 2025-10-10 18:50:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22297 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21812 | 8059 | 11006 | 19599 | 1627 | 2025-10-13 20:36:28 |
| [micropython](https://github.com/micropython/micropython) | 20937 | 8482 | 5845 | 7273 | 1776 | 2025-10-13 01:39:45 |
| [RustPython](https://github.com/RustPython/RustPython) | 20619 | 1351 | 1221 | 4907 | 449 | 2025-10-13 13:59:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18516 | 1576 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17828 | 2726 | 3264 | 1965 | 726 | 2025-10-09 18:25:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16034 | 2132 | 3151 | 8193 | 271 | 2025-10-13 16:25:55 |
| [httpx](https://github.com/encode/httpx) | 14632 | 961 | 919 | 1743 | 101 | 2025-10-13 14:00:51 |
| [scipy](https://github.com/scipy/scipy) | 14084 | 5498 | 11072 | 12680 | 1762 | 2025-10-13 20:51:21 |
| [dask](https://github.com/dask/dask) | 13527 | 1804 | 5441 | 6360 | 1191 | 2025-10-13 21:38:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13494 | 2034 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11549 | 1043 | 754 | 1720 | 48 | 2025-10-12 21:52:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11321 | 579 | 392 | 295 | 147 | 2025-10-10 03:26:18 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11011 | 1587 | 8097 | 988 | 219 | 2025-10-12 05:44:09 |
| [falcon](https://github.com/falconry/falcon) | 9733 | 967 | 1106 | 1376 | 166 | 2025-10-08 07:26:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8671 | 1486 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8618 | 527 | 950 | 440 | 416 | 2025-10-10 15:53:50 |
| [hug](https://github.com/hugapi/hug) | 6897 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6896 | 368 | 872 | 2459 | 311 | 2025-10-13 21:56:58 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5329 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5028 | 948 | 872 | 262 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4050 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3930 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3682 | 292 | 1163 | 196 | 118 | 2025-10-11 18:40:46 |
| [quart](https://github.com/pallets/quart) | 3494 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2692 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2313 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2246 | 166 | 406 | 525 | 69 | 2025-10-13 17:51:52 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 908 | 1077 | 1460 | 368 | 2025-10-12 18:08:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 368 | 1780 | 264 | 260 | 2025-10-13 17:45:09 |
| [pypy](https://github.com/pypy/pypy) | 1527 | 88 | 5150 | 171 | 738 | 2025-10-10 06:55:50 |
| [jython](https://github.com/jython/jython) | 1438 | 224 | 282 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-14T01:56:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
