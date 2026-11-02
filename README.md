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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201264 | 78175 | 41938 | 84259 | 3491 | 2026-11-02 04:39:39 |
| [transformers](https://github.com/huggingface/transformers) | 168431 | 35079 | 19758 | 29669 | 1053 | 2026-11-02 05:36:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 105071 | 31307 | 62179 | 140109 | 17839 | 2026-11-02 05:33:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 104543 | 10173 | 3556 | 6560 | 78 | 2026-11-01 12:15:51 |
| [django](https://github.com/django/django) | 91708 | 35991 | 0 | 22150 | 541 | 2026-10-31 02:48:02 |
| [cpython](https://github.com/python/cpython) | 77789 | 37160 | 79072 | 79693 | 9222 | 2026-11-02 03:43:16 |
| [flask](https://github.com/pallets/flask) | 75162 | 17266 | 2772 | 2913 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67967 | 27622 | 12357 | 21736 | 2160 | 2026-11-01 15:58:02 |
| [keras](https://github.com/keras-team/keras) | 64412 | 19820 | 13061 | 10186 | 283 | 2026-11-01 11:13:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 50286 | 20731 | 28665 | 39783 | 2058 | 2026-11-01 20:52:44 |
| [ray](https://github.com/ray-project/ray) | 44179 | 8236 | 23274 | 43952 | 3713 | 2026-11-02 04:38:03 |
| [gym](https://github.com/openai/gym) | 37231 | 8666 | 1837 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34013 | 4741 | 5781 | 4140 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33230 | 13096 | 14158 | 18939 | 2237 | 2026-11-01 00:28:47 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30227 | 7096 | 3966 | 5104 | 67 | 2026-10-28 07:03:26 |
| [celery](https://github.com/celery/celery) | 29117 | 5255 | 5357 | 4674 | 743 | 2026-11-01 15:19:53 |
| [dash](https://github.com/plotly/dash) | 24475 | 2332 | 2170 | 1806 | 435 | 2026-10-30 16:13:22 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23409 | 8539 | 11456 | 21039 | 1477 | 2026-11-01 19:15:43 |
| [RustPython](https://github.com/RustPython/RustPython) | 22452 | 1507 | 1453 | 7968 | 297 | 2026-11-02 05:31:12 |
| [micropython](https://github.com/micropython/micropython) | 22178 | 9035 | 6154 | 8183 | 1554 | 2026-11-02 03:07:51 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5598 | 1888 | 1903 | 234 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18869 | 2887 | 3400 | 2268 | 748 | 2026-11-01 07:37:22 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16602 | 2502 | 3269 | 10584 | 276 | 2026-11-01 21:24:43 |
| [httpx](https://github.com/encode/httpx) | 15952 | 2613 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15177 | 6055 | 11743 | 14816 | 1892 | 2026-11-01 19:39:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14096 | 2155 | 2668 | 1247 | 257 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13944 | 2010 | 5581 | 6800 | 1418 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12700 | 1428 | 795 | 2300 | 35 | 2026-11-01 20:39:28 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12277 | 1840 | 8371 | 1253 | 214 | 2026-11-01 15:19:46 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11928 | 620 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9811 | 1051 | 1148 | 1561 | 162 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9228 | 624 | 1055 | 596 | 205 | 2026-11-01 18:39:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1514 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7360 | 466 | 906 | 2659 | 340 | 2026-11-01 03:24:20 |
| [hug](https://github.com/hugapi/hug) | 6872 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5640 | 541 | 1301 | 977 | 555 | 2026-10-31 04:22:39 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5443 | 1053 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4464 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3681 | 209 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 680 | 1389 | 266 | 2026-11-02 03:40:41 |
| [anyio](https://github.com/agronholm/anyio) | 2567 | 343 | 495 | 878 | 136 | 2026-11-01 13:54:45 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1608 | 355 | 2026-10-30 11:34:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1791 | 278 | 279 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1823 | 130 | 5291 | 395 | 717 | 2026-11-01 20:52:54 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 104 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-02T05:43:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
