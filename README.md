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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193041 | 75138 | 41048 | 63899 | 2496 | 2025-12-24 23:13:06 |
| [transformers](https://github.com/huggingface/transformers) | 154211 | 31531 | 18368 | 24064 | 2148 | 2025-12-24 15:30:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 96128 | 26354 | 56036 | 114748 | 17913 | 2025-12-25 02:14:59 |
| [fastapi](https://github.com/fastapi/fastapi) | 93405 | 8419 | 3499 | 5042 | 200 | 2025-12-24 15:19:32 |
| [django](https://github.com/django/django) | 86247 | 33402 | 0 | 20394 | 370 | 2025-12-24 17:49:00 |
| [flask](https://github.com/pallets/flask) | 70958 | 16669 | 2707 | 2739 | 14 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70451 | 33744 | 74808 | 67373 | 9247 | 2025-12-24 22:03:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64367 | 26527 | 11857 | 19948 | 2117 | 2025-12-24 16:25:08 |
| [keras](https://github.com/keras-team/keras) | 63657 | 19659 | 12606 | 8551 | 242 | 2025-12-24 18:58:04 |
| [pandas](https://github.com/pandas-dev/pandas) | 47396 | 19435 | 27984 | 35437 | 3612 | 2025-12-23 18:12:04 |
| [ray](https://github.com/ray-project/ray) | 40463 | 7036 | 22054 | 37251 | 3214 | 2025-12-24 20:12:24 |
| [gym](https://github.com/openai/gym) | 36901 | 8719 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32989 | 4630 | 5735 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31080 | 11884 | 13714 | 16736 | 2380 | 2025-12-24 20:23:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29762 | 7043 | 3946 | 4892 | 80 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27773 | 4921 | 5178 | 3747 | 752 | 2025-12-22 17:26:19 |
| [dash](https://github.com/plotly/dash) | 24362 | 2246 | 2039 | 1395 | 553 | 2025-12-22 23:39:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22397 | 5544 | 1861 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22152 | 8149 | 11089 | 19760 | 1544 | 2025-12-23 16:28:00 |
| [micropython](https://github.com/micropython/micropython) | 21249 | 8601 | 5905 | 7456 | 1818 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 20940 | 1372 | 1255 | 5187 | 417 | 2025-12-25 02:14:02 |
| [sanic](https://github.com/sanic-org/sanic) | 18605 | 1586 | 1456 | 1636 | 130 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18118 | 2766 | 3309 | 1995 | 759 | 2025-12-24 16:24:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16159 | 2171 | 3168 | 8399 | 269 | 2025-12-24 16:48:06 |
| [httpx](https://github.com/encode/httpx) | 14865 | 997 | 925 | 1773 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14288 | 5566 | 11214 | 13004 | 1781 | 2025-12-24 11:21:56 |
| [dask](https://github.com/dask/dask) | 13666 | 1827 | 5480 | 6428 | 1207 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13639 | 2070 | 2642 | 1152 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11784 | 1093 | 760 | 1749 | 52 | 2025-12-24 11:58:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11535 | 591 | 399 | 299 | 151 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11310 | 1609 | 8133 | 1017 | 209 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9772 | 975 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8806 | 550 | 985 | 474 | 192 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8717 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7080 | 374 | 877 | 2483 | 314 | 2025-12-22 21:33:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 740 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5422 | 444 | 1212 | 732 | 510 | 2025-12-24 01:14:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5123 | 978 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4019 | 259 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3842 | 303 | 1171 | 205 | 118 | 2025-12-22 19:47:52 |
| [quart](https://github.com/pallets/quart) | 3563 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2719 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2336 | 180 | 421 | 561 | 76 | 2025-12-23 14:26:02 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2335 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1607 | 93 | 5169 | 172 | 753 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1460 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-25T02:19:05*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
