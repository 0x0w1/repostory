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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193088 | 75157 | 41051 | 64005 | 2587 | 2025-12-28 22:07:13 |
| [transformers](https://github.com/huggingface/transformers) | 154352 | 31566 | 18376 | 24082 | 2163 | 2025-12-24 15:30:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 96189 | 26376 | 56067 | 114873 | 17954 | 2025-12-29 02:26:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 93508 | 8438 | 3499 | 5054 | 197 | 2025-12-27 19:06:15 |
| [django](https://github.com/django/django) | 86278 | 33424 | 0 | 20408 | 374 | 2025-12-28 18:21:49 |
| [flask](https://github.com/pallets/flask) | 70982 | 16669 | 2707 | 2740 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70498 | 33764 | 74835 | 67451 | 9253 | 2025-12-28 22:12:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64399 | 26545 | 11865 | 19961 | 2128 | 2025-12-26 10:37:09 |
| [keras](https://github.com/keras-team/keras) | 63665 | 19663 | 12607 | 8561 | 245 | 2025-12-26 18:16:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 47431 | 19444 | 27986 | 35448 | 3612 | 2025-12-26 18:44:46 |
| [ray](https://github.com/ray-project/ray) | 40509 | 7051 | 22076 | 37310 | 3277 | 2025-12-28 10:35:23 |
| [gym](https://github.com/openai/gym) | 36911 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33004 | 4630 | 5736 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31099 | 11892 | 13719 | 16754 | 2383 | 2025-12-29 02:22:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29769 | 7045 | 3946 | 4892 | 80 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27787 | 4920 | 5178 | 3749 | 753 | 2025-12-22 17:26:19 |
| [dash](https://github.com/plotly/dash) | 24368 | 2246 | 2039 | 1395 | 553 | 2025-12-22 23:39:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22405 | 5545 | 1862 | 1690 | 210 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22165 | 8159 | 11092 | 19766 | 1541 | 2025-12-27 11:16:11 |
| [micropython](https://github.com/micropython/micropython) | 21263 | 8607 | 5907 | 7458 | 1817 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 21145 | 1377 | 1265 | 5240 | 398 | 2025-12-29 02:21:11 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1585 | 1457 | 1649 | 129 | 2025-12-28 17:39:38 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18126 | 2766 | 3309 | 1995 | 759 | 2025-12-24 16:24:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16163 | 2171 | 3168 | 8402 | 267 | 2025-12-27 22:50:38 |
| [httpx](https://github.com/encode/httpx) | 14872 | 999 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14292 | 5566 | 11215 | 13008 | 1774 | 2025-12-28 15:22:33 |
| [dask](https://github.com/dask/dask) | 13671 | 1829 | 5480 | 6429 | 1207 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13645 | 2071 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11791 | 1093 | 760 | 1750 | 53 | 2025-12-24 11:58:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11547 | 592 | 399 | 299 | 151 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11326 | 1610 | 8133 | 1017 | 209 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9776 | 975 | 1115 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8810 | 550 | 986 | 474 | 190 | 2025-12-26 14:55:26 |
| [bottle](https://github.com/bottlepy/bottle) | 8719 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7083 | 376 | 877 | 2483 | 314 | 2025-12-22 21:33:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 740 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5425 | 444 | 1212 | 734 | 512 | 2025-12-27 04:04:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5128 | 978 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4069 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4019 | 259 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3851 | 304 | 1172 | 206 | 118 | 2025-12-26 20:05:52 |
| [quart](https://github.com/pallets/quart) | 3567 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2339 | 181 | 421 | 562 | 75 | 2025-12-27 14:03:59 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2334 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1612 | 93 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1463 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-29T02:28:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
