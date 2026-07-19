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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196358 | 75566 | 41613 | 78387 | 2811 | 2026-07-19 03:02:45 |
| [transformers](https://github.com/huggingface/transformers) | 162712 | 33933 | 19199 | 27477 | 2475 | 2026-07-17 16:52:51 |
| [pytorch](https://github.com/pytorch/pytorch) | 101764 | 28433 | 59909 | 129928 | 18336 | 2026-07-19 03:21:32 |
| [fastapi](https://github.com/fastapi/fastapi) | 100647 | 9639 | 3541 | 6107 | 95 | 2026-07-17 14:03:18 |
| [django](https://github.com/django/django) | 88170 | 34113 | 0 | 21568 | 453 | 2026-07-17 18:44:35 |
| [cpython](https://github.com/python/cpython) | 73809 | 34943 | 77248 | 74447 | 9474 | 2026-07-19 00:24:16 |
| [flask](https://github.com/pallets/flask) | 71976 | 16906 | 2756 | 2867 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66720 | 27198 | 12187 | 21142 | 2124 | 2026-07-18 13:40:04 |
| [keras](https://github.com/keras-team/keras) | 64167 | 19741 | 12841 | 9586 | 227 | 2026-07-17 21:24:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 49225 | 20140 | 28392 | 37863 | 2978 | 2026-07-17 23:48:21 |
| [ray](https://github.com/ray-project/ray) | 43277 | 7804 | 22857 | 41611 | 3477 | 2026-07-19 00:59:40 |
| [gym](https://github.com/openai/gym) | 37243 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33754 | 4693 | 5768 | 4103 | 227 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32392 | 12573 | 14007 | 17941 | 2371 | 2026-07-18 13:20:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30103 | 7073 | 3967 | 5027 | 85 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28697 | 5106 | 5288 | 4187 | 784 | 2026-07-16 06:44:39 |
| [dash](https://github.com/plotly/dash) | 24329 | 2307 | 2130 | 1648 | 535 | 2026-07-17 13:33:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23013 | 8405 | 11362 | 20645 | 1476 | 2026-07-19 02:37:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 22207 | 1466 | 1379 | 6865 | 397 | 2026-07-18 14:47:04 |
| [tornado](https://github.com/tornadoweb/tornado) | 22191 | 5540 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21906 | 8910 | 6100 | 7964 | 1583 | 2026-07-17 13:35:37 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18682 | 2827 | 3372 | 2112 | 778 | 2026-07-16 19:56:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18633 | 1587 | 1467 | 1692 | 133 | 2026-07-15 18:25:33 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16500 | 2351 | 3224 | 9598 | 220 | 2026-07-18 23:08:44 |
| [httpx](https://github.com/encode/httpx) | 15355 | 1208 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14827 | 5807 | 11535 | 14096 | 1849 | 2026-07-18 12:09:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13964 | 2127 | 2656 | 1204 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13862 | 1905 | 5541 | 6655 | 1264 | 2026-07-14 13:22:10 |
| [starlette](https://github.com/Kludex/starlette) | 12485 | 1230 | 771 | 1978 | 62 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12002 | 1716 | 8244 | 1143 | 207 | 2026-07-18 18:50:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11863 | 611 | 417 | 325 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 1021 | 1138 | 1485 | 173 | 2026-07-18 13:54:44 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9138 | 602 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1501 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7298 | 408 | 896 | 2573 | 327 | 2026-07-16 04:09:29 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 499 | 1264 | 875 | 533 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5325 | 1029 | 921 | 312 | 204 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4263 | 351 | 1189 | 233 | 125 | 2026-07-16 17:14:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 204 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2508 | 224 | 455 | 701 | 101 | 2026-07-18 09:29:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 913 | 1084 | 1572 | 361 | 2026-07-17 15:38:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 266 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1767 | 119 | 5237 | 271 | 724 | 2026-07-18 20:16:41 |
| [jython](https://github.com/jython/jython) | 1527 | 231 | 298 | 139 | 103 | 2026-07-13 11:30:52 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-19T03:37:05*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
