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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191749 | 74863 | 40807 | 58007 | 1739 | 2025-09-23 01:21:14 |
| [transformers](https://github.com/huggingface/transformers) | 150105 | 30485 | 17961 | 22537 | 1991 | 2025-09-22 17:36:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 93371 | 25368 | 53886 | 109254 | 17153 | 2025-09-23 01:47:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 89709 | 7911 | 3468 | 4720 | 211 | 2025-09-22 19:30:48 |
| [django](https://github.com/django/django) | 85086 | 32995 | 0 | 19829 | 356 | 2025-09-23 01:53:22 |
| [flask](https://github.com/pallets/flask) | 70414 | 16545 | 2697 | 2703 | 8 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 68988 | 32922 | 73680 | 64646 | 9290 | 2025-09-22 21:46:19 |
| [keras](https://github.com/keras-team/keras) | 63421 | 19629 | 12551 | 8349 | 258 | 2025-09-22 16:11:02 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63420 | 26268 | 11721 | 19403 | 2189 | 2025-09-22 12:35:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 46634 | 18995 | 27722 | 34646 | 3645 | 2025-09-22 23:37:03 |
| [ray](https://github.com/ray-project/ray) | 39044 | 6818 | 21201 | 35266 | 3095 | 2025-09-23 01:53:19 |
| [gym](https://github.com/openai/gym) | 36569 | 8698 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32511 | 4578 | 5722 | 4068 | 204 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30433 | 11450 | 13547 | 16180 | 2358 | 2025-09-23 00:11:27 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29486 | 7009 | 3945 | 4839 | 104 | 2025-09-20 10:19:28 |
| [celery](https://github.com/celery/celery) | 27239 | 4849 | 5164 | 3662 | 751 | 2025-09-22 16:49:44 |
| [dash](https://github.com/plotly/dash) | 24083 | 2205 | 1997 | 1333 | 564 | 2025-09-23 00:45:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22212 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21718 | 8035 | 10991 | 19559 | 1626 | 2025-09-22 19:03:57 |
| [micropython](https://github.com/micropython/micropython) | 20865 | 8447 | 5822 | 7205 | 1794 | 2025-09-22 00:56:05 |
| [RustPython](https://github.com/RustPython/RustPython) | 20539 | 1349 | 1220 | 4889 | 445 | 2025-09-22 13:05:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18492 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17760 | 2717 | 3251 | 1953 | 722 | 2025-09-19 15:28:16 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16000 | 2125 | 3146 | 8090 | 272 | 2025-09-22 16:25:45 |
| [httpx](https://github.com/encode/httpx) | 14573 | 955 | 918 | 1731 | 98 | 2025-09-20 17:09:10 |
| [scipy](https://github.com/scipy/scipy) | 14042 | 5483 | 11037 | 12607 | 1757 | 2025-09-22 14:50:18 |
| [dask](https://github.com/dask/dask) | 13492 | 1797 | 5437 | 6346 | 1199 | 2025-09-16 14:21:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13450 | 2036 | 2627 | 1148 | 188 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11487 | 1044 | 754 | 1712 | 46 | 2025-09-20 21:43:28 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11273 | 574 | 388 | 289 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10929 | 1581 | 8088 | 982 | 226 | 2025-09-21 16:15:02 |
| [falcon](https://github.com/falconry/falcon) | 9722 | 959 | 1100 | 1370 | 156 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8664 | 1486 | 855 | 623 | 283 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8556 | 525 | 945 | 435 | 408 | 2025-09-21 09:38:28 |
| [hug](https://github.com/hugapi/hug) | 6895 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6865 | 366 | 869 | 2453 | 309 | 2025-09-22 22:36:12 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5297 | 438 | 1194 | 713 | 500 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5008 | 940 | 871 | 260 | 168 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 888 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3629 | 292 | 1158 | 196 | 117 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3465 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2687 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2308 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2216 | 163 | 401 | 512 | 64 | 2025-09-22 22:31:40 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1922 | 369 | 1780 | 264 | 261 | 2025-09-22 17:45:36 |
| [pypy](https://github.com/pypy/pypy) | 1501 | 86 | 5144 | 168 | 735 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1435 | 222 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-09-22 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-23T01:54:13*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
