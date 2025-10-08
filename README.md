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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191951 | 74902 | 40838 | 58959 | 1873 | 2025-10-08 01:49:05 |
| [transformers](https://github.com/huggingface/transformers) | 150733 | 30676 | 18022 | 22817 | 2048 | 2025-10-07 17:22:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 93749 | 25496 | 54166 | 110270 | 16956 | 2025-10-08 01:51:02 |
| [fastapi](https://github.com/fastapi/fastapi) | 90474 | 8011 | 3470 | 4763 | 202 | 2025-10-07 15:05:45 |
| [django](https://github.com/django/django) | 85342 | 33064 | 0 | 19863 | 346 | 2025-10-08 01:41:06 |
| [flask](https://github.com/pallets/flask) | 70505 | 16550 | 2699 | 2705 | 10 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69186 | 33022 | 73814 | 64996 | 9204 | 2025-10-08 00:37:30 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63583 | 26305 | 11751 | 19548 | 2137 | 2025-10-07 16:15:36 |
| [keras](https://github.com/keras-team/keras) | 63455 | 19623 | 12562 | 8377 | 258 | 2025-10-08 00:17:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 46768 | 19097 | 27768 | 34801 | 3609 | 2025-10-07 22:51:26 |
| [ray](https://github.com/ray-project/ray) | 39223 | 6857 | 21535 | 35649 | 3170 | 2025-10-08 01:43:18 |
| [gym](https://github.com/openai/gym) | 36635 | 8705 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32597 | 4590 | 5723 | 4071 | 208 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30525 | 11519 | 13577 | 16251 | 2361 | 2025-10-07 18:51:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29538 | 7012 | 3945 | 4842 | 105 | 2025-10-07 09:28:17 |
| [celery](https://github.com/celery/celery) | 27298 | 4856 | 5170 | 3675 | 754 | 2025-10-07 22:24:10 |
| [dash](https://github.com/plotly/dash) | 24136 | 2210 | 2004 | 1347 | 572 | 2025-10-07 22:00:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22281 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21782 | 8059 | 11001 | 19596 | 1630 | 2025-10-08 01:12:20 |
| [micropython](https://github.com/micropython/micropython) | 20912 | 8465 | 5842 | 7257 | 1769 | 2025-10-07 02:44:54 |
| [RustPython](https://github.com/RustPython/RustPython) | 20576 | 1350 | 1221 | 4900 | 451 | 2025-10-06 13:41:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18505 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17813 | 2723 | 3260 | 1960 | 720 | 2025-10-07 17:27:40 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16025 | 2129 | 3148 | 8157 | 271 | 2025-10-07 18:17:50 |
| [httpx](https://github.com/encode/httpx) | 14606 | 959 | 918 | 1737 | 100 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14065 | 5494 | 11061 | 12664 | 1755 | 2025-10-07 04:13:50 |
| [dask](https://github.com/dask/dask) | 13516 | 1800 | 5440 | 6357 | 1198 | 2025-10-07 14:45:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13485 | 2037 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11525 | 1045 | 754 | 1717 | 47 | 2025-10-02 20:15:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11309 | 575 | 390 | 289 | 144 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10973 | 1584 | 8095 | 988 | 224 | 2025-10-07 21:41:09 |
| [falcon](https://github.com/falconry/falcon) | 9726 | 965 | 1103 | 1375 | 163 | 2025-10-07 10:53:30 |
| [bottle](https://github.com/bottlepy/bottle) | 8669 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8603 | 527 | 948 | 439 | 413 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6885 | 368 | 872 | 2458 | 311 | 2025-10-06 22:56:19 |
| [eve](https://github.com/pyeve/eve) | 6735 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5629 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5319 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5027 | 945 | 871 | 261 | 168 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3670 | 291 | 1162 | 196 | 117 | 2025-10-07 02:53:39 |
| [quart](https://github.com/pallets/quart) | 3483 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2691 | 303 | 651 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2312 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2238 | 166 | 404 | 523 | 66 | 2025-10-07 22:17:51 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-10-06 17:57:17 |
| [pypy](https://github.com/pypy/pypy) | 1509 | 88 | 5149 | 171 | 737 | 2025-10-07 17:24:20 |
| [jython](https://github.com/jython/jython) | 1439 | 224 | 283 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-06 17:16:06 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-08T01:54:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
