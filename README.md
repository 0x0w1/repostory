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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194620 | 75262 | 41295 | 70837 | 4278 | 2026-04-10 03:30:55 |
| [transformers](https://github.com/huggingface/transformers) | 159129 | 32814 | 18846 | 25866 | 2375 | 2026-04-10 01:19:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 98987 | 27448 | 57765 | 121596 | 18269 | 2026-04-10 03:31:09 |
| [fastapi](https://github.com/fastapi/fastapi) | 97037 | 9042 | 3514 | 5564 | 168 | 2026-04-08 20:54:23 |
| [django](https://github.com/django/django) | 87246 | 33810 | 0 | 21010 | 427 | 2026-04-09 20:40:34 |
| [cpython](https://github.com/python/cpython) | 72260 | 34380 | 75887 | 70144 | 9332 | 2026-04-09 20:21:49 |
| [flask](https://github.com/pallets/flask) | 71407 | 16780 | 2729 | 2801 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65749 | 26920 | 12026 | 20527 | 2045 | 2026-04-09 19:29:47 |
| [keras](https://github.com/keras-team/keras) | 63957 | 19738 | 12727 | 9133 | 268 | 2026-04-09 01:10:16 |
| [pandas](https://github.com/pandas-dev/pandas) | 48449 | 19872 | 28235 | 36829 | 3433 | 2026-04-10 00:29:27 |
| [ray](https://github.com/ray-project/ray) | 42054 | 7420 | 22553 | 39584 | 3586 | 2026-04-10 03:01:01 |
| [gym](https://github.com/openai/gym) | 37145 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33432 | 4669 | 5750 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31799 | 12283 | 13866 | 17250 | 2331 | 2026-04-09 21:28:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29955 | 7069 | 3968 | 4997 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28338 | 5007 | 5266 | 4067 | 780 | 2026-04-09 08:59:29 |
| [dash](https://github.com/plotly/dash) | 24316 | 2273 | 2086 | 1523 | 545 | 2026-04-09 19:18:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22697 | 8312 | 11237 | 20189 | 1536 | 2026-04-09 19:01:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22328 | 5546 | 1870 | 1727 | 216 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21988 | 1423 | 1328 | 6178 | 375 | 2026-04-10 00:16:10 |
| [micropython](https://github.com/micropython/micropython) | 21613 | 8787 | 6018 | 7706 | 1871 | 2026-04-09 01:53:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1589 | 1465 | 1680 | 131 | 2026-04-10 00:47:30 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18438 | 2794 | 3339 | 2068 | 772 | 2026-04-09 22:07:00 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16401 | 2243 | 3188 | 8830 | 283 | 2026-04-09 10:41:39 |
| [httpx](https://github.com/encode/httpx) | 15184 | 1106 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14587 | 5686 | 11407 | 13567 | 1794 | 2026-04-07 21:08:23 |
| [dask](https://github.com/dask/dask) | 13797 | 1861 | 5521 | 6525 | 1245 | 2026-04-07 15:43:50 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13797 | 2094 | 2650 | 1170 | 214 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12190 | 1154 | 766 | 1860 | 52 | 2026-04-09 12:36:22 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11742 | 607 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11730 | 1668 | 8188 | 1054 | 215 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9802 | 987 | 1120 | 1429 | 163 | 2026-04-07 15:03:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8995 | 568 | 1026 | 501 | 221 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7236 | 396 | 889 | 2528 | 319 | 2026-04-08 14:07:02 |
| [hug](https://github.com/hugapi/hug) | 6897 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5602 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5543 | 473 | 1247 | 820 | 505 | 2026-04-09 16:56:25 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5228 | 1005 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4060 | 328 | 1182 | 217 | 116 | 2026-04-08 21:24:16 |
| [databases](https://github.com/encode/databases) | 4009 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3617 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2736 | 311 | 664 | 1307 | 306 | 2026-04-03 22:07:14 |
| [anyio](https://github.com/agronholm/anyio) | 2434 | 194 | 433 | 604 | 89 | 2026-04-07 22:16:53 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1082 | 1466 | 365 | 2026-04-08 10:17:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 367 | 1785 | 267 | 267 | 2026-04-06 17:51:41 |
| [pypy](https://github.com/pypy/pypy) | 1701 | 109 | 5192 | 205 | 751 | 2026-04-10 03:30:02 |
| [jython](https://github.com/jython/jython) | 1499 | 229 | 294 | 123 | 109 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-10T03:31:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
