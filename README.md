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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193561 | 75206 | 41132 | 65990 | 2966 | 2026-01-31 02:23:13 |
| [transformers](https://github.com/huggingface/transformers) | 155957 | 31911 | 18496 | 24538 | 2194 | 2026-01-30 20:52:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 97068 | 26698 | 56601 | 116868 | 17993 | 2026-01-31 02:38:09 |
| [fastapi](https://github.com/fastapi/fastapi) | 94643 | 8607 | 3501 | 5182 | 214 | 2026-01-29 08:23:49 |
| [django](https://github.com/django/django) | 86628 | 33573 | 0 | 20552 | 400 | 2026-01-31 01:48:59 |
| [cpython](https://github.com/python/cpython) | 71279 | 33982 | 75141 | 68198 | 9209 | 2026-01-30 18:18:57 |
| [flask](https://github.com/pallets/flask) | 71117 | 16680 | 2712 | 2760 | 2 | 2026-01-28 15:43:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64835 | 26647 | 11907 | 20112 | 2114 | 2026-01-30 09:11:43 |
| [keras](https://github.com/keras-team/keras) | 63751 | 19681 | 12623 | 8670 | 254 | 2026-01-31 01:36:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 47743 | 19591 | 28064 | 35829 | 3629 | 2026-01-30 21:24:12 |
| [ray](https://github.com/ray-project/ray) | 41057 | 7171 | 22255 | 38019 | 3316 | 2026-01-31 02:19:23 |
| [gym](https://github.com/openai/gym) | 36995 | 8711 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33145 | 4637 | 5738 | 4077 | 185 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31355 | 12008 | 13765 | 16920 | 2289 | 2026-01-29 17:25:14 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29843 | 7061 | 3946 | 4911 | 89 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27937 | 4935 | 5185 | 3776 | 760 | 2026-01-29 12:37:15 |
| [dash](https://github.com/plotly/dash) | 24429 | 2251 | 2050 | 1424 | 559 | 2026-01-27 22:05:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22436 | 5542 | 1863 | 1696 | 211 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22296 | 8176 | 11117 | 19886 | 1529 | 2026-01-30 00:47:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 21740 | 1400 | 1295 | 5549 | 372 | 2026-01-31 01:11:59 |
| [micropython](https://github.com/micropython/micropython) | 21402 | 8685 | 5945 | 7527 | 1850 | 2026-01-30 11:34:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1583 | 1464 | 1663 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18227 | 2774 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16235 | 2184 | 3175 | 8531 | 277 | 2026-01-30 16:29:02 |
| [httpx](https://github.com/encode/httpx) | 14955 | 1024 | 925 | 1781 | 128 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14409 | 5606 | 11274 | 13173 | 1749 | 2026-01-30 23:12:11 |
| [dask](https://github.com/dask/dask) | 13726 | 1838 | 5499 | 6460 | 1217 | 2026-01-30 20:59:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13697 | 2081 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11881 | 1100 | 763 | 1776 | 48 | 2026-01-27 08:14:03 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11619 | 601 | 403 | 311 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11446 | 1634 | 8146 | 1027 | 206 | 2026-01-30 19:09:56 |
| [falcon](https://github.com/falconry/falcon) | 9785 | 977 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8875 | 556 | 1000 | 482 | 200 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8736 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7119 | 380 | 878 | 2493 | 315 | 2026-01-29 06:38:14 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5615 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5462 | 447 | 1221 | 742 | 508 | 2026-01-30 16:42:31 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5171 | 998 | 896 | 285 | 188 | 2026-01-27 13:50:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3924 | 308 | 1180 | 207 | 115 | 2026-01-29 20:24:57 |
| [quart](https://github.com/pallets/quart) | 3585 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 657 | 1262 | 313 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2372 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1644 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1478 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-31T02:39:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
