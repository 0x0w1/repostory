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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201256 | 78684 | 41916 | 84003 | 3406 | 2026-10-26 03:04:17 |
| [transformers](https://github.com/huggingface/transformers) | 168166 | 34990 | 19694 | 29477 | 998 | 2026-10-26 02:30:58 |
| [pytorch](https://github.com/pytorch/pytorch) | 105080 | 31766 | 61998 | 139322 | 17778 | 2026-10-26 04:25:37 |
| [fastapi](https://github.com/fastapi/fastapi) | 104187 | 10121 | 3556 | 6529 | 62 | 2026-10-23 23:46:14 |
| [django](https://github.com/django/django) | 91656 | 36487 | 0 | 22117 | 536 | 2026-10-25 20:10:52 |
| [cpython](https://github.com/python/cpython) | 77766 | 37599 | 78897 | 79257 | 9262 | 2026-10-26 04:24:18 |
| [flask](https://github.com/pallets/flask) | 75089 | 17130 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67917 | 27583 | 12346 | 21685 | 2174 | 2026-10-25 14:38:20 |
| [keras](https://github.com/keras-team/keras) | 64389 | 19798 | 13040 | 10154 | 269 | 2026-10-23 22:31:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 50283 | 20600 | 28651 | 39703 | 2139 | 2026-10-25 23:14:28 |
| [ray](https://github.com/ray-project/ray) | 44123 | 8202 | 23247 | 43718 | 3647 | 2026-10-26 03:42:55 |
| [gym](https://github.com/openai/gym) | 37237 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33994 | 4735 | 5779 | 4136 | 259 | 2026-10-25 23:04:36 |
| [numpy](https://github.com/numpy/numpy) | 33153 | 12978 | 14150 | 18896 | 2240 | 2026-10-24 20:41:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30217 | 7096 | 3966 | 5099 | 64 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29070 | 5248 | 5353 | 4640 | 746 | 2026-10-25 05:51:54 |
| [dash](https://github.com/plotly/dash) | 24471 | 2331 | 2168 | 1788 | 433 | 2026-10-23 16:35:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23393 | 8527 | 11452 | 21020 | 1479 | 2026-10-23 19:17:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 22425 | 1507 | 1446 | 7833 | 303 | 2026-10-26 02:18:12 |
| [tornado](https://github.com/tornadoweb/tornado) | 22168 | 5595 | 1888 | 1898 | 234 | 2026-10-25 03:27:54 |
| [micropython](https://github.com/micropython/micropython) | 22153 | 9015 | 6151 | 8157 | 1550 | 2026-10-26 01:04:23 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18853 | 2882 | 3397 | 2253 | 743 | 2026-10-23 23:43:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16592 | 2484 | 3268 | 10475 | 265 | 2026-10-25 18:29:35 |
| [httpx](https://github.com/encode/httpx) | 15804 | 3254 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15152 | 6035 | 11722 | 14762 | 1878 | 2026-10-25 17:06:10 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14087 | 2150 | 2667 | 1246 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13939 | 2004 | 5577 | 6789 | 1403 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12685 | 1406 | 794 | 2264 | 41 | 2026-10-24 17:17:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12265 | 1831 | 8359 | 1241 | 212 | 2026-10-23 14:28:12 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 619 | 427 | 344 | 172 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1048 | 1148 | 1556 | 157 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9220 | 621 | 1054 | 578 | 244 | 2026-10-20 09:48:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1517 | 867 | 655 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7355 | 462 | 906 | 2648 | 340 | 2026-10-24 14:32:28 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5637 | 535 | 1300 | 969 | 554 | 2026-10-25 16:05:18 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5434 | 1051 | 937 | 326 | 204 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4456 | 388 | 1209 | 257 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 896 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 274 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 317 | 677 | 1379 | 264 | 2026-10-25 19:28:52 |
| [anyio](https://github.com/agronholm/anyio) | 2559 | 331 | 493 | 873 | 143 | 2026-10-25 14:15:47 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2357 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1604 | 356 | 2026-10-22 16:55:34 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1821 | 131 | 5287 | 380 | 719 | 2026-10-25 19:37:28 |
| [jython](https://github.com/jython/jython) | 1551 | 231 | 305 | 155 | 103 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-26T04:26:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
