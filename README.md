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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191858 | 74884 | 40822 | 58396 | 1708 | 2025-09-29 01:39:52 |
| [transformers](https://github.com/huggingface/transformers) | 150401 | 30542 | 17991 | 22616 | 2022 | 2025-09-28 18:25:19 |
| [pytorch](https://github.com/pytorch/pytorch) | 93560 | 25421 | 54010 | 109625 | 16981 | 2025-09-29 01:54:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 89910 | 7944 | 3469 | 4736 | 211 | 2025-09-28 13:54:55 |
| [django](https://github.com/django/django) | 85259 | 33015 | 0 | 19845 | 351 | 2025-09-26 14:57:24 |
| [flask](https://github.com/pallets/flask) | 70459 | 16544 | 2698 | 2704 | 8 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69066 | 32966 | 73733 | 64742 | 9303 | 2025-09-28 21:55:44 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63491 | 26271 | 11732 | 19430 | 2154 | 2025-09-27 10:43:58 |
| [keras](https://github.com/keras-team/keras) | 63432 | 19627 | 12555 | 8357 | 263 | 2025-09-26 19:42:54 |
| [pandas](https://github.com/pandas-dev/pandas) | 46692 | 19033 | 27743 | 34698 | 3670 | 2025-09-28 16:39:34 |
| [ray](https://github.com/ray-project/ray) | 39142 | 6838 | 21244 | 35403 | 3119 | 2025-09-29 00:51:24 |
| [gym](https://github.com/openai/gym) | 36597 | 8698 | 1840 | 1467 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32553 | 4586 | 5722 | 4069 | 205 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30472 | 11470 | 13558 | 16205 | 2355 | 2025-09-28 14:52:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29506 | 7009 | 3945 | 4840 | 104 | 2025-09-25 12:59:12 |
| [celery](https://github.com/celery/celery) | 27269 | 4856 | 5168 | 3671 | 756 | 2025-09-28 17:31:41 |
| [dash](https://github.com/plotly/dash) | 24113 | 2205 | 2000 | 1338 | 570 | 2025-09-26 22:35:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22233 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21749 | 8042 | 10996 | 19575 | 1634 | 2025-09-28 13:08:57 |
| [micropython](https://github.com/micropython/micropython) | 20884 | 8459 | 5824 | 7226 | 1785 | 2025-09-28 13:26:43 |
| [RustPython](https://github.com/RustPython/RustPython) | 20561 | 1349 | 1221 | 4891 | 448 | 2025-09-22 13:05:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18500 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17788 | 2718 | 3255 | 1953 | 726 | 2025-09-26 19:38:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16011 | 2125 | 3146 | 8099 | 273 | 2025-09-26 11:06:48 |
| [httpx](https://github.com/encode/httpx) | 14585 | 958 | 918 | 1732 | 99 | 2025-09-20 17:09:10 |
| [scipy](https://github.com/scipy/scipy) | 14052 | 5485 | 11045 | 12630 | 1761 | 2025-09-28 21:38:59 |
| [dask](https://github.com/dask/dask) | 13503 | 1798 | 5440 | 6351 | 1202 | 2025-09-24 22:41:19 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13469 | 2039 | 2627 | 1149 | 189 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11499 | 1045 | 754 | 1713 | 46 | 2025-09-25 13:10:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11292 | 575 | 389 | 289 | 143 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10946 | 1583 | 8091 | 986 | 228 | 2025-09-26 22:34:39 |
| [falcon](https://github.com/falconry/falcon) | 9722 | 959 | 1100 | 1370 | 156 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8669 | 1486 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8579 | 525 | 947 | 435 | 410 | 2025-09-21 09:38:28 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6873 | 367 | 871 | 2455 | 311 | 2025-09-25 18:22:47 |
| [eve](https://github.com/pyeve/eve) | 6738 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5633 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5310 | 438 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5018 | 943 | 871 | 261 | 169 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4049 | 888 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3651 | 292 | 1158 | 196 | 116 | 2025-09-27 16:48:59 |
| [quart](https://github.com/pallets/quart) | 3469 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2689 | 303 | 650 | 1261 | 307 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2308 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2220 | 164 | 404 | 516 | 64 | 2025-09-27 13:49:56 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 908 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1923 | 369 | 1780 | 264 | 261 | 2025-09-22 17:45:36 |
| [pypy](https://github.com/pypy/pypy) | 1504 | 87 | 5146 | 171 | 737 | 2025-09-28 09:38:24 |
| [jython](https://github.com/jython/jython) | 1436 | 223 | 282 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-09-22 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-29T01:58:41*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
