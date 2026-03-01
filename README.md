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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193944 | 75221 | 41172 | 68013 | 3540 | 2026-03-01 01:05:40 |
| [transformers](https://github.com/huggingface/transformers) | 157133 | 32247 | 18635 | 25122 | 2300 | 2026-02-27 23:18:08 |
| [pytorch](https://github.com/pytorch/pytorch) | 97838 | 27023 | 57000 | 118567 | 18043 | 2026-03-01 03:17:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 95703 | 8762 | 3507 | 5380 | 151 | 2026-02-27 21:17:51 |
| [django](https://github.com/django/django) | 86950 | 33701 | 0 | 20739 | 422 | 2026-02-28 17:46:44 |
| [cpython](https://github.com/python/cpython) | 71757 | 34145 | 75404 | 68971 | 9301 | 2026-02-28 23:20:21 |
| [flask](https://github.com/pallets/flask) | 71286 | 16736 | 2722 | 2781 | 3 | 2026-02-20 04:00:36 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65248 | 26737 | 11974 | 20301 | 2148 | 2026-02-27 13:12:16 |
| [keras](https://github.com/keras-team/keras) | 63878 | 19714 | 12649 | 8871 | 283 | 2026-03-01 03:16:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 48005 | 19711 | 28146 | 36138 | 3693 | 2026-02-28 19:40:27 |
| [ray](https://github.com/ray-project/ray) | 41525 | 7273 | 22385 | 38667 | 3434 | 2026-02-28 22:34:32 |
| [gym](https://github.com/openai/gym) | 37057 | 8711 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33256 | 4638 | 5743 | 4079 | 192 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31541 | 12102 | 13812 | 17029 | 2321 | 2026-02-28 19:55:21 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29909 | 7075 | 3946 | 4934 | 83 | 2026-02-27 13:44:31 |
| [celery](https://github.com/celery/celery) | 28158 | 4967 | 5197 | 3829 | 775 | 2026-02-28 13:57:18 |
| [dash](https://github.com/plotly/dash) | 24430 | 2259 | 2065 | 1449 | 566 | 2026-02-28 02:52:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22512 | 8223 | 11175 | 19997 | 1548 | 2026-02-28 22:02:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22405 | 5546 | 1863 | 1703 | 217 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21832 | 1403 | 1308 | 5907 | 385 | 2026-03-01 01:58:47 |
| [micropython](https://github.com/micropython/micropython) | 21498 | 8724 | 5969 | 7591 | 1849 | 2026-02-26 19:14:26 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1585 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18290 | 2780 | 3325 | 2048 | 780 | 2026-02-27 22:47:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16368 | 2207 | 3180 | 8683 | 268 | 2026-03-01 00:39:23 |
| [httpx](https://github.com/encode/httpx) | 15118 | 1047 | 0 | 1804 | 149 | 2026-02-23 10:40:42 |
| [scipy](https://github.com/scipy/scipy) | 14491 | 5632 | 11338 | 13351 | 1776 | 2026-02-28 13:45:10 |
| [dask](https://github.com/dask/dask) | 13750 | 1848 | 5508 | 6500 | 1233 | 2026-02-22 23:28:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13745 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11984 | 1124 | 763 | 1813 | 47 | 2026-02-23 22:17:04 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11669 | 601 | 403 | 314 | 151 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11645 | 1645 | 8158 | 1038 | 212 | 2026-02-28 18:11:49 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 979 | 1119 | 1415 | 164 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8923 | 558 | 1016 | 487 | 218 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8762 | 1499 | 862 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7184 | 387 | 880 | 2508 | 316 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6909 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5610 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5516 | 463 | 1235 | 781 | 488 | 2026-02-19 21:00:51 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5198 | 1001 | 907 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4075 | 893 | 1063 | 2728 | 79 | 2026-02-25 22:47:41 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3981 | 322 | 1181 | 214 | 115 | 2026-02-23 22:58:28 |
| [quart](https://github.com/pallets/quart) | 3604 | 192 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2730 | 310 | 660 | 1283 | 308 | 2026-02-27 12:12:17 |
| [anyio](https://github.com/agronholm/anyio) | 2399 | 183 | 427 | 577 | 82 | 2026-02-25 19:40:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1464 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1938 | 368 | 1785 | 267 | 267 | 2026-02-23 17:52:49 |
| [pypy](https://github.com/pypy/pypy) | 1658 | 100 | 5177 | 180 | 758 | 2026-02-25 13:46:28 |
| [jython](https://github.com/jython/jython) | 1487 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-01T03:17:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
