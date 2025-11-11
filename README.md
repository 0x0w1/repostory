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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192392 | 74973 | 40980 | 61088 | 2209 | 2025-11-11 01:54:16 |
| [transformers](https://github.com/huggingface/transformers) | 152365 | 31107 | 18165 | 23373 | 2126 | 2025-11-11 00:45:17 |
| [pytorch](https://github.com/pytorch/pytorch) | 94934 | 25858 | 54753 | 112269 | 17049 | 2025-11-11 02:04:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 91754 | 8206 | 3476 | 4863 | 214 | 2025-11-10 20:55:20 |
| [django](https://github.com/django/django) | 85746 | 33215 | 0 | 20011 | 354 | 2025-11-10 21:00:41 |
| [flask](https://github.com/pallets/flask) | 70752 | 16618 | 2701 | 2723 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69790 | 33375 | 74299 | 66135 | 9242 | 2025-11-10 21:44:06 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63983 | 26425 | 11802 | 19752 | 2129 | 2025-11-10 14:16:03 |
| [keras](https://github.com/keras-team/keras) | 63549 | 19646 | 12590 | 8464 | 270 | 2025-11-10 23:20:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 47072 | 19280 | 27867 | 35148 | 3590 | 2025-11-11 01:10:29 |
| [ray](https://github.com/ray-project/ray) | 39757 | 6889 | 21791 | 36385 | 3214 | 2025-11-11 01:56:24 |
| [gym](https://github.com/openai/gym) | 36756 | 8710 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32788 | 4620 | 5729 | 4072 | 196 | 2025-11-10 10:56:26 |
| [numpy](https://github.com/numpy/numpy) | 30790 | 11683 | 13641 | 16488 | 2358 | 2025-11-10 20:10:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29655 | 7031 | 3946 | 4864 | 84 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27517 | 4891 | 5176 | 3721 | 753 | 2025-11-10 19:33:37 |
| [dash](https://github.com/plotly/dash) | 24233 | 2227 | 2019 | 1363 | 581 | 2025-11-10 18:18:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22340 | 5543 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21954 | 8106 | 11038 | 19656 | 1620 | 2025-11-10 19:02:47 |
| [micropython](https://github.com/micropython/micropython) | 21070 | 8519 | 5869 | 7335 | 1796 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20781 | 1357 | 1227 | 4960 | 450 | 2025-11-10 22:35:08 |
| [sanic](https://github.com/sanic-org/sanic) | 18552 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17947 | 2744 | 3290 | 1976 | 751 | 2025-11-10 19:47:52 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16077 | 2154 | 3161 | 8294 | 278 | 2025-11-10 16:26:17 |
| [httpx](https://github.com/encode/httpx) | 14726 | 975 | 921 | 1754 | 110 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14177 | 5536 | 11126 | 12814 | 1797 | 2025-11-10 22:51:44 |
| [dask](https://github.com/dask/dask) | 13584 | 1820 | 5455 | 6397 | 1196 | 2025-11-10 22:04:14 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13551 | 2042 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11644 | 1078 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11408 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11111 | 1596 | 8116 | 1000 | 214 | 2025-11-11 01:20:40 |
| [falcon](https://github.com/falconry/falcon) | 9753 | 975 | 1110 | 1398 | 168 | 2025-11-10 20:07:53 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8696 | 536 | 966 | 452 | 175 | 2025-11-10 19:27:35 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6978 | 371 | 872 | 2468 | 313 | 2025-11-10 22:09:32 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5368 | 443 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5077 | 961 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4060 | 888 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3747 | 300 | 1166 | 200 | 117 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3533 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2704 | 304 | 654 | 1261 | 310 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2289 | 174 | 412 | 544 | 73 | 2025-11-10 17:59:53 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 370 | 1781 | 264 | 260 | 2025-11-10 17:52:34 |
| [pypy](https://github.com/pypy/pypy) | 1564 | 89 | 5160 | 171 | 746 | 2025-11-10 11:43:28 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-11-10 17:11:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-11T02:05:21*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
