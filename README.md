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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200263 | 77044 | 41794 | 82500 | 3328 | 2026-09-23 04:13:00 |
| [transformers](https://github.com/huggingface/transformers) | 166544 | 34657 | 19504 | 28738 | 2393 | 2026-09-22 20:09:34 |
| [pytorch](https://github.com/pytorch/pytorch) | 103185 | 30031 | 61172 | 136461 | 17565 | 2026-09-23 04:21:54 |
| [fastapi](https://github.com/fastapi/fastapi) | 102545 | 9938 | 3553 | 6356 | 86 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91162 | 35002 | 0 | 21888 | 509 | 2026-09-20 17:42:44 |
| [cpython](https://github.com/python/cpython) | 77241 | 36075 | 78230 | 77384 | 9707 | 2026-09-23 01:58:22 |
| [flask](https://github.com/pallets/flask) | 74771 | 16999 | 2767 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67351 | 27435 | 12293 | 21530 | 2155 | 2026-09-22 17:24:59 |
| [keras](https://github.com/keras-team/keras) | 64330 | 19805 | 12934 | 9918 | 235 | 2026-09-23 04:10:52 |
| [pandas](https://github.com/pandas-dev/pandas) | 49785 | 20416 | 28554 | 38878 | 2622 | 2026-09-23 02:08:41 |
| [ray](https://github.com/ray-project/ray) | 43902 | 8071 | 23093 | 42883 | 3595 | 2026-09-23 03:52:22 |
| [gym](https://github.com/openai/gym) | 37237 | 8674 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33916 | 4724 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32813 | 12835 | 14107 | 18557 | 2277 | 2026-09-22 21:58:00 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30190 | 7085 | 3966 | 5071 | 51 | 2026-09-23 03:44:54 |
| [celery](https://github.com/celery/celery) | 28912 | 5178 | 5305 | 4419 | 721 | 2026-09-23 03:18:40 |
| [dash](https://github.com/plotly/dash) | 24425 | 2321 | 2153 | 1724 | 433 | 2026-09-22 20:00:06 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23251 | 8491 | 11425 | 20888 | 1484 | 2026-09-23 00:54:33 |
| [RustPython](https://github.com/RustPython/RustPython) | 22352 | 1485 | 1428 | 7286 | 398 | 2026-09-23 03:52:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5558 | 1883 | 1835 | 259 | 2026-09-22 14:09:48 |
| [micropython](https://github.com/micropython/micropython) | 22084 | 8977 | 6132 | 8099 | 1525 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18798 | 2849 | 3386 | 2192 | 714 | 2026-09-22 21:25:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1602 | 1468 | 1678 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16556 | 2426 | 3256 | 10176 | 231 | 2026-09-22 11:28:04 |
| [httpx](https://github.com/encode/httpx) | 15504 | 1777 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15036 | 5963 | 11655 | 14553 | 1846 | 2026-09-23 01:00:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14035 | 2138 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13923 | 1963 | 5559 | 6729 | 1338 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12626 | 1324 | 783 | 2133 | 55 | 2026-09-20 10:07:50 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12174 | 1795 | 8302 | 1213 | 211 | 2026-09-21 17:07:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11901 | 616 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1036 | 1144 | 1527 | 158 | 2026-09-22 20:20:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9194 | 612 | 1046 | 550 | 222 | 2026-09-19 05:35:44 |
| [bottle](https://github.com/bottlepy/bottle) | 8790 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7334 | 433 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 516 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5406 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4409 | 376 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4101 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 269 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 312 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2547 | 274 | 477 | 784 | 116 | 2026-09-21 18:00:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1797 | 125 | 5262 | 304 | 715 | 2026-09-22 20:01:11 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-23T04:30:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
