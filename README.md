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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193506 | 75200 | 41117 | 65639 | 2760 | 2026-01-27 02:03:44 |
| [transformers](https://github.com/huggingface/transformers) | 155770 | 31869 | 18468 | 24440 | 2179 | 2026-01-26 20:50:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 96953 | 26646 | 56499 | 116462 | 17940 | 2026-01-27 02:29:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 94496 | 8585 | 3500 | 5176 | 210 | 2026-01-26 17:17:36 |
| [django](https://github.com/django/django) | 86575 | 33559 | 0 | 20527 | 397 | 2026-01-26 15:45:40 |
| [cpython](https://github.com/python/cpython) | 71233 | 33959 | 75105 | 68139 | 9220 | 2026-01-26 21:15:21 |
| [flask](https://github.com/pallets/flask) | 71099 | 16683 | 2712 | 2758 | 2 | 2026-01-25 18:38:47 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64795 | 26629 | 11901 | 20098 | 2125 | 2026-01-26 13:27:28 |
| [keras](https://github.com/keras-team/keras) | 63747 | 19676 | 12620 | 8647 | 250 | 2026-01-26 23:33:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 47702 | 19582 | 28051 | 35777 | 3643 | 2026-01-27 00:58:50 |
| [ray](https://github.com/ray-project/ray) | 40989 | 7160 | 22230 | 37939 | 3321 | 2026-01-27 02:26:22 |
| [gym](https://github.com/openai/gym) | 36979 | 8714 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33117 | 4637 | 5737 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31334 | 11996 | 13760 | 16906 | 2289 | 2026-01-26 20:50:15 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29830 | 7058 | 3946 | 4909 | 87 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27919 | 4932 | 5184 | 3772 | 758 | 2026-01-25 17:25:47 |
| [dash](https://github.com/plotly/dash) | 24421 | 2252 | 2048 | 1423 | 559 | 2026-01-26 19:56:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22434 | 5542 | 1862 | 1696 | 210 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22277 | 8175 | 11116 | 19877 | 1524 | 2026-01-27 00:47:23 |
| [RustPython](https://github.com/RustPython/RustPython) | 21730 | 1399 | 1294 | 5524 | 376 | 2026-01-27 01:57:35 |
| [micropython](https://github.com/micropython/micropython) | 21384 | 8670 | 5939 | 7502 | 1840 | 2026-01-27 02:21:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1583 | 1464 | 1662 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18218 | 2775 | 3318 | 2007 | 769 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16230 | 2183 | 3174 | 8524 | 275 | 2026-01-26 19:44:11 |
| [httpx](https://github.com/encode/httpx) | 14945 | 1018 | 925 | 1780 | 127 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14401 | 5598 | 11269 | 13156 | 1755 | 2026-01-26 21:39:51 |
| [dask](https://github.com/dask/dask) | 13728 | 1836 | 5497 | 6458 | 1216 | 2026-01-26 23:17:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13697 | 2083 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11866 | 1097 | 763 | 1776 | 49 | 2026-01-26 23:59:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11613 | 601 | 403 | 309 | 152 | 2026-01-19 17:03:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11426 | 1630 | 8144 | 1025 | 208 | 2026-01-24 19:22:06 |
| [falcon](https://github.com/falconry/falcon) | 9780 | 976 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8865 | 556 | 998 | 482 | 199 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8735 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7112 | 379 | 878 | 2491 | 315 | 2026-01-26 21:48:23 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5618 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5458 | 447 | 1221 | 737 | 513 | 2026-01-26 20:57:33 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5167 | 995 | 893 | 285 | 187 | 2026-01-22 06:45:33 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3916 | 306 | 1177 | 206 | 119 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3581 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2370 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1637 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1474 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-27T02:29:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
