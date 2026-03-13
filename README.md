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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194175 | 75241 | 41216 | 68918 | 3718 | 2026-03-13 02:30:01 |
| [transformers](https://github.com/huggingface/transformers) | 157799 | 32430 | 18700 | 25331 | 2267 | 2026-03-13 02:15:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 98236 | 27179 | 57292 | 119553 | 18094 | 2026-03-13 02:33:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 96212 | 8842 | 3507 | 5423 | 155 | 2026-03-12 21:15:20 |
| [django](https://github.com/django/django) | 87086 | 33750 | 0 | 20830 | 426 | 2026-03-13 00:01:02 |
| [cpython](https://github.com/python/cpython) | 71982 | 34222 | 75545 | 69346 | 9301 | 2026-03-13 02:06:13 |
| [flask](https://github.com/pallets/flask) | 71393 | 16745 | 2723 | 2782 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65414 | 26779 | 11988 | 20383 | 2146 | 2026-03-11 17:10:52 |
| [keras](https://github.com/keras-team/keras) | 63965 | 19729 | 12662 | 8949 | 253 | 2026-03-13 01:50:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 48125 | 19732 | 28168 | 36338 | 3675 | 2026-03-12 23:53:53 |
| [ray](https://github.com/ray-project/ray) | 41761 | 7328 | 22447 | 38905 | 3460 | 2026-03-13 02:14:22 |
| [gym](https://github.com/openai/gym) | 37082 | 8706 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33310 | 4654 | 5742 | 4083 | 194 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31589 | 12155 | 13827 | 17112 | 2329 | 2026-03-12 19:15:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29933 | 7078 | 3946 | 4942 | 78 | 2026-03-11 04:08:31 |
| [celery](https://github.com/celery/celery) | 28262 | 4987 | 5203 | 3860 | 768 | 2026-03-12 14:51:00 |
| [dash](https://github.com/plotly/dash) | 24456 | 2263 | 2070 | 1470 | 581 | 2026-03-12 21:16:12 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22568 | 8257 | 11199 | 20048 | 1537 | 2026-03-12 22:03:52 |
| [tornado](https://github.com/tornadoweb/tornado) | 22411 | 5546 | 1864 | 1711 | 218 | 2026-03-12 20:53:26 |
| [RustPython](https://github.com/RustPython/RustPython) | 21875 | 1406 | 1314 | 6032 | 360 | 2026-03-13 02:36:16 |
| [micropython](https://github.com/micropython/micropython) | 21535 | 8742 | 5972 | 7618 | 1847 | 2026-03-11 05:40:49 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18328 | 2785 | 3329 | 2054 | 776 | 2026-03-12 18:15:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16433 | 2209 | 3182 | 8740 | 274 | 2026-03-12 10:47:02 |
| [httpx](https://github.com/encode/httpx) | 15191 | 1063 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14526 | 5653 | 11362 | 13421 | 1788 | 2026-03-13 02:07:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13767 | 2080 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13765 | 1854 | 5514 | 6505 | 1226 | 2026-03-12 11:13:54 |
| [starlette](https://github.com/Kludex/starlette) | 12024 | 1134 | 764 | 1827 | 47 | 2026-03-12 21:11:55 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11713 | 1651 | 8165 | 1044 | 214 | 2026-03-09 22:58:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11684 | 601 | 407 | 315 | 155 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1419 | 162 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8944 | 562 | 1020 | 492 | 218 | 2026-03-12 08:45:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7200 | 391 | 880 | 2512 | 318 | 2026-03-11 03:55:14 |
| [hug](https://github.com/hugapi/hug) | 6907 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5515 | 466 | 1239 | 797 | 494 | 2026-03-08 17:01:54 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5204 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 894 | 1064 | 2732 | 82 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4019 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4008 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3605 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 312 | 661 | 1291 | 308 | 2026-03-12 11:02:06 |
| [anyio](https://github.com/agronholm/anyio) | 2407 | 186 | 429 | 583 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1080 | 1464 | 368 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1679 | 103 | 5178 | 184 | 757 | 2026-03-12 16:17:15 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-13T02:45:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
