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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192170 | 74920 | 40881 | 59866 | 1613 | 2025-10-24 01:41:19 |
| [transformers](https://github.com/huggingface/transformers) | 151526 | 30917 | 18093 | 23146 | 2080 | 2025-10-23 23:09:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 94201 | 25657 | 54457 | 111213 | 16994 | 2025-10-24 01:51:50 |
| [fastapi](https://github.com/fastapi/fastapi) | 91083 | 8101 | 3471 | 4794 | 197 | 2025-10-23 20:55:59 |
| [django](https://github.com/django/django) | 85516 | 33138 | 0 | 19932 | 351 | 2025-10-23 14:14:53 |
| [flask](https://github.com/pallets/flask) | 70639 | 16593 | 2699 | 2714 | 16 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69492 | 33186 | 74081 | 65505 | 9210 | 2025-10-23 23:38:02 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63777 | 26358 | 11777 | 19651 | 2145 | 2025-10-23 15:50:47 |
| [keras](https://github.com/keras-team/keras) | 63502 | 19629 | 12570 | 8414 | 262 | 2025-10-24 00:01:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 46914 | 19177 | 27814 | 34945 | 3631 | 2025-10-23 20:40:24 |
| [ray](https://github.com/ray-project/ray) | 39457 | 6818 | 21645 | 36080 | 3174 | 2025-10-24 01:30:50 |
| [gym](https://github.com/openai/gym) | 36710 | 8711 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32691 | 4607 | 5727 | 4071 | 211 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30652 | 11618 | 13605 | 16398 | 2341 | 2025-10-24 01:14:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29596 | 7024 | 3945 | 4852 | 84 | 2025-10-22 12:47:30 |
| [celery](https://github.com/celery/celery) | 27402 | 4867 | 5174 | 3700 | 753 | 2025-10-23 12:38:38 |
| [dash](https://github.com/plotly/dash) | 24192 | 2221 | 2012 | 1355 | 577 | 2025-10-23 15:32:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22320 | 5535 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21865 | 8082 | 11018 | 19614 | 1625 | 2025-10-23 19:34:39 |
| [micropython](https://github.com/micropython/micropython) | 20987 | 8500 | 5856 | 7296 | 1775 | 2025-10-23 05:32:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 20678 | 1354 | 1224 | 4925 | 443 | 2025-10-23 10:53:58 |
| [sanic](https://github.com/sanic-org/sanic) | 18530 | 1580 | 1450 | 1629 | 147 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17882 | 2733 | 3266 | 1966 | 725 | 2025-10-22 18:58:42 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16052 | 2140 | 3156 | 8248 | 263 | 2025-10-22 10:52:09 |
| [httpx](https://github.com/encode/httpx) | 14663 | 964 | 919 | 1746 | 101 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14117 | 5514 | 11093 | 12740 | 1792 | 2025-10-24 00:12:21 |
| [dask](https://github.com/dask/dask) | 13553 | 1808 | 5441 | 6368 | 1192 | 2025-10-22 11:17:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13514 | 2037 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11578 | 1048 | 755 | 1725 | 49 | 2025-10-21 19:01:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11364 | 580 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11041 | 1588 | 8106 | 994 | 219 | 2025-10-21 21:49:39 |
| [falcon](https://github.com/falconry/falcon) | 9740 | 969 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8679 | 1488 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8653 | 528 | 959 | 447 | 169 | 2025-10-23 07:16:59 |
| [trio](https://github.com/python-trio/trio) | 6912 | 371 | 872 | 2461 | 312 | 2025-10-20 23:42:03 |
| [hug](https://github.com/hugapi/hug) | 6902 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5343 | 440 | 1196 | 714 | 501 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5051 | 950 | 874 | 263 | 172 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4054 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3706 | 294 | 1163 | 196 | 118 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3505 | 190 | 277 | 123 | 63 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2698 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2317 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2261 | 167 | 408 | 532 | 70 | 2025-10-23 11:39:59 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 909 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 369 | 1780 | 264 | 260 | 2025-10-20 20:06:23 |
| [pypy](https://github.com/pypy/pypy) | 1544 | 86 | 5153 | 171 | 740 | 2025-10-20 16:20:39 |
| [jython](https://github.com/jython/jython) | 1447 | 225 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-24T01:55:07*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
