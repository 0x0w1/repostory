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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200660 | 77992 | 41826 | 82983 | 3238 | 2026-10-02 05:11:37 |
| [transformers](https://github.com/huggingface/transformers) | 166899 | 34741 | 19544 | 28912 | 2354 | 2026-10-02 05:06:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 103608 | 31035 | 61427 | 137322 | 17606 | 2026-10-02 05:19:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 102758 | 9980 | 3555 | 6400 | 97 | 2026-10-02 05:06:35 |
| [django](https://github.com/django/django) | 91240 | 35921 | 0 | 21979 | 524 | 2026-10-01 14:36:14 |
| [cpython](https://github.com/python/cpython) | 77384 | 37051 | 78377 | 77848 | 9735 | 2026-10-02 05:05:24 |
| [flask](https://github.com/pallets/flask) | 74806 | 17031 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67447 | 27472 | 12305 | 21557 | 2160 | 2026-10-01 14:58:08 |
| [keras](https://github.com/keras-team/keras) | 64344 | 19806 | 12970 | 9973 | 250 | 2026-10-02 05:19:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 49892 | 20453 | 28578 | 39111 | 2491 | 2026-10-01 21:43:34 |
| [ray](https://github.com/ray-project/ray) | 43963 | 8108 | 23115 | 43118 | 3536 | 2026-10-02 04:41:10 |
| [gym](https://github.com/openai/gym) | 37238 | 8671 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33934 | 4733 | 5774 | 4128 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 32897 | 12865 | 14118 | 18635 | 2246 | 2026-10-02 02:50:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30197 | 7086 | 3966 | 5076 | 50 | 2026-09-30 06:38:50 |
| [celery](https://github.com/celery/celery) | 28927 | 5194 | 5315 | 4479 | 728 | 2026-10-01 22:14:03 |
| [dash](https://github.com/plotly/dash) | 24441 | 2329 | 2160 | 1742 | 425 | 2026-10-01 09:54:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23314 | 8497 | 11431 | 20923 | 1494 | 2026-10-01 20:14:05 |
| [RustPython](https://github.com/RustPython/RustPython) | 22374 | 1492 | 1434 | 7430 | 406 | 2026-10-02 04:05:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22171 | 5562 | 1884 | 1845 | 247 | 2026-10-02 01:36:23 |
| [micropython](https://github.com/micropython/micropython) | 22105 | 8983 | 6133 | 8115 | 1529 | 2026-09-30 06:13:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18818 | 2858 | 3387 | 2208 | 728 | 2026-10-01 07:39:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1605 | 1469 | 1681 | 153 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16566 | 2436 | 3260 | 10287 | 244 | 2026-10-01 10:51:14 |
| [httpx](https://github.com/encode/httpx) | 15524 | 2664 | 925 | 1806 | 140 | 2026-10-01 21:43:48 |
| [scipy](https://github.com/scipy/scipy) | 15068 | 5981 | 11673 | 14623 | 1853 | 2026-10-01 12:12:21 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14053 | 2144 | 2663 | 1227 | 239 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13927 | 1970 | 5562 | 6738 | 1348 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12645 | 1352 | 784 | 2167 | 64 | 2026-10-01 19:45:03 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12195 | 1799 | 8317 | 1216 | 208 | 2026-10-02 04:22:59 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11909 | 616 | 422 | 335 | 163 | 2026-10-01 15:38:19 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1038 | 1145 | 1532 | 156 | 2026-09-30 18:05:10 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9204 | 614 | 1047 | 556 | 224 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8791 | 1512 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7342 | 438 | 902 | 2620 | 329 | 2026-10-01 07:30:18 |
| [hug](https://github.com/hugapi/hug) | 6880 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 520 | 1270 | 908 | 521 | 2026-10-01 05:56:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5414 | 1045 | 934 | 325 | 202 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4425 | 383 | 1202 | 252 | 118 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 272 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3674 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2767 | 316 | 675 | 1342 | 308 | 2026-10-01 11:14:34 |
| [anyio](https://github.com/agronholm/anyio) | 2550 | 294 | 484 | 812 | 133 | 2026-09-29 18:41:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1600 | 356 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1786 | 276 | 273 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1805 | 127 | 5268 | 318 | 716 | 2026-10-01 20:08:41 |
| [jython](https://github.com/jython/jython) | 1545 | 231 | 303 | 154 | 102 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-10-02T05:20:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
