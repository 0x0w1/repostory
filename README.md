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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194322 | 75249 | 41278 | 69768 | 3949 | 2026-03-25 02:46:15 |
| [transformers](https://github.com/huggingface/transformers) | 158353 | 32597 | 18768 | 25584 | 2289 | 2026-03-24 22:03:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 98545 | 27292 | 57475 | 120365 | 18130 | 2026-03-25 02:47:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 96531 | 8928 | 3514 | 5508 | 163 | 2026-03-24 16:39:59 |
| [django](https://github.com/django/django) | 87114 | 33782 | 0 | 20918 | 427 | 2026-03-24 21:54:02 |
| [cpython](https://github.com/python/cpython) | 72091 | 34302 | 75702 | 69682 | 9320 | 2026-03-25 01:42:19 |
| [flask](https://github.com/pallets/flask) | 71378 | 16757 | 2725 | 2793 | 3 | 2026-03-24 13:55:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65504 | 26840 | 12015 | 20452 | 2159 | 2026-03-24 10:57:09 |
| [keras](https://github.com/keras-team/keras) | 63923 | 19737 | 12683 | 9008 | 264 | 2026-03-24 21:32:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 48238 | 19779 | 28201 | 36562 | 3612 | 2026-03-25 00:30:29 |
| [ray](https://github.com/ray-project/ray) | 41841 | 7379 | 22487 | 39194 | 3512 | 2026-03-25 02:47:31 |
| [gym](https://github.com/openai/gym) | 37114 | 8707 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33379 | 4661 | 5747 | 4085 | 191 | 2026-03-23 17:48:01 |
| [numpy](https://github.com/numpy/numpy) | 31650 | 12197 | 13846 | 17155 | 2333 | 2026-03-24 20:12:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29941 | 7077 | 3947 | 4951 | 78 | 2026-03-24 16:57:27 |
| [celery](https://github.com/celery/celery) | 28280 | 4997 | 5209 | 3873 | 772 | 2026-03-20 22:13:14 |
| [dash](https://github.com/plotly/dash) | 24485 | 2269 | 2080 | 1489 | 590 | 2026-03-24 18:53:33 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22625 | 8282 | 11213 | 20113 | 1550 | 2026-03-25 01:30:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5547 | 1865 | 1722 | 211 | 2026-03-23 17:29:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 21911 | 1413 | 1317 | 6112 | 369 | 2026-03-24 08:51:13 |
| [micropython](https://github.com/micropython/micropython) | 21574 | 8755 | 5995 | 7656 | 1843 | 2026-03-23 19:19:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1587 | 1465 | 1674 | 125 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18382 | 2789 | 3330 | 2059 | 771 | 2026-03-24 17:23:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16377 | 2228 | 3182 | 8769 | 279 | 2026-03-24 19:39:28 |
| [httpx](https://github.com/encode/httpx) | 15144 | 1086 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14557 | 5669 | 11384 | 13494 | 1778 | 2026-03-24 17:52:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13781 | 2092 | 2649 | 1168 | 211 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13773 | 1858 | 5518 | 6510 | 1232 | 2026-03-24 00:04:43 |
| [starlette](https://github.com/Kludex/starlette) | 12115 | 1144 | 766 | 1840 | 46 | 2026-03-22 18:27:00 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11721 | 606 | 410 | 319 | 161 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11700 | 1656 | 8174 | 1050 | 209 | 2026-03-24 19:50:39 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 982 | 1119 | 1422 | 164 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8968 | 564 | 1024 | 497 | 217 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 863 | 632 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7218 | 393 | 882 | 2517 | 315 | 2026-03-23 22:25:09 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5606 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5530 | 470 | 1243 | 805 | 498 | 2026-03-21 22:19:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5214 | 1002 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4079 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4029 | 323 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4017 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3614 | 194 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2737 | 313 | 664 | 1304 | 309 | 2026-03-22 03:20:34 |
| [anyio](https://github.com/agronholm/anyio) | 2417 | 189 | 431 | 593 | 82 | 2026-03-25 01:30:25 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 904 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-23 17:46:41 |
| [pypy](https://github.com/pypy/pypy) | 1690 | 107 | 5187 | 191 | 766 | 2026-03-24 21:34:59 |
| [jython](https://github.com/jython/jython) | 1494 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-25T02:53:35*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
