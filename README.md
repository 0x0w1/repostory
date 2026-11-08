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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201390 | 78401 | 41963 | 84499 | 3520 | 2026-11-08 05:03:27 |
| [transformers](https://github.com/huggingface/transformers) | 168639 | 35136 | 19808 | 29836 | 1065 | 2026-11-08 00:34:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 105244 | 31326 | 62380 | 140869 | 18112 | 2026-11-08 05:45:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 104559 | 10202 | 3555 | 6580 | 59 | 2026-11-07 21:01:52 |
| [django](https://github.com/django/django) | 91688 | 35970 | 0 | 22184 | 536 | 2026-11-06 22:17:53 |
| [cpython](https://github.com/python/cpython) | 78084 | 37188 | 79181 | 80023 | 9270 | 2026-11-08 02:46:48 |
| [flask](https://github.com/pallets/flask) | 75069 | 17288 | 2778 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68089 | 27651 | 12369 | 21773 | 2164 | 2026-11-06 12:37:21 |
| [keras](https://github.com/keras-team/keras) | 64416 | 19815 | 13068 | 10224 | 284 | 2026-11-06 21:43:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 50525 | 20728 | 28669 | 39844 | 1978 | 2026-11-08 04:17:16 |
| [ray](https://github.com/ray-project/ray) | 44234 | 8253 | 23294 | 44187 | 3736 | 2026-11-08 03:19:23 |
| [gym](https://github.com/openai/gym) | 37233 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34038 | 4739 | 5782 | 4144 | 265 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33394 | 13092 | 14170 | 18976 | 2242 | 2026-11-07 21:05:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30229 | 7098 | 3966 | 5107 | 64 | 2026-11-07 13:50:43 |
| [celery](https://github.com/celery/celery) | 29143 | 5257 | 5360 | 4698 | 743 | 2026-11-07 14:32:22 |
| [dash](https://github.com/plotly/dash) | 24480 | 2341 | 2178 | 1822 | 447 | 2026-11-06 15:40:44 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23432 | 8543 | 11456 | 21038 | 1471 | 2026-11-08 05:20:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 22464 | 1509 | 1457 | 8186 | 312 | 2026-11-08 04:41:37 |
| [micropython](https://github.com/micropython/micropython) | 22179 | 9047 | 6174 | 8224 | 1584 | 2026-11-06 12:22:36 |
| [tornado](https://github.com/tornadoweb/tornado) | 22163 | 5607 | 1893 | 1914 | 229 | 2026-11-06 22:24:20 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18880 | 2893 | 3402 | 2280 | 755 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1616 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16605 | 2513 | 3273 | 10665 | 290 | 2026-11-07 22:31:18 |
| [httpx](https://github.com/encode/httpx) | 15747 | 2586 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15192 | 6068 | 11760 | 14864 | 1906 | 2026-11-07 23:37:42 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14099 | 2158 | 2668 | 1253 | 253 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13941 | 2016 | 5582 | 6810 | 1427 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12712 | 1442 | 796 | 2305 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12274 | 1846 | 8381 | 1261 | 209 | 2026-11-07 16:56:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11929 | 618 | 429 | 344 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9813 | 1053 | 1150 | 1569 | 164 | 2026-11-07 22:41:22 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9238 | 627 | 1057 | 610 | 155 | 2026-11-06 14:41:48 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1515 | 866 | 656 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7357 | 471 | 910 | 2663 | 342 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5646 | 543 | 1307 | 988 | 563 | 2026-11-07 04:17:10 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5446 | 1054 | 938 | 329 | 207 | 2026-11-07 09:09:52 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4468 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 896 | 1066 | 2743 | 92 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 279 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3680 | 211 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 319 | 681 | 1412 | 259 | 2026-11-08 04:41:14 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 498 | 885 | 146 | 2026-11-07 19:00:14 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 915 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 279 | 279 | 2026-11-06 00:44:46 |
| [pypy](https://github.com/pypy/pypy) | 1823 | 131 | 5299 | 406 | 719 | 2026-11-08 04:36:45 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 103 | 2026-11-07 21:07:33 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 103 | 39 | 16 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-08T05:45:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
