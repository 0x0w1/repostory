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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191696 | 74846 | 40804 | 57781 | 1667 | 2025-09-20 01:46:42 |
| [transformers](https://github.com/huggingface/transformers) | 149996 | 30460 | 17951 | 22487 | 1979 | 2025-09-19 19:55:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 93284 | 25344 | 53841 | 109099 | 17123 | 2025-09-20 01:26:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 89630 | 7897 | 3468 | 4722 | 246 | 2025-09-18 08:09:57 |
| [django](https://github.com/django/django) | 85037 | 32974 | 0 | 19822 | 356 | 2025-09-19 19:54:19 |
| [flask](https://github.com/pallets/flask) | 70375 | 16533 | 2696 | 2703 | 8 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 68934 | 32898 | 73656 | 64591 | 9274 | 2025-09-19 18:21:50 |
| [keras](https://github.com/keras-team/keras) | 63411 | 19625 | 12551 | 8345 | 259 | 2025-09-19 20:46:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63380 | 26252 | 11719 | 19379 | 2179 | 2025-09-19 10:40:49 |
| [pandas](https://github.com/pandas-dev/pandas) | 46614 | 18977 | 27722 | 34611 | 3654 | 2025-09-19 18:34:53 |
| [ray](https://github.com/ray-project/ray) | 39008 | 6809 | 21192 | 35220 | 3096 | 2025-09-20 00:38:31 |
| [gym](https://github.com/openai/gym) | 36552 | 8695 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32501 | 4576 | 5722 | 4068 | 204 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30423 | 11439 | 13546 | 16164 | 2356 | 2025-09-18 16:29:24 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29475 | 7005 | 3945 | 4836 | 104 | 2025-09-19 10:46:07 |
| [celery](https://github.com/celery/celery) | 27225 | 4848 | 5164 | 3659 | 756 | 2025-09-19 22:07:15 |
| [dash](https://github.com/plotly/dash) | 24081 | 2206 | 1996 | 1331 | 564 | 2025-09-19 21:42:17 |
| [tornado](https://github.com/tornadoweb/tornado) | 22202 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21711 | 8029 | 10989 | 19554 | 1622 | 2025-09-19 19:33:29 |
| [micropython](https://github.com/micropython/micropython) | 20845 | 8434 | 5817 | 7195 | 1785 | 2025-09-19 19:06:53 |
| [RustPython](https://github.com/RustPython/RustPython) | 20532 | 1347 | 1220 | 4872 | 438 | 2025-09-17 00:11:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18491 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17751 | 2714 | 3252 | 1952 | 722 | 2025-09-19 15:28:16 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15997 | 2125 | 3146 | 8084 | 272 | 2025-09-19 11:02:06 |
| [httpx](https://github.com/encode/httpx) | 14570 | 956 | 918 | 1730 | 99 | 2025-09-19 11:03:15 |
| [scipy](https://github.com/scipy/scipy) | 14033 | 5479 | 11034 | 12598 | 1763 | 2025-09-19 19:47:32 |
| [dask](https://github.com/dask/dask) | 13489 | 1796 | 5437 | 6346 | 1199 | 2025-09-16 14:21:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13447 | 2035 | 2627 | 1148 | 188 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11479 | 1041 | 754 | 1709 | 50 | 2025-09-19 07:01:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11263 | 574 | 388 | 289 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10914 | 1580 | 8087 | 982 | 231 | 2025-09-19 20:56:31 |
| [falcon](https://github.com/falconry/falcon) | 9720 | 959 | 1099 | 1369 | 157 | 2025-09-18 09:02:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8660 | 1486 | 855 | 623 | 283 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8552 | 524 | 945 | 434 | 411 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6895 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6861 | 367 | 869 | 2451 | 310 | 2025-09-18 04:41:45 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5295 | 438 | 1193 | 713 | 501 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5001 | 939 | 870 | 260 | 167 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4047 | 888 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3621 | 293 | 1157 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3461 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2688 | 304 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2308 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2213 | 163 | 401 | 510 | 67 | 2025-09-18 22:47:41 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-09-15 17:40:35 |
| [pypy](https://github.com/pypy/pypy) | 1498 | 86 | 5144 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1432 | 221 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-20T01:51:31*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
