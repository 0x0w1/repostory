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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191298 | 74792 | 40743 | 56527 | 1482 | 2025-08-23 23:52:48 |
| [transformers](https://github.com/huggingface/transformers) | 148721 | 30147 | 17823 | 22004 | 1968 | 2025-08-23 10:30:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 92627 | 25055 | 53280 | 107622 | 16933 | 2025-08-24 01:55:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 88700 | 7758 | 3466 | 4665 | 280 | 2025-08-20 09:12:14 |
| [django](https://github.com/django/django) | 84660 | 32849 | 0 | 19700 | 359 | 2025-08-23 18:07:08 |
| [flask](https://github.com/pallets/flask) | 70208 | 16521 | 2692 | 2688 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68501 | 32667 | 73374 | 63791 | 9295 | 2025-08-23 16:27:51 |
| [keras](https://github.com/keras-team/keras) | 63359 | 19611 | 12528 | 8297 | 294 | 2025-08-22 17:48:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63111 | 26172 | 11655 | 19215 | 2160 | 2025-08-23 15:40:04 |
| [pandas](https://github.com/pandas-dev/pandas) | 46378 | 18848 | 27669 | 34459 | 3703 | 2025-08-22 16:50:55 |
| [ray](https://github.com/ray-project/ray) | 38603 | 6731 | 20933 | 34584 | 3010 | 2025-08-23 22:52:33 |
| [gym](https://github.com/openai/gym) | 36405 | 8692 | 1838 | 1465 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32225 | 4565 | 5718 | 4065 | 200 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30219 | 11247 | 13495 | 16056 | 2342 | 2025-08-23 17:58:33 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29393 | 6996 | 3945 | 4828 | 98 | 2025-08-21 03:35:51 |
| [celery](https://github.com/celery/celery) | 27071 | 4829 | 5157 | 3641 | 762 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23970 | 2191 | 1978 | 1319 | 552 | 2025-08-22 21:25:47 |
| [tornado](https://github.com/tornadoweb/tornado) | 22110 | 5539 | 1851 | 1670 | 206 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21600 | 7969 | 10949 | 19468 | 1639 | 2025-08-23 09:05:26 |
| [micropython](https://github.com/micropython/micropython) | 20750 | 8379 | 5795 | 7127 | 1775 | 2025-08-22 03:54:31 |
| [RustPython](https://github.com/RustPython/RustPython) | 20428 | 1342 | 1210 | 4831 | 443 | 2025-08-21 04:22:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18482 | 1579 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17641 | 2703 | 3243 | 1945 | 721 | 2025-08-22 14:56:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15932 | 2115 | 3143 | 8005 | 263 | 2025-08-22 11:34:40 |
| [httpx](https://github.com/encode/httpx) | 14487 | 946 | 915 | 1708 | 103 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13945 | 5453 | 10977 | 12506 | 1763 | 2025-08-23 08:23:24 |
| [dask](https://github.com/dask/dask) | 13426 | 1793 | 5426 | 6333 | 1193 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13377 | 2029 | 2624 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11370 | 1032 | 750 | 1681 | 49 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11167 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10808 | 1576 | 8071 | 978 | 236 | 2025-08-22 17:07:29 |
| [falcon](https://github.com/falconry/falcon) | 9703 | 959 | 1093 | 1360 | 156 | 2025-08-21 17:47:09 |
| [bottle](https://github.com/bottlepy/bottle) | 8648 | 1488 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8458 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6736 | 364 | 864 | 2443 | 312 | 2025-08-23 20:10:19 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5256 | 436 | 1186 | 711 | 496 | 2025-08-20 19:50:16 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4952 | 926 | 864 | 257 | 158 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1061 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3542 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3408 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2677 | 303 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2179 | 165 | 399 | 500 | 67 | 2025-08-21 08:46:43 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-18 17:39:32 |
| [pypy](https://github.com/pypy/pypy) | 1478 | 83 | 5141 | 168 | 735 | 2025-08-19 15:10:36 |
| [jython](https://github.com/jython/jython) | 1426 | 217 | 280 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 100 | 36 | 15 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-24T02:18:17*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
