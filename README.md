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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191130 | 74762 | 40707 | 55896 | 1535 | 2025-08-11 02:01:10 |
| [transformers](https://github.com/huggingface/transformers) | 148147 | 29969 | 17740 | 21759 | 1976 | 2025-08-10 20:27:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 92264 | 24909 | 52995 | 106840 | 16759 | 2025-08-11 02:24:30 |
| [fastapi](https://github.com/fastapi/fastapi) | 88217 | 7708 | 3466 | 4654 | 299 | 2025-08-08 10:32:11 |
| [django](https://github.com/django/django) | 84541 | 32776 | 0 | 19655 | 358 | 2025-08-08 19:39:50 |
| [flask](https://github.com/pallets/flask) | 70150 | 16518 | 2692 | 2686 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68292 | 32538 | 73216 | 63485 | 9294 | 2025-08-10 22:32:50 |
| [keras](https://github.com/keras-team/keras) | 63299 | 19604 | 12519 | 8266 | 289 | 2025-08-09 17:37:50 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 62951 | 26120 | 11639 | 19153 | 2162 | 2025-08-08 16:17:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 46240 | 18778 | 27641 | 34395 | 3702 | 2025-08-08 19:54:59 |
| [ray](https://github.com/ray-project/ray) | 38410 | 6695 | 20853 | 34269 | 3003 | 2025-08-10 23:57:34 |
| [gym](https://github.com/openai/gym) | 36356 | 8686 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32147 | 4557 | 5715 | 4064 | 196 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30130 | 11181 | 13475 | 15993 | 2328 | 2025-08-08 23:55:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29365 | 6990 | 3945 | 4820 | 97 | 2025-08-10 17:06:47 |
| [celery](https://github.com/celery/celery) | 26975 | 4822 | 5153 | 3633 | 757 | 2025-08-10 07:19:25 |
| [dash](https://github.com/plotly/dash) | 23906 | 2187 | 1971 | 1311 | 546 | 2025-08-09 00:05:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22090 | 5538 | 1851 | 1667 | 207 | 2025-08-08 18:27:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21532 | 7952 | 10934 | 19438 | 1655 | 2025-08-07 21:18:23 |
| [micropython](https://github.com/micropython/micropython) | 20711 | 8347 | 5773 | 7077 | 1761 | 2025-08-10 02:01:34 |
| [RustPython](https://github.com/RustPython/RustPython) | 20388 | 1336 | 1205 | 4817 | 435 | 2025-08-08 22:41:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18463 | 1576 | 1448 | 1625 | 142 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17578 | 2689 | 3233 | 1937 | 711 | 2025-08-07 21:42:57 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15902 | 2111 | 3141 | 7967 | 259 | 2025-08-10 00:05:24 |
| [httpx](https://github.com/encode/httpx) | 14445 | 937 | 911 | 1704 | 97 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13906 | 5440 | 10964 | 12476 | 1752 | 2025-08-10 18:27:59 |
| [dask](https://github.com/dask/dask) | 13391 | 1791 | 5417 | 6331 | 1185 | 2025-08-04 17:59:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13354 | 2025 | 2621 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11326 | 1028 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11125 | 567 | 387 | 287 | 140 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10756 | 1572 | 8063 | 975 | 237 | 2025-08-07 14:52:25 |
| [falcon](https://github.com/falconry/falcon) | 9700 | 961 | 1092 | 1355 | 161 | 2025-08-09 11:43:51 |
| [bottle](https://github.com/bottlepy/bottle) | 8646 | 1486 | 853 | 621 | 283 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8440 | 517 | 934 | 429 | 410 | 2025-08-10 16:04:02 |
| [hug](https://github.com/hugapi/hug) | 6894 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6688 | 360 | 863 | 2439 | 312 | 2025-08-07 04:47:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5636 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5243 | 434 | 1183 | 707 | 491 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4936 | 923 | 860 | 258 | 156 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4040 | 891 | 1060 | 2712 | 82 | 2025-02-23 16:39:21 |
| [databases](https://github.com/encode/databases) | 3933 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3513 | 286 | 1150 | 193 | 114 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3390 | 185 | 277 | 120 | 62 | 2025-07-29 15:07:12 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2673 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2296 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2166 | 163 | 399 | 496 | 67 | 2025-08-04 18:10:59 |
| [web2py](https://github.com/web2py/web2py) | 2150 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1919 | 369 | 1779 | 264 | 260 | 2025-08-04 17:44:33 |
| [pypy](https://github.com/pypy/pypy) | 1466 | 83 | 5138 | 166 | 732 | 2025-08-09 19:29:09 |
| [jython](https://github.com/jython/jython) | 1418 | 216 | 278 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-11T02:26:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
