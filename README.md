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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195624 | 75175 | 41542 | 76052 | 3413 | 2026-06-13 04:38:42 |
| [transformers](https://github.com/huggingface/transformers) | 161550 | 33496 | 19060 | 26840 | 2423 | 2026-06-13 04:38:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 100702 | 27998 | 59227 | 127391 | 18385 | 2026-06-13 04:38:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 99155 | 9430 | 3534 | 5892 | 94 | 2026-06-10 23:14:27 |
| [django](https://github.com/django/django) | 87839 | 33856 | 0 | 21397 | 448 | 2026-06-11 20:27:10 |
| [cpython](https://github.com/python/cpython) | 73190 | 34729 | 76708 | 72386 | 9283 | 2026-06-12 16:11:06 |
| [flask](https://github.com/pallets/flask) | 71636 | 16872 | 2750 | 2836 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66311 | 27059 | 12135 | 20963 | 2059 | 2026-06-12 16:58:05 |
| [keras](https://github.com/keras-team/keras) | 64085 | 19733 | 12789 | 9439 | 176 | 2026-06-12 19:49:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 48967 | 20011 | 28314 | 37461 | 3219 | 2026-06-11 22:16:14 |
| [ray](https://github.com/ray-project/ray) | 42855 | 7674 | 22741 | 40943 | 3457 | 2026-06-13 01:11:25 |
| [gym](https://github.com/openai/gym) | 37224 | 8705 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33656 | 4687 | 5758 | 4096 | 211 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32181 | 12442 | 13940 | 17595 | 2384 | 2026-06-12 18:39:07 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30069 | 7069 | 3967 | 5013 | 78 | 2026-06-10 05:40:50 |
| [celery](https://github.com/celery/celery) | 28583 | 5073 | 5280 | 4144 | 781 | 2026-06-11 14:47:38 |
| [dash](https://github.com/plotly/dash) | 24257 | 2299 | 2106 | 1584 | 543 | 2026-06-11 16:47:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22881 | 8350 | 11309 | 20518 | 1452 | 2026-06-12 22:26:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22185 | 5533 | 1872 | 1744 | 217 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22114 | 1443 | 1355 | 6666 | 383 | 2026-06-12 19:43:55 |
| [micropython](https://github.com/micropython/micropython) | 21800 | 8863 | 6067 | 7870 | 1633 | 2026-06-12 08:01:36 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1591 | 1467 | 1689 | 132 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18601 | 2809 | 3360 | 2094 | 766 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16446 | 2327 | 3212 | 9368 | 224 | 2026-06-13 02:49:52 |
| [httpx](https://github.com/encode/httpx) | 15293 | 1171 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14749 | 5760 | 11475 | 13869 | 1799 | 2026-06-12 21:59:28 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13913 | 2119 | 2653 | 1184 | 223 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13848 | 1886 | 5539 | 6611 | 1244 | 2026-06-11 17:31:35 |
| [starlette](https://github.com/Kludex/starlette) | 12391 | 1199 | 770 | 1945 | 43 | 2026-06-12 09:20:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11907 | 1697 | 8228 | 1114 | 212 | 2026-06-12 20:08:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11818 | 609 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1001 | 1128 | 1460 | 160 | 2026-06-12 20:36:12 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9090 | 599 | 1039 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7281 | 399 | 892 | 2552 | 319 | 2026-06-09 06:57:17 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5593 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5578 | 486 | 1257 | 849 | 514 | 2026-06-10 08:36:34 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5292 | 1022 | 914 | 303 | 212 | 2026-06-09 07:01:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4194 | 339 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4002 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3642 | 201 | 283 | 129 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 311 | 666 | 1320 | 306 | 2026-06-11 12:40:47 |
| [anyio](https://github.com/agronholm/anyio) | 2479 | 207 | 443 | 649 | 85 | 2026-06-11 22:12:33 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 912 | 1084 | 1546 | 363 | 2026-06-12 17:54:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 364 | 1785 | 268 | 266 | 2026-06-08 17:45:57 |
| [pypy](https://github.com/pypy/pypy) | 1750 | 114 | 5220 | 261 | 735 | 2026-06-11 07:52:24 |
| [jython](https://github.com/jython/jython) | 1513 | 230 | 297 | 135 | 109 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-13T04:39:41*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
