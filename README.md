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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200160 | 76717 | 41778 | 82229 | 3174 | 2026-09-18 04:11:30 |
| [transformers](https://github.com/huggingface/transformers) | 166261 | 34619 | 19488 | 28657 | 2418 | 2026-09-18 04:13:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 103076 | 29659 | 61031 | 135799 | 17596 | 2026-09-18 04:10:01 |
| [fastapi](https://github.com/fastapi/fastapi) | 102408 | 9905 | 3552 | 6340 | 81 | 2026-09-14 18:49:48 |
| [django](https://github.com/django/django) | 91129 | 34657 | 0 | 21857 | 502 | 2026-09-18 01:46:40 |
| [cpython](https://github.com/python/cpython) | 77204 | 35742 | 78176 | 77194 | 9687 | 2026-09-18 02:43:39 |
| [flask](https://github.com/pallets/flask) | 74748 | 16980 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67286 | 27421 | 12284 | 21503 | 2157 | 2026-09-17 17:17:26 |
| [keras](https://github.com/keras-team/keras) | 64320 | 19796 | 12914 | 9890 | 202 | 2026-09-18 01:39:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49739 | 20396 | 28547 | 38802 | 2697 | 2026-09-17 20:55:18 |
| [ray](https://github.com/ray-project/ray) | 43861 | 8050 | 23079 | 42770 | 3591 | 2026-09-18 04:13:28 |
| [gym](https://github.com/openai/gym) | 37240 | 8675 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33906 | 4723 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32762 | 12813 | 14100 | 18491 | 2286 | 2026-09-17 21:16:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30183 | 7079 | 3966 | 5068 | 51 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28898 | 5168 | 5301 | 4396 | 735 | 2026-09-17 22:13:42 |
| [dash](https://github.com/plotly/dash) | 24411 | 2314 | 2152 | 1705 | 476 | 2026-09-17 15:07:40 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23228 | 8486 | 11424 | 20876 | 1489 | 2026-09-16 06:18:56 |
| [RustPython](https://github.com/RustPython/RustPython) | 22354 | 1486 | 1425 | 7229 | 395 | 2026-09-18 02:03:47 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5555 | 1883 | 1826 | 259 | 2026-09-16 18:23:07 |
| [micropython](https://github.com/micropython/micropython) | 22071 | 8974 | 6129 | 8098 | 1533 | 2026-09-16 23:31:27 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18788 | 2847 | 3384 | 2188 | 713 | 2026-09-18 01:23:08 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1597 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16549 | 2412 | 3253 | 10139 | 220 | 2026-09-17 19:26:44 |
| [httpx](https://github.com/encode/httpx) | 15495 | 1445 | 925 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15020 | 5944 | 11649 | 14526 | 1840 | 2026-09-18 00:55:55 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14023 | 2134 | 2662 | 1223 | 234 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13921 | 1956 | 5559 | 6727 | 1337 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12618 | 1313 | 782 | 2119 | 48 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12164 | 1784 | 8300 | 1209 | 209 | 2026-09-15 21:07:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11896 | 616 | 420 | 331 | 161 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 1033 | 1142 | 1520 | 158 | 2026-09-17 04:49:17 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9191 | 613 | 1046 | 549 | 223 | 2026-09-14 13:10:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 292 | 2026-09-15 07:20:39 |
| [trio](https://github.com/python-trio/trio) | 7331 | 431 | 901 | 2609 | 328 | 2026-09-17 02:12:00 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5631 | 515 | 1270 | 904 | 523 | 2026-09-17 17:44:43 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5394 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4400 | 376 | 1202 | 250 | 119 | 2026-09-11 19:10:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3669 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2544 | 266 | 477 | 774 | 111 | 2026-09-15 17:39:30 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 136 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1795 | 125 | 5257 | 303 | 711 | 2026-09-17 21:09:59 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-18T04:24:41*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
