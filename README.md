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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196942 | 75975 | 41674 | 79708 | 2885 | 2026-08-10 02:07:16 |
| [transformers](https://github.com/huggingface/transformers) | 163507 | 34161 | 19283 | 27835 | 2366 | 2026-08-09 23:36:51 |
| [pytorch](https://github.com/pytorch/pytorch) | 102302 | 28790 | 60248 | 131796 | 16996 | 2026-08-10 02:23:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 101442 | 9759 | 3544 | 6217 | 74 | 2026-08-09 08:12:45 |
| [django](https://github.com/django/django) | 88400 | 34128 | 0 | 21639 | 457 | 2026-08-07 15:01:48 |
| [cpython](https://github.com/python/cpython) | 74255 | 35177 | 77595 | 75509 | 9556 | 2026-08-09 21:27:58 |
| [flask](https://github.com/pallets/flask) | 72181 | 16936 | 2763 | 2887 | 8 | 2026-07-30 17:29:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66956 | 27269 | 12231 | 21263 | 2116 | 2026-08-07 16:08:16 |
| [keras](https://github.com/keras-team/keras) | 64223 | 19749 | 12865 | 9680 | 212 | 2026-08-07 23:06:58 |
| [pandas](https://github.com/pandas-dev/pandas) | 49502 | 20248 | 28463 | 38117 | 2846 | 2026-08-10 02:13:56 |
| [ray](https://github.com/ray-project/ray) | 43479 | 7906 | 22912 | 41998 | 3463 | 2026-08-09 19:01:13 |
| [gym](https://github.com/openai/gym) | 37246 | 8684 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33814 | 4706 | 5768 | 4107 | 228 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32528 | 12624 | 14040 | 18105 | 2330 | 2026-08-09 22:36:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30126 | 7074 | 3966 | 5042 | 59 | 2026-08-07 14:52:28 |
| [celery](https://github.com/celery/celery) | 28778 | 5124 | 5291 | 4225 | 801 | 2026-08-09 15:24:47 |
| [dash](https://github.com/plotly/dash) | 24372 | 2314 | 2141 | 1676 | 539 | 2026-08-07 14:56:36 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23069 | 8431 | 11391 | 20732 | 1467 | 2026-08-09 05:28:23 |
| [RustPython](https://github.com/RustPython/RustPython) | 22260 | 1472 | 1414 | 6988 | 402 | 2026-08-09 15:50:46 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5552 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21982 | 8926 | 6115 | 8023 | 1566 | 2026-08-07 05:32:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18724 | 2834 | 3375 | 2129 | 767 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1595 | 1471 | 1700 | 143 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16514 | 2370 | 3233 | 9774 | 230 | 2026-08-10 01:51:38 |
| [httpx](https://github.com/encode/httpx) | 15402 | 1241 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14897 | 5853 | 11582 | 14264 | 1853 | 2026-08-10 01:25:42 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13989 | 2132 | 2658 | 1210 | 226 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13885 | 1924 | 5548 | 6686 | 1296 | 2026-08-03 22:03:26 |
| [starlette](https://github.com/Kludex/starlette) | 12534 | 1256 | 773 | 2021 | 61 | 2026-08-09 10:40:14 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12058 | 1741 | 8259 | 1172 | 216 | 2026-08-07 19:23:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11882 | 612 | 417 | 326 | 154 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1025 | 1139 | 1498 | 159 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 605 | 1042 | 527 | 225 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8776 | 1500 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 413 | 898 | 2586 | 323 | 2026-08-03 02:34:09 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5610 | 499 | 1265 | 884 | 540 | 2026-08-08 06:00:40 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5342 | 1032 | 927 | 316 | 202 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4304 | 359 | 1194 | 239 | 127 | 2026-08-08 16:45:58 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3998 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3655 | 202 | 284 | 133 | 37 | 2026-08-09 20:23:31 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2521 | 237 | 466 | 725 | 104 | 2026-08-06 22:30:16 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1582 | 356 | 2026-08-06 18:09:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-03 17:54:08 |
| [pypy](https://github.com/pypy/pypy) | 1778 | 121 | 5247 | 287 | 730 | 2026-08-08 03:22:03 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 299 | 148 | 97 | 2026-08-09 15:52:59 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-02 09:46:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-10T02:23:51*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
