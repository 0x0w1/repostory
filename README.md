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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193945 | 75213 | 41181 | 68137 | 3569 | 2026-03-03 02:15:45 |
| [transformers](https://github.com/huggingface/transformers) | 157259 | 32268 | 18647 | 25148 | 2264 | 2026-03-02 22:21:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 97877 | 27042 | 57059 | 118672 | 18069 | 2026-03-03 02:47:14 |
| [fastapi](https://github.com/fastapi/fastapi) | 95755 | 8774 | 3506 | 5392 | 148 | 2026-03-03 00:17:07 |
| [django](https://github.com/django/django) | 86944 | 33709 | 0 | 20749 | 422 | 2026-03-02 19:18:12 |
| [cpython](https://github.com/python/cpython) | 71763 | 34159 | 75415 | 69027 | 9280 | 2026-03-03 01:11:24 |
| [flask](https://github.com/pallets/flask) | 71278 | 16737 | 2722 | 2782 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65253 | 26739 | 11976 | 20313 | 2146 | 2026-03-02 16:31:54 |
| [keras](https://github.com/keras-team/keras) | 63868 | 19711 | 12651 | 8883 | 297 | 2026-03-03 02:40:38 |
| [pandas](https://github.com/pandas-dev/pandas) | 48015 | 19712 | 28147 | 36154 | 3687 | 2026-03-02 21:40:07 |
| [ray](https://github.com/ray-project/ray) | 41530 | 7282 | 22392 | 38690 | 3422 | 2026-03-03 02:27:15 |
| [gym](https://github.com/openai/gym) | 37067 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33264 | 4641 | 5742 | 4080 | 192 | 2026-03-02 19:31:26 |
| [numpy](https://github.com/numpy/numpy) | 31546 | 12106 | 13817 | 17036 | 2323 | 2026-03-02 20:01:24 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29912 | 7075 | 3946 | 4935 | 80 | 2026-03-01 19:09:34 |
| [celery](https://github.com/celery/celery) | 28152 | 4972 | 5197 | 3839 | 771 | 2026-03-02 23:41:16 |
| [dash](https://github.com/plotly/dash) | 24430 | 2261 | 2066 | 1451 | 569 | 2026-03-01 08:54:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22516 | 8226 | 11180 | 20002 | 1542 | 2026-03-03 01:25:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22403 | 5545 | 1863 | 1703 | 217 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21840 | 1403 | 1309 | 5943 | 383 | 2026-03-03 02:25:47 |
| [micropython](https://github.com/micropython/micropython) | 21506 | 8724 | 5970 | 7593 | 1852 | 2026-02-26 19:14:26 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18292 | 2781 | 3325 | 2050 | 778 | 2026-03-02 22:40:59 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16339 | 2208 | 3180 | 8698 | 271 | 2026-03-03 00:32:20 |
| [httpx](https://github.com/encode/httpx) | 15102 | 1049 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14498 | 5636 | 11338 | 13361 | 1773 | 2026-03-02 20:18:13 |
| [dask](https://github.com/dask/dask) | 13754 | 1848 | 5508 | 6501 | 1231 | 2026-03-02 23:30:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13747 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11987 | 1124 | 764 | 1818 | 46 | 2026-03-01 20:46:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11675 | 601 | 404 | 314 | 152 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11619 | 1647 | 8159 | 1038 | 212 | 2026-03-02 15:29:24 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 979 | 1119 | 1415 | 164 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8924 | 558 | 1017 | 489 | 221 | 2026-03-01 21:26:10 |
| [bottle](https://github.com/bottlepy/bottle) | 8761 | 1499 | 862 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7186 | 387 | 880 | 2508 | 316 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6910 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5610 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5515 | 464 | 1235 | 791 | 498 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5198 | 1001 | 907 | 291 | 198 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4075 | 893 | 1063 | 2728 | 79 | 2026-03-02 19:42:51 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3983 | 321 | 1181 | 214 | 115 | 2026-03-02 16:28:40 |
| [quart](https://github.com/pallets/quart) | 3603 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2731 | 310 | 660 | 1283 | 308 | 2026-02-27 12:12:17 |
| [anyio](https://github.com/agronholm/anyio) | 2400 | 183 | 427 | 579 | 84 | 2026-03-03 00:52:14 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1464 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1937 | 368 | 1785 | 267 | 267 | 2026-03-02 18:13:20 |
| [pypy](https://github.com/pypy/pypy) | 1660 | 100 | 5177 | 182 | 759 | 2026-03-02 18:40:57 |
| [jython](https://github.com/jython/jython) | 1488 | 226 | 291 | 121 | 105 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-03T02:50:21*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
