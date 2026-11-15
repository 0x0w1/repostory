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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201620 | 77975 | 41977 | 84767 | 3462 | 2026-11-15 05:45:14 |
| [transformers](https://github.com/huggingface/transformers) | 168996 | 35217 | 19877 | 30051 | 1141 | 2026-11-15 00:10:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 105515 | 30726 | 62621 | 141609 | 18244 | 2026-11-15 06:01:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 104737 | 10268 | 3555 | 6634 | 76 | 2026-11-15 05:16:34 |
| [django](https://github.com/django/django) | 91755 | 35219 | 0 | 22202 | 528 | 2026-11-13 17:06:51 |
| [cpython](https://github.com/python/cpython) | 78222 | 36603 | 79281 | 80334 | 9289 | 2026-11-15 04:43:44 |
| [flask](https://github.com/pallets/flask) | 75133 | 17341 | 2780 | 2911 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68183 | 27678 | 12382 | 21811 | 2171 | 2026-11-13 12:58:16 |
| [keras](https://github.com/keras-team/keras) | 64426 | 19817 | 13085 | 10265 | 234 | 2026-11-14 20:23:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 50523 | 20741 | 28692 | 40001 | 1848 | 2026-11-15 04:17:26 |
| [ray](https://github.com/ray-project/ray) | 44289 | 8285 | 23323 | 44365 | 3785 | 2026-11-15 02:15:23 |
| [gym](https://github.com/openai/gym) | 37239 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34053 | 4739 | 5784 | 4148 | 270 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33368 | 13098 | 14187 | 19042 | 2246 | 2026-11-15 05:12:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30236 | 7102 | 3966 | 5113 | 65 | 2026-11-12 10:27:24 |
| [celery](https://github.com/celery/celery) | 29202 | 5265 | 5392 | 4735 | 806 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24489 | 2347 | 2182 | 1835 | 437 | 2026-11-13 15:25:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23457 | 8546 | 11462 | 21069 | 1474 | 2026-11-14 18:26:52 |
| [RustPython](https://github.com/RustPython/RustPython) | 22484 | 1510 | 1463 | 8276 | 311 | 2026-11-15 01:13:24 |
| [micropython](https://github.com/micropython/micropython) | 22200 | 9062 | 6180 | 8257 | 1606 | 2026-11-12 12:22:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5607 | 1896 | 1930 | 223 | 2026-11-13 20:46:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18900 | 2896 | 3403 | 2283 | 755 | 2026-11-13 07:35:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18633 | 1618 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16607 | 2525 | 3277 | 10711 | 307 | 2026-11-14 22:26:46 |
| [httpx](https://github.com/encode/httpx) | 15792 | 1882 | 925 | 1801 | 136 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15216 | 6087 | 11769 | 14907 | 1912 | 2026-11-14 14:17:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14111 | 2162 | 2668 | 1256 | 255 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13950 | 2026 | 5583 | 6836 | 1433 | 2026-11-13 16:55:52 |
| [starlette](https://github.com/Kludex/starlette) | 12720 | 1446 | 798 | 2302 | 34 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12283 | 1855 | 8407 | 1263 | 221 | 2026-11-14 20:53:35 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11936 | 622 | 431 | 347 | 179 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9815 | 1056 | 1152 | 1579 | 161 | 2026-11-11 09:13:34 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9246 | 626 | 1057 | 617 | 159 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1513 | 866 | 657 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7363 | 474 | 911 | 2671 | 343 | 2026-11-13 19:20:22 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 546 | 1309 | 990 | 559 | 2026-11-12 09:12:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5578 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5452 | 1054 | 938 | 334 | 200 | 2026-11-14 15:09:10 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4477 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3984 | 281 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 321 | 682 | 1418 | 258 | 2026-11-15 02:58:14 |
| [anyio](https://github.com/agronholm/anyio) | 2570 | 351 | 503 | 894 | 153 | 2026-11-13 20:51:47 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2354 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 372 | 1791 | 284 | 280 | 2026-11-14 20:48:56 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 133 | 5302 | 431 | 721 | 2026-11-14 23:34:50 |
| [jython](https://github.com/jython/jython) | 1551 | 237 | 306 | 163 | 108 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-15T06:03:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
