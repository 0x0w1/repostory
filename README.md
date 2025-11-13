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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192416 | 74986 | 40981 | 61195 | 2231 | 2025-11-13 01:31:45 |
| [transformers](https://github.com/huggingface/transformers) | 152451 | 31120 | 18175 | 23399 | 2112 | 2025-11-13 00:24:04 |
| [pytorch](https://github.com/pytorch/pytorch) | 95008 | 25879 | 54809 | 112406 | 17068 | 2025-11-13 02:05:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 91849 | 8221 | 3476 | 4867 | 215 | 2025-11-12 16:24:25 |
| [django](https://github.com/django/django) | 85765 | 33213 | 0 | 20022 | 357 | 2025-11-12 22:42:24 |
| [flask](https://github.com/pallets/flask) | 70766 | 16620 | 2701 | 2724 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69828 | 33397 | 74320 | 66218 | 9200 | 2025-11-12 23:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64013 | 26434 | 11806 | 19759 | 2122 | 2025-11-12 20:10:27 |
| [keras](https://github.com/keras-team/keras) | 63554 | 19649 | 12590 | 8466 | 267 | 2025-11-11 23:41:11 |
| [pandas](https://github.com/pandas-dev/pandas) | 47091 | 19287 | 27876 | 35171 | 3610 | 2025-11-12 21:55:41 |
| [ray](https://github.com/ray-project/ray) | 39801 | 6899 | 21808 | 36425 | 3215 | 2025-11-13 01:30:25 |
| [gym](https://github.com/openai/gym) | 36763 | 8709 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32805 | 4621 | 5729 | 4072 | 195 | 2025-11-10 10:56:26 |
| [numpy](https://github.com/numpy/numpy) | 30810 | 11689 | 13643 | 16498 | 2354 | 2025-11-12 19:20:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29660 | 7034 | 3946 | 4866 | 86 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27541 | 4891 | 5176 | 3722 | 755 | 2025-11-12 22:48:57 |
| [dash](https://github.com/plotly/dash) | 24240 | 2229 | 2023 | 1368 | 583 | 2025-11-12 15:52:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22343 | 5544 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21971 | 8111 | 11044 | 19660 | 1628 | 2025-11-10 19:02:47 |
| [micropython](https://github.com/micropython/micropython) | 21082 | 8528 | 5871 | 7342 | 1801 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20791 | 1358 | 1227 | 4960 | 447 | 2025-11-11 23:24:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18556 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17961 | 2744 | 3291 | 1976 | 746 | 2025-11-12 21:34:20 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16088 | 2155 | 3161 | 8295 | 279 | 2025-11-12 10:12:12 |
| [httpx](https://github.com/encode/httpx) | 14732 | 975 | 921 | 1754 | 110 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14182 | 5537 | 11133 | 12830 | 1801 | 2025-11-13 01:41:37 |
| [dask](https://github.com/dask/dask) | 13587 | 1820 | 5456 | 6399 | 1191 | 2025-11-12 10:53:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13555 | 2043 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11653 | 1077 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11415 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11123 | 1596 | 8116 | 1000 | 211 | 2025-11-12 23:07:42 |
| [falcon](https://github.com/falconry/falcon) | 9757 | 975 | 1110 | 1400 | 164 | 2025-11-12 21:05:21 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8704 | 536 | 966 | 452 | 175 | 2025-11-10 19:27:35 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6996 | 371 | 872 | 2469 | 312 | 2025-11-11 03:51:31 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5370 | 444 | 1197 | 715 | 503 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5078 | 963 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 888 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3934 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3751 | 300 | 1166 | 200 | 117 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3535 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2705 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2294 | 175 | 414 | 545 | 75 | 2025-11-12 11:08:38 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 371 | 1782 | 265 | 262 | 2025-11-10 17:52:34 |
| [pypy](https://github.com/pypy/pypy) | 1565 | 89 | 5161 | 171 | 747 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-12 22:55:46 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-11-10 17:11:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-13T02:06:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
