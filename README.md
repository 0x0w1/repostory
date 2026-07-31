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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196617 | 75723 | 41647 | 79175 | 2901 | 2026-07-31 03:38:39 |
| [transformers](https://github.com/huggingface/transformers) | 163187 | 34084 | 19248 | 27678 | 2332 | 2026-07-30 18:50:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 102080 | 28611 | 60107 | 130952 | 18387 | 2026-07-31 03:35:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 101076 | 9715 | 3542 | 6173 | 73 | 2026-07-29 17:17:25 |
| [django](https://github.com/django/django) | 88237 | 34040 | 0 | 21589 | 449 | 2026-07-30 20:38:25 |
| [cpython](https://github.com/python/cpython) | 73979 | 35067 | 77466 | 75152 | 9496 | 2026-07-31 01:28:21 |
| [flask](https://github.com/pallets/flask) | 72014 | 16923 | 2757 | 2880 | 7 | 2026-07-30 17:29:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66835 | 27237 | 12206 | 21211 | 2107 | 2026-07-30 04:27:49 |
| [keras](https://github.com/keras-team/keras) | 64190 | 19743 | 12853 | 9641 | 211 | 2026-07-31 02:55:19 |
| [pandas](https://github.com/pandas-dev/pandas) | 49367 | 20206 | 28441 | 38008 | 2923 | 2026-07-30 17:56:39 |
| [ray](https://github.com/ray-project/ray) | 43397 | 7862 | 22889 | 41849 | 3491 | 2026-07-31 03:00:38 |
| [gym](https://github.com/openai/gym) | 37249 | 8686 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33788 | 4697 | 5767 | 4106 | 229 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32461 | 12600 | 14029 | 18037 | 2319 | 2026-07-31 02:50:18 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30115 | 7075 | 3965 | 5036 | 69 | 2026-07-30 07:16:57 |
| [celery](https://github.com/celery/celery) | 28743 | 5118 | 5289 | 4204 | 790 | 2026-07-30 22:14:01 |
| [dash](https://github.com/plotly/dash) | 24359 | 2311 | 2134 | 1666 | 535 | 2026-07-30 18:21:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23050 | 8420 | 11381 | 20696 | 1471 | 2026-07-31 02:10:32 |
| [RustPython](https://github.com/RustPython/RustPython) | 22229 | 1468 | 1406 | 6939 | 409 | 2026-07-30 13:13:22 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5548 | 1876 | 1800 | 249 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21946 | 8913 | 6110 | 8003 | 1568 | 2026-07-31 03:37:40 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18699 | 2829 | 3374 | 2125 | 773 | 2026-07-30 17:03:48 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1593 | 1471 | 1699 | 142 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16505 | 2359 | 3227 | 9712 | 217 | 2026-07-30 11:22:30 |
| [httpx](https://github.com/encode/httpx) | 15379 | 1226 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14869 | 5837 | 11551 | 14177 | 1843 | 2026-07-31 02:45:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13983 | 2129 | 2655 | 1206 | 221 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13872 | 1920 | 5545 | 6675 | 1282 | 2026-07-28 14:48:11 |
| [starlette](https://github.com/Kludex/starlette) | 12506 | 1251 | 772 | 1990 | 74 | 2026-07-28 10:44:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12039 | 1732 | 8253 | 1161 | 209 | 2026-07-28 21:16:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11871 | 613 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 1021 | 1139 | 1493 | 162 | 2026-07-27 04:23:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9156 | 602 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1500 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7307 | 410 | 898 | 2582 | 325 | 2026-07-30 16:22:45 |
| [hug](https://github.com/hugapi/hug) | 6886 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5605 | 502 | 1265 | 879 | 538 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5336 | 1028 | 924 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4290 | 357 | 1190 | 237 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 203 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2516 | 234 | 461 | 719 | 101 | 2026-07-30 21:51:12 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1084 | 1581 | 357 | 2026-07-29 16:59:19 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 367 | 1785 | 269 | 267 | 2026-07-27 17:48:12 |
| [pypy](https://github.com/pypy/pypy) | 1778 | 121 | 5243 | 280 | 729 | 2026-07-30 14:48:56 |
| [jython](https://github.com/jython/jython) | 1528 | 230 | 299 | 148 | 106 | 2026-07-26 19:12:04 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-31T03:39:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
