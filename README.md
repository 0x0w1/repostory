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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192403 | 74982 | 40980 | 61138 | 2211 | 2025-11-12 01:56:26 |
| [transformers](https://github.com/huggingface/transformers) | 152409 | 31115 | 18171 | 23383 | 2119 | 2025-11-11 23:25:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 94973 | 25865 | 54778 | 112341 | 17054 | 2025-11-12 01:57:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 91799 | 8213 | 3476 | 4865 | 216 | 2025-11-11 15:54:30 |
| [django](https://github.com/django/django) | 85756 | 33212 | 0 | 20018 | 357 | 2025-11-11 23:28:08 |
| [flask](https://github.com/pallets/flask) | 70760 | 16620 | 2701 | 2723 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69810 | 33382 | 74311 | 66184 | 9223 | 2025-11-12 01:33:50 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64000 | 26429 | 11804 | 19756 | 2125 | 2025-11-11 15:57:38 |
| [keras](https://github.com/keras-team/keras) | 63555 | 19646 | 12590 | 8464 | 268 | 2025-11-11 23:41:11 |
| [pandas](https://github.com/pandas-dev/pandas) | 47082 | 19285 | 27870 | 35163 | 3601 | 2025-11-11 18:04:17 |
| [ray](https://github.com/ray-project/ray) | 39783 | 6893 | 21798 | 36407 | 3227 | 2025-11-12 02:03:18 |
| [gym](https://github.com/openai/gym) | 36759 | 8710 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32797 | 4621 | 5729 | 4072 | 196 | 2025-11-10 10:56:26 |
| [numpy](https://github.com/numpy/numpy) | 30797 | 11689 | 13643 | 16496 | 2361 | 2025-11-11 20:36:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29658 | 7034 | 3946 | 4865 | 85 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27528 | 4890 | 5176 | 3721 | 755 | 2025-11-11 05:19:44 |
| [dash](https://github.com/plotly/dash) | 24238 | 2229 | 2020 | 1365 | 583 | 2025-11-10 18:18:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22341 | 5544 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21962 | 8108 | 11040 | 19658 | 1623 | 2025-11-10 19:02:47 |
| [micropython](https://github.com/micropython/micropython) | 21075 | 8521 | 5870 | 7340 | 1802 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20787 | 1358 | 1227 | 4960 | 447 | 2025-11-11 23:24:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18554 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17955 | 2744 | 3290 | 1976 | 748 | 2025-11-11 16:51:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16086 | 2154 | 3161 | 8294 | 278 | 2025-11-10 16:26:17 |
| [httpx](https://github.com/encode/httpx) | 14730 | 975 | 921 | 1754 | 110 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14179 | 5535 | 11129 | 12823 | 1800 | 2025-11-11 23:06:20 |
| [dask](https://github.com/dask/dask) | 13586 | 1820 | 5456 | 6398 | 1194 | 2025-11-11 15:04:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13553 | 2043 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11652 | 1078 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11410 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11116 | 1596 | 8116 | 1000 | 212 | 2025-11-12 01:43:51 |
| [falcon](https://github.com/falconry/falcon) | 9755 | 975 | 1110 | 1400 | 167 | 2025-11-11 20:33:23 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8702 | 536 | 966 | 452 | 175 | 2025-11-10 19:27:35 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6990 | 371 | 872 | 2469 | 312 | 2025-11-11 03:51:31 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5370 | 444 | 1197 | 715 | 503 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5078 | 962 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 888 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3934 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3749 | 300 | 1166 | 200 | 117 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3533 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2705 | 305 | 654 | 1261 | 310 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2292 | 175 | 414 | 545 | 76 | 2025-11-10 17:59:53 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 371 | 1782 | 265 | 262 | 2025-11-10 17:52:34 |
| [pypy](https://github.com/pypy/pypy) | 1565 | 89 | 5160 | 171 | 746 | 2025-11-11 21:27:39 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-11-10 17:11:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-12T02:04:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
