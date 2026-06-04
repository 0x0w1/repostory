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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195396 | 75352 | 41512 | 75287 | 3173 | 2026-06-04 04:50:59 |
| [transformers](https://github.com/huggingface/transformers) | 161258 | 33402 | 19026 | 26660 | 2401 | 2026-06-04 04:50:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 100368 | 27928 | 59034 | 126537 | 18274 | 2026-06-04 04:51:24 |
| [fastapi](https://github.com/fastapi/fastapi) | 98868 | 9391 | 3529 | 5859 | 94 | 2026-06-04 00:21:04 |
| [django](https://github.com/django/django) | 87632 | 34006 | 0 | 21345 | 445 | 2026-06-03 20:58:44 |
| [cpython](https://github.com/python/cpython) | 72974 | 34696 | 76605 | 71964 | 9323 | 2026-06-04 00:21:16 |
| [flask](https://github.com/pallets/flask) | 71637 | 16847 | 2740 | 2833 | 3 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66238 | 27050 | 12123 | 20893 | 2034 | 2026-06-03 15:45:52 |
| [keras](https://github.com/keras-team/keras) | 64085 | 19750 | 12775 | 9402 | 174 | 2026-06-03 23:21:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 48898 | 19981 | 28301 | 37415 | 3226 | 2026-06-03 20:52:27 |
| [ray](https://github.com/ray-project/ray) | 42764 | 7629 | 22718 | 40740 | 3445 | 2026-06-04 04:46:40 |
| [gym](https://github.com/openai/gym) | 37207 | 8702 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33631 | 4687 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32145 | 12412 | 13930 | 17550 | 2370 | 2026-06-03 21:03:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30048 | 7068 | 3967 | 5008 | 77 | 2026-06-04 00:44:25 |
| [celery](https://github.com/celery/celery) | 28548 | 5065 | 5279 | 4128 | 781 | 2026-06-03 07:47:09 |
| [dash](https://github.com/plotly/dash) | 24231 | 2287 | 2103 | 1579 | 538 | 2026-06-04 03:26:41 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22859 | 8347 | 11300 | 20453 | 1477 | 2026-06-03 22:03:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5540 | 1872 | 1741 | 218 | 2026-06-02 20:08:23 |
| [RustPython](https://github.com/RustPython/RustPython) | 22092 | 1443 | 1351 | 6615 | 373 | 2026-06-04 02:18:48 |
| [micropython](https://github.com/micropython/micropython) | 21775 | 8848 | 6065 | 7843 | 1701 | 2026-06-03 12:53:49 |
| [sanic](https://github.com/sanic-org/sanic) | 18627 | 1590 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18575 | 2805 | 3349 | 2094 | 757 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16440 | 2290 | 3210 | 9261 | 238 | 2026-06-04 02:14:45 |
| [httpx](https://github.com/encode/httpx) | 15274 | 1163 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14727 | 5743 | 11459 | 13813 | 1788 | 2026-06-03 18:37:14 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13901 | 2117 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1880 | 5534 | 6597 | 1242 | 2026-06-03 14:48:00 |
| [starlette](https://github.com/Kludex/starlette) | 12359 | 1189 | 770 | 1932 | 58 | 2026-06-03 20:44:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11883 | 1694 | 8222 | 1100 | 212 | 2026-06-03 18:02:24 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11812 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 998 | 1126 | 1452 | 158 | 2026-06-01 11:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9080 | 594 | 1036 | 517 | 213 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1503 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7275 | 397 | 892 | 2549 | 319 | 2026-06-01 23:07:35 |
| [hug](https://github.com/hugapi/hug) | 6887 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5595 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5572 | 485 | 1257 | 844 | 514 | 2026-06-03 23:44:35 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5275 | 1016 | 914 | 300 | 212 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4173 | 336 | 1184 | 223 | 114 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4085 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3639 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2748 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2476 | 206 | 441 | 645 | 81 | 2026-06-03 21:40:29 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1531 | 359 | 2026-06-03 17:35:39 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-01 17:59:42 |
| [pypy](https://github.com/pypy/pypy) | 1743 | 113 | 5215 | 258 | 735 | 2026-06-04 03:34:18 |
| [jython](https://github.com/jython/jython) | 1512 | 230 | 297 | 135 | 110 | 2026-06-03 08:15:01 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 37 | 15 | 2026-06-02 10:34:29 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 447 | 113 | 77 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-04T04:54:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
