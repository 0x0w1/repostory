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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192319 | 74957 | 40911 | 60663 | 1975 | 2025-11-06 02:02:51 |
| [transformers](https://github.com/huggingface/transformers) | 152141 | 31052 | 18147 | 23308 | 2118 | 2025-11-05 23:30:53 |
| [pytorch](https://github.com/pytorch/pytorch) | 94714 | 25792 | 54668 | 112020 | 17078 | 2025-11-06 02:03:24 |
| [fastapi](https://github.com/fastapi/fastapi) | 91561 | 8164 | 3474 | 4847 | 208 | 2025-11-04 08:39:31 |
| [django](https://github.com/django/django) | 85664 | 33194 | 0 | 19997 | 356 | 2025-11-05 22:06:51 |
| [flask](https://github.com/pallets/flask) | 70708 | 16610 | 2701 | 2721 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69682 | 33296 | 74248 | 65893 | 9227 | 2025-11-05 22:52:43 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63923 | 26404 | 11794 | 19729 | 2133 | 2025-11-05 13:44:10 |
| [keras](https://github.com/keras-team/keras) | 63531 | 19644 | 12586 | 8450 | 268 | 2025-11-06 00:39:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 47033 | 19245 | 27855 | 35094 | 3609 | 2025-11-06 00:06:17 |
| [ray](https://github.com/ray-project/ray) | 39682 | 6867 | 21772 | 36298 | 3208 | 2025-11-06 01:10:02 |
| [gym](https://github.com/openai/gym) | 36744 | 8713 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32763 | 4614 | 5729 | 4071 | 195 | 2025-11-06 00:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30753 | 11662 | 13631 | 16463 | 2356 | 2025-11-06 00:52:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29641 | 7031 | 3946 | 4862 | 81 | 2025-11-04 13:56:36 |
| [celery](https://github.com/celery/celery) | 27492 | 4887 | 5175 | 3715 | 749 | 2025-11-01 23:53:30 |
| [dash](https://github.com/plotly/dash) | 24224 | 2227 | 2018 | 1357 | 580 | 2025-11-06 00:51:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22329 | 5539 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21934 | 8104 | 11032 | 19652 | 1616 | 2025-11-03 19:15:50 |
| [micropython](https://github.com/micropython/micropython) | 21042 | 8516 | 5867 | 7324 | 1786 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20763 | 1359 | 1225 | 4948 | 444 | 2025-11-04 18:14:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18549 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17916 | 2740 | 3269 | 1974 | 730 | 2025-11-05 14:56:08 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16066 | 2151 | 3160 | 8281 | 265 | 2025-11-04 10:38:16 |
| [httpx](https://github.com/encode/httpx) | 14706 | 971 | 919 | 1753 | 107 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14160 | 5533 | 11119 | 12803 | 1795 | 2025-11-06 00:36:09 |
| [dask](https://github.com/dask/dask) | 13574 | 1817 | 5451 | 6386 | 1190 | 2025-11-04 14:32:21 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13538 | 2040 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11621 | 1069 | 759 | 1743 | 50 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11397 | 585 | 396 | 298 | 148 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11089 | 1593 | 8114 | 999 | 220 | 2025-11-04 21:57:21 |
| [falcon](https://github.com/falconry/falcon) | 9750 | 972 | 1109 | 1392 | 169 | 2025-11-04 21:54:41 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8685 | 534 | 965 | 451 | 175 | 2025-11-03 10:41:32 |
| [trio](https://github.com/python-trio/trio) | 6932 | 371 | 872 | 2466 | 311 | 2025-11-03 23:11:41 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5364 | 442 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5066 | 958 | 875 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4059 | 887 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3736 | 298 | 1164 | 198 | 115 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3512 | 191 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2701 | 303 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2318 | 133 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2277 | 174 | 412 | 542 | 72 | 2025-11-04 11:44:32 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 370 | 1781 | 264 | 261 | 2025-11-03 17:44:55 |
| [pypy](https://github.com/pypy/pypy) | 1559 | 89 | 5157 | 171 | 744 | 2025-10-28 13:51:47 |
| [jython](https://github.com/jython/jython) | 1453 | 225 | 284 | 114 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-06T02:04:54*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
