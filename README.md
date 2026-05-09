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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195036 | 75267 | 41382 | 73123 | 5004 | 2026-05-09 03:04:35 |
| [transformers](https://github.com/huggingface/transformers) | 160405 | 33145 | 18939 | 26259 | 2351 | 2026-05-08 19:23:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 99770 | 27722 | 58594 | 123895 | 18528 | 2026-05-09 03:42:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 98029 | 9220 | 3524 | 5710 | 189 | 2026-05-08 15:55:13 |
| [django](https://github.com/django/django) | 87440 | 33844 | 0 | 21189 | 427 | 2026-05-08 17:41:14 |
| [cpython](https://github.com/python/cpython) | 72619 | 34565 | 76298 | 70992 | 9302 | 2026-05-09 00:28:21 |
| [flask](https://github.com/pallets/flask) | 71499 | 16834 | 2736 | 2818 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66009 | 26996 | 12070 | 20713 | 2020 | 2026-05-08 14:21:03 |
| [keras](https://github.com/keras-team/keras) | 64062 | 19767 | 12749 | 9298 | 198 | 2026-05-08 21:41:18 |
| [pandas](https://github.com/pandas-dev/pandas) | 48695 | 19919 | 28275 | 37190 | 3361 | 2026-05-09 00:09:46 |
| [ray](https://github.com/ray-project/ray) | 42467 | 7535 | 22658 | 40233 | 3541 | 2026-05-09 03:41:26 |
| [gym](https://github.com/openai/gym) | 37185 | 8702 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33557 | 4681 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31993 | 12347 | 13907 | 17426 | 2366 | 2026-05-08 20:04:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29999 | 7066 | 3967 | 5005 | 78 | 2026-05-06 11:55:49 |
| [celery](https://github.com/celery/celery) | 28458 | 5035 | 5273 | 4107 | 776 | 2026-05-07 22:19:07 |
| [dash](https://github.com/plotly/dash) | 24158 | 2277 | 2095 | 1554 | 546 | 2026-05-08 22:47:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22778 | 8327 | 11263 | 20320 | 1486 | 2026-05-08 22:16:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5541 | 1871 | 1729 | 218 | 2026-05-07 19:07:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 22038 | 1436 | 1340 | 6389 | 379 | 2026-05-08 23:54:07 |
| [micropython](https://github.com/micropython/micropython) | 21684 | 8817 | 6049 | 7783 | 1771 | 2026-05-08 14:48:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1588 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18508 | 2802 | 3343 | 2082 | 764 | 2026-05-08 17:08:49 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16426 | 2262 | 3191 | 8968 | 265 | 2026-05-09 02:54:08 |
| [httpx](https://github.com/encode/httpx) | 15258 | 1141 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14676 | 5720 | 11433 | 13655 | 1781 | 2026-05-08 22:48:25 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13848 | 2111 | 2653 | 1180 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13825 | 1870 | 5525 | 6554 | 1247 | 2026-05-08 17:04:32 |
| [starlette](https://github.com/Kludex/starlette) | 12291 | 1167 | 766 | 1886 | 56 | 2026-05-03 06:45:09 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11836 | 1683 | 8204 | 1076 | 217 | 2026-05-07 20:09:21 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11783 | 605 | 414 | 323 | 154 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9044 | 576 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8762 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7259 | 393 | 891 | 2540 | 320 | 2026-05-01 17:34:53 |
| [hug](https://github.com/hugapi/hug) | 6893 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5566 | 479 | 1250 | 825 | 502 | 2026-05-07 14:02:10 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5250 | 1013 | 912 | 294 | 205 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4125 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4083 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3630 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2741 | 311 | 663 | 1310 | 305 | 2026-05-08 01:06:34 |
| [anyio](https://github.com/agronholm/anyio) | 2460 | 203 | 438 | 623 | 85 | 2026-05-07 20:49:46 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 907 | 1084 | 1497 | 362 | 2026-05-06 11:00:56 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1722 | 112 | 5206 | 240 | 739 | 2026-05-08 15:37:04 |
| [jython](https://github.com/jython/jython) | 1507 | 229 | 294 | 128 | 112 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-09T03:45:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
