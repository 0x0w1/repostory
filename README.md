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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195725 | 75194 | 41555 | 76405 | 3459 | 2026-06-18 04:46:17 |
| [transformers](https://github.com/huggingface/transformers) | 161683 | 33538 | 19087 | 26934 | 2438 | 2026-06-17 19:29:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 100844 | 28041 | 59316 | 127708 | 18321 | 2026-06-18 04:47:13 |
| [fastapi](https://github.com/fastapi/fastapi) | 99312 | 9447 | 3536 | 5929 | 90 | 2026-06-17 20:50:30 |
| [django](https://github.com/django/django) | 87868 | 33862 | 0 | 21444 | 455 | 2026-06-17 21:33:16 |
| [cpython](https://github.com/python/cpython) | 73267 | 34746 | 76759 | 72526 | 9300 | 2026-06-18 00:08:00 |
| [flask](https://github.com/pallets/flask) | 71652 | 16881 | 2752 | 2837 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66358 | 27072 | 12150 | 20998 | 2086 | 2026-06-17 14:46:09 |
| [keras](https://github.com/keras-team/keras) | 64094 | 19735 | 12794 | 9457 | 193 | 2026-06-18 00:22:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 49004 | 20020 | 28327 | 37481 | 3186 | 2026-06-17 21:42:33 |
| [ray](https://github.com/ray-project/ray) | 42921 | 7699 | 22752 | 41056 | 3484 | 2026-06-18 04:43:50 |
| [gym](https://github.com/openai/gym) | 37223 | 8703 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33663 | 4688 | 5759 | 4098 | 214 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32217 | 12456 | 13948 | 17646 | 2394 | 2026-06-18 04:38:30 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30078 | 7069 | 3967 | 5016 | 81 | 2026-06-16 19:13:19 |
| [celery](https://github.com/celery/celery) | 28600 | 5076 | 5280 | 4146 | 779 | 2026-06-16 11:48:20 |
| [dash](https://github.com/plotly/dash) | 24265 | 2300 | 2113 | 1589 | 554 | 2026-06-17 20:32:37 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22902 | 8356 | 11317 | 20540 | 1460 | 2026-06-18 04:04:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22183 | 5532 | 1873 | 1745 | 219 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22124 | 1443 | 1357 | 6698 | 383 | 2026-06-17 19:25:20 |
| [micropython](https://github.com/micropython/micropython) | 21813 | 8876 | 6069 | 7880 | 1637 | 2026-06-12 08:01:36 |
| [sanic](https://github.com/sanic-org/sanic) | 18626 | 1590 | 1467 | 1689 | 132 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18610 | 2812 | 3361 | 2095 | 765 | 2026-06-17 21:53:52 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16446 | 2330 | 3215 | 9400 | 226 | 2026-06-17 11:18:42 |
| [httpx](https://github.com/encode/httpx) | 15298 | 1173 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14758 | 5762 | 11482 | 13897 | 1805 | 2026-06-18 01:27:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13918 | 2118 | 2654 | 1185 | 225 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13846 | 1887 | 5539 | 6618 | 1245 | 2026-06-17 13:35:08 |
| [starlette](https://github.com/Kludex/starlette) | 12397 | 1203 | 770 | 1950 | 45 | 2026-06-17 09:45:13 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11926 | 1697 | 8231 | 1116 | 211 | 2026-06-15 20:29:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11820 | 610 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1002 | 1129 | 1465 | 161 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9097 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1503 | 864 | 635 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7279 | 398 | 892 | 2553 | 319 | 2026-06-16 05:03:49 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 737 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5586 | 489 | 1257 | 856 | 517 | 2026-06-17 15:57:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5296 | 1023 | 914 | 303 | 212 | 2026-06-09 07:01:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4209 | 341 | 1185 | 225 | 117 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4002 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 283 | 131 | 70 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 312 | 669 | 1332 | 308 | 2026-06-17 23:50:45 |
| [anyio](https://github.com/agronholm/anyio) | 2482 | 210 | 446 | 658 | 90 | 2026-06-15 21:59:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1084 | 1546 | 363 | 2026-06-12 17:54:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-15 17:49:21 |
| [pypy](https://github.com/pypy/pypy) | 1752 | 114 | 5223 | 261 | 734 | 2026-06-17 11:29:58 |
| [jython](https://github.com/jython/jython) | 1516 | 230 | 297 | 136 | 110 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-18T04:50:23*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
