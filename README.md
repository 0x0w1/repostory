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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192361 | 74975 | 40974 | 61001 | 2203 | 2025-11-09 00:20:37 |
| [transformers](https://github.com/huggingface/transformers) | 152271 | 31092 | 18157 | 23354 | 2123 | 2025-11-08 22:39:01 |
| [pytorch](https://github.com/pytorch/pytorch) | 94856 | 25835 | 54732 | 112201 | 17049 | 2025-11-09 02:06:39 |
| [fastapi](https://github.com/fastapi/fastapi) | 91680 | 8192 | 3476 | 4853 | 207 | 2025-11-08 21:47:46 |
| [django](https://github.com/django/django) | 85731 | 33218 | 0 | 20005 | 357 | 2025-11-07 21:41:57 |
| [flask](https://github.com/pallets/flask) | 70743 | 16621 | 2701 | 2721 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69752 | 33332 | 74277 | 66052 | 9245 | 2025-11-08 19:28:32 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63973 | 26422 | 11799 | 19744 | 2125 | 2025-11-08 09:42:35 |
| [keras](https://github.com/keras-team/keras) | 63554 | 19655 | 12588 | 8457 | 266 | 2025-11-07 22:14:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 47051 | 19263 | 27864 | 35132 | 3591 | 2025-11-08 20:40:33 |
| [ray](https://github.com/ray-project/ray) | 39723 | 6876 | 21786 | 36344 | 3203 | 2025-11-09 00:39:30 |
| [gym](https://github.com/openai/gym) | 36752 | 8711 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32780 | 4618 | 5729 | 4072 | 196 | 2025-11-06 10:03:30 |
| [numpy](https://github.com/numpy/numpy) | 30775 | 11670 | 13639 | 16477 | 2355 | 2025-11-07 19:50:59 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29650 | 7030 | 3946 | 4863 | 83 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27511 | 4891 | 5175 | 3716 | 750 | 2025-11-01 23:53:30 |
| [dash](https://github.com/plotly/dash) | 24234 | 2227 | 2019 | 1360 | 580 | 2025-11-07 21:45:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22337 | 5542 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21955 | 8107 | 11034 | 19654 | 1616 | 2025-11-06 19:49:39 |
| [micropython](https://github.com/micropython/micropython) | 21065 | 8518 | 5868 | 7332 | 1793 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20771 | 1358 | 1226 | 4950 | 447 | 2025-11-04 18:14:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18550 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17933 | 2742 | 3289 | 1975 | 750 | 2025-11-07 19:19:37 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16071 | 2154 | 3160 | 8287 | 270 | 2025-11-06 11:01:47 |
| [httpx](https://github.com/encode/httpx) | 14719 | 975 | 920 | 1754 | 109 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14173 | 5535 | 11124 | 12809 | 1800 | 2025-11-08 04:09:24 |
| [dask](https://github.com/dask/dask) | 13582 | 1819 | 5453 | 6393 | 1194 | 2025-11-07 10:56:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13548 | 2040 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11633 | 1075 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11404 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11101 | 1596 | 8116 | 1000 | 219 | 2025-11-08 19:58:18 |
| [falcon](https://github.com/falconry/falcon) | 9751 | 974 | 1110 | 1397 | 168 | 2025-11-08 12:29:30 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8694 | 535 | 965 | 452 | 176 | 2025-11-03 10:41:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6941 | 371 | 872 | 2466 | 311 | 2025-11-03 23:11:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5366 | 443 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5073 | 959 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4060 | 888 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3745 | 299 | 1166 | 199 | 116 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3525 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2703 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2284 | 174 | 412 | 542 | 71 | 2025-11-07 13:52:43 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 370 | 1781 | 264 | 260 | 2025-11-03 17:44:55 |
| [pypy](https://github.com/pypy/pypy) | 1562 | 89 | 5158 | 171 | 745 | 2025-10-28 13:51:47 |
| [jython](https://github.com/jython/jython) | 1454 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-09T02:07:45*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
