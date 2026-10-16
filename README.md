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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200985 | 79521 | 41894 | 83657 | 3397 | 2026-10-16 04:10:58 |
| [transformers](https://github.com/huggingface/transformers) | 167741 | 34876 | 19636 | 29235 | 2324 | 2026-10-16 03:12:34 |
| [pytorch](https://github.com/pytorch/pytorch) | 104707 | 32596 | 61750 | 138704 | 17670 | 2026-10-16 04:13:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 103124 | 10044 | 3556 | 6440 | 81 | 2026-10-15 14:24:58 |
| [django](https://github.com/django/django) | 91334 | 37363 | 0 | 22075 | 541 | 2026-10-15 06:51:05 |
| [cpython](https://github.com/python/cpython) | 77573 | 38476 | 78713 | 78407 | 9798 | 2026-10-16 01:50:24 |
| [flask](https://github.com/pallets/flask) | 74910 | 17079 | 2767 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67629 | 27531 | 12326 | 21624 | 2155 | 2026-10-14 13:00:44 |
| [keras](https://github.com/keras-team/keras) | 64376 | 19799 | 13013 | 10085 | 233 | 2026-10-16 03:01:22 |
| [pandas](https://github.com/pandas-dev/pandas) | 50058 | 20521 | 28609 | 39485 | 2220 | 2026-10-15 22:55:36 |
| [ray](https://github.com/ray-project/ray) | 44037 | 8154 | 23194 | 43471 | 3600 | 2026-10-16 01:46:37 |
| [gym](https://github.com/openai/gym) | 37241 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33967 | 4736 | 5776 | 4130 | 251 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33021 | 12919 | 14131 | 18826 | 2242 | 2026-10-16 03:40:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30208 | 7095 | 3966 | 5093 | 57 | 2026-10-14 22:32:27 |
| [celery](https://github.com/celery/celery) | 28989 | 5220 | 5334 | 4569 | 718 | 2026-10-15 22:13:14 |
| [dash](https://github.com/plotly/dash) | 24454 | 2329 | 2167 | 1773 | 433 | 2026-10-15 19:38:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23374 | 8515 | 11438 | 20974 | 1490 | 2026-10-15 20:08:53 |
| [RustPython](https://github.com/RustPython/RustPython) | 22400 | 1502 | 1438 | 7619 | 290 | 2026-10-16 01:18:13 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5580 | 1888 | 1867 | 227 | 2026-10-15 19:43:23 |
| [micropython](https://github.com/micropython/micropython) | 22130 | 9006 | 6142 | 8135 | 1530 | 2026-10-16 03:43:25 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18843 | 2873 | 3391 | 2233 | 729 | 2026-10-15 23:05:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1610 | 1471 | 1686 | 158 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16574 | 2457 | 3262 | 10414 | 233 | 2026-10-15 11:21:43 |
| [httpx](https://github.com/encode/httpx) | 15602 | 4164 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15115 | 6014 | 11699 | 14690 | 1874 | 2026-10-15 16:49:39 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14075 | 2149 | 2667 | 1239 | 253 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13935 | 1984 | 5569 | 6761 | 1368 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12665 | 1377 | 787 | 2213 | 56 | 2026-10-13 07:53:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12245 | 1817 | 8342 | 1227 | 214 | 2026-10-15 19:14:44 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11911 | 615 | 426 | 339 | 169 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9808 | 1040 | 1147 | 1547 | 157 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9212 | 618 | 1050 | 563 | 225 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8796 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7346 | 452 | 903 | 2633 | 334 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5636 | 530 | 1283 | 945 | 552 | 2026-10-15 16:02:24 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5428 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4450 | 383 | 1207 | 254 | 120 | 2026-10-15 21:56:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 894 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3675 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1359 | 270 | 2026-10-13 23:26:13 |
| [anyio](https://github.com/agronholm/anyio) | 2557 | 314 | 489 | 852 | 133 | 2026-10-15 22:01:45 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1603 | 356 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1814 | 129 | 5281 | 353 | 712 | 2026-10-15 19:23:12 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-16T04:15:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
