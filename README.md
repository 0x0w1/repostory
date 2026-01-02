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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193141 | 75154 | 41051 | 64180 | 2714 | 2026-01-01 19:04:40 |
| [transformers](https://github.com/huggingface/transformers) | 154499 | 31600 | 18384 | 24092 | 2170 | 2026-01-01 13:51:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 96270 | 26408 | 56106 | 114996 | 17907 | 2026-01-02 02:21:29 |
| [fastapi](https://github.com/fastapi/fastapi) | 93632 | 8452 | 3499 | 5065 | 204 | 2026-01-01 12:15:06 |
| [django](https://github.com/django/django) | 86331 | 33425 | 0 | 20419 | 372 | 2025-12-31 15:48:14 |
| [flask](https://github.com/pallets/flask) | 71001 | 16666 | 2707 | 2744 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70559 | 33788 | 74856 | 67506 | 9245 | 2026-01-01 21:10:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64437 | 26552 | 11866 | 19981 | 2129 | 2026-01-01 14:10:28 |
| [keras](https://github.com/keras-team/keras) | 63681 | 19662 | 12607 | 8569 | 240 | 2026-01-01 11:04:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 47455 | 19468 | 27991 | 35478 | 3596 | 2026-01-01 19:33:34 |
| [ray](https://github.com/ray-project/ray) | 40570 | 7060 | 22089 | 37362 | 3271 | 2026-01-01 00:07:35 |
| [gym](https://github.com/openai/gym) | 36918 | 8717 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33019 | 4632 | 5736 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31125 | 11906 | 13723 | 16772 | 2386 | 2026-01-02 01:26:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29775 | 7049 | 3946 | 4895 | 83 | 2025-12-23 11:29:00 |
| [celery](https://github.com/celery/celery) | 27808 | 4926 | 5180 | 3755 | 759 | 2025-12-29 21:48:53 |
| [dash](https://github.com/plotly/dash) | 24375 | 2245 | 2039 | 1400 | 557 | 2026-01-01 21:48:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22409 | 5545 | 1862 | 1690 | 210 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22174 | 8164 | 11095 | 19779 | 1543 | 2026-01-01 10:22:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 21591 | 1396 | 1271 | 5288 | 388 | 2026-01-01 23:29:42 |
| [micropython](https://github.com/micropython/micropython) | 21268 | 8616 | 5912 | 7463 | 1824 | 2025-12-30 13:40:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1585 | 1457 | 1661 | 107 | 2025-12-31 19:42:35 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18134 | 2768 | 3309 | 1996 | 760 | 2025-12-31 20:57:58 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16168 | 2171 | 3168 | 8409 | 266 | 2026-01-02 01:50:41 |
| [httpx](https://github.com/encode/httpx) | 14874 | 1000 | 925 | 1774 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14302 | 5570 | 11219 | 13028 | 1758 | 2026-01-01 18:17:37 |
| [dask](https://github.com/dask/dask) | 13681 | 1831 | 5481 | 6437 | 1208 | 2026-01-01 16:30:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13650 | 2072 | 2643 | 1154 | 201 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11808 | 1095 | 760 | 1757 | 54 | 2026-01-01 19:01:22 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11557 | 596 | 400 | 301 | 154 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11335 | 1612 | 8134 | 1017 | 209 | 2026-01-01 22:42:43 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 974 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8823 | 550 | 987 | 476 | 192 | 2026-01-01 20:11:23 |
| [bottle](https://github.com/bottlepy/bottle) | 8719 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7086 | 376 | 877 | 2484 | 313 | 2026-01-01 00:06:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5430 | 444 | 1213 | 734 | 511 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5130 | 980 | 883 | 274 | 179 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4070 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3861 | 305 | 1172 | 207 | 119 | 2025-12-26 20:05:52 |
| [quart](https://github.com/pallets/quart) | 3569 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2721 | 307 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2343 | 181 | 421 | 562 | 75 | 2025-12-31 01:53:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1618 | 93 | 5169 | 173 | 754 | 2025-12-28 21:26:02 |
| [jython](https://github.com/jython/jython) | 1464 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-02T02:21:42*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
