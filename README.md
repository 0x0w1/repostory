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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191464 | 74808 | 40765 | 56939 | 1571 | 2025-09-04 01:52:27 |
| [transformers](https://github.com/huggingface/transformers) | 149134 | 30258 | 17878 | 22219 | 1978 | 2025-09-03 21:20:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 92905 | 25161 | 53488 | 108176 | 17045 | 2025-09-04 01:40:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 89102 | 7828 | 3467 | 4686 | 273 | 2025-09-01 17:33:14 |
| [django](https://github.com/django/django) | 84885 | 32893 | 0 | 19745 | 360 | 2025-09-03 21:38:59 |
| [flask](https://github.com/pallets/flask) | 70283 | 16515 | 2694 | 2693 | 5 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68693 | 32736 | 73479 | 64074 | 9340 | 2025-09-03 23:27:15 |
| [keras](https://github.com/keras-team/keras) | 63384 | 19618 | 12533 | 8313 | 286 | 2025-09-03 16:57:19 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63220 | 26190 | 11678 | 19291 | 2174 | 2025-09-03 14:33:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 46475 | 18873 | 27688 | 34511 | 3694 | 2025-09-03 23:46:37 |
| [ray](https://github.com/ray-project/ray) | 38765 | 6758 | 21030 | 34833 | 3028 | 2025-09-04 01:30:01 |
| [gym](https://github.com/openai/gym) | 36454 | 8689 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32407 | 4577 | 5719 | 4067 | 202 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30304 | 11296 | 13512 | 16086 | 2357 | 2025-09-04 00:32:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29431 | 6999 | 3945 | 4829 | 99 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27136 | 4838 | 5158 | 3650 | 751 | 2025-08-31 09:27:30 |
| [dash](https://github.com/plotly/dash) | 24004 | 2196 | 1984 | 1326 | 557 | 2025-09-03 22:32:15 |
| [tornado](https://github.com/tornadoweb/tornado) | 22141 | 5537 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21649 | 7985 | 10961 | 19509 | 1634 | 2025-09-03 23:41:23 |
| [micropython](https://github.com/micropython/micropython) | 20785 | 8401 | 5805 | 7159 | 1786 | 2025-09-02 04:19:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 20460 | 1341 | 1211 | 4847 | 440 | 2025-09-03 23:44:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18488 | 1581 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17684 | 2705 | 3247 | 1946 | 720 | 2025-08-29 20:22:39 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15963 | 2121 | 3144 | 8021 | 264 | 2025-09-03 10:30:42 |
| [httpx](https://github.com/encode/httpx) | 14522 | 950 | 916 | 1717 | 110 | 2025-09-03 11:20:00 |
| [scipy](https://github.com/scipy/scipy) | 13981 | 5462 | 10995 | 12536 | 1758 | 2025-09-03 10:20:14 |
| [dask](https://github.com/dask/dask) | 13458 | 1795 | 5429 | 6338 | 1195 | 2025-09-02 21:26:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13412 | 2029 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11416 | 1033 | 751 | 1688 | 51 | 2025-09-02 14:26:53 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11228 | 570 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10846 | 1577 | 8077 | 979 | 228 | 2025-09-03 15:27:44 |
| [falcon](https://github.com/falconry/falcon) | 9710 | 958 | 1096 | 1364 | 156 | 2025-08-31 19:21:18 |
| [bottle](https://github.com/bottlepy/bottle) | 8655 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8503 | 520 | 937 | 434 | 406 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6893 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6769 | 365 | 866 | 2447 | 312 | 2025-09-03 04:38:37 |
| [eve](https://github.com/pyeve/eve) | 6729 | 747 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5272 | 436 | 1189 | 713 | 498 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4972 | 932 | 866 | 258 | 161 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4045 | 891 | 1061 | 2718 | 88 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3934 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3570 | 290 | 1156 | 195 | 115 | 2025-08-28 16:27:29 |
| [quart](https://github.com/pallets/quart) | 3433 | 187 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2683 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2305 | 131 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2194 | 164 | 400 | 502 | 69 | 2025-09-01 17:42:57 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 908 | 1077 | 1458 | 369 | 2025-09-01 17:32:42 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-09-01 17:37:10 |
| [pypy](https://github.com/pypy/pypy) | 1490 | 84 | 5142 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1429 | 219 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-04T01:52:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
