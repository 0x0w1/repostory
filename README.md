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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201726 | 77999 | 41980 | 84866 | 3460 | 2026-11-18 07:01:03 |
| [transformers](https://github.com/huggingface/transformers) | 169303 | 35276 | 19903 | 30140 | 1113 | 2026-11-18 04:54:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 105792 | 30785 | 62740 | 141994 | 18419 | 2026-11-18 07:01:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 104986 | 10390 | 3555 | 6645 | 49 | 2026-11-17 18:28:44 |
| [django](https://github.com/django/django) | 91996 | 35243 | 0 | 22214 | 531 | 2026-11-17 20:07:14 |
| [cpython](https://github.com/python/cpython) | 78478 | 36656 | 79320 | 80460 | 9323 | 2026-11-18 02:41:40 |
| [flask](https://github.com/pallets/flask) | 75368 | 17384 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68225 | 27688 | 12392 | 21843 | 2176 | 2026-11-17 21:32:44 |
| [keras](https://github.com/keras-team/keras) | 64429 | 19817 | 13092 | 10289 | 238 | 2026-11-18 00:28:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 50560 | 20748 | 28696 | 40077 | 1828 | 2026-11-18 02:14:46 |
| [ray](https://github.com/ray-project/ray) | 44316 | 8291 | 23337 | 44466 | 3813 | 2026-11-18 06:41:40 |
| [gym](https://github.com/openai/gym) | 37238 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34067 | 4743 | 5785 | 4153 | 276 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33403 | 13106 | 14193 | 19066 | 2249 | 2026-11-18 00:22:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30244 | 7102 | 3966 | 5115 | 61 | 2026-11-18 06:44:57 |
| [celery](https://github.com/celery/celery) | 29224 | 5265 | 5398 | 4745 | 813 | 2026-11-17 17:59:22 |
| [dash](https://github.com/plotly/dash) | 24495 | 2347 | 2184 | 1842 | 432 | 2026-11-17 20:23:07 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23474 | 8552 | 11465 | 21084 | 1483 | 2026-11-18 03:51:16 |
| [RustPython](https://github.com/RustPython/RustPython) | 22491 | 1510 | 1469 | 8361 | 317 | 2026-11-18 05:59:30 |
| [micropython](https://github.com/micropython/micropython) | 22209 | 9066 | 6181 | 8270 | 1588 | 2026-11-18 04:00:33 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5610 | 1896 | 1940 | 213 | 2026-11-18 02:54:16 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18909 | 2898 | 3404 | 2289 | 736 | 2026-11-17 21:08:23 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1619 | 1474 | 1690 | 164 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16609 | 2528 | 3278 | 10746 | 325 | 2026-11-17 15:42:10 |
| [httpx](https://github.com/encode/httpx) | 15800 | 1996 | 925 | 1817 | 143 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15224 | 6099 | 11780 | 14936 | 1924 | 2026-11-18 03:25:32 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14117 | 2164 | 2669 | 1262 | 261 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13958 | 2031 | 5583 | 6844 | 1433 | 2026-11-17 00:50:22 |
| [starlette](https://github.com/Kludex/starlette) | 12727 | 1447 | 799 | 2304 | 35 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12296 | 1953 | 8409 | 1264 | 218 | 2026-11-16 21:02:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11942 | 623 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9822 | 1056 | 1154 | 1580 | 163 | 2026-11-16 21:28:35 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9247 | 626 | 1057 | 620 | 159 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8802 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7366 | 477 | 911 | 2674 | 345 | 2026-11-17 15:39:51 |
| [hug](https://github.com/hugapi/hug) | 6870 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 548 | 1311 | 995 | 562 | 2026-11-16 17:48:02 |
| [vibora](https://github.com/vibora-io/vibora) | 5578 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5455 | 1054 | 939 | 336 | 198 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4483 | 393 | 1212 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3984 | 359 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1426 | 257 | 2026-11-17 15:54:21 |
| [anyio](https://github.com/agronholm/anyio) | 2572 | 358 | 506 | 909 | 167 | 2026-11-17 00:12:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1950 | 372 | 1791 | 283 | 279 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1825 | 133 | 5304 | 461 | 733 | 2026-11-17 21:09:09 |
| [jython](https://github.com/jython/jython) | 1550 | 236 | 307 | 163 | 107 | 2026-11-16 18:03:33 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-18T07:02:13*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
