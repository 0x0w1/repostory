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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200942 | 79389 | 41893 | 83575 | 3425 | 2026-10-14 04:12:21 |
| [transformers](https://github.com/huggingface/transformers) | 167686 | 34874 | 19621 | 29161 | 2325 | 2026-10-14 03:48:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 104860 | 32401 | 61702 | 138507 | 17709 | 2026-10-14 04:35:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 103097 | 10038 | 3556 | 6421 | 88 | 2026-10-08 12:29:28 |
| [django](https://github.com/django/django) | 91427 | 37201 | 0 | 22062 | 539 | 2026-10-14 01:04:34 |
| [cpython](https://github.com/python/cpython) | 77727 | 38292 | 78692 | 78328 | 9751 | 2026-10-14 03:36:44 |
| [flask](https://github.com/pallets/flask) | 75052 | 17074 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67584 | 27524 | 12324 | 21619 | 2152 | 2026-10-14 01:45:59 |
| [keras](https://github.com/keras-team/keras) | 64371 | 19799 | 13006 | 10063 | 229 | 2026-10-14 01:10:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 50057 | 20509 | 28601 | 39433 | 2235 | 2026-10-14 02:40:57 |
| [ray](https://github.com/ray-project/ray) | 44024 | 8147 | 23165 | 43390 | 3575 | 2026-10-14 03:11:07 |
| [gym](https://github.com/openai/gym) | 37243 | 8668 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33957 | 4731 | 5775 | 4129 | 251 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33102 | 12910 | 14129 | 18789 | 2244 | 2026-10-14 03:10:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30207 | 7094 | 3966 | 5090 | 56 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28973 | 5217 | 5333 | 4559 | 730 | 2026-10-14 04:18:11 |
| [dash](https://github.com/plotly/dash) | 24450 | 2328 | 2166 | 1766 | 430 | 2026-10-14 00:44:09 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23366 | 8509 | 11437 | 20969 | 1495 | 2026-10-14 04:33:25 |
| [RustPython](https://github.com/RustPython/RustPython) | 22391 | 1501 | 1438 | 7562 | 292 | 2026-10-14 00:53:14 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5574 | 1889 | 1886 | 223 | 2026-10-13 21:18:18 |
| [micropython](https://github.com/micropython/micropython) | 22123 | 9006 | 6141 | 8130 | 1529 | 2026-10-14 01:31:42 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18839 | 2869 | 3389 | 2226 | 729 | 2026-10-09 16:12:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1610 | 1471 | 1685 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16574 | 2456 | 3264 | 10429 | 232 | 2026-10-13 12:29:45 |
| [httpx](https://github.com/encode/httpx) | 15651 | 3996 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15109 | 6010 | 11689 | 14684 | 1871 | 2026-10-13 21:05:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14067 | 2149 | 2663 | 1239 | 249 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1979 | 5568 | 6756 | 1363 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12662 | 1376 | 787 | 2209 | 53 | 2026-10-13 07:53:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12239 | 1815 | 8340 | 1226 | 217 | 2026-10-13 17:12:37 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 615 | 426 | 339 | 169 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 1038 | 1147 | 1545 | 157 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9210 | 617 | 1050 | 562 | 224 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8795 | 1516 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7346 | 451 | 903 | 2631 | 333 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 527 | 1275 | 926 | 528 | 2026-10-13 16:50:29 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5425 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4447 | 384 | 1206 | 254 | 122 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 894 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1358 | 269 | 2026-10-13 23:26:13 |
| [anyio](https://github.com/agronholm/anyio) | 2556 | 311 | 489 | 847 | 134 | 2026-10-13 07:42:05 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1813 | 130 | 5280 | 349 | 716 | 2026-10-13 17:09:08 |
| [jython](https://github.com/jython/jython) | 1547 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-14T04:37:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
