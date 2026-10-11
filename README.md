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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200772 | 78975 | 41862 | 83339 | 3311 | 2026-10-11 05:20:26 |
| [transformers](https://github.com/huggingface/transformers) | 167352 | 34806 | 19601 | 29092 | 2347 | 2026-10-11 01:24:19 |
| [pytorch](https://github.com/pytorch/pytorch) | 104187 | 31961 | 61631 | 138230 | 17718 | 2026-10-11 05:12:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 102977 | 10019 | 3555 | 6421 | 88 | 2026-10-08 12:29:28 |
| [django](https://github.com/django/django) | 91363 | 36837 | 0 | 22048 | 540 | 2026-10-10 01:48:43 |
| [cpython](https://github.com/python/cpython) | 77611 | 37914 | 78623 | 78170 | 9735 | 2026-10-10 23:12:36 |
| [flask](https://github.com/pallets/flask) | 74995 | 17067 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67522 | 27501 | 12321 | 21604 | 2165 | 2026-10-10 08:33:16 |
| [keras](https://github.com/keras-team/keras) | 64364 | 19799 | 12996 | 10037 | 237 | 2026-10-11 04:57:46 |
| [pandas](https://github.com/pandas-dev/pandas) | 49995 | 20484 | 28594 | 39376 | 2334 | 2026-10-11 04:49:25 |
| [ray](https://github.com/ray-project/ray) | 44004 | 8126 | 23153 | 43330 | 3555 | 2026-10-10 23:07:26 |
| [gym](https://github.com/openai/gym) | 37245 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33951 | 4732 | 5773 | 4129 | 249 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33051 | 12899 | 14125 | 18744 | 2246 | 2026-10-10 22:28:57 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30201 | 7095 | 3966 | 5090 | 56 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28938 | 5210 | 5330 | 4543 | 743 | 2026-10-10 08:55:44 |
| [dash](https://github.com/plotly/dash) | 24445 | 2329 | 2166 | 1759 | 434 | 2026-10-09 21:04:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23351 | 8504 | 11434 | 20958 | 1495 | 2026-10-10 01:01:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 22394 | 1501 | 1437 | 7541 | 307 | 2026-10-11 03:57:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5569 | 1888 | 1877 | 221 | 2026-10-10 21:27:46 |
| [micropython](https://github.com/micropython/micropython) | 22110 | 8995 | 6139 | 8123 | 1533 | 2026-10-10 14:08:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18827 | 2868 | 3389 | 2224 | 728 | 2026-10-09 16:12:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1610 | 1470 | 1684 | 156 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16573 | 2447 | 3263 | 10391 | 223 | 2026-10-11 01:23:50 |
| [httpx](https://github.com/encode/httpx) | 15596 | 3609 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15104 | 6001 | 11681 | 14666 | 1859 | 2026-10-10 08:56:56 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14061 | 2146 | 2663 | 1234 | 244 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1976 | 5563 | 6750 | 1354 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12657 | 1369 | 787 | 2203 | 60 | 2026-10-09 14:25:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12214 | 1811 | 8337 | 1225 | 215 | 2026-10-09 16:52:33 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11912 | 616 | 426 | 338 | 168 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 1038 | 1146 | 1542 | 164 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9207 | 615 | 1050 | 559 | 226 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8793 | 1515 | 867 | 652 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7346 | 449 | 902 | 2629 | 332 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5632 | 523 | 1275 | 923 | 532 | 2026-10-07 04:44:53 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5421 | 1046 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4445 | 383 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 677 | 1357 | 281 | 2026-10-08 18:45:59 |
| [anyio](https://github.com/agronholm/anyio) | 2556 | 303 | 489 | 840 | 130 | 2026-10-11 00:06:20 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1811 | 129 | 5276 | 339 | 724 | 2026-10-10 21:43:18 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-10 15:23:03 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-11T05:29:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
