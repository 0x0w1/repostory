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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192717 | 75035 | 41031 | 62732 | 2722 | 2025-12-09 02:03:15 |
| [transformers](https://github.com/huggingface/transformers) | 153614 | 31351 | 18298 | 23823 | 2129 | 2025-12-08 21:17:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 95701 | 26144 | 55733 | 113682 | 17836 | 2025-12-09 02:08:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 92872 | 8342 | 3483 | 4944 | 192 | 2025-12-08 13:05:21 |
| [django](https://github.com/django/django) | 86093 | 33300 | 0 | 20318 | 368 | 2025-12-08 15:26:38 |
| [flask](https://github.com/pallets/flask) | 70900 | 16646 | 2704 | 2730 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70173 | 33621 | 74592 | 66878 | 9239 | 2025-12-08 23:16:28 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64238 | 26494 | 11840 | 19891 | 2123 | 2025-12-08 13:52:28 |
| [keras](https://github.com/keras-team/keras) | 63624 | 19652 | 12601 | 8512 | 259 | 2025-12-07 02:35:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 47278 | 19368 | 27941 | 35304 | 3574 | 2025-12-08 18:39:28 |
| [ray](https://github.com/ray-project/ray) | 40213 | 6982 | 21982 | 36951 | 3215 | 2025-12-09 02:07:33 |
| [gym](https://github.com/openai/gym) | 36852 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32922 | 4637 | 5733 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30967 | 11809 | 13690 | 16649 | 2385 | 2025-12-09 01:08:34 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29714 | 7040 | 3946 | 4880 | 80 | 2025-12-08 08:34:28 |
| [celery](https://github.com/celery/celery) | 27693 | 4912 | 5177 | 3738 | 752 | 2025-12-05 12:28:43 |
| [dash](https://github.com/plotly/dash) | 24322 | 2243 | 2034 | 1386 | 557 | 2025-12-05 17:17:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22381 | 5543 | 1857 | 1678 | 206 | 2025-12-08 16:30:26 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22100 | 8138 | 11064 | 19717 | 1587 | 2025-12-08 23:08:32 |
| [micropython](https://github.com/micropython/micropython) | 21191 | 8579 | 5890 | 7413 | 1787 | 2025-12-08 03:20:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 20879 | 1366 | 1242 | 5064 | 441 | 2025-12-09 01:46:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18592 | 1584 | 1454 | 1635 | 128 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18065 | 2758 | 3304 | 1990 | 754 | 2025-12-08 15:18:54 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16131 | 2166 | 3164 | 8354 | 270 | 2025-12-09 00:38:27 |
| [httpx](https://github.com/encode/httpx) | 14822 | 984 | 923 | 1759 | 117 | 2025-12-01 17:39:25 |
| [scipy](https://github.com/scipy/scipy) | 14246 | 5555 | 11174 | 12928 | 1764 | 2025-12-08 09:36:09 |
| [dask](https://github.com/dask/dask) | 13643 | 1824 | 5473 | 6414 | 1201 | 2025-12-05 11:49:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13603 | 2059 | 2637 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11740 | 1089 | 760 | 1746 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11503 | 589 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11230 | 1604 | 8128 | 1009 | 211 | 2025-12-08 20:16:16 |
| [falcon](https://github.com/falconry/falcon) | 9768 | 971 | 1114 | 1403 | 162 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8764 | 546 | 981 | 465 | 181 | 2025-12-04 11:35:16 |
| [bottle](https://github.com/bottlepy/bottle) | 8709 | 1488 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7045 | 371 | 877 | 2480 | 313 | 2025-12-09 00:42:38 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 744 | 979 | 581 | 35 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5405 | 445 | 1203 | 725 | 508 | 2025-12-09 01:00:15 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5108 | 971 | 879 | 264 | 172 | 2025-12-08 08:41:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3807 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3557 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2715 | 306 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2331 | 135 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2321 | 180 | 419 | 555 | 74 | 2025-12-08 17:56:30 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-08 17:49:38 |
| [pypy](https://github.com/pypy/pypy) | 1593 | 91 | 5166 | 172 | 750 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-09T02:08:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
