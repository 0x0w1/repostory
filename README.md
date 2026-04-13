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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194684 | 75279 | 41306 | 70982 | 4359 | 2026-04-13 03:39:32 |
| [transformers](https://github.com/huggingface/transformers) | 159262 | 32849 | 18854 | 25892 | 2368 | 2026-04-11 01:27:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 99076 | 27474 | 57937 | 121734 | 18469 | 2026-04-13 03:37:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 97126 | 9061 | 3517 | 5572 | 172 | 2026-04-10 15:48:08 |
| [django](https://github.com/django/django) | 87261 | 33814 | 0 | 21031 | 432 | 2026-04-11 12:54:08 |
| [cpython](https://github.com/python/cpython) | 72302 | 34394 | 75934 | 70259 | 9336 | 2026-04-13 01:40:54 |
| [flask](https://github.com/pallets/flask) | 71413 | 16785 | 2730 | 2801 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65797 | 26940 | 12027 | 20535 | 2051 | 2026-04-09 19:29:47 |
| [keras](https://github.com/keras-team/keras) | 63977 | 19741 | 12727 | 9140 | 269 | 2026-04-10 18:13:03 |
| [pandas](https://github.com/pandas-dev/pandas) | 48490 | 19868 | 28238 | 36880 | 3430 | 2026-04-12 20:47:10 |
| [ray](https://github.com/ray-project/ray) | 42088 | 7426 | 22560 | 39634 | 3581 | 2026-04-13 03:24:43 |
| [gym](https://github.com/openai/gym) | 37157 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33455 | 4672 | 5752 | 4089 | 198 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31839 | 12295 | 13869 | 17288 | 2339 | 2026-04-12 15:50:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29962 | 7067 | 3968 | 4997 | 76 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28346 | 5008 | 5266 | 4070 | 782 | 2026-04-12 14:55:07 |
| [dash](https://github.com/plotly/dash) | 24197 | 2275 | 2088 | 1528 | 547 | 2026-04-11 09:31:26 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22708 | 8317 | 11237 | 20199 | 1505 | 2026-04-12 21:58:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22272 | 5546 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21994 | 1426 | 1328 | 6184 | 375 | 2026-04-12 14:35:48 |
| [micropython](https://github.com/micropython/micropython) | 21611 | 8792 | 6023 | 7711 | 1880 | 2026-04-10 19:14:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1587 | 1465 | 1682 | 132 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18443 | 2798 | 3339 | 2070 | 772 | 2026-04-10 22:12:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16398 | 2243 | 3187 | 8844 | 288 | 2026-04-13 00:56:46 |
| [httpx](https://github.com/encode/httpx) | 15190 | 1108 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14593 | 5689 | 11408 | 13575 | 1791 | 2026-04-12 22:18:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13802 | 2094 | 2651 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13800 | 1863 | 5521 | 6527 | 1247 | 2026-04-07 15:43:50 |
| [starlette](https://github.com/Kludex/starlette) | 12199 | 1154 | 766 | 1863 | 52 | 2026-04-11 13:05:00 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11746 | 605 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11744 | 1668 | 8188 | 1054 | 215 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 988 | 1121 | 1432 | 165 | 2026-04-12 14:11:25 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9000 | 570 | 1027 | 502 | 223 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7238 | 395 | 889 | 2529 | 320 | 2026-04-08 14:07:02 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5601 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5545 | 474 | 1248 | 820 | 506 | 2026-04-09 16:56:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5235 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 895 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4065 | 330 | 1182 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4008 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3618 | 195 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2436 | 195 | 434 | 606 | 91 | 2026-04-12 22:41:31 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 366 | 1785 | 267 | 267 | 2026-04-06 17:51:41 |
| [pypy](https://github.com/pypy/pypy) | 1704 | 110 | 5194 | 215 | 750 | 2026-04-12 18:37:55 |
| [jython](https://github.com/jython/jython) | 1499 | 229 | 294 | 124 | 110 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-13T03:41:56*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
