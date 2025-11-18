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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192469 | 74995 | 40998 | 61579 | 2439 | 2025-11-18 02:03:50 |
| [transformers](https://github.com/huggingface/transformers) | 152638 | 31159 | 18198 | 23450 | 2124 | 2025-11-18 00:24:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 95155 | 25932 | 54919 | 112651 | 17119 | 2025-11-18 02:00:07 |
| [fastapi](https://github.com/fastapi/fastapi) | 92017 | 8239 | 3477 | 4880 | 220 | 2025-11-17 19:34:17 |
| [django](https://github.com/django/django) | 85815 | 33233 | 0 | 20199 | 360 | 2025-11-17 20:15:56 |
| [flask](https://github.com/pallets/flask) | 70789 | 16626 | 2701 | 2724 | 12 | 2025-11-17 18:05:57 |
| [cpython](https://github.com/python/cpython) | 69903 | 33439 | 74379 | 66361 | 9212 | 2025-11-17 22:57:47 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64047 | 26448 | 11816 | 19782 | 2114 | 2025-11-17 16:43:45 |
| [keras](https://github.com/keras-team/keras) | 63564 | 19650 | 12592 | 8474 | 267 | 2025-11-14 19:35:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 47128 | 19311 | 27884 | 35199 | 3626 | 2025-11-17 08:08:10 |
| [ray](https://github.com/ray-project/ray) | 39865 | 6905 | 21841 | 36534 | 3213 | 2025-11-18 01:45:20 |
| [gym](https://github.com/openai/gym) | 36782 | 8711 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32831 | 4625 | 5732 | 4072 | 192 | 2025-11-17 17:59:58 |
| [numpy](https://github.com/numpy/numpy) | 30841 | 11709 | 13650 | 16533 | 2358 | 2025-11-17 20:28:04 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29666 | 7035 | 3946 | 4867 | 87 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27573 | 4895 | 5176 | 3724 | 752 | 2025-11-17 21:40:22 |
| [dash](https://github.com/plotly/dash) | 24255 | 2235 | 2026 | 1369 | 580 | 2025-11-17 23:56:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22346 | 5545 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22002 | 8120 | 11045 | 19667 | 1623 | 2025-11-17 19:02:49 |
| [micropython](https://github.com/micropython/micropython) | 21106 | 8537 | 5875 | 7352 | 1808 | 2025-11-17 04:13:07 |
| [RustPython](https://github.com/RustPython/RustPython) | 20793 | 1358 | 1234 | 4985 | 446 | 2025-11-17 13:10:53 |
| [sanic](https://github.com/sanic-org/sanic) | 18562 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17979 | 2749 | 3291 | 1983 | 749 | 2025-11-17 21:28:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16096 | 2156 | 3163 | 8300 | 285 | 2025-11-17 18:53:12 |
| [httpx](https://github.com/encode/httpx) | 14748 | 979 | 921 | 1755 | 111 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14198 | 5542 | 11143 | 12849 | 1793 | 2025-11-17 21:01:35 |
| [dask](https://github.com/dask/dask) | 13599 | 1825 | 5461 | 6402 | 1195 | 2025-11-17 11:22:34 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13563 | 2048 | 2633 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11665 | 1080 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11426 | 585 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11144 | 1599 | 8117 | 1000 | 209 | 2025-11-16 15:58:47 |
| [falcon](https://github.com/falconry/falcon) | 9758 | 972 | 1111 | 1402 | 162 | 2025-11-16 10:15:20 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8717 | 537 | 969 | 454 | 176 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8690 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7000 | 372 | 873 | 2470 | 313 | 2025-11-17 21:56:02 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5380 | 444 | 1198 | 716 | 505 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5086 | 964 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 887 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3758 | 300 | 1166 | 200 | 116 | 2025-11-15 18:32:45 |
| [quart](https://github.com/pallets/quart) | 3542 | 191 | 278 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2707 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2321 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2297 | 176 | 414 | 547 | 75 | 2025-11-17 17:49:19 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 372 | 1783 | 266 | 264 | 2025-11-17 17:42:45 |
| [pypy](https://github.com/pypy/pypy) | 1569 | 89 | 5162 | 171 | 748 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1458 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-17 13:16:04 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-18T02:04:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
