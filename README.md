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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194166 | 75221 | 41211 | 68831 | 3672 | 2026-03-12 02:41:43 |
| [transformers](https://github.com/huggingface/transformers) | 157766 | 32373 | 18694 | 25309 | 2258 | 2026-03-11 21:37:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 98223 | 27144 | 57257 | 119446 | 18074 | 2026-03-12 02:46:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 96178 | 8823 | 3507 | 5420 | 154 | 2026-03-11 21:31:58 |
| [django](https://github.com/django/django) | 87092 | 33744 | 0 | 20826 | 431 | 2026-03-11 17:53:26 |
| [cpython](https://github.com/python/cpython) | 71997 | 34209 | 75526 | 69313 | 9291 | 2026-03-12 00:41:14 |
| [flask](https://github.com/pallets/flask) | 71405 | 16742 | 2723 | 2782 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65413 | 26754 | 11988 | 20379 | 2143 | 2026-03-11 17:10:52 |
| [keras](https://github.com/keras-team/keras) | 63977 | 19717 | 12659 | 8942 | 257 | 2026-03-12 02:40:11 |
| [pandas](https://github.com/pandas-dev/pandas) | 48118 | 19722 | 28166 | 36315 | 3687 | 2026-03-11 21:58:18 |
| [ray](https://github.com/ray-project/ray) | 41752 | 7312 | 22440 | 38880 | 3456 | 2026-03-12 01:50:46 |
| [gym](https://github.com/openai/gym) | 37083 | 8706 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33301 | 4644 | 5742 | 4083 | 194 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31587 | 12149 | 13826 | 17103 | 2321 | 2026-03-12 01:29:42 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29935 | 7080 | 3946 | 4942 | 78 | 2026-03-11 04:08:31 |
| [celery](https://github.com/celery/celery) | 28274 | 4986 | 5203 | 3860 | 770 | 2026-03-11 15:15:14 |
| [dash](https://github.com/plotly/dash) | 24456 | 2263 | 2070 | 1467 | 582 | 2026-03-11 23:00:31 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22559 | 8255 | 11197 | 20043 | 1534 | 2026-03-11 21:28:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22408 | 5545 | 1864 | 1710 | 218 | 2026-03-11 01:59:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 21874 | 1404 | 1314 | 6016 | 357 | 2026-03-12 02:02:41 |
| [micropython](https://github.com/micropython/micropython) | 21531 | 8740 | 5972 | 7613 | 1842 | 2026-03-11 05:40:49 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18327 | 2781 | 3327 | 2054 | 776 | 2026-03-10 22:29:23 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16442 | 2210 | 3182 | 8739 | 274 | 2026-03-11 23:38:18 |
| [httpx](https://github.com/encode/httpx) | 15206 | 1061 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14521 | 5651 | 11361 | 13414 | 1790 | 2026-03-11 20:35:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13765 | 2079 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13764 | 1854 | 5514 | 6505 | 1227 | 2026-03-11 14:29:00 |
| [starlette](https://github.com/Kludex/starlette) | 12021 | 1134 | 764 | 1826 | 49 | 2026-03-07 11:57:25 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11731 | 1650 | 8164 | 1044 | 213 | 2026-03-09 22:58:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11682 | 601 | 406 | 314 | 153 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1419 | 162 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8940 | 562 | 1020 | 492 | 218 | 2026-03-06 14:12:06 |
| [bottle](https://github.com/bottlepy/bottle) | 8762 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7198 | 391 | 880 | 2512 | 318 | 2026-03-11 03:55:14 |
| [hug](https://github.com/hugapi/hug) | 6907 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5513 | 466 | 1238 | 797 | 495 | 2026-03-08 17:01:54 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5205 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 894 | 1064 | 2732 | 82 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4019 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4004 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3605 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 312 | 661 | 1289 | 310 | 2026-03-12 01:12:52 |
| [anyio](https://github.com/agronholm/anyio) | 2407 | 185 | 429 | 581 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1080 | 1464 | 368 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1679 | 103 | 5178 | 184 | 758 | 2026-03-11 19:41:23 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-12T02:47:46*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
