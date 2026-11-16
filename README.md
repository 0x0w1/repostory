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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201628 | 77973 | 41977 | 84785 | 3463 | 2026-11-16 05:58:07 |
| [transformers](https://github.com/huggingface/transformers) | 169035 | 35214 | 19883 | 30068 | 1142 | 2026-11-16 05:34:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 105552 | 30732 | 62662 | 141693 | 18315 | 2026-11-16 05:47:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 104769 | 10307 | 3555 | 6637 | 76 | 2026-11-15 17:10:39 |
| [django](https://github.com/django/django) | 91775 | 35222 | 0 | 22205 | 531 | 2026-11-13 17:06:51 |
| [cpython](https://github.com/python/cpython) | 78249 | 36608 | 79296 | 80371 | 9304 | 2026-11-16 05:30:07 |
| [flask](https://github.com/pallets/flask) | 75156 | 17336 | 2780 | 2911 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68191 | 27680 | 12383 | 21822 | 2164 | 2026-11-16 00:51:39 |
| [keras](https://github.com/keras-team/keras) | 64424 | 19815 | 13088 | 10265 | 237 | 2026-11-14 20:23:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 50536 | 20743 | 28692 | 40034 | 1841 | 2026-11-15 19:46:08 |
| [ray](https://github.com/ray-project/ray) | 44292 | 8285 | 23323 | 44389 | 3805 | 2026-11-16 06:00:02 |
| [gym](https://github.com/openai/gym) | 37239 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34059 | 4740 | 5785 | 4150 | 273 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33379 | 13100 | 14188 | 19052 | 2251 | 2026-11-16 03:51:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30239 | 7101 | 3966 | 5113 | 64 | 2026-11-12 10:27:24 |
| [celery](https://github.com/celery/celery) | 29204 | 5263 | 5392 | 4735 | 805 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24488 | 2348 | 2182 | 1836 | 438 | 2026-11-13 15:25:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23463 | 8549 | 11463 | 21079 | 1479 | 2026-11-15 20:03:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22486 | 1510 | 1468 | 8295 | 307 | 2026-11-16 05:58:03 |
| [micropython](https://github.com/micropython/micropython) | 22202 | 9061 | 6181 | 8266 | 1604 | 2026-11-16 02:41:54 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5608 | 1896 | 1930 | 223 | 2026-11-13 20:46:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18906 | 2898 | 3403 | 2284 | 756 | 2026-11-13 07:35:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18634 | 1617 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16609 | 2524 | 3277 | 10718 | 314 | 2026-11-14 22:26:46 |
| [httpx](https://github.com/encode/httpx) | 15798 | 1924 | 925 | 1801 | 136 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15219 | 6090 | 11770 | 14917 | 1913 | 2026-11-15 20:37:39 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14112 | 2162 | 2669 | 1256 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13953 | 2027 | 5583 | 6838 | 1435 | 2026-11-13 16:55:52 |
| [starlette](https://github.com/Kludex/starlette) | 12723 | 1447 | 799 | 2302 | 35 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12287 | 1890 | 8407 | 1263 | 218 | 2026-11-15 22:34:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11937 | 621 | 431 | 347 | 179 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9816 | 1056 | 1154 | 1580 | 164 | 2026-11-11 09:13:34 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9245 | 626 | 1057 | 617 | 159 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1512 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7365 | 475 | 911 | 2673 | 344 | 2026-11-13 19:20:22 |
| [hug](https://github.com/hugapi/hug) | 6870 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 545 | 1310 | 991 | 561 | 2026-11-12 09:12:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5578 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5453 | 1054 | 938 | 335 | 201 | 2026-11-14 15:09:10 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4479 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3984 | 320 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 321 | 682 | 1421 | 258 | 2026-11-16 04:51:36 |
| [anyio](https://github.com/agronholm/anyio) | 2571 | 353 | 505 | 901 | 161 | 2026-11-15 23:59:05 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1950 | 373 | 1791 | 284 | 280 | 2026-11-14 20:48:56 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 133 | 5303 | 438 | 726 | 2026-11-16 05:40:12 |
| [jython](https://github.com/jython/jython) | 1550 | 237 | 306 | 163 | 108 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-16T06:03:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
