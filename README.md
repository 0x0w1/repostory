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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201658 | 77966 | 41985 | 84936 | 3452 | 2026-11-20 06:54:15 |
| [transformers](https://github.com/huggingface/transformers) | 169306 | 35253 | 19914 | 30215 | 1100 | 2026-11-20 06:51:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 105731 | 30766 | 62835 | 142251 | 18470 | 2026-11-20 06:55:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 104960 | 10377 | 3555 | 6645 | 49 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91872 | 35203 | 0 | 22228 | 535 | 2026-11-19 22:44:16 |
| [cpython](https://github.com/python/cpython) | 78425 | 36625 | 79350 | 80540 | 9351 | 2026-11-20 04:41:56 |
| [flask](https://github.com/pallets/flask) | 75285 | 17355 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68261 | 27691 | 12398 | 21863 | 2165 | 2026-11-20 03:14:08 |
| [keras](https://github.com/keras-team/keras) | 64441 | 19819 | 13101 | 10307 | 243 | 2026-11-20 02:15:20 |
| [pandas](https://github.com/pandas-dev/pandas) | 50577 | 20765 | 28703 | 40121 | 1813 | 2026-11-19 23:13:45 |
| [ray](https://github.com/ray-project/ray) | 44345 | 8298 | 23355 | 44554 | 3825 | 2026-11-20 06:48:25 |
| [gym](https://github.com/openai/gym) | 37237 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34076 | 4747 | 5785 | 4154 | 277 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33430 | 13119 | 14199 | 19079 | 2253 | 2026-11-20 03:53:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30253 | 7106 | 3966 | 5119 | 58 | 2026-11-19 09:00:18 |
| [celery](https://github.com/celery/celery) | 29246 | 5276 | 5400 | 4750 | 805 | 2026-11-19 19:15:56 |
| [dash](https://github.com/plotly/dash) | 24498 | 2347 | 2185 | 1849 | 424 | 2026-11-19 21:30:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23492 | 8565 | 11465 | 21091 | 1479 | 2026-11-20 04:20:50 |
| [RustPython](https://github.com/RustPython/RustPython) | 22497 | 1508 | 1472 | 8396 | 339 | 2026-11-19 05:06:22 |
| [micropython](https://github.com/micropython/micropython) | 22213 | 9070 | 6183 | 8278 | 1595 | 2026-11-19 02:54:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22174 | 5616 | 1900 | 1946 | 205 | 2026-11-20 02:35:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18914 | 2900 | 3406 | 2293 | 733 | 2026-11-19 23:40:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1618 | 1475 | 1690 | 165 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16620 | 2533 | 3279 | 10751 | 330 | 2026-11-19 11:08:43 |
| [httpx](https://github.com/encode/httpx) | 15811 | 2007 | 925 | 1820 | 146 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15225 | 6107 | 11785 | 14952 | 1931 | 2026-11-19 20:48:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14118 | 2164 | 2669 | 1262 | 261 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13959 | 2029 | 5583 | 6843 | 1431 | 2026-11-17 00:50:22 |
| [starlette](https://github.com/Kludex/starlette) | 12733 | 1450 | 799 | 2304 | 35 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12296 | 1960 | 8409 | 1263 | 218 | 2026-11-19 21:09:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11944 | 624 | 431 | 348 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9821 | 1056 | 1154 | 1582 | 166 | 2026-11-16 21:28:35 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9250 | 624 | 1059 | 620 | 161 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7367 | 479 | 911 | 2678 | 344 | 2026-11-18 11:55:16 |
| [hug](https://github.com/hugapi/hug) | 6869 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5641 | 548 | 1311 | 995 | 560 | 2026-11-19 14:41:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5456 | 1054 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4481 | 394 | 1212 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2751 | 83 | 2026-11-20 03:37:34 |
| [databases](https://github.com/encode/databases) | 3984 | 369 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 214 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1426 | 256 | 2026-11-18 19:48:44 |
| [anyio](https://github.com/agronholm/anyio) | 2572 | 358 | 506 | 913 | 164 | 2026-11-20 00:26:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 372 | 1791 | 283 | 279 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5304 | 468 | 725 | 2026-11-19 22:09:50 |
| [jython](https://github.com/jython/jython) | 1549 | 237 | 306 | 164 | 109 | 2026-11-16 18:03:33 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-20T06:55:50*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
