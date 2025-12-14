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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192784 | 75065 | 41035 | 63025 | 2773 | 2025-12-14 02:19:41 |
| [transformers](https://github.com/huggingface/transformers) | 153826 | 31417 | 18327 | 23930 | 2165 | 2025-12-12 20:59:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 95863 | 26209 | 55838 | 114057 | 17840 | 2025-12-14 02:22:39 |
| [fastapi](https://github.com/fastapi/fastapi) | 93043 | 8358 | 3499 | 4967 | 179 | 2025-12-12 17:00:39 |
| [django](https://github.com/django/django) | 86138 | 33315 | 0 | 20337 | 366 | 2025-12-13 15:38:04 |
| [flask](https://github.com/pallets/flask) | 70917 | 16649 | 2705 | 2732 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70290 | 33662 | 74666 | 67046 | 9254 | 2025-12-13 23:24:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64283 | 26505 | 11846 | 19914 | 2122 | 2025-12-12 14:39:05 |
| [keras](https://github.com/keras-team/keras) | 63630 | 19649 | 12604 | 8528 | 256 | 2025-12-14 01:52:40 |
| [pandas](https://github.com/pandas-dev/pandas) | 47305 | 19400 | 27949 | 35346 | 3596 | 2025-12-13 16:50:13 |
| [ray](https://github.com/ray-project/ray) | 40304 | 7008 | 22013 | 37058 | 3177 | 2025-12-13 08:19:55 |
| [gym](https://github.com/openai/gym) | 36868 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32947 | 4635 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31003 | 11831 | 13695 | 16671 | 2387 | 2025-12-12 18:06:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29731 | 7040 | 3946 | 4884 | 76 | 2025-12-12 11:54:26 |
| [celery](https://github.com/celery/celery) | 27705 | 4913 | 5179 | 3740 | 753 | 2025-12-09 10:17:07 |
| [dash](https://github.com/plotly/dash) | 24335 | 2244 | 2035 | 1389 | 559 | 2025-12-12 15:47:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22382 | 5544 | 1859 | 1687 | 208 | 2025-12-11 14:59:09 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22114 | 8142 | 11075 | 19735 | 1570 | 2025-12-14 00:17:33 |
| [micropython](https://github.com/micropython/micropython) | 21202 | 8587 | 5897 | 7434 | 1810 | 2025-12-12 19:05:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 20897 | 1369 | 1245 | 5125 | 444 | 2025-12-13 13:06:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18597 | 1585 | 1455 | 1635 | 129 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18087 | 2762 | 3306 | 1992 | 754 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16140 | 2167 | 3165 | 8370 | 269 | 2025-12-12 22:25:56 |
| [httpx](https://github.com/encode/httpx) | 14837 | 991 | 923 | 1766 | 115 | 2025-12-10 15:17:09 |
| [scipy](https://github.com/scipy/scipy) | 14255 | 5557 | 11185 | 12954 | 1765 | 2025-12-14 00:23:06 |
| [dask](https://github.com/dask/dask) | 13651 | 1827 | 5476 | 6418 | 1200 | 2025-12-12 14:58:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13615 | 2064 | 2640 | 1150 | 199 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11756 | 1089 | 760 | 1747 | 53 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11521 | 589 | 397 | 298 | 148 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11257 | 1605 | 8128 | 1010 | 205 | 2025-12-10 20:45:00 |
| [falcon](https://github.com/falconry/falcon) | 9768 | 972 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8772 | 548 | 983 | 471 | 188 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8712 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7053 | 373 | 877 | 2481 | 314 | 2025-12-09 00:42:38 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 743 | 979 | 581 | 35 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5623 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5412 | 445 | 1207 | 727 | 511 | 2025-12-12 14:08:28 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5111 | 970 | 880 | 269 | 171 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3812 | 300 | 1169 | 202 | 118 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3559 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2716 | 307 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2325 | 180 | 420 | 555 | 75 | 2025-12-08 17:56:30 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-08 17:49:38 |
| [pypy](https://github.com/pypy/pypy) | 1599 | 91 | 5166 | 172 | 751 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 287 | 115 | 104 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-14T02:24:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
