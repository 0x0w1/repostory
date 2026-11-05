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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201314 | 78236 | 41961 | 84401 | 3485 | 2026-11-05 05:23:40 |
| [transformers](https://github.com/huggingface/transformers) | 168557 | 35116 | 19781 | 29774 | 1042 | 2026-11-05 06:12:57 |
| [pytorch](https://github.com/pytorch/pytorch) | 105148 | 31300 | 62289 | 140538 | 17929 | 2026-11-05 06:20:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 104412 | 10186 | 3556 | 6568 | 61 | 2026-11-04 20:10:51 |
| [django](https://github.com/django/django) | 91512 | 35955 | 0 | 22167 | 538 | 2026-11-05 01:17:53 |
| [cpython](https://github.com/python/cpython) | 77879 | 37142 | 79120 | 79866 | 9245 | 2026-11-05 05:59:44 |
| [flask](https://github.com/pallets/flask) | 74954 | 17248 | 2773 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68020 | 27630 | 12360 | 21753 | 2147 | 2026-11-04 18:30:07 |
| [keras](https://github.com/keras-team/keras) | 64419 | 19818 | 13066 | 10216 | 285 | 2026-11-05 04:43:39 |
| [pandas](https://github.com/pandas-dev/pandas) | 50339 | 20706 | 28665 | 39816 | 2006 | 2026-11-05 01:42:57 |
| [ray](https://github.com/ray-project/ray) | 44206 | 8250 | 23286 | 44115 | 3746 | 2026-11-05 06:04:25 |
| [gym](https://github.com/openai/gym) | 37231 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34026 | 4740 | 5781 | 4140 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33274 | 13075 | 14165 | 18950 | 2233 | 2026-11-04 19:26:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30230 | 7096 | 3966 | 5105 | 64 | 2026-11-05 00:01:21 |
| [celery](https://github.com/celery/celery) | 29138 | 5255 | 5361 | 4688 | 741 | 2026-11-05 05:51:23 |
| [dash](https://github.com/plotly/dash) | 24477 | 2338 | 2173 | 1818 | 441 | 2026-11-04 14:53:26 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23427 | 8543 | 11454 | 21031 | 1471 | 2026-11-05 02:59:33 |
| [RustPython](https://github.com/RustPython/RustPython) | 22454 | 1509 | 1456 | 8163 | 383 | 2026-11-05 06:14:04 |
| [micropython](https://github.com/micropython/micropython) | 22181 | 9044 | 6168 | 8211 | 1576 | 2026-11-03 03:35:46 |
| [tornado](https://github.com/tornadoweb/tornado) | 22163 | 5606 | 1891 | 1904 | 237 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18878 | 2892 | 3402 | 2273 | 752 | 2026-11-03 22:37:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1615 | 1473 | 1687 | 161 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16606 | 2504 | 3270 | 10625 | 280 | 2026-11-04 18:21:56 |
| [httpx](https://github.com/encode/httpx) | 15751 | 2592 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15185 | 6064 | 11751 | 14837 | 1909 | 2026-11-04 21:16:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14099 | 2158 | 2668 | 1253 | 253 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13941 | 2015 | 5581 | 6808 | 1424 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12712 | 1434 | 795 | 2303 | 37 | 2026-11-01 20:39:28 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12275 | 1843 | 8379 | 1258 | 212 | 2026-11-04 15:12:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11927 | 619 | 428 | 344 | 173 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9812 | 1052 | 1150 | 1567 | 165 | 2026-11-04 21:49:13 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9232 | 625 | 1057 | 604 | 159 | 2026-11-04 16:56:40 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1515 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7358 | 468 | 908 | 2660 | 339 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6871 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 543 | 1304 | 986 | 563 | 2026-11-05 05:50:49 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5445 | 1053 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4466 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3679 | 210 | 289 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 318 | 681 | 1404 | 267 | 2026-11-04 20:42:10 |
| [anyio](https://github.com/agronholm/anyio) | 2566 | 347 | 497 | 881 | 141 | 2026-11-03 20:41:26 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1610 | 355 | 2026-11-03 14:17:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1791 | 278 | 279 | 2026-11-04 19:16:56 |
| [pypy](https://github.com/pypy/pypy) | 1822 | 131 | 5298 | 402 | 717 | 2026-11-04 19:47:56 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 104 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 103 | 39 | 16 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-05T06:21:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
