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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193598 | 75206 | 41133 | 66158 | 3078 | 2026-02-03 02:45:46 |
| [transformers](https://github.com/huggingface/transformers) | 156076 | 31928 | 18510 | 24581 | 2207 | 2026-02-03 01:20:52 |
| [pytorch](https://github.com/pytorch/pytorch) | 97122 | 26732 | 56642 | 116999 | 18015 | 2026-02-03 02:49:10 |
| [fastapi](https://github.com/fastapi/fastapi) | 94741 | 8616 | 3501 | 5200 | 222 | 2026-02-02 19:16:42 |
| [django](https://github.com/django/django) | 86662 | 33606 | 0 | 20566 | 402 | 2026-02-03 02:05:44 |
| [cpython](https://github.com/python/cpython) | 71326 | 34006 | 75158 | 68240 | 9218 | 2026-02-02 21:57:54 |
| [flask](https://github.com/pallets/flask) | 71128 | 16688 | 2713 | 2762 | 2 | 2026-01-28 15:43:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64873 | 26659 | 11911 | 20144 | 2125 | 2026-02-02 13:53:20 |
| [keras](https://github.com/keras-team/keras) | 63753 | 19685 | 12624 | 8683 | 255 | 2026-02-03 01:33:48 |
| [pandas](https://github.com/pandas-dev/pandas) | 47777 | 19602 | 28068 | 35860 | 3623 | 2026-02-02 18:47:21 |
| [ray](https://github.com/ray-project/ray) | 41104 | 7177 | 22268 | 38073 | 3361 | 2026-02-03 02:17:53 |
| [gym](https://github.com/openai/gym) | 37006 | 8711 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33154 | 4637 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31369 | 12015 | 13772 | 16937 | 2296 | 2026-02-03 00:27:40 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29850 | 7063 | 3946 | 4912 | 90 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27947 | 4935 | 5186 | 3779 | 763 | 2026-01-29 12:37:15 |
| [dash](https://github.com/plotly/dash) | 24439 | 2251 | 2051 | 1425 | 561 | 2026-01-27 22:05:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22437 | 5544 | 1863 | 1698 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22302 | 8177 | 11119 | 19898 | 1525 | 2026-02-03 01:19:34 |
| [RustPython](https://github.com/RustPython/RustPython) | 21750 | 1400 | 1295 | 5611 | 373 | 2026-02-03 02:46:11 |
| [micropython](https://github.com/micropython/micropython) | 21414 | 8690 | 5947 | 7530 | 1847 | 2026-02-03 02:26:46 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1583 | 1464 | 1663 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18233 | 2776 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16242 | 2184 | 3175 | 8537 | 275 | 2026-02-03 01:44:54 |
| [httpx](https://github.com/encode/httpx) | 14967 | 1027 | 925 | 1783 | 129 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14416 | 5608 | 11281 | 13202 | 1754 | 2026-02-02 17:52:16 |
| [dask](https://github.com/dask/dask) | 13728 | 1839 | 5501 | 6463 | 1220 | 2026-01-30 20:59:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13701 | 2080 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11890 | 1102 | 763 | 1779 | 50 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11625 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11452 | 1635 | 8146 | 1027 | 206 | 2026-01-30 19:09:56 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 978 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8880 | 556 | 1001 | 482 | 201 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8739 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7139 | 381 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5470 | 453 | 1222 | 745 | 508 | 2026-02-02 19:39:50 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5173 | 998 | 897 | 287 | 187 | 2026-02-02 17:09:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3930 | 309 | 1182 | 208 | 116 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3586 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2724 | 308 | 657 | 1265 | 313 | 2026-02-03 02:15:22 |
| [anyio](https://github.com/agronholm/anyio) | 2373 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1644 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1477 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-03T02:49:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
