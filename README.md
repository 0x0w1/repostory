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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195614 | 75181 | 41524 | 75588 | 3263 | 2026-06-09 04:15:14 |
| [transformers](https://github.com/huggingface/transformers) | 161423 | 33427 | 19046 | 26758 | 2409 | 2026-06-08 23:54:07 |
| [pytorch](https://github.com/pytorch/pytorch) | 100602 | 27951 | 59110 | 127037 | 18336 | 2026-06-09 04:15:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 99027 | 9403 | 3528 | 5876 | 94 | 2026-06-08 06:10:05 |
| [django](https://github.com/django/django) | 87809 | 33853 | 0 | 21369 | 451 | 2026-06-08 23:07:44 |
| [cpython](https://github.com/python/cpython) | 73159 | 34709 | 76652 | 72138 | 9298 | 2026-06-08 22:55:57 |
| [flask](https://github.com/pallets/flask) | 71637 | 16853 | 2741 | 2836 | 4 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66272 | 27047 | 12125 | 20915 | 2044 | 2026-06-08 16:25:05 |
| [keras](https://github.com/keras-team/keras) | 64079 | 19731 | 12777 | 9424 | 179 | 2026-06-09 03:32:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 48932 | 19999 | 28303 | 37438 | 3227 | 2026-06-08 17:01:27 |
| [ray](https://github.com/ray-project/ray) | 42813 | 7663 | 22730 | 40826 | 3444 | 2026-06-09 03:08:56 |
| [gym](https://github.com/openai/gym) | 37217 | 8703 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33642 | 4686 | 5757 | 4096 | 210 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32164 | 12435 | 13933 | 17571 | 2376 | 2026-06-08 07:51:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30058 | 7068 | 3967 | 5009 | 77 | 2026-06-06 13:20:03 |
| [celery](https://github.com/celery/celery) | 28569 | 5070 | 5280 | 4137 | 784 | 2026-06-08 22:13:00 |
| [dash](https://github.com/plotly/dash) | 24239 | 2292 | 2103 | 1581 | 537 | 2026-06-08 16:59:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22873 | 8350 | 11302 | 20496 | 1462 | 2026-06-06 02:08:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5536 | 1872 | 1743 | 217 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22104 | 1440 | 1354 | 6634 | 393 | 2026-06-09 01:12:57 |
| [micropython](https://github.com/micropython/micropython) | 21792 | 8858 | 6067 | 7861 | 1678 | 2026-06-08 19:14:34 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1591 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18591 | 2806 | 3359 | 2094 | 766 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2320 | 3211 | 9335 | 223 | 2026-06-08 23:39:53 |
| [httpx](https://github.com/encode/httpx) | 15289 | 1163 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14740 | 5755 | 11468 | 13847 | 1797 | 2026-06-09 02:08:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13903 | 2115 | 2653 | 1182 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13849 | 1882 | 5537 | 6604 | 1243 | 2026-06-08 22:02:51 |
| [starlette](https://github.com/Kludex/starlette) | 12373 | 1193 | 770 | 1938 | 59 | 2026-06-08 08:55:22 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11899 | 1695 | 8226 | 1108 | 214 | 2026-06-08 15:12:41 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11813 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 999 | 1127 | 1454 | 158 | 2026-06-08 18:21:50 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9082 | 597 | 1037 | 517 | 214 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7277 | 398 | 892 | 2551 | 321 | 2026-06-08 21:37:50 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5593 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5575 | 486 | 1257 | 849 | 517 | 2026-06-07 04:29:18 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5283 | 1018 | 914 | 300 | 212 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4182 | 337 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4002 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3639 | 200 | 283 | 128 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2750 | 311 | 666 | 1320 | 307 | 2026-06-06 13:02:09 |
| [anyio](https://github.com/agronholm/anyio) | 2479 | 207 | 441 | 648 | 84 | 2026-06-08 17:52:21 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1084 | 1540 | 363 | 2026-06-06 20:15:33 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-08 17:45:57 |
| [pypy](https://github.com/pypy/pypy) | 1747 | 113 | 5218 | 258 | 738 | 2026-06-08 20:15:25 |
| [jython](https://github.com/jython/jython) | 1515 | 230 | 297 | 135 | 110 | 2026-06-03 08:15:01 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 113 | 78 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-09T04:15:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
