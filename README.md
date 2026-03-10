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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194119 | 75220 | 41202 | 68648 | 3788 | 2026-03-10 02:38:22 |
| [transformers](https://github.com/huggingface/transformers) | 157670 | 32338 | 18682 | 25261 | 2255 | 2026-03-09 23:25:58 |
| [pytorch](https://github.com/pytorch/pytorch) | 98138 | 27127 | 57204 | 119261 | 18137 | 2026-03-10 02:42:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 96086 | 8807 | 3506 | 5411 | 147 | 2026-03-07 09:29:24 |
| [django](https://github.com/django/django) | 87064 | 33730 | 0 | 20811 | 434 | 2026-03-09 20:45:50 |
| [cpython](https://github.com/python/cpython) | 71965 | 34208 | 75495 | 69220 | 9314 | 2026-03-09 22:51:00 |
| [flask](https://github.com/pallets/flask) | 71398 | 16743 | 2723 | 2781 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65386 | 26749 | 11983 | 20362 | 2143 | 2026-03-09 15:12:17 |
| [keras](https://github.com/keras-team/keras) | 63969 | 19713 | 12658 | 8932 | 284 | 2026-03-09 23:42:58 |
| [pandas](https://github.com/pandas-dev/pandas) | 48085 | 19719 | 28162 | 36266 | 3684 | 2026-03-10 00:21:07 |
| [ray](https://github.com/ray-project/ray) | 41730 | 7305 | 22434 | 38825 | 3441 | 2026-03-10 02:35:47 |
| [gym](https://github.com/openai/gym) | 37079 | 8708 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33290 | 4644 | 5742 | 4083 | 194 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31579 | 12139 | 13824 | 17096 | 2325 | 2026-03-09 22:45:12 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29930 | 7079 | 3946 | 4940 | 79 | 2026-03-04 15:27:11 |
| [celery](https://github.com/celery/celery) | 28255 | 4987 | 5201 | 3857 | 773 | 2026-03-09 16:53:23 |
| [dash](https://github.com/plotly/dash) | 24447 | 2262 | 2069 | 1456 | 572 | 2026-03-06 19:02:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22542 | 8243 | 11191 | 20025 | 1539 | 2026-03-09 22:10:53 |
| [tornado](https://github.com/tornadoweb/tornado) | 22405 | 5545 | 1864 | 1704 | 219 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21868 | 1404 | 1313 | 6012 | 365 | 2026-03-10 01:25:00 |
| [micropython](https://github.com/micropython/micropython) | 21522 | 8733 | 5972 | 7608 | 1848 | 2026-03-09 13:10:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18317 | 2780 | 3326 | 2053 | 776 | 2026-03-09 15:27:54 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16439 | 2210 | 3181 | 8724 | 276 | 2026-03-09 16:26:44 |
| [httpx](https://github.com/encode/httpx) | 15192 | 1058 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14513 | 5647 | 11358 | 13405 | 1787 | 2026-03-10 00:00:02 |
| [dask](https://github.com/dask/dask) | 13763 | 1853 | 5513 | 6503 | 1227 | 2026-03-05 10:51:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13760 | 2079 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12011 | 1130 | 764 | 1824 | 47 | 2026-03-07 11:57:25 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11726 | 1650 | 8164 | 1043 | 213 | 2026-03-09 22:58:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11678 | 601 | 406 | 314 | 153 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 980 | 1119 | 1418 | 164 | 2026-03-06 07:42:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8935 | 561 | 1020 | 492 | 218 | 2026-03-06 14:12:06 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7193 | 391 | 880 | 2512 | 319 | 2026-03-10 00:05:15 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5513 | 465 | 1238 | 794 | 492 | 2026-03-08 17:01:54 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5203 | 1000 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1063 | 2731 | 80 | 2026-03-09 23:49:52 |
| [databases](https://github.com/encode/databases) | 4019 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4001 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3604 | 193 | 280 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2733 | 311 | 660 | 1286 | 308 | 2026-03-09 23:12:29 |
| [anyio](https://github.com/agronholm/anyio) | 2405 | 184 | 429 | 581 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1080 | 1464 | 368 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1940 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1673 | 101 | 5177 | 183 | 759 | 2026-03-09 19:15:22 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-10T02:42:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
