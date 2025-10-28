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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192232 | 74931 | 40886 | 59992 | 1658 | 2025-10-28 01:36:40 |
| [transformers](https://github.com/huggingface/transformers) | 151708 | 30965 | 18114 | 23195 | 2103 | 2025-10-27 21:57:44 |
| [pytorch](https://github.com/pytorch/pytorch) | 94298 | 25676 | 54501 | 111377 | 16987 | 2025-10-28 01:55:10 |
| [fastapi](https://github.com/fastapi/fastapi) | 91238 | 8129 | 3472 | 4807 | 203 | 2025-10-27 17:53:01 |
| [django](https://github.com/django/django) | 85574 | 33166 | 0 | 19945 | 355 | 2025-10-27 19:11:19 |
| [flask](https://github.com/pallets/flask) | 70668 | 16598 | 2700 | 2714 | 17 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69562 | 33238 | 74132 | 65620 | 9208 | 2025-10-27 23:49:11 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63824 | 26368 | 11783 | 19675 | 2158 | 2025-10-27 13:39:41 |
| [keras](https://github.com/keras-team/keras) | 63517 | 19637 | 12574 | 8428 | 263 | 2025-10-27 21:06:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 46948 | 19200 | 27829 | 35006 | 3637 | 2025-10-27 22:47:49 |
| [ray](https://github.com/ray-project/ray) | 39543 | 6833 | 21736 | 36149 | 3189 | 2025-10-28 01:11:53 |
| [gym](https://github.com/openai/gym) | 36713 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32720 | 4612 | 5728 | 4071 | 212 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30688 | 11631 | 13608 | 16411 | 2342 | 2025-10-27 23:16:46 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29619 | 7029 | 3945 | 4853 | 81 | 2025-10-27 16:45:11 |
| [celery](https://github.com/celery/celery) | 27423 | 4872 | 5174 | 3705 | 749 | 2025-10-27 23:08:52 |
| [dash](https://github.com/plotly/dash) | 24206 | 2225 | 2013 | 1355 | 576 | 2025-10-24 22:59:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22328 | 5537 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21884 | 8092 | 11021 | 19625 | 1628 | 2025-10-27 20:02:37 |
| [micropython](https://github.com/micropython/micropython) | 20993 | 8507 | 5859 | 7305 | 1777 | 2025-10-28 01:50:35 |
| [RustPython](https://github.com/RustPython/RustPython) | 20693 | 1356 | 1225 | 4934 | 443 | 2025-10-28 00:37:38 |
| [sanic](https://github.com/sanic-org/sanic) | 18533 | 1581 | 1450 | 1629 | 147 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17893 | 2734 | 3266 | 1966 | 725 | 2025-10-22 18:58:42 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16055 | 2145 | 3158 | 8266 | 269 | 2025-10-27 21:55:41 |
| [httpx](https://github.com/encode/httpx) | 14678 | 968 | 919 | 1749 | 104 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14125 | 5519 | 11099 | 12759 | 1788 | 2025-10-28 01:24:23 |
| [dask](https://github.com/dask/dask) | 13555 | 1816 | 5444 | 6372 | 1195 | 2025-10-27 22:44:24 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13520 | 2038 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11586 | 1053 | 755 | 1725 | 48 | 2025-10-26 16:30:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11374 | 582 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11054 | 1590 | 8107 | 995 | 217 | 2025-10-27 16:19:20 |
| [falcon](https://github.com/falconry/falcon) | 9743 | 970 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8681 | 1489 | 855 | 624 | 283 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8659 | 529 | 963 | 449 | 175 | 2025-10-23 07:16:59 |
| [trio](https://github.com/python-trio/trio) | 6918 | 372 | 872 | 2462 | 312 | 2025-10-24 13:13:16 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5349 | 442 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5056 | 955 | 874 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4058 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3716 | 295 | 1163 | 197 | 119 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3508 | 191 | 277 | 123 | 63 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2699 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2317 | 132 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2265 | 171 | 411 | 535 | 71 | 2025-10-27 17:43:04 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 370 | 1781 | 264 | 261 | 2025-10-27 17:37:16 |
| [pypy](https://github.com/pypy/pypy) | 1546 | 87 | 5153 | 171 | 740 | 2025-10-20 16:20:39 |
| [jython](https://github.com/jython/jython) | 1447 | 225 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-28T01:59:37*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
