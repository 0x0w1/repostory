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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193718 | 75228 | 41158 | 67186 | 3558 | 2026-02-15 01:49:34 |
| [transformers](https://github.com/huggingface/transformers) | 156472 | 32072 | 18579 | 24822 | 2243 | 2026-02-14 15:01:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 97414 | 26859 | 56804 | 117725 | 18006 | 2026-02-15 02:22:09 |
| [fastapi](https://github.com/fastapi/fastapi) | 95100 | 8688 | 3503 | 5298 | 158 | 2026-02-14 08:57:26 |
| [django](https://github.com/django/django) | 86763 | 33641 | 0 | 20642 | 408 | 2026-02-13 21:58:37 |
| [cpython](https://github.com/python/cpython) | 71495 | 34077 | 75249 | 68584 | 9216 | 2026-02-15 03:06:51 |
| [flask](https://github.com/pallets/flask) | 71157 | 16710 | 2717 | 2769 | 3 | 2026-02-12 21:59:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65022 | 26693 | 11937 | 20204 | 2131 | 2026-02-14 17:48:31 |
| [keras](https://github.com/keras-team/keras) | 63757 | 19694 | 12633 | 8754 | 288 | 2026-02-14 01:20:52 |
| [pandas](https://github.com/pandas-dev/pandas) | 47882 | 19655 | 28097 | 35991 | 3656 | 2026-02-13 17:24:03 |
| [ray](https://github.com/ray-project/ray) | 41260 | 7217 | 22325 | 38392 | 3360 | 2026-02-15 01:32:47 |
| [gym](https://github.com/openai/gym) | 37034 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33204 | 4637 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31440 | 12055 | 13793 | 16977 | 2318 | 2026-02-13 19:46:10 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29872 | 7068 | 3946 | 4922 | 89 | 2026-02-11 20:55:01 |
| [celery](https://github.com/celery/celery) | 28014 | 4948 | 5195 | 3802 | 775 | 2026-02-14 07:53:28 |
| [dash](https://github.com/plotly/dash) | 24476 | 2255 | 2054 | 1437 | 560 | 2026-02-14 03:49:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22441 | 5547 | 1863 | 1699 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22411 | 8189 | 11153 | 19962 | 1539 | 2026-02-14 16:01:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 21784 | 1399 | 1300 | 5782 | 378 | 2026-02-15 00:05:42 |
| [micropython](https://github.com/micropython/micropython) | 21464 | 8708 | 5954 | 7559 | 1849 | 2026-02-14 08:06:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1585 | 1464 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18250 | 2775 | 3322 | 2034 | 780 | 2026-02-13 17:34:52 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16259 | 2190 | 3177 | 8583 | 290 | 2026-02-15 02:27:28 |
| [httpx](https://github.com/encode/httpx) | 14992 | 1034 | 925 | 1790 | 135 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14452 | 5617 | 11306 | 13270 | 1768 | 2026-02-13 12:41:05 |
| [dask](https://github.com/dask/dask) | 13743 | 1843 | 5504 | 6488 | 1224 | 2026-02-13 08:33:06 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13726 | 2079 | 2646 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11923 | 1116 | 763 | 1796 | 44 | 2026-02-14 16:21:20 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11643 | 601 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11509 | 1638 | 8152 | 1031 | 208 | 2026-02-09 14:28:51 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 979 | 1119 | 1413 | 163 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8897 | 557 | 1010 | 484 | 209 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8753 | 1495 | 861 | 628 | 282 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7163 | 384 | 879 | 2500 | 314 | 2026-02-14 18:50:38 |
| [hug](https://github.com/hugapi/hug) | 6907 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5495 | 460 | 1229 | 775 | 483 | 2026-02-14 07:45:37 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5183 | 999 | 903 | 289 | 193 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 891 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3953 | 311 | 1181 | 210 | 116 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3596 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2727 | 308 | 658 | 1272 | 310 | 2026-02-14 13:30:50 |
| [anyio](https://github.com/agronholm/anyio) | 2386 | 181 | 426 | 571 | 77 | 2026-02-15 00:48:12 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1936 | 367 | 1785 | 266 | 266 | 2026-02-09 18:28:59 |
| [pypy](https://github.com/pypy/pypy) | 1649 | 98 | 5176 | 179 | 758 | 2026-02-11 08:06:08 |
| [jython](https://github.com/jython/jython) | 1479 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-15T03:13:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
