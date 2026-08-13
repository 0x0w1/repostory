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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196982 | 76001 | 41678 | 79936 | 2827 | 2026-08-13 02:28:20 |
| [transformers](https://github.com/huggingface/transformers) | 164022 | 34225 | 19303 | 27896 | 2378 | 2026-08-12 23:11:45 |
| [pytorch](https://github.com/pytorch/pytorch) | 102351 | 28847 | 60307 | 132304 | 17127 | 2026-08-13 02:32:27 |
| [fastapi](https://github.com/fastapi/fastapi) | 101542 | 9774 | 3544 | 6223 | 73 | 2026-08-12 07:19:26 |
| [django](https://github.com/django/django) | 88414 | 34130 | 0 | 21652 | 456 | 2026-08-12 09:43:53 |
| [cpython](https://github.com/python/cpython) | 74298 | 35198 | 77639 | 75659 | 9502 | 2026-08-13 00:30:45 |
| [flask](https://github.com/pallets/flask) | 72186 | 16945 | 2763 | 2892 | 3 | 2026-08-11 22:32:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66967 | 27287 | 12241 | 21309 | 2125 | 2026-08-12 13:39:52 |
| [keras](https://github.com/keras-team/keras) | 64227 | 19753 | 12867 | 9696 | 215 | 2026-08-12 17:11:54 |
| [pandas](https://github.com/pandas-dev/pandas) | 49507 | 20270 | 28474 | 38160 | 2847 | 2026-08-13 00:21:51 |
| [ray](https://github.com/ray-project/ray) | 43504 | 7920 | 22936 | 42101 | 3474 | 2026-08-12 21:46:41 |
| [gym](https://github.com/openai/gym) | 37242 | 8684 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33813 | 4708 | 5770 | 4109 | 231 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32527 | 12624 | 14043 | 18136 | 2324 | 2026-08-12 22:18:10 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30129 | 7077 | 3966 | 5043 | 56 | 2026-08-12 11:26:08 |
| [celery](https://github.com/celery/celery) | 28785 | 5131 | 5293 | 4233 | 802 | 2026-08-10 16:55:09 |
| [dash](https://github.com/plotly/dash) | 24374 | 2312 | 2142 | 1678 | 537 | 2026-08-12 18:46:28 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23077 | 8434 | 11393 | 20746 | 1475 | 2026-08-12 05:48:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22275 | 1473 | 1420 | 7011 | 405 | 2026-08-12 22:24:50 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5552 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21986 | 8930 | 6116 | 8036 | 1546 | 2026-08-12 13:47:42 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18736 | 2833 | 3375 | 2137 | 774 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1596 | 1471 | 1701 | 144 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16521 | 2375 | 3236 | 9817 | 234 | 2026-08-12 15:19:33 |
| [httpx](https://github.com/encode/httpx) | 15411 | 1242 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14908 | 5861 | 11591 | 14288 | 1849 | 2026-08-12 23:42:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13993 | 2127 | 2658 | 1211 | 226 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13886 | 1925 | 5548 | 6691 | 1300 | 2026-08-10 22:03:29 |
| [starlette](https://github.com/Kludex/starlette) | 12539 | 1256 | 773 | 2025 | 62 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12074 | 1746 | 8262 | 1179 | 212 | 2026-08-12 22:47:35 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11883 | 613 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1025 | 1139 | 1498 | 159 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 605 | 1042 | 528 | 226 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8776 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7305 | 413 | 898 | 2588 | 321 | 2026-08-11 00:45:57 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5611 | 500 | 1266 | 885 | 541 | 2026-08-10 10:46:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5347 | 1033 | 929 | 316 | 204 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4316 | 363 | 1197 | 244 | 130 | 2026-08-12 14:11:42 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3997 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3657 | 202 | 284 | 133 | 37 | 2026-08-09 20:23:31 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2524 | 238 | 469 | 729 | 103 | 2026-08-13 00:13:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1583 | 356 | 2026-08-11 15:13:53 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-10 17:58:57 |
| [pypy](https://github.com/pypy/pypy) | 1782 | 121 | 5247 | 290 | 731 | 2026-08-13 01:03:18 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 300 | 149 | 97 | 2026-08-10 15:30:18 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-13T02:33:50*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
