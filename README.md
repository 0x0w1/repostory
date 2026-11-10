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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201426 | 77763 | 41965 | 84568 | 3429 | 2026-11-10 06:36:55 |
| [transformers](https://github.com/huggingface/transformers) | 168722 | 35149 | 19825 | 29890 | 1073 | 2026-11-10 06:54:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 105305 | 30609 | 62432 | 141047 | 18158 | 2026-11-10 06:52:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 104604 | 10208 | 3555 | 6597 | 60 | 2026-11-09 20:01:16 |
| [django](https://github.com/django/django) | 91702 | 35210 | 0 | 22189 | 535 | 2026-11-09 09:19:25 |
| [cpython](https://github.com/python/cpython) | 78143 | 36532 | 79219 | 80117 | 9275 | 2026-11-10 06:45:41 |
| [flask](https://github.com/pallets/flask) | 75086 | 17290 | 2778 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68122 | 27661 | 12374 | 21789 | 2166 | 2026-11-10 03:58:32 |
| [keras](https://github.com/keras-team/keras) | 64419 | 19821 | 13074 | 10239 | 259 | 2026-11-10 02:55:37 |
| [pandas](https://github.com/pandas-dev/pandas) | 50561 | 20738 | 28678 | 39895 | 1912 | 2026-11-10 04:29:50 |
| [ray](https://github.com/ray-project/ray) | 44245 | 8259 | 23302 | 44230 | 3756 | 2026-11-10 06:33:10 |
| [gym](https://github.com/openai/gym) | 37234 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34039 | 4739 | 5783 | 4145 | 266 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33413 | 13106 | 14174 | 18991 | 2245 | 2026-11-10 01:28:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30230 | 7098 | 3966 | 5108 | 63 | 2026-11-09 17:39:52 |
| [celery](https://github.com/celery/celery) | 29166 | 5260 | 5378 | 4714 | 775 | 2026-11-10 02:57:55 |
| [dash](https://github.com/plotly/dash) | 24483 | 2342 | 2180 | 1829 | 449 | 2026-11-09 19:08:32 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23440 | 8545 | 11459 | 21059 | 1475 | 2026-11-09 12:38:47 |
| [RustPython](https://github.com/RustPython/RustPython) | 22470 | 1511 | 1460 | 8218 | 325 | 2026-11-10 03:32:30 |
| [micropython](https://github.com/micropython/micropython) | 22183 | 9051 | 6176 | 8231 | 1588 | 2026-11-08 12:20:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5607 | 1893 | 1922 | 229 | 2026-11-09 22:44:01 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18886 | 2895 | 3402 | 2281 | 753 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1615 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16606 | 2516 | 3275 | 10692 | 300 | 2026-11-09 15:30:00 |
| [httpx](https://github.com/encode/httpx) | 15764 | 1858 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15196 | 6072 | 11764 | 14877 | 1900 | 2026-11-09 22:02:28 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14104 | 2160 | 2668 | 1254 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13942 | 2018 | 5582 | 6812 | 1429 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12716 | 1442 | 797 | 2305 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12272 | 1848 | 8384 | 1263 | 209 | 2026-11-09 20:20:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11931 | 619 | 430 | 346 | 177 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9813 | 1054 | 1151 | 1572 | 164 | 2026-11-10 01:11:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9241 | 627 | 1057 | 615 | 159 | 2026-11-08 16:39:21 |
| [bottle](https://github.com/bottlepy/bottle) | 8797 | 1514 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7358 | 472 | 910 | 2665 | 343 | 2026-11-10 01:52:37 |
| [hug](https://github.com/hugapi/hug) | 6869 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 736 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5647 | 544 | 1307 | 989 | 560 | 2026-11-10 06:31:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5449 | 1054 | 938 | 329 | 205 | 2026-11-09 13:12:20 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4471 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4104 | 896 | 1066 | 2743 | 92 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 279 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 212 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 320 | 681 | 1412 | 258 | 2026-11-08 22:25:11 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 350 | 498 | 891 | 150 | 2026-11-09 22:34:42 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 915 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 281 | 279 | 2026-11-09 18:05:48 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 132 | 5300 | 406 | 719 | 2026-11-09 22:00:36 |
| [jython](https://github.com/jython/jython) | 1551 | 235 | 305 | 159 | 104 | 2026-11-07 21:07:33 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-10T06:59:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
