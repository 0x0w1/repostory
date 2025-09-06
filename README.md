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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191500 | 74814 | 40770 | 57046 | 1569 | 2025-09-06 01:48:22 |
| [transformers](https://github.com/huggingface/transformers) | 149228 | 30279 | 17888 | 22272 | 1993 | 2025-09-05 16:05:48 |
| [pytorch](https://github.com/pytorch/pytorch) | 92962 | 25176 | 53549 | 108318 | 17054 | 2025-09-06 01:31:59 |
| [fastapi](https://github.com/fastapi/fastapi) | 89176 | 7831 | 3466 | 4693 | 235 | 2025-09-05 12:49:23 |
| [django](https://github.com/django/django) | 84900 | 32898 | 0 | 19762 | 365 | 2025-09-05 19:56:16 |
| [flask](https://github.com/pallets/flask) | 70298 | 16518 | 2694 | 2693 | 5 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68711 | 32767 | 73497 | 64160 | 9348 | 2025-09-05 22:48:16 |
| [keras](https://github.com/keras-team/keras) | 63392 | 19619 | 12535 | 8315 | 286 | 2025-09-04 15:11:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63252 | 26199 | 11683 | 19302 | 2180 | 2025-09-05 09:55:25 |
| [pandas](https://github.com/pandas-dev/pandas) | 46491 | 18878 | 27695 | 34524 | 3704 | 2025-09-06 00:43:16 |
| [ray](https://github.com/ray-project/ray) | 38807 | 6766 | 21052 | 34899 | 3049 | 2025-09-06 01:21:36 |
| [gym](https://github.com/openai/gym) | 36460 | 8690 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32423 | 4577 | 5719 | 4069 | 202 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30336 | 11306 | 13520 | 16111 | 2358 | 2025-09-05 20:56:45 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29441 | 7000 | 3945 | 4830 | 100 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27150 | 4839 | 5158 | 3650 | 750 | 2025-08-31 09:27:30 |
| [dash](https://github.com/plotly/dash) | 24008 | 2196 | 1985 | 1326 | 558 | 2025-09-05 21:22:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22138 | 5537 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21661 | 7988 | 10963 | 19516 | 1637 | 2025-09-05 09:57:18 |
| [micropython](https://github.com/micropython/micropython) | 20794 | 8408 | 5805 | 7162 | 1788 | 2025-09-04 19:06:37 |
| [RustPython](https://github.com/RustPython/RustPython) | 20467 | 1341 | 1213 | 4855 | 444 | 2025-09-04 06:34:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18491 | 1582 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17697 | 2705 | 3250 | 1947 | 723 | 2025-08-29 20:22:39 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15971 | 2121 | 3144 | 8038 | 269 | 2025-09-05 11:03:09 |
| [httpx](https://github.com/encode/httpx) | 14528 | 950 | 916 | 1721 | 103 | 2025-09-05 15:15:17 |
| [scipy](https://github.com/scipy/scipy) | 13981 | 5467 | 11005 | 12541 | 1762 | 2025-09-05 09:09:25 |
| [dask](https://github.com/dask/dask) | 13463 | 1795 | 5431 | 6338 | 1197 | 2025-09-02 21:26:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13411 | 2029 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11430 | 1033 | 751 | 1689 | 51 | 2025-09-02 14:26:53 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11238 | 570 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10853 | 1578 | 8076 | 979 | 228 | 2025-09-05 17:23:04 |
| [falcon](https://github.com/falconry/falcon) | 9711 | 958 | 1096 | 1364 | 156 | 2025-08-31 19:21:18 |
| [bottle](https://github.com/bottlepy/bottle) | 8657 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8509 | 520 | 939 | 434 | 408 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6893 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6821 | 367 | 866 | 2447 | 312 | 2025-09-03 04:38:37 |
| [eve](https://github.com/pyeve/eve) | 6730 | 747 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5633 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5272 | 436 | 1189 | 713 | 498 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4972 | 933 | 867 | 258 | 162 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4045 | 891 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3577 | 289 | 1156 | 195 | 116 | 2025-08-28 16:27:29 |
| [quart](https://github.com/pallets/quart) | 3438 | 187 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2684 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2306 | 131 | 426 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2196 | 164 | 400 | 503 | 70 | 2025-09-05 23:08:15 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 908 | 1077 | 1458 | 369 | 2025-09-01 17:32:42 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1923 | 369 | 1780 | 264 | 261 | 2025-09-01 17:37:10 |
| [pypy](https://github.com/pypy/pypy) | 1493 | 85 | 5143 | 168 | 736 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1432 | 219 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-06T01:52:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
