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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198793 | 76233 | 41744 | 81448 | 3069 | 2026-09-04 04:00:30 |
| [transformers](https://github.com/huggingface/transformers) | 164763 | 34435 | 19400 | 28351 | 2391 | 2026-09-04 04:06:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 102745 | 29101 | 60752 | 134556 | 17498 | 2026-09-04 04:13:19 |
| [fastapi](https://github.com/fastapi/fastapi) | 102068 | 9847 | 3548 | 6307 | 81 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 89932 | 34229 | 0 | 21763 | 487 | 2026-09-03 19:25:45 |
| [cpython](https://github.com/python/cpython) | 75975 | 35321 | 77939 | 76622 | 9630 | 2026-09-03 22:20:53 |
| [flask](https://github.com/pallets/flask) | 72165 | 16958 | 2765 | 2900 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67155 | 27355 | 12263 | 21425 | 2148 | 2026-09-03 07:29:11 |
| [keras](https://github.com/keras-team/keras) | 64274 | 19771 | 12895 | 9796 | 224 | 2026-09-04 03:23:58 |
| [pandas](https://github.com/pandas-dev/pandas) | 49631 | 20318 | 28526 | 38465 | 2725 | 2026-09-04 03:16:42 |
| [ray](https://github.com/ray-project/ray) | 43699 | 7998 | 23015 | 42484 | 3557 | 2026-09-04 03:49:25 |
| [gym](https://github.com/openai/gym) | 37243 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33874 | 4722 | 5771 | 4120 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32650 | 12709 | 14082 | 18320 | 2333 | 2026-09-03 20:42:05 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30156 | 7085 | 3966 | 5051 | 58 | 2026-09-03 16:07:55 |
| [celery](https://github.com/celery/celery) | 28855 | 5148 | 5297 | 4295 | 742 | 2026-09-03 22:13:17 |
| [dash](https://github.com/plotly/dash) | 24394 | 2317 | 2148 | 1694 | 531 | 2026-09-03 20:29:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23145 | 8469 | 11411 | 20806 | 1471 | 2026-09-04 00:47:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 22326 | 1482 | 1423 | 7147 | 397 | 2026-09-03 16:28:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22176 | 5555 | 1879 | 1809 | 253 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22040 | 8958 | 6121 | 8081 | 1532 | 2026-09-03 06:23:09 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18760 | 2837 | 3378 | 2150 | 704 | 2026-09-03 19:56:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1599 | 1467 | 1674 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16533 | 2393 | 3242 | 10028 | 217 | 2026-09-03 15:23:54 |
| [httpx](https://github.com/encode/httpx) | 15459 | 1271 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14985 | 5905 | 11622 | 14437 | 1825 | 2026-09-03 12:48:31 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14010 | 2128 | 2659 | 1216 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13910 | 1941 | 5554 | 6714 | 1324 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12592 | 1288 | 781 | 2076 | 67 | 2026-09-01 19:21:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12132 | 1773 | 8285 | 1199 | 206 | 2026-09-02 20:54:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 613 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 1032 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9180 | 610 | 1044 | 543 | 223 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1505 | 865 | 648 | 290 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7314 | 419 | 900 | 2596 | 325 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6881 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5622 | 503 | 1266 | 893 | 543 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5377 | 1037 | 934 | 323 | 202 | 2026-09-02 10:45:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4368 | 373 | 1200 | 248 | 127 | 2026-09-03 20:03:09 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3663 | 206 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 315 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 251 | 473 | 756 | 107 | 2026-09-03 23:29:58 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 274 | 272 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1787 | 125 | 5255 | 299 | 721 | 2026-09-03 20:17:57 |
| [jython](https://github.com/jython/jython) | 1539 | 231 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-04T04:13:56*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
