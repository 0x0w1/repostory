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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195360 | 75333 | 41480 | 74985 | 3085 | 2026-06-02 04:50:06 |
| [transformers](https://github.com/huggingface/transformers) | 161182 | 33380 | 19019 | 26607 | 2394 | 2026-06-02 03:24:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 100322 | 27908 | 59007 | 126277 | 18298 | 2026-06-02 04:48:07 |
| [fastapi](https://github.com/fastapi/fastapi) | 98773 | 9375 | 3529 | 5855 | 91 | 2026-06-01 17:55:54 |
| [django](https://github.com/django/django) | 87610 | 33982 | 0 | 21333 | 449 | 2026-06-01 19:24:49 |
| [cpython](https://github.com/python/cpython) | 72942 | 34691 | 76571 | 71853 | 9307 | 2026-06-02 02:11:52 |
| [flask](https://github.com/pallets/flask) | 71597 | 16846 | 2738 | 2834 | 3 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66221 | 27052 | 12121 | 20877 | 2033 | 2026-06-02 01:51:18 |
| [keras](https://github.com/keras-team/keras) | 64080 | 19748 | 12771 | 9390 | 172 | 2026-06-02 02:03:01 |
| [pandas](https://github.com/pandas-dev/pandas) | 48889 | 19972 | 28298 | 37383 | 3232 | 2026-06-02 00:53:21 |
| [ray](https://github.com/ray-project/ray) | 42747 | 7628 | 22710 | 40689 | 3471 | 2026-06-02 03:59:17 |
| [gym](https://github.com/openai/gym) | 37203 | 8702 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33625 | 4687 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32130 | 12403 | 13930 | 17539 | 2384 | 2026-06-02 00:07:31 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30047 | 7064 | 3967 | 5007 | 76 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28541 | 5060 | 5279 | 4126 | 784 | 2026-05-30 08:13:32 |
| [dash](https://github.com/plotly/dash) | 24226 | 2285 | 2103 | 1576 | 543 | 2026-06-01 20:52:17 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22852 | 8348 | 11297 | 20442 | 1484 | 2026-05-30 18:51:37 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5540 | 1872 | 1739 | 217 | 2026-06-01 01:34:16 |
| [RustPython](https://github.com/RustPython/RustPython) | 22090 | 1443 | 1349 | 6587 | 384 | 2026-06-01 15:35:44 |
| [micropython](https://github.com/micropython/micropython) | 21765 | 8848 | 6064 | 7837 | 1707 | 2026-05-29 08:50:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1591 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18568 | 2805 | 3348 | 2090 | 757 | 2026-06-01 22:01:59 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16437 | 2285 | 3209 | 9213 | 234 | 2026-06-01 18:22:41 |
| [httpx](https://github.com/encode/httpx) | 15279 | 1161 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14724 | 5742 | 11458 | 13802 | 1790 | 2026-06-02 01:15:15 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13899 | 2117 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1880 | 5533 | 6596 | 1242 | 2026-06-01 23:20:55 |
| [starlette](https://github.com/Kludex/starlette) | 12355 | 1191 | 770 | 1929 | 59 | 2026-05-31 11:24:20 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11874 | 1693 | 8220 | 1100 | 213 | 2026-05-30 14:13:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11807 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 997 | 1126 | 1451 | 158 | 2026-06-01 11:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9076 | 589 | 1036 | 516 | 213 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1504 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7276 | 397 | 892 | 2549 | 319 | 2026-06-01 23:07:35 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 737 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5596 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5573 | 485 | 1257 | 843 | 514 | 2026-05-31 15:57:06 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5271 | 1017 | 914 | 299 | 211 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4169 | 336 | 1184 | 223 | 114 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3638 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2747 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2476 | 206 | 440 | 645 | 84 | 2026-06-01 21:48:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1530 | 373 | 2026-06-01 10:43:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-01 17:59:42 |
| [pypy](https://github.com/pypy/pypy) | 1743 | 113 | 5215 | 255 | 735 | 2026-06-01 21:52:08 |
| [jython](https://github.com/jython/jython) | 1512 | 230 | 296 | 135 | 111 | 2026-05-27 06:12:49 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 101 | 37 | 14 | 2026-06-02 00:24:41 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-02T04:51:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
