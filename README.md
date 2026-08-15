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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197024 | 76027 | 41681 | 80111 | 2852 | 2026-08-15 01:38:28 |
| [transformers](https://github.com/huggingface/transformers) | 164084 | 34242 | 19310 | 27932 | 2381 | 2026-08-14 22:31:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 102379 | 28871 | 60338 | 132657 | 17307 | 2026-08-15 01:41:24 |
| [fastapi](https://github.com/fastapi/fastapi) | 101597 | 9781 | 3544 | 6229 | 73 | 2026-08-14 13:05:49 |
| [django](https://github.com/django/django) | 88427 | 34133 | 0 | 21669 | 458 | 2026-08-14 21:35:51 |
| [cpython](https://github.com/python/cpython) | 74321 | 35203 | 77668 | 75798 | 9485 | 2026-08-14 23:55:35 |
| [flask](https://github.com/pallets/flask) | 72162 | 16936 | 2762 | 2892 | 3 | 2026-08-11 22:32:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66952 | 27281 | 12243 | 21316 | 2125 | 2026-08-13 22:04:45 |
| [keras](https://github.com/keras-team/keras) | 64228 | 19747 | 12868 | 9703 | 216 | 2026-08-14 17:42:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 49498 | 20264 | 28476 | 38181 | 2847 | 2026-08-14 22:22:19 |
| [ray](https://github.com/ray-project/ray) | 43513 | 7923 | 22946 | 42143 | 3471 | 2026-08-15 00:09:48 |
| [gym](https://github.com/openai/gym) | 37240 | 8685 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33821 | 4709 | 5770 | 4110 | 232 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32543 | 12631 | 14047 | 18157 | 2327 | 2026-08-14 23:22:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30131 | 7076 | 3966 | 5044 | 56 | 2026-08-12 11:26:08 |
| [celery](https://github.com/celery/celery) | 28784 | 5134 | 5294 | 4236 | 804 | 2026-08-14 17:52:08 |
| [dash](https://github.com/plotly/dash) | 24378 | 2313 | 2143 | 1679 | 538 | 2026-08-13 15:02:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23080 | 8435 | 11394 | 20749 | 1474 | 2026-08-14 19:17:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22279 | 1473 | 1421 | 7034 | 408 | 2026-08-14 19:40:53 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5550 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21990 | 8929 | 6117 | 8046 | 1532 | 2026-08-14 03:00:27 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18738 | 2832 | 3376 | 2137 | 775 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18646 | 1597 | 1471 | 1702 | 145 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16526 | 2372 | 3236 | 9833 | 235 | 2026-08-15 00:46:05 |
| [httpx](https://github.com/encode/httpx) | 15422 | 1245 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14921 | 5863 | 11593 | 14308 | 1849 | 2026-08-15 00:43:46 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14001 | 2126 | 2658 | 1212 | 227 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13888 | 1927 | 5548 | 6693 | 1302 | 2026-08-10 22:03:29 |
| [starlette](https://github.com/Kludex/starlette) | 12544 | 1258 | 773 | 2027 | 63 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12082 | 1750 | 8266 | 1180 | 211 | 2026-08-14 13:03:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11884 | 612 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 1026 | 1139 | 1499 | 160 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 607 | 1042 | 532 | 230 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8775 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 415 | 899 | 2589 | 322 | 2026-08-11 00:45:57 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 500 | 1265 | 886 | 539 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5349 | 1033 | 929 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4320 | 363 | 1197 | 244 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3997 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3657 | 204 | 284 | 135 | 37 | 2026-08-14 14:43:56 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2525 | 244 | 469 | 734 | 106 | 2026-08-14 07:04:46 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 915 | 1084 | 1584 | 356 | 2026-08-14 23:59:43 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-10 17:58:57 |
| [pypy](https://github.com/pypy/pypy) | 1782 | 121 | 5247 | 290 | 731 | 2026-08-14 07:51:21 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 300 | 150 | 98 | 2026-08-10 15:30:18 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-15T01:41:37*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
