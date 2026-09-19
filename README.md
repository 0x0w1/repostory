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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200176 | 76835 | 41782 | 82301 | 3184 | 2026-09-19 03:11:54 |
| [transformers](https://github.com/huggingface/transformers) | 166309 | 34628 | 19491 | 28678 | 2410 | 2026-09-19 04:19:23 |
| [pytorch](https://github.com/pytorch/pytorch) | 103094 | 29794 | 61056 | 135935 | 17584 | 2026-09-19 04:18:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 102442 | 9910 | 3552 | 6341 | 81 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91144 | 34789 | 0 | 21861 | 498 | 2026-09-18 19:11:24 |
| [cpython](https://github.com/python/cpython) | 77211 | 35873 | 78189 | 77227 | 9692 | 2026-09-18 21:37:16 |
| [flask](https://github.com/pallets/flask) | 74756 | 16984 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67295 | 27420 | 12288 | 21509 | 2164 | 2026-09-18 17:14:10 |
| [keras](https://github.com/keras-team/keras) | 64320 | 19800 | 12917 | 9900 | 210 | 2026-09-19 04:16:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 49744 | 20400 | 28550 | 38819 | 2703 | 2026-09-18 16:09:53 |
| [ray](https://github.com/ray-project/ray) | 43868 | 8056 | 23083 | 42807 | 3596 | 2026-09-19 03:04:47 |
| [gym](https://github.com/openai/gym) | 37239 | 8675 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33912 | 4723 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32772 | 12817 | 14101 | 18499 | 2283 | 2026-09-18 22:21:26 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7081 | 3966 | 5068 | 51 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28899 | 5169 | 5301 | 4400 | 731 | 2026-09-18 14:05:46 |
| [dash](https://github.com/plotly/dash) | 24414 | 2315 | 2152 | 1705 | 471 | 2026-09-18 20:02:03 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23237 | 8487 | 11424 | 20882 | 1491 | 2026-09-19 02:38:26 |
| [RustPython](https://github.com/RustPython/RustPython) | 22355 | 1486 | 1425 | 7237 | 398 | 2026-09-19 01:38:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5555 | 1883 | 1826 | 259 | 2026-09-16 18:23:07 |
| [micropython](https://github.com/micropython/micropython) | 22074 | 8974 | 6129 | 8099 | 1532 | 2026-09-19 00:47:50 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18793 | 2848 | 3385 | 2190 | 714 | 2026-09-18 22:49:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1598 | 1468 | 1677 | 150 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16552 | 2414 | 3254 | 10142 | 221 | 2026-09-19 01:38:41 |
| [httpx](https://github.com/encode/httpx) | 15501 | 1581 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15023 | 5944 | 11649 | 14532 | 1839 | 2026-09-19 00:12:47 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14025 | 2135 | 2663 | 1223 | 235 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13921 | 1956 | 5559 | 6727 | 1336 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12619 | 1313 | 782 | 2124 | 53 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12166 | 1787 | 8300 | 1209 | 209 | 2026-09-15 21:07:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 616 | 420 | 331 | 161 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1035 | 1142 | 1521 | 156 | 2026-09-18 17:07:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9192 | 613 | 1046 | 550 | 224 | 2026-09-14 13:10:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7331 | 431 | 901 | 2610 | 329 | 2026-09-17 02:12:00 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 515 | 1270 | 905 | 522 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5398 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4402 | 375 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3991 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2544 | 266 | 477 | 775 | 112 | 2026-09-15 17:39:30 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1796 | 125 | 5257 | 303 | 711 | 2026-09-18 13:45:12 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-19T04:21:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
