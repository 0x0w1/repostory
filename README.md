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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194980 | 75342 | 41352 | 72710 | 4887 | 2026-05-04 03:25:34 |
| [transformers](https://github.com/huggingface/transformers) | 160216 | 33100 | 18925 | 26191 | 2361 | 2026-05-04 03:47:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 99603 | 27646 | 58395 | 123338 | 18504 | 2026-05-04 02:55:02 |
| [fastapi](https://github.com/fastapi/fastapi) | 97861 | 9189 | 3524 | 5697 | 186 | 2026-05-03 13:45:04 |
| [django](https://github.com/django/django) | 87392 | 33913 | 0 | 21158 | 435 | 2026-05-02 12:19:54 |
| [cpython](https://github.com/python/cpython) | 72561 | 34550 | 76224 | 70822 | 9355 | 2026-05-04 00:30:24 |
| [flask](https://github.com/pallets/flask) | 71480 | 16828 | 2736 | 2817 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65967 | 26992 | 12065 | 20690 | 2066 | 2026-05-01 17:48:25 |
| [keras](https://github.com/keras-team/keras) | 64054 | 19760 | 12745 | 9274 | 242 | 2026-05-01 23:22:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 48652 | 19899 | 28265 | 37107 | 3386 | 2026-05-03 17:38:52 |
| [ray](https://github.com/ray-project/ray) | 42414 | 7524 | 22635 | 40101 | 3556 | 2026-05-03 14:19:18 |
| [gym](https://github.com/openai/gym) | 37180 | 8704 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33540 | 4679 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31954 | 12329 | 13900 | 17405 | 2369 | 2026-05-04 01:55:10 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29991 | 7068 | 3967 | 5004 | 78 | 2026-04-28 07:27:54 |
| [celery](https://github.com/celery/celery) | 28426 | 5027 | 5272 | 4098 | 776 | 2026-05-03 02:58:10 |
| [dash](https://github.com/plotly/dash) | 24172 | 2277 | 2092 | 1547 | 542 | 2026-05-01 21:47:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22764 | 8323 | 11260 | 20293 | 1495 | 2026-05-02 12:37:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22214 | 5542 | 1871 | 1728 | 218 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22032 | 1433 | 1340 | 6360 | 370 | 2026-05-04 01:28:43 |
| [micropython](https://github.com/micropython/micropython) | 21675 | 8812 | 6042 | 7767 | 1805 | 2026-05-01 12:38:24 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18498 | 2804 | 3342 | 2080 | 762 | 2026-05-01 19:02:48 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16428 | 2263 | 3192 | 8924 | 263 | 2026-05-04 02:53:35 |
| [httpx](https://github.com/encode/httpx) | 15256 | 1137 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14658 | 5717 | 11429 | 13641 | 1785 | 2026-05-03 21:54:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13837 | 2105 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13820 | 1868 | 5522 | 6536 | 1247 | 2026-04-28 16:39:15 |
| [starlette](https://github.com/Kludex/starlette) | 12273 | 1168 | 766 | 1886 | 56 | 2026-05-03 06:45:09 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11818 | 1675 | 8202 | 1071 | 216 | 2026-05-03 19:29:36 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11779 | 605 | 413 | 323 | 157 | 2026-05-02 15:22:41 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 998 | 1125 | 1445 | 158 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9034 | 574 | 1033 | 510 | 207 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8759 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7256 | 393 | 891 | 2540 | 320 | 2026-05-01 17:34:53 |
| [hug](https://github.com/hugapi/hug) | 6892 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5564 | 480 | 1249 | 825 | 506 | 2026-05-01 04:21:03 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5247 | 1009 | 912 | 292 | 203 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4113 | 331 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 893 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3630 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2739 | 311 | 663 | 1309 | 306 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2454 | 201 | 436 | 620 | 82 | 2026-05-03 20:13:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 907 | 1084 | 1489 | 361 | 2026-05-01 12:01:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 266 | 2026-04-27 17:52:32 |
| [pypy](https://github.com/pypy/pypy) | 1719 | 112 | 5205 | 236 | 739 | 2026-05-03 17:26:47 |
| [jython](https://github.com/jython/jython) | 1506 | 228 | 294 | 127 | 111 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-04T03:57:21*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
