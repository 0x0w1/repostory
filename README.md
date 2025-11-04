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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192300 | 74946 | 40900 | 60533 | 1933 | 2025-11-04 01:59:51 |
| [transformers](https://github.com/huggingface/transformers) | 152039 | 31030 | 18136 | 23267 | 2113 | 2025-11-03 23:46:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 94593 | 25762 | 54625 | 111813 | 17044 | 2025-11-04 01:58:33 |
| [fastapi](https://github.com/fastapi/fastapi) | 91483 | 8157 | 3474 | 4840 | 207 | 2025-11-03 17:40:31 |
| [django](https://github.com/django/django) | 85639 | 33190 | 0 | 19983 | 357 | 2025-11-04 01:45:49 |
| [flask](https://github.com/pallets/flask) | 70700 | 16606 | 2701 | 2717 | 17 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69651 | 33289 | 74223 | 65804 | 9220 | 2025-11-03 20:37:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63908 | 26395 | 11792 | 19718 | 2142 | 2025-11-03 13:26:31 |
| [keras](https://github.com/keras-team/keras) | 63540 | 19647 | 12585 | 8446 | 270 | 2025-11-03 23:11:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 47006 | 19234 | 27850 | 35071 | 3627 | 2025-11-03 22:12:12 |
| [ray](https://github.com/ray-project/ray) | 39654 | 6859 | 21761 | 36281 | 3194 | 2025-11-04 01:40:36 |
| [gym](https://github.com/openai/gym) | 36735 | 8713 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32756 | 4614 | 5729 | 4071 | 207 | 2025-10-28 08:43:48 |
| [numpy](https://github.com/numpy/numpy) | 30734 | 11651 | 13628 | 16448 | 2355 | 2025-11-03 00:59:23 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29634 | 7031 | 3946 | 4861 | 81 | 2025-11-03 10:09:41 |
| [celery](https://github.com/celery/celery) | 27476 | 4885 | 5175 | 3715 | 750 | 2025-11-01 23:53:30 |
| [dash](https://github.com/plotly/dash) | 24219 | 2227 | 2016 | 1357 | 579 | 2025-10-29 15:00:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22329 | 5539 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21921 | 8104 | 11030 | 19649 | 1620 | 2025-11-03 19:15:50 |
| [micropython](https://github.com/micropython/micropython) | 21027 | 8514 | 5864 | 7317 | 1784 | 2025-11-03 03:10:56 |
| [RustPython](https://github.com/RustPython/RustPython) | 20751 | 1356 | 1225 | 4945 | 444 | 2025-11-03 09:15:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18544 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17913 | 2740 | 3269 | 1972 | 730 | 2025-11-03 17:28:54 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16065 | 2152 | 3159 | 8280 | 263 | 2025-10-29 10:52:58 |
| [httpx](https://github.com/encode/httpx) | 14696 | 970 | 919 | 1752 | 107 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14150 | 5529 | 11114 | 12789 | 1789 | 2025-11-03 15:06:08 |
| [dask](https://github.com/dask/dask) | 13568 | 1817 | 5451 | 6381 | 1191 | 2025-11-03 17:27:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13535 | 2041 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11612 | 1068 | 758 | 1741 | 50 | 2025-11-02 22:17:44 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11386 | 583 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11081 | 1590 | 8114 | 997 | 218 | 2025-11-03 22:06:32 |
| [falcon](https://github.com/falconry/falcon) | 9749 | 971 | 1107 | 1390 | 167 | 2025-10-30 08:18:07 |
| [bottle](https://github.com/bottlepy/bottle) | 8687 | 1490 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8680 | 532 | 964 | 449 | 174 | 2025-11-03 10:41:32 |
| [trio](https://github.com/python-trio/trio) | 6928 | 371 | 872 | 2466 | 311 | 2025-11-03 23:11:41 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5359 | 442 | 1197 | 714 | 501 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5066 | 959 | 875 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4059 | 887 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3732 | 297 | 1163 | 198 | 115 | 2025-11-01 05:03:35 |
| [quart](https://github.com/pallets/quart) | 3513 | 191 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2701 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2316 | 133 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2272 | 172 | 411 | 541 | 72 | 2025-11-03 17:52:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 370 | 1781 | 264 | 261 | 2025-11-03 17:44:55 |
| [pypy](https://github.com/pypy/pypy) | 1556 | 87 | 5156 | 171 | 743 | 2025-10-28 13:51:47 |
| [jython](https://github.com/jython/jython) | 1452 | 225 | 284 | 114 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-04T02:03:04*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
