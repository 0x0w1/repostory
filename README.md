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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194855 | 75280 | 41326 | 71907 | 4651 | 2026-04-24 03:33:22 |
| [transformers](https://github.com/huggingface/transformers) | 159843 | 32997 | 18891 | 26071 | 2341 | 2026-04-23 20:07:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 99395 | 27575 | 58208 | 122590 | 18533 | 2026-04-24 03:34:47 |
| [fastapi](https://github.com/fastapi/fastapi) | 97582 | 9142 | 3522 | 5656 | 173 | 2026-04-23 16:49:26 |
| [django](https://github.com/django/django) | 87324 | 33825 | 0 | 21092 | 432 | 2026-04-23 08:54:14 |
| [cpython](https://github.com/python/cpython) | 72435 | 34478 | 76085 | 70567 | 9409 | 2026-04-23 19:30:14 |
| [flask](https://github.com/pallets/flask) | 71441 | 16810 | 2735 | 2811 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65902 | 26974 | 12051 | 20626 | 2052 | 2026-04-23 21:17:08 |
| [keras](https://github.com/keras-team/keras) | 64030 | 19763 | 12739 | 9222 | 279 | 2026-04-24 01:34:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 48559 | 19877 | 28254 | 37018 | 3414 | 2026-04-23 17:19:17 |
| [ray](https://github.com/ray-project/ray) | 42283 | 7493 | 22604 | 39943 | 3580 | 2026-04-24 03:14:23 |
| [gym](https://github.com/openai/gym) | 37175 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33502 | 4676 | 5754 | 4091 | 202 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31879 | 12311 | 13890 | 17354 | 2367 | 2026-04-23 22:44:02 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29986 | 7066 | 3968 | 5002 | 80 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28401 | 5019 | 5270 | 4089 | 775 | 2026-04-23 22:23:41 |
| [dash](https://github.com/plotly/dash) | 24145 | 2277 | 2091 | 1543 | 542 | 2026-04-23 21:31:39 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22730 | 8325 | 11248 | 20256 | 1493 | 2026-04-23 23:19:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22222 | 5542 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22023 | 1429 | 1335 | 6258 | 376 | 2026-04-24 00:10:32 |
| [micropython](https://github.com/micropython/micropython) | 21651 | 8804 | 6039 | 7749 | 1882 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18472 | 2803 | 3340 | 2078 | 763 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16411 | 2257 | 3191 | 8901 | 281 | 2026-04-23 11:55:35 |
| [httpx](https://github.com/encode/httpx) | 15220 | 1124 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14629 | 5709 | 11424 | 13622 | 1787 | 2026-04-23 07:15:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13828 | 2103 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13806 | 1868 | 5522 | 6532 | 1247 | 2026-04-22 10:20:36 |
| [starlette](https://github.com/Kludex/starlette) | 12231 | 1160 | 766 | 1880 | 56 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11790 | 1674 | 8198 | 1063 | 219 | 2026-04-22 13:01:43 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11766 | 605 | 412 | 321 | 165 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 988 | 1122 | 1434 | 154 | 2026-04-23 18:19:06 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9025 | 571 | 1032 | 505 | 202 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8753 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7247 | 392 | 890 | 2536 | 320 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6895 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6734 | 733 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5557 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5243 | 1008 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4090 | 330 | 1183 | 218 | 116 | 2026-04-20 21:11:28 |
| [pyramid](https://github.com/Pylons/pyramid) | 4081 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3626 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2444 | 199 | 434 | 614 | 85 | 2026-04-21 12:21:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 904 | 1083 | 1472 | 367 | 2026-04-23 09:38:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1712 | 111 | 5200 | 226 | 747 | 2026-04-23 21:02:44 |
| [jython](https://github.com/jython/jython) | 1501 | 228 | 294 | 127 | 112 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-24T03:38:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
