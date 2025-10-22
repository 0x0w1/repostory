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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192128 | 74912 | 40877 | 59769 | 1591 | 2025-10-22 01:39:48 |
| [transformers](https://github.com/huggingface/transformers) | 151422 | 30886 | 18081 | 23097 | 2060 | 2025-10-22 00:23:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 94137 | 25628 | 54425 | 111141 | 16977 | 2025-10-22 02:02:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 90993 | 8078 | 3470 | 4790 | 195 | 2025-10-21 20:32:58 |
| [django](https://github.com/django/django) | 85489 | 33119 | 0 | 19919 | 348 | 2025-10-21 14:46:56 |
| [flask](https://github.com/pallets/flask) | 70610 | 16593 | 2699 | 2710 | 12 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69462 | 33166 | 74042 | 65466 | 9210 | 2025-10-22 01:07:33 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63755 | 26354 | 11773 | 19644 | 2142 | 2025-10-21 16:22:25 |
| [keras](https://github.com/keras-team/keras) | 63495 | 19624 | 12567 | 8407 | 256 | 2025-10-21 05:42:17 |
| [pandas](https://github.com/pandas-dev/pandas) | 46895 | 19164 | 27807 | 34918 | 3625 | 2025-10-21 19:53:26 |
| [ray](https://github.com/ray-project/ray) | 39412 | 6801 | 21625 | 36008 | 3182 | 2025-10-22 01:52:32 |
| [gym](https://github.com/openai/gym) | 36701 | 8709 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32681 | 4602 | 5727 | 4071 | 211 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30632 | 11604 | 13601 | 16380 | 2342 | 2025-10-22 00:01:29 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29591 | 7022 | 3945 | 4851 | 84 | 2025-10-21 13:20:14 |
| [celery](https://github.com/celery/celery) | 27390 | 4868 | 5174 | 3700 | 753 | 2025-10-21 22:09:34 |
| [dash](https://github.com/plotly/dash) | 24183 | 2222 | 2012 | 1355 | 577 | 2025-10-21 19:44:08 |
| [tornado](https://github.com/tornadoweb/tornado) | 22318 | 5534 | 1853 | 1674 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21860 | 8074 | 11015 | 19607 | 1625 | 2025-10-21 22:53:54 |
| [micropython](https://github.com/micropython/micropython) | 20975 | 8496 | 5854 | 7294 | 1779 | 2025-10-21 23:46:44 |
| [RustPython](https://github.com/RustPython/RustPython) | 20672 | 1354 | 1223 | 4917 | 448 | 2025-10-21 03:14:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18528 | 1580 | 1450 | 1629 | 147 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17869 | 2731 | 3266 | 1966 | 726 | 2025-10-20 13:19:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16048 | 2137 | 3155 | 8246 | 262 | 2025-10-21 10:47:17 |
| [httpx](https://github.com/encode/httpx) | 14654 | 963 | 919 | 1746 | 101 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14112 | 5513 | 11090 | 12730 | 1789 | 2025-10-21 23:59:22 |
| [dask](https://github.com/dask/dask) | 13546 | 1808 | 5441 | 6367 | 1192 | 2025-10-21 14:57:49 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13510 | 2035 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11572 | 1047 | 755 | 1725 | 49 | 2025-10-21 19:01:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11357 | 579 | 396 | 296 | 146 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11034 | 1586 | 8105 | 994 | 219 | 2025-10-21 21:49:39 |
| [falcon](https://github.com/falconry/falcon) | 9739 | 968 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8678 | 1487 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8647 | 528 | 958 | 447 | 170 | 2025-10-21 12:10:07 |
| [trio](https://github.com/python-trio/trio) | 6908 | 370 | 872 | 2461 | 312 | 2025-10-20 23:42:03 |
| [hug](https://github.com/hugapi/hug) | 6901 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5339 | 439 | 1196 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5044 | 951 | 874 | 263 | 173 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4054 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3699 | 294 | 1163 | 196 | 118 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3506 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2697 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2317 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2257 | 166 | 408 | 531 | 71 | 2025-10-21 15:35:25 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 909 | 1077 | 1462 | 369 | 2025-10-14 17:45:08 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 369 | 1780 | 264 | 260 | 2025-10-20 20:06:23 |
| [pypy](https://github.com/pypy/pypy) | 1545 | 86 | 5153 | 171 | 740 | 2025-10-20 16:20:39 |
| [jython](https://github.com/jython/jython) | 1445 | 224 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-22T02:03:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
