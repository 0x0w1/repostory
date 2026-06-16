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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195680 | 75186 | 41548 | 76230 | 3454 | 2026-06-16 05:18:40 |
| [transformers](https://github.com/huggingface/transformers) | 161620 | 33517 | 19075 | 26893 | 2438 | 2026-06-16 04:30:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 100804 | 28028 | 59273 | 127523 | 18351 | 2026-06-16 05:19:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 99227 | 9438 | 3536 | 5914 | 93 | 2026-06-15 22:12:19 |
| [django](https://github.com/django/django) | 87855 | 33862 | 0 | 21421 | 451 | 2026-06-15 21:41:18 |
| [cpython](https://github.com/python/cpython) | 73243 | 34742 | 76737 | 72461 | 9280 | 2026-06-16 04:51:39 |
| [flask](https://github.com/pallets/flask) | 71639 | 16877 | 2751 | 2836 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66344 | 27065 | 12141 | 20984 | 2078 | 2026-06-16 05:18:55 |
| [keras](https://github.com/keras-team/keras) | 64094 | 19737 | 12792 | 9449 | 186 | 2026-06-12 19:49:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 48986 | 20015 | 28319 | 37473 | 3198 | 2026-06-15 18:38:39 |
| [ray](https://github.com/ray-project/ray) | 42893 | 7689 | 22745 | 40996 | 3479 | 2026-06-16 04:42:55 |
| [gym](https://github.com/openai/gym) | 37223 | 8704 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33659 | 4687 | 5758 | 4097 | 212 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32205 | 12453 | 13945 | 17628 | 2397 | 2026-06-16 00:31:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30072 | 7069 | 3967 | 5014 | 79 | 2026-06-10 05:40:50 |
| [celery](https://github.com/celery/celery) | 28594 | 5073 | 5280 | 4145 | 779 | 2026-06-14 09:05:50 |
| [dash](https://github.com/plotly/dash) | 24258 | 2300 | 2108 | 1586 | 547 | 2026-06-15 22:52:05 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22888 | 8353 | 11316 | 20532 | 1463 | 2026-06-16 02:01:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22184 | 5531 | 1872 | 1745 | 218 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22119 | 1443 | 1357 | 6687 | 389 | 2026-06-15 13:38:07 |
| [micropython](https://github.com/micropython/micropython) | 21804 | 8870 | 6069 | 7876 | 1640 | 2026-06-12 08:01:36 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1591 | 1467 | 1689 | 132 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18604 | 2812 | 3361 | 2095 | 767 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16444 | 2328 | 3214 | 9391 | 220 | 2026-06-16 02:27:47 |
| [httpx](https://github.com/encode/httpx) | 15296 | 1170 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14753 | 5758 | 11478 | 13885 | 1802 | 2026-06-15 20:39:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13913 | 2120 | 2653 | 1185 | 224 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13845 | 1887 | 5539 | 6613 | 1245 | 2026-06-15 22:12:27 |
| [starlette](https://github.com/Kludex/starlette) | 12395 | 1200 | 770 | 1945 | 42 | 2026-06-12 09:20:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11917 | 1695 | 8228 | 1115 | 207 | 2026-06-15 20:29:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11818 | 609 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1002 | 1129 | 1463 | 160 | 2026-06-16 05:11:13 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9092 | 599 | 1039 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1503 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7279 | 398 | 892 | 2553 | 319 | 2026-06-16 05:03:49 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5593 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5581 | 489 | 1257 | 852 | 516 | 2026-06-15 13:33:40 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5293 | 1023 | 914 | 303 | 212 | 2026-06-09 07:01:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4202 | 341 | 1184 | 225 | 116 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4085 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4001 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 283 | 131 | 70 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 312 | 668 | 1324 | 309 | 2026-06-16 02:40:36 |
| [anyio](https://github.com/agronholm/anyio) | 2481 | 210 | 445 | 656 | 90 | 2026-06-15 21:59:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1084 | 1546 | 363 | 2026-06-12 17:54:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-15 17:49:21 |
| [pypy](https://github.com/pypy/pypy) | 1752 | 114 | 5222 | 261 | 734 | 2026-06-15 17:57:21 |
| [jython](https://github.com/jython/jython) | 1516 | 230 | 297 | 136 | 110 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-16T05:21:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
