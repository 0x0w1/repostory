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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192370 | 74973 | 40980 | 61028 | 2196 | 2025-11-10 00:35:34 |
| [transformers](https://github.com/huggingface/transformers) | 152305 | 31098 | 18159 | 23356 | 2123 | 2025-11-09 22:10:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 94895 | 25843 | 54740 | 112212 | 17053 | 2025-11-10 02:06:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 91714 | 8195 | 3476 | 4856 | 211 | 2025-11-08 21:47:46 |
| [django](https://github.com/django/django) | 85734 | 33215 | 0 | 20006 | 358 | 2025-11-07 21:41:57 |
| [flask](https://github.com/pallets/flask) | 70742 | 16618 | 2701 | 2722 | 16 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69769 | 33347 | 74285 | 66101 | 9240 | 2025-11-10 00:49:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63973 | 26421 | 11801 | 19746 | 2125 | 2025-11-09 08:01:22 |
| [keras](https://github.com/keras-team/keras) | 63551 | 19647 | 12588 | 8458 | 267 | 2025-11-07 22:14:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 47062 | 19273 | 27864 | 35139 | 3597 | 2025-11-08 20:40:33 |
| [ray](https://github.com/ray-project/ray) | 39737 | 6880 | 21788 | 36348 | 3206 | 2025-11-09 17:30:40 |
| [gym](https://github.com/openai/gym) | 36752 | 8710 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32785 | 4618 | 5729 | 4072 | 196 | 2025-11-06 10:03:30 |
| [numpy](https://github.com/numpy/numpy) | 30779 | 11673 | 13640 | 16483 | 2359 | 2025-11-09 13:12:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29650 | 7029 | 3946 | 4863 | 83 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27513 | 4891 | 5175 | 3718 | 752 | 2025-11-01 23:53:30 |
| [dash](https://github.com/plotly/dash) | 24233 | 2226 | 2019 | 1360 | 580 | 2025-11-07 21:45:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22339 | 5543 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21956 | 8104 | 11035 | 19656 | 1618 | 2025-11-09 22:48:30 |
| [micropython](https://github.com/micropython/micropython) | 21068 | 8519 | 5869 | 7332 | 1793 | 2025-11-06 01:29:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20776 | 1359 | 1226 | 4952 | 446 | 2025-11-10 00:48:25 |
| [sanic](https://github.com/sanic-org/sanic) | 18551 | 1583 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17941 | 2742 | 3289 | 1975 | 750 | 2025-11-07 19:19:37 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16073 | 2154 | 3161 | 8287 | 271 | 2025-11-06 11:01:47 |
| [httpx](https://github.com/encode/httpx) | 14724 | 975 | 921 | 1754 | 110 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14176 | 5534 | 11124 | 12810 | 1796 | 2025-11-09 20:45:47 |
| [dask](https://github.com/dask/dask) | 13583 | 1820 | 5454 | 6394 | 1196 | 2025-11-07 10:56:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13548 | 2040 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11640 | 1075 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11406 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11103 | 1596 | 8116 | 1000 | 219 | 2025-11-09 19:21:36 |
| [falcon](https://github.com/falconry/falcon) | 9753 | 975 | 1110 | 1397 | 168 | 2025-11-08 12:29:30 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8694 | 535 | 965 | 452 | 176 | 2025-11-03 10:41:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8689 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6951 | 370 | 872 | 2466 | 311 | 2025-11-03 23:11:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5367 | 443 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5074 | 959 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4060 | 888 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3746 | 299 | 1166 | 199 | 116 | 2025-11-05 15:38:15 |
| [quart](https://github.com/pallets/quart) | 3531 | 190 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2704 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2288 | 174 | 412 | 543 | 72 | 2025-11-09 20:35:41 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 370 | 1781 | 264 | 260 | 2025-11-03 17:44:55 |
| [pypy](https://github.com/pypy/pypy) | 1563 | 89 | 5159 | 171 | 745 | 2025-11-09 09:58:19 |
| [jython](https://github.com/jython/jython) | 1457 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-10T02:09:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
