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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192897 | 75184 | 41048 | 63704 | 2428 | 2025-12-22 02:14:36 |
| [transformers](https://github.com/huggingface/transformers) | 154115 | 31501 | 18354 | 24029 | 2150 | 2025-12-21 17:06:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 96068 | 26323 | 55989 | 114538 | 17928 | 2025-12-22 02:20:32 |
| [fastapi](https://github.com/fastapi/fastapi) | 93310 | 8401 | 3499 | 5034 | 199 | 2025-12-21 18:24:52 |
| [django](https://github.com/django/django) | 86226 | 33461 | 0 | 20376 | 372 | 2025-12-19 20:10:12 |
| [flask](https://github.com/pallets/flask) | 70953 | 16667 | 2706 | 2737 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70411 | 33716 | 74783 | 67296 | 9259 | 2025-12-21 19:36:23 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64355 | 26514 | 11854 | 19934 | 2126 | 2025-12-21 03:48:44 |
| [keras](https://github.com/keras-team/keras) | 63656 | 19654 | 12606 | 8546 | 247 | 2025-12-20 00:20:41 |
| [pandas](https://github.com/pandas-dev/pandas) | 47373 | 19423 | 27978 | 35414 | 3606 | 2025-12-21 17:43:10 |
| [ray](https://github.com/ray-project/ray) | 40424 | 7022 | 22037 | 37222 | 3205 | 2025-12-22 01:23:53 |
| [gym](https://github.com/openai/gym) | 36885 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32973 | 4631 | 5735 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31069 | 11872 | 13711 | 16721 | 2379 | 2025-12-20 20:32:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29755 | 7044 | 3946 | 4891 | 82 | 2025-12-15 16:01:56 |
| [celery](https://github.com/celery/celery) | 27753 | 4919 | 5179 | 3745 | 752 | 2025-12-18 05:06:57 |
| [dash](https://github.com/plotly/dash) | 24350 | 2247 | 2039 | 1395 | 553 | 2025-12-18 16:31:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22391 | 5542 | 1861 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22147 | 8145 | 11087 | 19756 | 1546 | 2025-12-19 19:34:09 |
| [micropython](https://github.com/micropython/micropython) | 21240 | 8596 | 5903 | 7451 | 1813 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 20930 | 1371 | 1248 | 5154 | 436 | 2025-12-20 23:25:17 |
| [sanic](https://github.com/sanic-org/sanic) | 18603 | 1586 | 1456 | 1636 | 130 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18106 | 2764 | 3309 | 1993 | 758 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16155 | 2167 | 3168 | 8390 | 268 | 2025-12-21 17:27:39 |
| [httpx](https://github.com/encode/httpx) | 14856 | 995 | 925 | 1772 | 121 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14280 | 5563 | 11208 | 12994 | 1780 | 2025-12-21 20:05:04 |
| [dask](https://github.com/dask/dask) | 13659 | 1826 | 5479 | 6428 | 1206 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13627 | 2070 | 2641 | 1150 | 200 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11774 | 1093 | 760 | 1748 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11530 | 591 | 398 | 299 | 150 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11296 | 1607 | 8132 | 1015 | 207 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9770 | 975 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8799 | 550 | 985 | 474 | 192 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8715 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7072 | 374 | 877 | 2482 | 314 | 2025-12-15 22:18:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 741 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5418 | 444 | 1210 | 732 | 509 | 2025-12-22 01:19:21 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5120 | 978 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4018 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3829 | 304 | 1170 | 205 | 119 | 2025-12-18 06:57:55 |
| [quart](https://github.com/pallets/quart) | 3562 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2334 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2331 | 180 | 420 | 560 | 75 | 2025-12-17 13:22:00 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-15 17:49:12 |
| [pypy](https://github.com/pypy/pypy) | 1609 | 92 | 5168 | 172 | 752 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1461 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-22T02:23:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
