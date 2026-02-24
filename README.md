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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193893 | 75227 | 41168 | 67638 | 3541 | 2026-02-24 02:39:44 |
| [transformers](https://github.com/huggingface/transformers) | 156866 | 32177 | 18614 | 25027 | 2284 | 2026-02-23 22:25:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 97701 | 26963 | 56914 | 118172 | 17977 | 2026-02-24 02:49:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 95499 | 8740 | 3503 | 5344 | 149 | 2026-02-23 23:31:56 |
| [django](https://github.com/django/django) | 86912 | 33680 | 0 | 20692 | 425 | 2026-02-23 18:14:03 |
| [cpython](https://github.com/python/cpython) | 71683 | 34123 | 75341 | 68823 | 9251 | 2026-02-24 01:18:32 |
| [flask](https://github.com/pallets/flask) | 71253 | 16731 | 2722 | 2779 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65208 | 26731 | 11965 | 20274 | 2146 | 2026-02-23 22:13:29 |
| [keras](https://github.com/keras-team/keras) | 63865 | 19704 | 12641 | 8827 | 285 | 2026-02-23 22:21:32 |
| [pandas](https://github.com/pandas-dev/pandas) | 47958 | 19695 | 28131 | 36088 | 3668 | 2026-02-23 18:33:25 |
| [ray](https://github.com/ray-project/ray) | 41444 | 7249 | 22361 | 38562 | 3412 | 2026-02-24 02:21:28 |
| [gym](https://github.com/openai/gym) | 37053 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33236 | 4638 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31497 | 12075 | 13799 | 17003 | 2313 | 2026-02-24 01:22:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29889 | 7067 | 3946 | 4927 | 83 | 2026-02-21 13:18:05 |
| [celery](https://github.com/celery/celery) | 28139 | 4961 | 5196 | 3820 | 774 | 2026-02-23 18:02:54 |
| [dash](https://github.com/plotly/dash) | 24513 | 2257 | 2061 | 1442 | 566 | 2026-02-23 19:09:28 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22485 | 8217 | 11161 | 19983 | 1542 | 2026-02-23 21:41:41 |
| [tornado](https://github.com/tornadoweb/tornado) | 22443 | 5547 | 1863 | 1702 | 216 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21815 | 1402 | 1304 | 5844 | 380 | 2026-02-24 01:14:37 |
| [micropython](https://github.com/micropython/micropython) | 21483 | 8722 | 5962 | 7583 | 1854 | 2026-02-23 02:35:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1464 | 1671 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18279 | 2777 | 3324 | 2045 | 781 | 2026-02-23 20:39:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16362 | 2202 | 3178 | 8648 | 269 | 2026-02-23 17:21:46 |
| [httpx](https://github.com/encode/httpx) | 15099 | 1043 | 925 | 1799 | 142 | 2026-02-23 10:40:42 |
| [scipy](https://github.com/scipy/scipy) | 14478 | 5624 | 11324 | 13324 | 1771 | 2026-02-23 23:35:31 |
| [dask](https://github.com/dask/dask) | 13746 | 1847 | 5508 | 6498 | 1232 | 2026-02-22 23:28:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13741 | 2080 | 2647 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11954 | 1119 | 763 | 1809 | 46 | 2026-02-23 22:17:04 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11656 | 602 | 403 | 314 | 151 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11626 | 1641 | 8158 | 1035 | 212 | 2026-02-23 22:56:50 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 980 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8917 | 558 | 1016 | 487 | 218 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8760 | 1497 | 861 | 630 | 283 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7175 | 387 | 880 | 2507 | 316 | 2026-02-23 22:21:21 |
| [hug](https://github.com/hugapi/hug) | 6909 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6754 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5611 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5504 | 460 | 1232 | 779 | 484 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5193 | 1001 | 906 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 893 | 1063 | 2726 | 89 | 2026-02-24 01:22:36 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3972 | 317 | 1180 | 213 | 115 | 2026-02-23 22:58:28 |
| [quart](https://github.com/pallets/quart) | 3600 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2729 | 310 | 660 | 1280 | 308 | 2026-02-24 02:46:22 |
| [anyio](https://github.com/agronholm/anyio) | 2397 | 183 | 426 | 577 | 81 | 2026-02-24 01:03:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 907 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-02-23 17:52:49 |
| [pypy](https://github.com/pypy/pypy) | 1656 | 99 | 5176 | 179 | 757 | 2026-02-19 08:17:00 |
| [jython](https://github.com/jython/jython) | 1485 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-24T02:50:20*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
