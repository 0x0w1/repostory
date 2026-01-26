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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193490 | 75203 | 41117 | 65580 | 2745 | 2026-01-25 21:53:24 |
| [transformers](https://github.com/huggingface/transformers) | 155702 | 31854 | 18462 | 24414 | 2193 | 2026-01-25 23:15:16 |
| [pytorch](https://github.com/pytorch/pytorch) | 96908 | 26631 | 56466 | 116354 | 17913 | 2026-01-26 02:22:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 94457 | 8581 | 3500 | 5173 | 212 | 2026-01-24 21:29:42 |
| [django](https://github.com/django/django) | 86564 | 33551 | 0 | 20522 | 398 | 2026-01-25 10:51:02 |
| [cpython](https://github.com/python/cpython) | 71221 | 33964 | 75098 | 68134 | 9229 | 2026-01-26 01:28:59 |
| [flask](https://github.com/pallets/flask) | 71091 | 16681 | 2711 | 2758 | 3 | 2026-01-25 18:38:47 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64778 | 26627 | 11899 | 20091 | 2124 | 2026-01-24 22:29:32 |
| [keras](https://github.com/keras-team/keras) | 63744 | 19675 | 12618 | 8645 | 252 | 2026-01-24 01:17:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 47695 | 19574 | 28049 | 35763 | 3636 | 2026-01-24 18:14:04 |
| [ray](https://github.com/ray-project/ray) | 40975 | 7157 | 22221 | 37913 | 3306 | 2026-01-26 01:48:03 |
| [gym](https://github.com/openai/gym) | 36976 | 8714 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33108 | 4635 | 5737 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31321 | 11989 | 13758 | 16903 | 2289 | 2026-01-26 02:16:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29824 | 7059 | 3946 | 4909 | 87 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27910 | 4932 | 5184 | 3772 | 758 | 2026-01-25 17:25:47 |
| [dash](https://github.com/plotly/dash) | 24415 | 2251 | 2048 | 1423 | 560 | 2026-01-24 14:42:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22433 | 5542 | 1862 | 1696 | 210 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22273 | 8174 | 11116 | 19872 | 1529 | 2026-01-25 22:25:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 21729 | 1398 | 1294 | 5513 | 373 | 2026-01-26 01:39:08 |
| [micropython](https://github.com/micropython/micropython) | 21378 | 8671 | 5939 | 7502 | 1845 | 2026-01-23 23:25:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1583 | 1463 | 1662 | 113 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18214 | 2775 | 3317 | 2005 | 767 | 2026-01-14 21:23:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16227 | 2183 | 3174 | 8515 | 275 | 2026-01-25 20:48:33 |
| [httpx](https://github.com/encode/httpx) | 14942 | 1016 | 925 | 1779 | 126 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14396 | 5597 | 11267 | 13149 | 1757 | 2026-01-25 18:48:07 |
| [dask](https://github.com/dask/dask) | 13728 | 1837 | 5497 | 6455 | 1215 | 2026-01-24 20:45:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13695 | 2083 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11867 | 1097 | 763 | 1775 | 48 | 2026-01-25 20:51:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11611 | 601 | 403 | 309 | 152 | 2026-01-19 17:03:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11424 | 1630 | 8143 | 1024 | 206 | 2026-01-24 19:22:06 |
| [falcon](https://github.com/falconry/falcon) | 9780 | 976 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8864 | 556 | 998 | 482 | 199 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8734 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7111 | 379 | 878 | 2490 | 314 | 2026-01-20 02:39:49 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5618 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5457 | 447 | 1221 | 737 | 513 | 2026-01-25 09:55:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5167 | 995 | 891 | 284 | 185 | 2026-01-22 06:45:33 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3912 | 307 | 1177 | 207 | 119 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3580 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2722 | 307 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2369 | 179 | 423 | 564 | 75 | 2026-01-24 16:46:44 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 367 | 1785 | 266 | 266 | 2026-01-19 17:53:24 |
| [pypy](https://github.com/pypy/pypy) | 1636 | 96 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1474 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-26T02:34:15*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
