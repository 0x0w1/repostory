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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192114 | 74914 | 40877 | 59707 | 1586 | 2025-10-21 01:56:51 |
| [transformers](https://github.com/huggingface/transformers) | 151372 | 30872 | 18078 | 23082 | 2064 | 2025-10-21 01:35:48 |
| [pytorch](https://github.com/pytorch/pytorch) | 94102 | 25616 | 54402 | 111072 | 16977 | 2025-10-21 01:59:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 90947 | 8075 | 3470 | 4786 | 200 | 2025-10-20 17:32:04 |
| [django](https://github.com/django/django) | 85480 | 33114 | 0 | 19911 | 344 | 2025-10-20 19:22:32 |
| [flask](https://github.com/pallets/flask) | 70603 | 16595 | 2699 | 2710 | 12 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69443 | 33156 | 74028 | 65432 | 9209 | 2025-10-20 23:54:45 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63742 | 26352 | 11773 | 19642 | 2145 | 2025-10-20 16:16:40 |
| [keras](https://github.com/keras-team/keras) | 63491 | 19626 | 12567 | 8407 | 258 | 2025-10-19 00:13:52 |
| [pandas](https://github.com/pandas-dev/pandas) | 46892 | 19158 | 27804 | 34913 | 3624 | 2025-10-20 22:24:31 |
| [ray](https://github.com/ray-project/ray) | 39400 | 6796 | 21617 | 35974 | 3198 | 2025-10-21 01:59:40 |
| [gym](https://github.com/openai/gym) | 36696 | 8708 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32677 | 4601 | 5727 | 4071 | 211 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30625 | 11594 | 13599 | 16370 | 2343 | 2025-10-21 00:11:51 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29586 | 7021 | 3945 | 4849 | 84 | 2025-10-20 17:52:44 |
| [celery](https://github.com/celery/celery) | 27384 | 4866 | 5174 | 3699 | 752 | 2025-10-20 13:13:23 |
| [dash](https://github.com/plotly/dash) | 24175 | 2221 | 2012 | 1354 | 578 | 2025-10-20 19:52:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22316 | 5534 | 1853 | 1674 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21854 | 8070 | 11014 | 19605 | 1630 | 2025-10-20 19:03:04 |
| [micropython](https://github.com/micropython/micropython) | 20969 | 8495 | 5852 | 7293 | 1778 | 2025-10-20 03:06:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 20666 | 1353 | 1223 | 4917 | 451 | 2025-10-21 00:33:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18526 | 1579 | 1450 | 1629 | 147 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17864 | 2731 | 3266 | 1966 | 726 | 2025-10-20 13:19:45 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16048 | 2138 | 3153 | 8243 | 259 | 2025-10-20 12:40:11 |
| [httpx](https://github.com/encode/httpx) | 14646 | 963 | 919 | 1746 | 101 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14106 | 5511 | 11088 | 12725 | 1786 | 2025-10-20 17:39:34 |
| [dask](https://github.com/dask/dask) | 13543 | 1808 | 5441 | 6366 | 1195 | 2025-10-15 06:34:30 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13509 | 2035 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11569 | 1047 | 755 | 1725 | 50 | 2025-10-19 09:58:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11355 | 579 | 396 | 296 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11029 | 1587 | 8103 | 994 | 218 | 2025-10-20 21:08:55 |
| [falcon](https://github.com/falconry/falcon) | 9739 | 968 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8676 | 1487 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8643 | 528 | 957 | 446 | 169 | 2025-10-19 18:27:37 |
| [trio](https://github.com/python-trio/trio) | 6908 | 369 | 872 | 2461 | 312 | 2025-10-20 23:42:03 |
| [hug](https://github.com/hugapi/hug) | 6901 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5338 | 439 | 1196 | 713 | 501 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5041 | 951 | 874 | 263 | 173 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4054 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3694 | 293 | 1163 | 196 | 118 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3505 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2697 | 303 | 652 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2317 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2257 | 166 | 408 | 530 | 72 | 2025-10-20 19:48:55 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 909 | 1077 | 1462 | 369 | 2025-10-14 17:45:08 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 369 | 1780 | 264 | 260 | 2025-10-20 20:06:23 |
| [pypy](https://github.com/pypy/pypy) | 1540 | 87 | 5153 | 171 | 740 | 2025-10-20 16:20:39 |
| [jython](https://github.com/jython/jython) | 1444 | 224 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-21T02:00:37*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
