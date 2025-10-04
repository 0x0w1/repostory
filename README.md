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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191908 | 74898 | 40837 | 58730 | 1784 | 2025-10-04 01:25:18 |
| [transformers](https://github.com/huggingface/transformers) | 150610 | 30626 | 18009 | 22737 | 2020 | 2025-10-03 16:35:08 |
| [pytorch](https://github.com/pytorch/pytorch) | 93685 | 25476 | 54110 | 110069 | 16886 | 2025-10-04 01:48:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 90355 | 7997 | 3470 | 4756 | 204 | 2025-10-02 06:56:52 |
| [django](https://github.com/django/django) | 85308 | 33049 | 0 | 19851 | 339 | 2025-10-03 21:12:58 |
| [flask](https://github.com/pallets/flask) | 70492 | 16553 | 2698 | 2705 | 9 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69132 | 32994 | 73777 | 64842 | 9306 | 2025-10-03 21:52:46 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63547 | 26285 | 11742 | 19489 | 2152 | 2025-10-03 10:46:08 |
| [keras](https://github.com/keras-team/keras) | 63450 | 19624 | 12562 | 8371 | 263 | 2025-10-03 22:08:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 46734 | 19064 | 27760 | 34759 | 3682 | 2025-10-03 17:17:37 |
| [ray](https://github.com/ray-project/ray) | 39185 | 6849 | 21275 | 35556 | 3138 | 2025-10-04 01:31:40 |
| [gym](https://github.com/openai/gym) | 36617 | 8704 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32582 | 4589 | 5722 | 4070 | 206 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30497 | 11502 | 13569 | 16239 | 2357 | 2025-10-03 18:21:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29529 | 7009 | 3945 | 4840 | 104 | 2025-09-25 12:59:12 |
| [celery](https://github.com/celery/celery) | 27286 | 4854 | 5169 | 3674 | 756 | 2025-10-01 22:12:35 |
| [dash](https://github.com/plotly/dash) | 24131 | 2207 | 2004 | 1347 | 577 | 2025-10-03 23:07:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22255 | 5536 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21761 | 8052 | 10999 | 19589 | 1631 | 2025-10-03 17:30:42 |
| [micropython](https://github.com/micropython/micropython) | 20895 | 8462 | 5839 | 7244 | 1778 | 2025-10-03 14:25:30 |
| [RustPython](https://github.com/RustPython/RustPython) | 20572 | 1348 | 1221 | 4896 | 450 | 2025-09-30 00:07:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18504 | 1579 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17802 | 2721 | 3258 | 1959 | 719 | 2025-10-03 19:12:17 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16022 | 2126 | 3146 | 8111 | 278 | 2025-10-03 10:37:13 |
| [httpx](https://github.com/encode/httpx) | 14602 | 958 | 918 | 1734 | 101 | 2025-10-01 16:03:23 |
| [scipy](https://github.com/scipy/scipy) | 14058 | 5489 | 11057 | 12654 | 1759 | 2025-10-03 09:49:29 |
| [dask](https://github.com/dask/dask) | 13508 | 1800 | 5440 | 6355 | 1200 | 2025-10-03 18:13:00 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13479 | 2037 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11519 | 1044 | 754 | 1717 | 47 | 2025-10-02 20:15:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11303 | 575 | 389 | 289 | 143 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10956 | 1584 | 8093 | 988 | 225 | 2025-10-03 19:08:54 |
| [falcon](https://github.com/falconry/falcon) | 9724 | 962 | 1102 | 1371 | 159 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8670 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8598 | 527 | 947 | 439 | 412 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6877 | 367 | 871 | 2457 | 311 | 2025-10-03 07:56:14 |
| [eve](https://github.com/pyeve/eve) | 6737 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5633 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5315 | 438 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5023 | 947 | 871 | 261 | 169 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 886 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3662 | 292 | 1160 | 196 | 117 | 2025-10-04 00:44:51 |
| [quart](https://github.com/pallets/quart) | 3472 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2692 | 303 | 651 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2312 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2228 | 165 | 404 | 522 | 66 | 2025-10-03 08:03:26 |
| [web2py](https://github.com/web2py/web2py) | 2164 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-09-29 17:34:25 |
| [pypy](https://github.com/pypy/pypy) | 1506 | 88 | 5149 | 171 | 739 | 2025-10-03 06:56:12 |
| [jython](https://github.com/jython/jython) | 1437 | 224 | 282 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-09-22 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-04T01:49:18*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
