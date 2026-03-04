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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193965 | 75209 | 41188 | 68217 | 3556 | 2026-03-04 02:27:28 |
| [transformers](https://github.com/huggingface/transformers) | 157311 | 32273 | 18653 | 25162 | 2268 | 2026-03-03 21:49:58 |
| [pytorch](https://github.com/pytorch/pytorch) | 97905 | 27052 | 57078 | 118771 | 18064 | 2026-03-04 02:33:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 95803 | 8777 | 3505 | 5394 | 147 | 2026-03-03 12:40:40 |
| [django](https://github.com/django/django) | 86949 | 33711 | 0 | 20758 | 421 | 2026-03-04 00:36:47 |
| [cpython](https://github.com/python/cpython) | 71783 | 34167 | 75428 | 69055 | 9274 | 2026-03-03 21:47:39 |
| [flask](https://github.com/pallets/flask) | 71287 | 16739 | 2722 | 2782 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65262 | 26743 | 11978 | 20320 | 2139 | 2026-03-03 23:55:33 |
| [keras](https://github.com/keras-team/keras) | 63876 | 19711 | 12654 | 8891 | 285 | 2026-03-04 01:43:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 48031 | 19712 | 28149 | 36170 | 3690 | 2026-03-03 20:06:19 |
| [ray](https://github.com/ray-project/ray) | 41545 | 7284 | 22400 | 38718 | 3436 | 2026-03-04 02:15:11 |
| [gym](https://github.com/openai/gym) | 37069 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33270 | 4640 | 5742 | 4080 | 191 | 2026-03-03 08:56:07 |
| [numpy](https://github.com/numpy/numpy) | 31551 | 12105 | 13818 | 17043 | 2330 | 2026-03-03 22:06:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29919 | 7075 | 3946 | 4938 | 80 | 2026-03-03 22:58:57 |
| [celery](https://github.com/celery/celery) | 28159 | 4973 | 5197 | 3844 | 768 | 2026-03-03 22:13:36 |
| [dash](https://github.com/plotly/dash) | 24432 | 2261 | 2067 | 1453 | 572 | 2026-03-03 21:33:22 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22520 | 8227 | 11181 | 20004 | 1544 | 2026-03-03 13:32:33 |
| [tornado](https://github.com/tornadoweb/tornado) | 22403 | 5543 | 1863 | 1703 | 217 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21851 | 1404 | 1309 | 5959 | 383 | 2026-03-03 21:33:59 |
| [micropython](https://github.com/micropython/micropython) | 21511 | 8724 | 5971 | 7598 | 1845 | 2026-03-04 01:31:22 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18303 | 2780 | 3325 | 2052 | 777 | 2026-03-03 22:18:19 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16338 | 2208 | 3180 | 8700 | 272 | 2026-03-04 00:53:37 |
| [httpx](https://github.com/encode/httpx) | 15108 | 1050 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14500 | 5639 | 11344 | 13368 | 1776 | 2026-03-04 01:19:47 |
| [dask](https://github.com/dask/dask) | 13755 | 1849 | 5508 | 6501 | 1229 | 2026-03-03 11:15:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13752 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11991 | 1126 | 763 | 1820 | 47 | 2026-03-01 20:46:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11675 | 601 | 404 | 314 | 152 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11624 | 1649 | 8160 | 1039 | 212 | 2026-03-03 22:14:24 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 980 | 1119 | 1417 | 166 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8925 | 559 | 1018 | 490 | 220 | 2026-03-03 19:55:48 |
| [bottle](https://github.com/bottlepy/bottle) | 8760 | 1499 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7186 | 387 | 880 | 2510 | 318 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6910 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5610 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5515 | 464 | 1235 | 791 | 488 | 2026-03-03 15:53:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5199 | 1001 | 907 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4074 | 893 | 1063 | 2728 | 79 | 2026-03-02 19:42:51 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3984 | 321 | 1181 | 214 | 115 | 2026-03-02 16:28:40 |
| [quart](https://github.com/pallets/quart) | 3606 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2731 | 310 | 660 | 1284 | 308 | 2026-03-04 02:34:39 |
| [anyio](https://github.com/agronholm/anyio) | 2401 | 183 | 428 | 579 | 85 | 2026-03-03 00:52:14 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1464 | 367 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-03-02 18:13:20 |
| [pypy](https://github.com/pypy/pypy) | 1663 | 100 | 5177 | 182 | 759 | 2026-03-02 18:40:57 |
| [jython](https://github.com/jython/jython) | 1488 | 226 | 291 | 121 | 105 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-04T02:43:04*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
