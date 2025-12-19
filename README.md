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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192859 | 75148 | 41046 | 63537 | 2583 | 2025-12-19 02:10:56 |
| [transformers](https://github.com/huggingface/transformers) | 154030 | 31482 | 18348 | 23999 | 2136 | 2025-12-19 00:45:53 |
| [pytorch](https://github.com/pytorch/pytorch) | 95998 | 26282 | 55943 | 114401 | 17902 | 2025-12-19 02:10:13 |
| [fastapi](https://github.com/fastapi/fastapi) | 93221 | 8386 | 3499 | 5014 | 194 | 2025-12-18 13:24:48 |
| [django](https://github.com/django/django) | 86189 | 33429 | 0 | 20363 | 372 | 2025-12-18 22:53:24 |
| [flask](https://github.com/pallets/flask) | 70938 | 16665 | 2706 | 2736 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70375 | 33703 | 74739 | 67247 | 9237 | 2025-12-18 21:29:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64322 | 26509 | 11853 | 19932 | 2127 | 2025-12-18 23:08:39 |
| [keras](https://github.com/keras-team/keras) | 63649 | 19654 | 12605 | 8543 | 245 | 2025-12-19 02:08:41 |
| [pandas](https://github.com/pandas-dev/pandas) | 47342 | 19418 | 27969 | 35389 | 3602 | 2025-12-18 23:18:28 |
| [ray](https://github.com/ray-project/ray) | 40389 | 7018 | 22030 | 37183 | 3197 | 2025-12-19 01:54:08 |
| [gym](https://github.com/openai/gym) | 36871 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32967 | 4634 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31038 | 11859 | 13703 | 16707 | 2387 | 2025-12-18 22:53:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29750 | 7043 | 3946 | 4888 | 79 | 2025-12-15 16:01:56 |
| [celery](https://github.com/celery/celery) | 27732 | 4916 | 5179 | 3745 | 752 | 2025-12-18 05:06:57 |
| [dash](https://github.com/plotly/dash) | 24347 | 2248 | 2039 | 1395 | 553 | 2025-12-18 16:31:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22390 | 5543 | 1861 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22136 | 8144 | 11085 | 19751 | 1554 | 2025-12-18 20:54:13 |
| [micropython](https://github.com/micropython/micropython) | 21232 | 8593 | 5902 | 7448 | 1813 | 2025-12-18 01:05:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 20924 | 1372 | 1247 | 5145 | 436 | 2025-12-18 15:49:02 |
| [sanic](https://github.com/sanic-org/sanic) | 18601 | 1586 | 1456 | 1636 | 130 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18100 | 2761 | 3308 | 1992 | 756 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16151 | 2166 | 3167 | 8386 | 274 | 2025-12-17 10:49:52 |
| [httpx](https://github.com/encode/httpx) | 14847 | 994 | 925 | 1771 | 120 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14266 | 5559 | 11194 | 12977 | 1770 | 2025-12-19 00:31:09 |
| [dask](https://github.com/dask/dask) | 13657 | 1826 | 5479 | 6426 | 1204 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13623 | 2069 | 2641 | 1150 | 200 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11769 | 1093 | 760 | 1748 | 53 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11527 | 591 | 398 | 299 | 150 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11283 | 1607 | 8131 | 1015 | 210 | 2025-12-18 20:24:03 |
| [falcon](https://github.com/falconry/falcon) | 9770 | 974 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8791 | 550 | 984 | 474 | 191 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8713 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7055 | 373 | 877 | 2482 | 314 | 2025-12-15 22:18:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 741 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5416 | 444 | 1209 | 731 | 511 | 2025-12-17 09:19:42 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5113 | 974 | 882 | 271 | 175 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 889 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4018 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3824 | 303 | 1169 | 203 | 118 | 2025-12-18 06:57:55 |
| [quart](https://github.com/pallets/quart) | 3562 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2333 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2327 | 180 | 420 | 560 | 75 | 2025-12-17 13:22:00 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-15 17:49:12 |
| [pypy](https://github.com/pypy/pypy) | 1607 | 92 | 5167 | 172 | 751 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1463 | 225 | 288 | 118 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-19T02:11:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
