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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201669 | 77412 | 41990 | 84958 | 3469 | 2026-11-21 06:28:19 |
| [transformers](https://github.com/huggingface/transformers) | 169335 | 35251 | 19929 | 30260 | 1096 | 2026-11-21 05:27:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 105760 | 30690 | 62857 | 142396 | 18467 | 2026-11-21 06:48:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 104988 | 10364 | 3555 | 6646 | 49 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91886 | 35119 | 0 | 22234 | 538 | 2026-11-19 22:44:16 |
| [cpython](https://github.com/python/cpython) | 78434 | 36554 | 79365 | 80576 | 9343 | 2026-11-21 06:29:54 |
| [flask](https://github.com/pallets/flask) | 75300 | 17274 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68276 | 27679 | 12401 | 21876 | 2174 | 2026-11-21 05:56:34 |
| [keras](https://github.com/keras-team/keras) | 64445 | 19805 | 13104 | 10319 | 251 | 2026-11-20 23:54:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 50582 | 20702 | 28705 | 40125 | 1804 | 2026-11-20 17:43:26 |
| [ray](https://github.com/ray-project/ray) | 44351 | 8298 | 23358 | 44576 | 3826 | 2026-11-21 02:17:35 |
| [gym](https://github.com/openai/gym) | 37236 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34080 | 4748 | 5785 | 4154 | 276 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33443 | 13057 | 14198 | 19086 | 2257 | 2026-11-20 20:29:10 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30252 | 7106 | 3966 | 5119 | 58 | 2026-11-19 09:00:18 |
| [celery](https://github.com/celery/celery) | 29254 | 5275 | 5404 | 4750 | 809 | 2026-11-19 19:15:56 |
| [dash](https://github.com/plotly/dash) | 24500 | 2347 | 2185 | 1852 | 427 | 2026-11-20 20:30:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23496 | 8568 | 11466 | 21094 | 1474 | 2026-11-21 02:29:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22498 | 1508 | 1473 | 8397 | 341 | 2026-11-19 05:06:22 |
| [micropython](https://github.com/micropython/micropython) | 22215 | 9072 | 6185 | 8278 | 1595 | 2026-11-21 05:26:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22173 | 5614 | 1901 | 1950 | 201 | 2026-11-21 03:23:15 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18916 | 2900 | 3406 | 2293 | 733 | 2026-11-19 23:40:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1619 | 1475 | 1693 | 167 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16619 | 2536 | 3279 | 10759 | 333 | 2026-11-20 17:28:38 |
| [httpx](https://github.com/encode/httpx) | 15821 | 2008 | 925 | 1822 | 148 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15231 | 6110 | 11786 | 14956 | 1927 | 2026-11-20 19:12:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14119 | 2166 | 2669 | 1262 | 261 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13960 | 2033 | 5583 | 6849 | 1437 | 2026-11-17 00:50:22 |
| [starlette](https://github.com/Kludex/starlette) | 12742 | 1452 | 800 | 2304 | 36 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12297 | 1959 | 8409 | 1263 | 218 | 2026-11-19 21:09:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11946 | 624 | 431 | 348 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9821 | 1055 | 1154 | 1582 | 164 | 2026-11-21 06:32:57 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9250 | 624 | 1059 | 622 | 163 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 479 | 911 | 2678 | 344 | 2026-11-18 11:55:16 |
| [hug](https://github.com/hugapi/hug) | 6868 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5641 | 548 | 1311 | 995 | 559 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5457 | 1054 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4481 | 395 | 1212 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2752 | 84 | 2026-11-20 03:37:34 |
| [databases](https://github.com/encode/databases) | 3984 | 368 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 214 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1427 | 255 | 2026-11-21 04:06:03 |
| [anyio](https://github.com/agronholm/anyio) | 2572 | 359 | 506 | 913 | 163 | 2026-11-20 00:26:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5304 | 471 | 727 | 2026-11-20 13:55:52 |
| [jython](https://github.com/jython/jython) | 1549 | 237 | 306 | 164 | 109 | 2026-11-16 18:03:33 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-21T06:51:04*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
