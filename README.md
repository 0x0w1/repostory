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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194944 | 75300 | 41345 | 72570 | 4808 | 2026-05-01 04:02:27 |
| [transformers](https://github.com/huggingface/transformers) | 160133 | 33066 | 18911 | 26167 | 2343 | 2026-05-01 04:01:16 |
| [pytorch](https://github.com/pytorch/pytorch) | 99563 | 27630 | 58357 | 123198 | 18519 | 2026-05-01 03:53:30 |
| [fastapi](https://github.com/fastapi/fastapi) | 97798 | 9177 | 3524 | 5686 | 180 | 2026-04-30 20:20:52 |
| [django](https://github.com/django/django) | 87366 | 33868 | 0 | 21134 | 429 | 2026-04-30 23:52:11 |
| [cpython](https://github.com/python/cpython) | 72535 | 34525 | 76183 | 70723 | 9397 | 2026-04-30 22:13:52 |
| [flask](https://github.com/pallets/flask) | 71484 | 16829 | 2736 | 2813 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65954 | 26984 | 12064 | 20680 | 2062 | 2026-04-30 10:27:49 |
| [keras](https://github.com/keras-team/keras) | 64051 | 19762 | 12742 | 9264 | 242 | 2026-04-30 22:50:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 48633 | 19889 | 28263 | 37093 | 3393 | 2026-04-30 20:19:48 |
| [ray](https://github.com/ray-project/ray) | 42384 | 7519 | 22631 | 40077 | 3550 | 2026-05-01 03:36:38 |
| [gym](https://github.com/openai/gym) | 37177 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33533 | 4678 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31937 | 12326 | 13900 | 17394 | 2366 | 2026-04-30 21:18:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29984 | 7067 | 3967 | 5002 | 78 | 2026-04-28 07:27:54 |
| [celery](https://github.com/celery/celery) | 28421 | 5027 | 5272 | 4097 | 775 | 2026-04-29 14:03:56 |
| [dash](https://github.com/plotly/dash) | 24168 | 2276 | 2092 | 1547 | 542 | 2026-05-01 01:11:51 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22757 | 8326 | 11257 | 20279 | 1502 | 2026-04-30 21:58:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22218 | 5542 | 1871 | 1728 | 218 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22031 | 1433 | 1339 | 6336 | 380 | 2026-04-30 15:30:17 |
| [micropython](https://github.com/micropython/micropython) | 21666 | 8812 | 6042 | 7761 | 1873 | 2026-05-01 04:04:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18492 | 2804 | 3342 | 2080 | 765 | 2026-04-30 21:36:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16427 | 2260 | 3191 | 8916 | 281 | 2026-04-30 13:37:11 |
| [httpx](https://github.com/encode/httpx) | 15249 | 1135 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14651 | 5717 | 11427 | 13633 | 1786 | 2026-04-30 23:28:00 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13835 | 2104 | 2653 | 1175 | 218 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13814 | 1867 | 5522 | 6535 | 1246 | 2026-04-28 16:39:15 |
| [starlette](https://github.com/Kludex/starlette) | 12265 | 1166 | 766 | 1884 | 57 | 2026-04-30 17:24:20 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11814 | 1673 | 8202 | 1070 | 216 | 2026-04-30 20:06:13 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11778 | 605 | 413 | 323 | 162 | 2026-04-28 20:38:57 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 996 | 1125 | 1443 | 157 | 2026-04-26 06:35:15 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9035 | 573 | 1033 | 510 | 207 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8759 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7252 | 393 | 891 | 2539 | 321 | 2026-05-01 03:43:47 |
| [hug](https://github.com/hugapi/hug) | 6893 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5562 | 480 | 1249 | 824 | 506 | 2026-04-30 15:33:58 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5249 | 1008 | 912 | 291 | 202 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4104 | 330 | 1183 | 218 | 113 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4006 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3627 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2452 | 201 | 436 | 620 | 84 | 2026-04-30 10:39:40 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 907 | 1084 | 1487 | 360 | 2026-04-29 16:54:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-27 17:52:32 |
| [pypy](https://github.com/pypy/pypy) | 1717 | 112 | 5203 | 235 | 736 | 2026-04-30 21:14:06 |
| [jython](https://github.com/jython/jython) | 1506 | 229 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-04-26 08:05:46 |

*Last Automatic Update: 2026-05-01T04:05:02*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
