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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201599 | 77959 | 41984 | 84897 | 3437 | 2026-11-19 06:44:35 |
| [transformers](https://github.com/huggingface/transformers) | 169205 | 35234 | 19909 | 30169 | 1102 | 2026-11-19 06:50:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 105660 | 30754 | 62774 | 142124 | 18407 | 2026-11-19 06:59:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 104880 | 10356 | 3555 | 6649 | 49 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91802 | 35195 | 0 | 22220 | 535 | 2026-11-17 20:07:14 |
| [cpython](https://github.com/python/cpython) | 78352 | 36606 | 79334 | 80504 | 9336 | 2026-11-19 05:44:24 |
| [flask](https://github.com/pallets/flask) | 75224 | 17340 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68239 | 27688 | 12397 | 21851 | 2168 | 2026-11-19 06:15:19 |
| [keras](https://github.com/keras-team/keras) | 64427 | 19815 | 13100 | 10295 | 241 | 2026-11-19 03:56:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 50568 | 20754 | 28700 | 40113 | 1827 | 2026-11-18 19:00:25 |
| [ray](https://github.com/ray-project/ray) | 44325 | 8292 | 23346 | 44497 | 3811 | 2026-11-19 06:08:43 |
| [gym](https://github.com/openai/gym) | 37239 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34074 | 4745 | 5785 | 4153 | 276 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33412 | 13109 | 14196 | 19074 | 2249 | 2026-11-18 21:12:27 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30241 | 7101 | 3966 | 5116 | 62 | 2026-11-18 06:44:57 |
| [celery](https://github.com/celery/celery) | 29227 | 5266 | 5399 | 4748 | 809 | 2026-11-18 18:05:15 |
| [dash](https://github.com/plotly/dash) | 24495 | 2347 | 2185 | 1847 | 428 | 2026-11-18 20:49:42 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23479 | 8557 | 11465 | 21088 | 1483 | 2026-11-19 06:37:55 |
| [RustPython](https://github.com/RustPython/RustPython) | 22495 | 1511 | 1470 | 8381 | 322 | 2026-11-19 05:06:22 |
| [micropython](https://github.com/micropython/micropython) | 22211 | 9068 | 6183 | 8273 | 1591 | 2026-11-19 02:54:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5610 | 1899 | 1944 | 209 | 2026-11-18 20:57:24 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18911 | 2899 | 3404 | 2289 | 734 | 2026-11-18 22:25:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1619 | 1474 | 1691 | 165 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16609 | 2528 | 3278 | 10747 | 326 | 2026-11-17 15:42:10 |
| [httpx](https://github.com/encode/httpx) | 15804 | 2011 | 925 | 1818 | 144 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15224 | 6101 | 11781 | 14943 | 1928 | 2026-11-18 12:43:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14118 | 2164 | 2669 | 1262 | 261 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13958 | 2031 | 5583 | 6844 | 1432 | 2026-11-17 00:50:22 |
| [starlette](https://github.com/Kludex/starlette) | 12731 | 1449 | 799 | 2304 | 35 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12296 | 1960 | 8409 | 1266 | 220 | 2026-11-16 21:02:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11945 | 623 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9822 | 1057 | 1154 | 1583 | 166 | 2026-11-16 21:28:35 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9249 | 626 | 1057 | 620 | 159 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 478 | 911 | 2677 | 344 | 2026-11-18 11:55:16 |
| [hug](https://github.com/hugapi/hug) | 6870 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 549 | 1311 | 996 | 563 | 2026-11-16 17:48:02 |
| [vibora](https://github.com/vibora-io/vibora) | 5578 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5456 | 1053 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4483 | 395 | 1212 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2750 | 90 | 2026-11-19 00:38:40 |
| [databases](https://github.com/encode/databases) | 3985 | 369 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3684 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 320 | 682 | 1426 | 256 | 2026-11-18 19:48:44 |
| [anyio](https://github.com/agronholm/anyio) | 2573 | 358 | 506 | 910 | 167 | 2026-11-17 00:12:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2354 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1950 | 372 | 1791 | 283 | 279 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5304 | 462 | 730 | 2026-11-18 20:51:44 |
| [jython](https://github.com/jython/jython) | 1550 | 237 | 308 | 164 | 109 | 2026-11-16 18:03:33 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-19T07:03:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
