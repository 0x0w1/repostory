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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193700 | 75230 | 41154 | 66933 | 3431 | 2026-02-12 02:49:04 |
| [transformers](https://github.com/huggingface/transformers) | 156389 | 32040 | 18566 | 24761 | 2214 | 2026-02-11 21:36:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 97352 | 26835 | 56762 | 117568 | 18005 | 2026-02-12 02:54:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 95024 | 8677 | 3503 | 5277 | 159 | 2026-02-11 23:29:21 |
| [django](https://github.com/django/django) | 86742 | 33638 | 0 | 20613 | 397 | 2026-02-11 23:07:40 |
| [cpython](https://github.com/python/cpython) | 71462 | 34062 | 75229 | 68503 | 9202 | 2026-02-12 00:15:33 |
| [flask](https://github.com/pallets/flask) | 71148 | 16706 | 2715 | 2766 | 2 | 2026-02-06 21:23:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64995 | 26682 | 11932 | 20189 | 2131 | 2026-02-11 16:35:03 |
| [keras](https://github.com/keras-team/keras) | 63764 | 19693 | 12631 | 8734 | 285 | 2026-02-11 23:56:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 47856 | 19646 | 28090 | 35968 | 3641 | 2026-02-11 18:07:53 |
| [ray](https://github.com/ray-project/ray) | 41239 | 7210 | 22314 | 38334 | 3365 | 2026-02-12 02:36:25 |
| [gym](https://github.com/openai/gym) | 37033 | 8709 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33186 | 4639 | 5739 | 4079 | 188 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31424 | 12048 | 13790 | 16970 | 2318 | 2026-02-11 22:03:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29868 | 7066 | 3946 | 4921 | 88 | 2026-02-11 20:55:01 |
| [celery](https://github.com/celery/celery) | 28002 | 4945 | 5193 | 3792 | 768 | 2026-02-11 12:30:18 |
| [dash](https://github.com/plotly/dash) | 24466 | 2254 | 2054 | 1433 | 560 | 2026-02-11 16:33:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22443 | 5547 | 1863 | 1699 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22326 | 8184 | 11144 | 19944 | 1534 | 2026-02-11 00:33:19 |
| [RustPython](https://github.com/RustPython/RustPython) | 21778 | 1401 | 1297 | 5727 | 372 | 2026-02-11 15:30:19 |
| [micropython](https://github.com/micropython/micropython) | 21456 | 8699 | 5953 | 7553 | 1843 | 2026-02-11 00:35:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1585 | 1465 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18247 | 2774 | 3321 | 2027 | 774 | 2026-02-10 19:15:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16257 | 2189 | 3177 | 8569 | 287 | 2026-02-11 10:44:57 |
| [httpx](https://github.com/encode/httpx) | 14983 | 1031 | 925 | 1789 | 134 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14449 | 5614 | 11301 | 13248 | 1763 | 2026-02-12 00:17:31 |
| [dask](https://github.com/dask/dask) | 13737 | 1842 | 5504 | 6487 | 1225 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13721 | 2079 | 2646 | 1160 | 204 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11912 | 1116 | 763 | 1787 | 55 | 2026-02-11 13:25:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11639 | 601 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11500 | 1635 | 8152 | 1030 | 207 | 2026-02-09 14:28:51 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 979 | 1119 | 1413 | 163 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8899 | 557 | 1008 | 483 | 208 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8750 | 1493 | 860 | 628 | 282 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7162 | 384 | 878 | 2498 | 316 | 2026-02-10 22:42:45 |
| [hug](https://github.com/hugapi/hug) | 6906 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5494 | 460 | 1226 | 773 | 483 | 2026-02-11 22:19:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5183 | 999 | 902 | 289 | 192 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3954 | 310 | 1181 | 209 | 115 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3594 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 658 | 1271 | 312 | 2026-02-12 02:13:18 |
| [anyio](https://github.com/agronholm/anyio) | 2384 | 180 | 423 | 569 | 74 | 2026-02-09 18:37:13 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1935 | 367 | 1785 | 266 | 266 | 2026-02-09 18:28:59 |
| [pypy](https://github.com/pypy/pypy) | 1650 | 98 | 5176 | 179 | 758 | 2026-02-11 08:06:08 |
| [jython](https://github.com/jython/jython) | 1479 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-12T02:56:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
