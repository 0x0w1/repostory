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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192510 | 74995 | 41014 | 61810 | 2493 | 2025-11-22 01:48:07 |
| [transformers](https://github.com/huggingface/transformers) | 152841 | 31198 | 18213 | 23519 | 2116 | 2025-11-21 17:51:10 |
| [pytorch](https://github.com/pytorch/pytorch) | 95270 | 25971 | 55494 | 112901 | 17640 | 2025-11-22 01:57:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 92142 | 8248 | 3477 | 4891 | 220 | 2025-11-21 13:03:23 |
| [django](https://github.com/django/django) | 85867 | 33249 | 0 | 20226 | 355 | 2025-11-21 22:15:39 |
| [flask](https://github.com/pallets/flask) | 70805 | 16628 | 2703 | 2723 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69952 | 33467 | 74419 | 66446 | 9208 | 2025-11-21 21:36:30 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64094 | 26457 | 11820 | 19807 | 2116 | 2025-11-21 10:47:09 |
| [keras](https://github.com/keras-team/keras) | 63582 | 19653 | 12594 | 8479 | 271 | 2025-11-21 02:04:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 47160 | 19320 | 27897 | 35218 | 3634 | 2025-11-20 19:48:59 |
| [ray](https://github.com/ray-project/ray) | 39950 | 6930 | 21901 | 36658 | 3229 | 2025-11-22 01:00:40 |
| [gym](https://github.com/openai/gym) | 36795 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32846 | 4629 | 5732 | 4073 | 193 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30874 | 11722 | 13664 | 16552 | 2363 | 2025-11-21 18:35:24 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29677 | 7037 | 3946 | 4871 | 91 | 2025-11-21 12:29:35 |
| [celery](https://github.com/celery/celery) | 27604 | 4900 | 5176 | 3728 | 754 | 2025-11-21 10:59:04 |
| [dash](https://github.com/plotly/dash) | 24268 | 2234 | 2026 | 1378 | 582 | 2025-11-21 18:12:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22356 | 5543 | 1854 | 1676 | 204 | 2025-11-21 18:59:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22029 | 8124 | 11052 | 19680 | 1627 | 2025-11-21 15:59:36 |
| [micropython](https://github.com/micropython/micropython) | 21114 | 8536 | 5877 | 7373 | 1799 | 2025-11-21 13:37:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 20823 | 1357 | 1236 | 4988 | 450 | 2025-11-18 16:00:41 |
| [sanic](https://github.com/sanic-org/sanic) | 18572 | 1584 | 1453 | 1630 | 151 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18004 | 2749 | 3294 | 1984 | 747 | 2025-11-19 19:31:04 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16101 | 2157 | 3163 | 8308 | 288 | 2025-11-21 18:01:14 |
| [httpx](https://github.com/encode/httpx) | 14760 | 980 | 921 | 1756 | 112 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14203 | 5543 | 11150 | 12871 | 1786 | 2025-11-21 22:34:14 |
| [dask](https://github.com/dask/dask) | 13608 | 1825 | 5466 | 6406 | 1195 | 2025-11-21 17:21:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13573 | 2049 | 2634 | 1149 | 194 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11678 | 1081 | 760 | 1744 | 52 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11436 | 585 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11156 | 1600 | 8120 | 1003 | 208 | 2025-11-21 21:17:16 |
| [falcon](https://github.com/falconry/falcon) | 9760 | 972 | 1111 | 1402 | 162 | 2025-11-16 10:15:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8723 | 538 | 970 | 454 | 176 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8696 | 1487 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7007 | 371 | 873 | 2470 | 313 | 2025-11-17 21:56:02 |
| [hug](https://github.com/hugapi/hug) | 6903 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 745 | 979 | 576 | 32 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5626 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5386 | 445 | 1200 | 716 | 507 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5092 | 969 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4063 | 887 | 1062 | 2722 | 90 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3772 | 301 | 1168 | 201 | 115 | 2025-11-20 22:26:20 |
| [quart](https://github.com/pallets/quart) | 3546 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2709 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2300 | 176 | 415 | 548 | 74 | 2025-11-20 02:00:13 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 912 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1928 | 372 | 1784 | 266 | 265 | 2025-11-20 00:37:23 |
| [pypy](https://github.com/pypy/pypy) | 1573 | 89 | 5164 | 172 | 750 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1459 | 225 | 286 | 114 | 104 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-18 10:59:56 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-22T01:59:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
