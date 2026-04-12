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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194663 | 75278 | 41305 | 70952 | 4332 | 2026-04-12 03:11:44 |
| [transformers](https://github.com/huggingface/transformers) | 159212 | 32835 | 18854 | 25885 | 2364 | 2026-04-11 01:27:31 |
| [pytorch](https://github.com/pytorch/pytorch) | 99044 | 27464 | 57931 | 121707 | 18463 | 2026-04-12 03:35:06 |
| [fastapi](https://github.com/fastapi/fastapi) | 97087 | 9052 | 3514 | 5569 | 171 | 2026-04-10 15:48:08 |
| [django](https://github.com/django/django) | 87253 | 33814 | 0 | 21028 | 436 | 2026-04-11 12:54:08 |
| [cpython](https://github.com/python/cpython) | 72290 | 34394 | 75909 | 70226 | 9328 | 2026-04-12 03:07:43 |
| [flask](https://github.com/pallets/flask) | 71410 | 16783 | 2730 | 2801 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65778 | 26938 | 12027 | 20533 | 2049 | 2026-04-09 19:29:47 |
| [keras](https://github.com/keras-team/keras) | 63965 | 19741 | 12727 | 9137 | 266 | 2026-04-10 18:13:03 |
| [pandas](https://github.com/pandas-dev/pandas) | 48475 | 19873 | 28237 | 36870 | 3429 | 2026-04-11 17:58:22 |
| [ray](https://github.com/ray-project/ray) | 42074 | 7425 | 22558 | 39617 | 3578 | 2026-04-12 03:07:58 |
| [gym](https://github.com/openai/gym) | 37155 | 8705 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33440 | 4670 | 5752 | 4089 | 198 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31830 | 12293 | 13869 | 17278 | 2335 | 2026-04-11 23:22:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29960 | 7067 | 3968 | 4997 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28340 | 5008 | 5266 | 4070 | 783 | 2026-04-09 08:59:29 |
| [dash](https://github.com/plotly/dash) | 24194 | 2275 | 2088 | 1528 | 548 | 2026-04-11 09:31:26 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22704 | 8313 | 11237 | 20197 | 1508 | 2026-04-12 02:47:17 |
| [tornado](https://github.com/tornadoweb/tornado) | 22272 | 5547 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21992 | 1426 | 1328 | 6183 | 375 | 2026-04-11 20:14:23 |
| [micropython](https://github.com/micropython/micropython) | 21610 | 8792 | 6021 | 7710 | 1878 | 2026-04-10 19:14:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1588 | 1465 | 1682 | 132 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18439 | 2797 | 3339 | 2069 | 771 | 2026-04-10 22:12:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16395 | 2243 | 3187 | 8836 | 285 | 2026-04-11 18:04:12 |
| [httpx](https://github.com/encode/httpx) | 15183 | 1107 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14592 | 5687 | 11407 | 13571 | 1792 | 2026-04-12 02:08:33 |
| [dask](https://github.com/dask/dask) | 13800 | 1862 | 5521 | 6526 | 1246 | 2026-04-07 15:43:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13800 | 2094 | 2651 | 1170 | 214 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12198 | 1155 | 766 | 1863 | 52 | 2026-04-11 13:05:00 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11746 | 606 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11741 | 1668 | 8188 | 1054 | 215 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 987 | 1120 | 1430 | 164 | 2026-04-07 15:03:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8999 | 569 | 1026 | 501 | 221 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8755 | 1498 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7238 | 395 | 889 | 2528 | 319 | 2026-04-08 14:07:02 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5601 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5546 | 474 | 1247 | 820 | 505 | 2026-04-09 16:56:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5233 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 895 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4063 | 330 | 1182 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4008 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3618 | 195 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2435 | 194 | 433 | 605 | 90 | 2026-04-11 16:30:25 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 367 | 1785 | 267 | 267 | 2026-04-06 17:51:41 |
| [pypy](https://github.com/pypy/pypy) | 1704 | 110 | 5194 | 212 | 750 | 2026-04-11 21:18:54 |
| [jython](https://github.com/jython/jython) | 1499 | 229 | 294 | 123 | 109 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-12T03:35:45*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
