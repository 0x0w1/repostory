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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195115 | 75294 | 41437 | 73602 | 5237 | 2026-05-15 04:00:26 |
| [transformers](https://github.com/huggingface/transformers) | 160625 | 33212 | 18954 | 26350 | 2350 | 2026-05-15 01:52:44 |
| [pytorch](https://github.com/pytorch/pytorch) | 99916 | 27795 | 58701 | 124577 | 18470 | 2026-05-15 04:07:26 |
| [fastapi](https://github.com/fastapi/fastapi) | 98212 | 9290 | 3525 | 5728 | 201 | 2026-05-13 11:43:52 |
| [django](https://github.com/django/django) | 87487 | 33869 | 0 | 21221 | 427 | 2026-05-14 11:49:25 |
| [cpython](https://github.com/python/cpython) | 72698 | 34602 | 76365 | 71180 | 9314 | 2026-05-14 22:38:11 |
| [flask](https://github.com/pallets/flask) | 71537 | 16843 | 2736 | 2822 | 3 | 2026-05-13 14:37:58 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66084 | 27020 | 12084 | 20757 | 2019 | 2026-05-14 17:38:46 |
| [keras](https://github.com/keras-team/keras) | 64067 | 19774 | 12754 | 9314 | 184 | 2026-05-14 23:26:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 48767 | 19950 | 28278 | 37278 | 3279 | 2026-05-14 17:46:45 |
| [ray](https://github.com/ray-project/ray) | 42540 | 7565 | 22670 | 40314 | 3532 | 2026-05-15 02:26:02 |
| [gym](https://github.com/openai/gym) | 37199 | 8701 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33574 | 4685 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 32035 | 12371 | 13918 | 17445 | 2372 | 2026-05-14 18:52:27 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30011 | 7064 | 3967 | 5005 | 75 | 2026-05-14 08:01:41 |
| [celery](https://github.com/celery/celery) | 28487 | 5041 | 5275 | 4108 | 772 | 2026-05-14 04:34:35 |
| [dash](https://github.com/plotly/dash) | 24181 | 2282 | 2097 | 1563 | 552 | 2026-05-14 17:13:28 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22799 | 8336 | 11265 | 20348 | 1488 | 2026-05-15 00:39:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5542 | 1871 | 1733 | 220 | 2026-05-12 15:07:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 22047 | 1437 | 1341 | 6460 | 371 | 2026-05-14 04:13:41 |
| [micropython](https://github.com/micropython/micropython) | 21703 | 8830 | 6055 | 7796 | 1762 | 2026-05-15 03:28:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1588 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18524 | 2805 | 3344 | 2084 | 758 | 2026-05-13 21:56:53 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16435 | 2264 | 3193 | 9010 | 254 | 2026-05-15 02:33:59 |
| [httpx](https://github.com/encode/httpx) | 15265 | 1142 | 0 | 1805 | 146 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14691 | 5721 | 11439 | 13679 | 1783 | 2026-05-14 20:59:12 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13869 | 2113 | 2653 | 1180 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13832 | 1871 | 5525 | 6566 | 1240 | 2026-05-14 21:18:18 |
| [starlette](https://github.com/Kludex/starlette) | 12311 | 1170 | 766 | 1893 | 59 | 2026-05-14 21:50:25 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11851 | 1685 | 8207 | 1081 | 221 | 2026-05-12 13:03:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11783 | 606 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9053 | 579 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8766 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7261 | 394 | 892 | 2542 | 320 | 2026-05-11 22:08:12 |
| [hug](https://github.com/hugapi/hug) | 6892 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5598 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5567 | 481 | 1252 | 830 | 502 | 2026-05-15 00:37:02 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5254 | 1015 | 912 | 299 | 209 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4133 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3634 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2743 | 311 | 663 | 1314 | 306 | 2026-05-13 00:38:23 |
| [anyio](https://github.com/agronholm/anyio) | 2463 | 206 | 438 | 633 | 83 | 2026-05-12 20:41:10 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1501 | 361 | 2026-05-13 09:07:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1729 | 112 | 5206 | 243 | 737 | 2026-05-14 10:43:02 |
| [jython](https://github.com/jython/jython) | 1509 | 231 | 295 | 129 | 114 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-15T04:08:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
