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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193623 | 75211 | 41147 | 66556 | 3287 | 2026-02-06 02:18:18 |
| [transformers](https://github.com/huggingface/transformers) | 156142 | 31970 | 18531 | 24653 | 2219 | 2026-02-05 20:59:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 97186 | 26763 | 56709 | 117232 | 18017 | 2026-02-06 02:44:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 94835 | 8633 | 3502 | 5232 | 173 | 2026-02-05 19:52:51 |
| [django](https://github.com/django/django) | 86689 | 33624 | 0 | 20578 | 404 | 2026-02-05 14:18:55 |
| [cpython](https://github.com/python/cpython) | 71373 | 34025 | 75182 | 68337 | 9214 | 2026-02-05 20:37:06 |
| [flask](https://github.com/pallets/flask) | 71137 | 16693 | 2713 | 2762 | 2 | 2026-02-03 18:22:23 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64921 | 26669 | 11915 | 20156 | 2117 | 2026-02-05 18:10:49 |
| [keras](https://github.com/keras-team/keras) | 63754 | 19687 | 12625 | 8698 | 259 | 2026-02-05 19:39:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 47796 | 19617 | 28080 | 35903 | 3632 | 2026-02-05 20:12:49 |
| [ray](https://github.com/ray-project/ray) | 41158 | 7189 | 22286 | 38158 | 3345 | 2026-02-06 02:18:10 |
| [gym](https://github.com/openai/gym) | 37011 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33166 | 4636 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31386 | 12024 | 13779 | 16947 | 2298 | 2026-02-05 19:16:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29855 | 7063 | 3946 | 4918 | 90 | 2026-02-05 15:11:44 |
| [celery](https://github.com/celery/celery) | 27970 | 4937 | 5187 | 3787 | 762 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24456 | 2253 | 2053 | 1429 | 559 | 2026-02-05 23:11:54 |
| [tornado](https://github.com/tornadoweb/tornado) | 22439 | 5543 | 1863 | 1698 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22309 | 8181 | 11128 | 19920 | 1527 | 2026-02-06 02:06:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 21756 | 1400 | 1295 | 5661 | 373 | 2026-02-06 02:42:37 |
| [micropython](https://github.com/micropython/micropython) | 21434 | 8696 | 5950 | 7543 | 1850 | 2026-02-05 13:21:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1583 | 1465 | 1663 | 115 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18235 | 2779 | 3320 | 2010 | 774 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16250 | 2185 | 3176 | 8551 | 279 | 2026-02-05 16:58:15 |
| [httpx](https://github.com/encode/httpx) | 14972 | 1027 | 925 | 1783 | 129 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14423 | 5608 | 11289 | 13211 | 1756 | 2026-02-05 14:08:26 |
| [dask](https://github.com/dask/dask) | 13731 | 1842 | 5504 | 6481 | 1225 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13702 | 2079 | 2645 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11895 | 1105 | 763 | 1782 | 51 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11629 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11470 | 1634 | 8150 | 1028 | 208 | 2026-02-05 16:47:53 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 978 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8886 | 556 | 1005 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8741 | 1492 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7153 | 381 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5476 | 453 | 1222 | 747 | 505 | 2026-02-06 02:29:41 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5180 | 1000 | 900 | 289 | 190 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3940 | 310 | 1181 | 208 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3590 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2724 | 308 | 657 | 1269 | 313 | 2026-02-05 22:02:07 |
| [anyio](https://github.com/agronholm/anyio) | 2378 | 178 | 423 | 565 | 75 | 2026-02-04 20:13:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1933 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1645 | 97 | 5173 | 179 | 756 | 2026-02-05 13:17:55 |
| [jython](https://github.com/jython/jython) | 1480 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-06T02:47:20*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
