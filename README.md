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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195072 | 75273 | 41404 | 73293 | 5117 | 2026-05-12 03:43:34 |
| [transformers](https://github.com/huggingface/transformers) | 160501 | 33175 | 18947 | 26288 | 2362 | 2026-05-12 03:50:08 |
| [pytorch](https://github.com/pytorch/pytorch) | 99832 | 27747 | 58627 | 124222 | 18419 | 2026-05-12 03:50:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 98109 | 9226 | 3525 | 5715 | 189 | 2026-05-11 17:21:41 |
| [django](https://github.com/django/django) | 87465 | 33857 | 0 | 21205 | 431 | 2026-05-11 18:50:41 |
| [cpython](https://github.com/python/cpython) | 72652 | 34576 | 76331 | 71068 | 9309 | 2026-05-12 02:54:10 |
| [flask](https://github.com/pallets/flask) | 71516 | 16834 | 2736 | 2819 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66047 | 27002 | 12079 | 20739 | 2029 | 2026-05-12 00:15:00 |
| [keras](https://github.com/keras-team/keras) | 64058 | 19761 | 12752 | 9306 | 205 | 2026-05-11 17:52:35 |
| [pandas](https://github.com/pandas-dev/pandas) | 48734 | 19933 | 28278 | 37249 | 3314 | 2026-05-12 00:27:44 |
| [ray](https://github.com/ray-project/ray) | 42503 | 7540 | 22666 | 40259 | 3547 | 2026-05-12 03:25:26 |
| [gym](https://github.com/openai/gym) | 37191 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33566 | 4682 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 32015 | 12355 | 13909 | 17427 | 2365 | 2026-05-11 19:44:21 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30002 | 7066 | 3967 | 5005 | 78 | 2026-05-06 11:55:49 |
| [celery](https://github.com/celery/celery) | 28468 | 5038 | 5273 | 4106 | 772 | 2026-05-11 16:47:01 |
| [dash](https://github.com/plotly/dash) | 24172 | 2281 | 2095 | 1560 | 551 | 2026-05-12 00:25:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22787 | 8328 | 11264 | 20338 | 1488 | 2026-05-11 21:11:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5539 | 1871 | 1730 | 219 | 2026-05-11 16:19:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 22038 | 1437 | 1341 | 6429 | 378 | 2026-05-11 21:16:24 |
| [micropython](https://github.com/micropython/micropython) | 21696 | 8819 | 6053 | 7787 | 1766 | 2026-05-12 01:42:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1587 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18513 | 2805 | 3343 | 2082 | 764 | 2026-05-11 18:18:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16430 | 2261 | 3193 | 8983 | 262 | 2026-05-12 01:28:49 |
| [httpx](https://github.com/encode/httpx) | 15261 | 1140 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14683 | 5721 | 11436 | 13667 | 1782 | 2026-05-12 02:37:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13866 | 2111 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13825 | 1871 | 5525 | 6554 | 1247 | 2026-05-08 17:04:32 |
| [starlette](https://github.com/Kludex/starlette) | 12299 | 1168 | 766 | 1888 | 57 | 2026-05-11 17:31:55 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11843 | 1682 | 8204 | 1077 | 216 | 2026-05-10 20:24:46 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11784 | 606 | 414 | 323 | 154 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9048 | 578 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7259 | 393 | 892 | 2541 | 320 | 2026-05-11 22:08:12 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5567 | 479 | 1251 | 826 | 503 | 2026-05-11 16:22:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5251 | 1013 | 912 | 298 | 208 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4130 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3632 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2743 | 311 | 663 | 1313 | 306 | 2026-05-11 22:33:49 |
| [anyio](https://github.com/agronholm/anyio) | 2462 | 206 | 438 | 632 | 82 | 2026-05-11 21:29:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1084 | 1499 | 364 | 2026-05-06 11:00:56 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1726 | 112 | 5206 | 242 | 739 | 2026-05-11 15:20:04 |
| [jython](https://github.com/jython/jython) | 1507 | 229 | 294 | 128 | 112 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-12T03:56:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
