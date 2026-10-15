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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200971 | 79431 | 41895 | 83620 | 3423 | 2026-10-15 04:17:09 |
| [transformers](https://github.com/huggingface/transformers) | 167702 | 34868 | 19625 | 29211 | 2327 | 2026-10-15 02:36:50 |
| [pytorch](https://github.com/pytorch/pytorch) | 104687 | 32495 | 61721 | 138605 | 17663 | 2026-10-15 04:11:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 103099 | 10043 | 3556 | 6425 | 85 | 2026-10-14 20:38:38 |
| [django](https://github.com/django/django) | 91327 | 37271 | 0 | 22070 | 538 | 2026-10-15 01:12:00 |
| [cpython](https://github.com/python/cpython) | 77554 | 38374 | 78709 | 78362 | 9753 | 2026-10-15 04:17:52 |
| [flask](https://github.com/pallets/flask) | 74898 | 17078 | 2770 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67606 | 27529 | 12326 | 21622 | 2154 | 2026-10-14 13:00:44 |
| [keras](https://github.com/keras-team/keras) | 64372 | 19798 | 13009 | 10075 | 227 | 2026-10-15 03:15:12 |
| [pandas](https://github.com/pandas-dev/pandas) | 50041 | 20521 | 28608 | 39461 | 2231 | 2026-10-15 02:32:56 |
| [ray](https://github.com/ray-project/ray) | 44029 | 8149 | 23176 | 43431 | 3584 | 2026-10-15 02:51:12 |
| [gym](https://github.com/openai/gym) | 37242 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33962 | 4733 | 5776 | 4129 | 250 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33004 | 12916 | 14130 | 18814 | 2244 | 2026-10-15 03:35:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30208 | 7094 | 3966 | 5093 | 57 | 2026-10-14 22:32:27 |
| [celery](https://github.com/celery/celery) | 28980 | 5220 | 5333 | 4566 | 721 | 2026-10-15 04:17:17 |
| [dash](https://github.com/plotly/dash) | 24450 | 2329 | 2167 | 1771 | 434 | 2026-10-14 21:43:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23369 | 8513 | 11437 | 20974 | 1492 | 2026-10-15 02:09:03 |
| [RustPython](https://github.com/RustPython/RustPython) | 22390 | 1501 | 1438 | 7590 | 292 | 2026-10-15 01:31:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5579 | 1889 | 1898 | 228 | 2026-10-15 01:41:28 |
| [micropython](https://github.com/micropython/micropython) | 22127 | 9003 | 6142 | 8135 | 1532 | 2026-10-15 03:42:53 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18840 | 2872 | 3391 | 2229 | 731 | 2026-10-14 18:56:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1610 | 1471 | 1686 | 158 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16574 | 2458 | 3264 | 10431 | 232 | 2026-10-14 17:38:00 |
| [httpx](https://github.com/encode/httpx) | 15602 | 4062 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15112 | 6013 | 11696 | 14687 | 1876 | 2026-10-14 18:30:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14069 | 2149 | 2663 | 1239 | 249 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1982 | 5568 | 6759 | 1366 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12665 | 1377 | 787 | 2211 | 54 | 2026-10-13 07:53:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12243 | 1816 | 8341 | 1226 | 216 | 2026-10-14 13:32:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11912 | 615 | 426 | 339 | 169 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1039 | 1147 | 1546 | 157 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9211 | 618 | 1050 | 563 | 225 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8795 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7347 | 453 | 903 | 2633 | 334 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6876 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5635 | 530 | 1277 | 933 | 536 | 2026-10-14 05:48:41 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5426 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4448 | 384 | 1206 | 254 | 122 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4101 | 894 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 272 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1358 | 269 | 2026-10-13 23:26:13 |
| [anyio](https://github.com/agronholm/anyio) | 2557 | 313 | 489 | 850 | 135 | 2026-10-14 23:01:05 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1813 | 129 | 5281 | 352 | 712 | 2026-10-15 04:02:54 |
| [jython](https://github.com/jython/jython) | 1547 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-15T04:19:42*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
