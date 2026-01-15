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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193347 | 75162 | 41088 | 65082 | 2755 | 2026-01-15 01:53:59 |
| [transformers](https://github.com/huggingface/transformers) | 155072 | 31733 | 18420 | 24272 | 2169 | 2026-01-14 19:27:43 |
| [pytorch](https://github.com/pytorch/pytorch) | 96619 | 26507 | 56310 | 115708 | 17855 | 2026-01-15 02:21:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 94074 | 8523 | 3500 | 5127 | 203 | 2026-01-12 10:13:31 |
| [django](https://github.com/django/django) | 86468 | 33478 | 0 | 20474 | 381 | 2026-01-14 20:07:11 |
| [cpython](https://github.com/python/cpython) | 71064 | 33894 | 74981 | 67880 | 9208 | 2026-01-15 00:53:01 |
| [flask](https://github.com/pallets/flask) | 71045 | 16677 | 2709 | 2748 | 12 | 2026-01-05 16:50:56 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64630 | 26599 | 11888 | 20056 | 2126 | 2026-01-14 14:33:03 |
| [keras](https://github.com/keras-team/keras) | 63714 | 19676 | 12609 | 8606 | 239 | 2026-01-14 20:22:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 47589 | 19515 | 28019 | 35606 | 3618 | 2026-01-14 21:56:17 |
| [ray](https://github.com/ray-project/ray) | 40773 | 7112 | 22154 | 37647 | 3272 | 2026-01-15 01:58:03 |
| [gym](https://github.com/openai/gym) | 36952 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33067 | 4633 | 5736 | 4077 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31229 | 11959 | 13745 | 16845 | 2334 | 2026-01-14 13:12:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29804 | 7049 | 3946 | 4900 | 82 | 2026-01-13 22:15:14 |
| [celery](https://github.com/celery/celery) | 27870 | 4931 | 5183 | 3768 | 758 | 2026-01-10 18:43:35 |
| [dash](https://github.com/plotly/dash) | 24395 | 2249 | 2041 | 1411 | 555 | 2026-01-12 20:29:24 |
| [tornado](https://github.com/tornadoweb/tornado) | 22420 | 5544 | 1862 | 1693 | 209 | 2026-01-13 20:42:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22225 | 8176 | 11104 | 19814 | 1533 | 2026-01-14 19:42:56 |
| [RustPython](https://github.com/RustPython/RustPython) | 21666 | 1401 | 1284 | 5385 | 372 | 2026-01-15 00:06:38 |
| [micropython](https://github.com/micropython/micropython) | 21343 | 8651 | 5937 | 7485 | 1831 | 2026-01-14 11:59:52 |
| [sanic](https://github.com/sanic-org/sanic) | 18611 | 1584 | 1460 | 1662 | 110 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18179 | 2772 | 3313 | 2002 | 762 | 2026-01-14 21:23:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16200 | 2179 | 3171 | 8488 | 269 | 2026-01-13 11:19:18 |
| [httpx](https://github.com/encode/httpx) | 14905 | 1007 | 925 | 1776 | 124 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14346 | 5587 | 11253 | 13110 | 1760 | 2026-01-15 01:15:46 |
| [dask](https://github.com/dask/dask) | 13711 | 1835 | 5486 | 6448 | 1211 | 2026-01-13 12:40:31 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13684 | 2081 | 2644 | 1156 | 203 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11839 | 1098 | 761 | 1765 | 51 | 2026-01-11 21:47:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11585 | 600 | 401 | 305 | 152 | 2026-01-14 23:28:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11382 | 1621 | 8142 | 1021 | 212 | 2026-01-14 18:44:05 |
| [falcon](https://github.com/falconry/falcon) | 9775 | 974 | 1115 | 1407 | 163 | 2026-01-10 11:15:16 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8842 | 555 | 996 | 480 | 199 | 2026-01-13 18:26:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8727 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7102 | 378 | 877 | 2487 | 312 | 2026-01-12 21:58:36 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5619 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5447 | 445 | 1218 | 735 | 510 | 2026-01-14 06:28:04 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5154 | 988 | 885 | 280 | 178 | 2026-01-14 04:30:10 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4024 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3886 | 305 | 1175 | 207 | 118 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3573 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2722 | 307 | 655 | 1261 | 310 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2357 | 180 | 421 | 563 | 74 | 2026-01-12 17:50:45 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1784 | 266 | 265 | 2026-01-12 17:44:15 |
| [pypy](https://github.com/pypy/pypy) | 1629 | 95 | 5169 | 177 | 754 | 2026-01-12 22:21:27 |
| [jython](https://github.com/jython/jython) | 1469 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-15T02:21:31*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
