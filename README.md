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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 199700 | 76293 | 41775 | 81881 | 3121 | 2026-09-11 04:19:05 |
| [transformers](https://github.com/huggingface/transformers) | 165099 | 34511 | 19446 | 28489 | 2403 | 2026-09-11 03:23:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 102915 | 29186 | 60912 | 135136 | 17716 | 2026-09-11 04:18:59 |
| [fastapi](https://github.com/fastapi/fastapi) | 102241 | 9871 | 3550 | 6321 | 81 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 90757 | 34246 | 0 | 21824 | 499 | 2026-09-08 19:01:03 |
| [cpython](https://github.com/python/cpython) | 76829 | 35362 | 78072 | 76865 | 9639 | 2026-09-11 01:22:36 |
| [flask](https://github.com/pallets/flask) | 74267 | 16978 | 2765 | 2906 | 5 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67227 | 27383 | 12275 | 21458 | 2150 | 2026-09-10 23:25:59 |
| [keras](https://github.com/keras-team/keras) | 64317 | 19784 | 12898 | 9838 | 180 | 2026-09-11 00:54:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 49715 | 20365 | 28535 | 38624 | 2717 | 2026-09-11 02:01:58 |
| [ray](https://github.com/ray-project/ray) | 43770 | 8020 | 23041 | 42620 | 3576 | 2026-09-11 01:25:06 |
| [gym](https://github.com/openai/gym) | 37238 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33890 | 4722 | 5772 | 4120 | 240 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32714 | 12765 | 14089 | 18405 | 2292 | 2026-09-11 04:08:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30176 | 7082 | 3966 | 5058 | 52 | 2026-09-09 06:49:15 |
| [celery](https://github.com/celery/celery) | 28875 | 5156 | 5299 | 4333 | 734 | 2026-09-10 22:13:43 |
| [dash](https://github.com/plotly/dash) | 24401 | 2313 | 2151 | 1699 | 504 | 2026-09-08 21:04:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23206 | 8479 | 11421 | 20848 | 1476 | 2026-09-11 02:42:48 |
| [RustPython](https://github.com/RustPython/RustPython) | 22344 | 1486 | 1424 | 7186 | 397 | 2026-09-11 00:54:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5556 | 1879 | 1812 | 255 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22054 | 8965 | 6123 | 8088 | 1525 | 2026-09-09 05:55:46 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18776 | 2837 | 3381 | 2152 | 700 | 2026-09-10 21:20:36 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1597 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16547 | 2401 | 3249 | 10076 | 216 | 2026-09-10 11:27:14 |
| [httpx](https://github.com/encode/httpx) | 15472 | 1286 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15006 | 5922 | 11636 | 14485 | 1836 | 2026-09-10 16:40:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14022 | 2129 | 2662 | 1221 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13913 | 1948 | 5557 | 6721 | 1330 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12614 | 1300 | 782 | 2109 | 50 | 2026-09-07 17:36:27 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12149 | 1779 | 8293 | 1203 | 205 | 2026-09-10 19:10:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11898 | 614 | 420 | 330 | 160 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 1032 | 1141 | 1514 | 156 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9188 | 612 | 1045 | 545 | 226 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8781 | 1505 | 866 | 649 | 290 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7320 | 425 | 900 | 2605 | 326 | 2026-09-07 22:29:47 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5625 | 508 | 1268 | 898 | 545 | 2026-09-10 17:48:33 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5384 | 1040 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4387 | 375 | 1201 | 249 | 118 | 2026-09-10 16:21:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 205 | 285 | 135 | 26 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2760 | 316 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2541 | 258 | 476 | 764 | 110 | 2026-09-10 22:38:09 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1596 | 357 | 2026-09-08 02:20:54 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1786 | 274 | 272 | 2026-09-07 18:00:00 |
| [pypy](https://github.com/pypy/pypy) | 1793 | 125 | 5256 | 303 | 721 | 2026-09-10 19:20:55 |
| [jython](https://github.com/jython/jython) | 1540 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-11T04:20:18*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
