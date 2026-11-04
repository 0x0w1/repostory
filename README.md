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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201295 | 78168 | 41960 | 84370 | 3481 | 2026-11-04 05:22:24 |
| [transformers](https://github.com/huggingface/transformers) | 168519 | 35104 | 19775 | 29744 | 1044 | 2026-11-04 04:20:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 105118 | 31309 | 62249 | 140375 | 17902 | 2026-11-04 05:52:30 |
| [fastapi](https://github.com/fastapi/fastapi) | 104391 | 10180 | 3556 | 6564 | 61 | 2026-11-02 14:05:20 |
| [django](https://github.com/django/django) | 91498 | 35976 | 0 | 22162 | 543 | 2026-11-03 21:03:16 |
| [cpython](https://github.com/python/cpython) | 77816 | 37162 | 79105 | 79798 | 9243 | 2026-11-04 05:55:13 |
| [flask](https://github.com/pallets/flask) | 74944 | 17257 | 2771 | 2913 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68003 | 27629 | 12359 | 21751 | 2148 | 2026-11-03 18:23:23 |
| [keras](https://github.com/keras-team/keras) | 64417 | 19818 | 13065 | 10205 | 283 | 2026-11-04 01:10:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 50321 | 20706 | 28664 | 39793 | 2021 | 2026-11-03 21:08:07 |
| [ray](https://github.com/ray-project/ray) | 44197 | 8243 | 23285 | 44073 | 3746 | 2026-11-04 04:58:30 |
| [gym](https://github.com/openai/gym) | 37229 | 8666 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34019 | 4741 | 5781 | 4140 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33252 | 13083 | 14164 | 18949 | 2239 | 2026-11-03 19:40:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30228 | 7096 | 3966 | 5105 | 68 | 2026-11-03 19:17:31 |
| [celery](https://github.com/celery/celery) | 29133 | 5253 | 5360 | 4684 | 738 | 2026-11-03 22:13:28 |
| [dash](https://github.com/plotly/dash) | 24477 | 2337 | 2173 | 1817 | 442 | 2026-11-04 02:45:48 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23421 | 8542 | 11454 | 21029 | 1472 | 2026-11-03 08:21:12 |
| [RustPython](https://github.com/RustPython/RustPython) | 22455 | 1509 | 1455 | 8131 | 402 | 2026-11-04 05:53:40 |
| [micropython](https://github.com/micropython/micropython) | 22180 | 9039 | 6167 | 8201 | 1574 | 2026-11-03 03:35:46 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5603 | 1890 | 1900 | 233 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18875 | 2891 | 3402 | 2272 | 752 | 2026-11-03 22:37:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16604 | 2504 | 3269 | 10619 | 304 | 2026-11-03 10:41:38 |
| [httpx](https://github.com/encode/httpx) | 15743 | 2615 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15182 | 6062 | 11747 | 14830 | 1901 | 2026-11-03 15:24:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14098 | 2158 | 2668 | 1253 | 263 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13942 | 2016 | 5581 | 6804 | 1420 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12706 | 1433 | 795 | 2303 | 38 | 2026-11-01 20:39:28 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12272 | 1840 | 8378 | 1256 | 209 | 2026-11-04 01:47:24 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11927 | 619 | 428 | 344 | 173 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9812 | 1053 | 1150 | 1566 | 169 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9231 | 624 | 1055 | 598 | 171 | 2026-11-03 12:13:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1515 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7358 | 468 | 907 | 2661 | 338 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6872 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5640 | 541 | 1302 | 983 | 562 | 2026-10-31 04:22:39 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5445 | 1053 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4464 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 278 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3681 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 681 | 1398 | 263 | 2026-11-04 05:32:25 |
| [anyio](https://github.com/agronholm/anyio) | 2567 | 348 | 497 | 881 | 140 | 2026-11-03 20:41:26 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1610 | 355 | 2026-11-03 14:17:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1791 | 278 | 279 | 2026-11-02 18:22:13 |
| [pypy](https://github.com/pypy/pypy) | 1822 | 131 | 5297 | 400 | 721 | 2026-11-03 16:18:17 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 104 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 103 | 39 | 16 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-04T05:57:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
