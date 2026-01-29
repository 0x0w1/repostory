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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193534 | 75204 | 41126 | 65855 | 2900 | 2026-01-29 02:23:32 |
| [transformers](https://github.com/huggingface/transformers) | 155883 | 31889 | 18477 | 24493 | 2190 | 2026-01-28 19:23:10 |
| [pytorch](https://github.com/pytorch/pytorch) | 97024 | 26671 | 56553 | 116692 | 17985 | 2026-01-29 02:40:32 |
| [fastapi](https://github.com/fastapi/fastapi) | 94579 | 8594 | 3500 | 5178 | 211 | 2026-01-27 21:31:46 |
| [django](https://github.com/django/django) | 86610 | 33564 | 0 | 20546 | 404 | 2026-01-28 22:04:39 |
| [cpython](https://github.com/python/cpython) | 71256 | 33963 | 75128 | 68178 | 9220 | 2026-01-29 00:42:14 |
| [flask](https://github.com/pallets/flask) | 71106 | 16681 | 2712 | 2760 | 2 | 2026-01-28 15:43:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64815 | 26638 | 11903 | 20106 | 2112 | 2026-01-28 15:35:43 |
| [keras](https://github.com/keras-team/keras) | 63753 | 19681 | 12621 | 8659 | 250 | 2026-01-29 02:32:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 47732 | 19583 | 28059 | 35797 | 3635 | 2026-01-28 22:36:29 |
| [ray](https://github.com/ray-project/ray) | 41015 | 7166 | 22244 | 37978 | 3325 | 2026-01-29 02:35:46 |
| [gym](https://github.com/openai/gym) | 36987 | 8711 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33128 | 4636 | 5738 | 4077 | 185 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31349 | 12005 | 13763 | 16915 | 2288 | 2026-01-28 22:56:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29836 | 7059 | 3946 | 4910 | 88 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27929 | 4932 | 5185 | 3775 | 761 | 2026-01-25 17:25:47 |
| [dash](https://github.com/plotly/dash) | 24428 | 2251 | 2049 | 1424 | 558 | 2026-01-27 22:05:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22435 | 5542 | 1862 | 1696 | 210 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22291 | 8180 | 11116 | 19885 | 1531 | 2026-01-27 23:58:20 |
| [RustPython](https://github.com/RustPython/RustPython) | 21735 | 1399 | 1295 | 5530 | 374 | 2026-01-28 08:01:06 |
| [micropython](https://github.com/micropython/micropython) | 21391 | 8678 | 5944 | 7508 | 1843 | 2026-01-28 22:18:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18633 | 1583 | 1464 | 1662 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18220 | 2775 | 3319 | 2007 | 770 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16231 | 2183 | 3174 | 8529 | 277 | 2026-01-28 18:23:45 |
| [httpx](https://github.com/encode/httpx) | 14951 | 1022 | 925 | 1781 | 128 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14407 | 5603 | 11273 | 13167 | 1755 | 2026-01-28 23:48:16 |
| [dask](https://github.com/dask/dask) | 13726 | 1836 | 5498 | 6458 | 1215 | 2026-01-28 17:53:12 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13695 | 2082 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11874 | 1098 | 763 | 1776 | 48 | 2026-01-27 08:14:03 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11616 | 601 | 403 | 310 | 151 | 2026-01-28 14:22:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11442 | 1633 | 8145 | 1026 | 208 | 2026-01-29 01:13:07 |
| [falcon](https://github.com/falconry/falcon) | 9781 | 977 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8870 | 556 | 998 | 482 | 199 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8735 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7115 | 379 | 878 | 2491 | 315 | 2026-01-26 21:48:23 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5617 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5459 | 447 | 1221 | 740 | 512 | 2026-01-28 21:20:31 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5169 | 996 | 895 | 285 | 187 | 2026-01-27 13:50:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3922 | 308 | 1178 | 207 | 115 | 2026-01-28 21:24:01 |
| [quart](https://github.com/pallets/quart) | 3583 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2371 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1639 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1477 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-29T02:42:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
