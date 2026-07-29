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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196574 | 75641 | 41636 | 78989 | 2847 | 2026-07-29 03:24:07 |
| [transformers](https://github.com/huggingface/transformers) | 163080 | 34056 | 19243 | 27642 | 2345 | 2026-07-29 01:06:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 102047 | 28566 | 60066 | 130724 | 18337 | 2026-07-29 03:21:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 100998 | 9703 | 3542 | 6164 | 73 | 2026-07-28 15:36:47 |
| [django](https://github.com/django/django) | 88218 | 34012 | 0 | 21575 | 449 | 2026-07-28 20:24:39 |
| [cpython](https://github.com/python/cpython) | 73941 | 35031 | 77439 | 75060 | 9488 | 2026-07-28 22:46:43 |
| [flask](https://github.com/pallets/flask) | 72008 | 16923 | 2757 | 2876 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66807 | 27228 | 12204 | 21197 | 2104 | 2026-07-28 14:38:13 |
| [keras](https://github.com/keras-team/keras) | 64187 | 19740 | 12852 | 9627 | 218 | 2026-07-28 23:41:19 |
| [pandas](https://github.com/pandas-dev/pandas) | 49345 | 20182 | 28428 | 37981 | 2898 | 2026-07-29 03:22:06 |
| [ray](https://github.com/ray-project/ray) | 43374 | 7847 | 22886 | 41811 | 3493 | 2026-07-29 03:15:08 |
| [gym](https://github.com/openai/gym) | 37246 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33781 | 4699 | 5767 | 4106 | 229 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32449 | 12598 | 14026 | 18019 | 2328 | 2026-07-28 23:21:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30108 | 7075 | 3965 | 5035 | 72 | 2026-07-28 19:14:21 |
| [celery](https://github.com/celery/celery) | 28739 | 5116 | 5289 | 4202 | 789 | 2026-07-27 14:09:39 |
| [dash](https://github.com/plotly/dash) | 24353 | 2309 | 2132 | 1663 | 534 | 2026-07-28 20:06:05 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23043 | 8419 | 11376 | 20688 | 1470 | 2026-07-28 21:06:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 22228 | 1467 | 1403 | 6932 | 414 | 2026-07-28 01:20:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5549 | 1876 | 1800 | 249 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21941 | 8916 | 6110 | 7996 | 1575 | 2026-07-27 04:26:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18691 | 2827 | 3373 | 2124 | 777 | 2026-07-28 22:52:11 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1591 | 1470 | 1696 | 138 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16504 | 2358 | 3227 | 9703 | 215 | 2026-07-28 11:15:34 |
| [httpx](https://github.com/encode/httpx) | 15375 | 1223 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14862 | 5830 | 11549 | 14155 | 1841 | 2026-07-28 16:52:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13977 | 2128 | 2655 | 1205 | 220 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13871 | 1917 | 5545 | 6669 | 1276 | 2026-07-28 14:48:11 |
| [starlette](https://github.com/Kludex/starlette) | 12505 | 1246 | 772 | 1989 | 74 | 2026-07-28 10:44:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12031 | 1728 | 8250 | 1158 | 204 | 2026-07-28 21:16:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11868 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 1021 | 1139 | 1493 | 162 | 2026-07-27 04:23:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9154 | 602 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1502 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 410 | 898 | 2582 | 327 | 2026-07-27 21:57:27 |
| [hug](https://github.com/hugapi/hug) | 6885 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5607 | 501 | 1265 | 879 | 538 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5334 | 1028 | 924 | 315 | 199 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4285 | 355 | 1190 | 235 | 124 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4092 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3652 | 202 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2757 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2514 | 232 | 458 | 713 | 96 | 2026-07-27 23:44:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1580 | 358 | 2026-07-24 11:00:35 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-27 17:48:12 |
| [pypy](https://github.com/pypy/pypy) | 1772 | 121 | 5237 | 276 | 722 | 2026-07-28 05:44:02 |
| [jython](https://github.com/jython/jython) | 1526 | 230 | 299 | 147 | 105 | 2026-07-26 19:12:04 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-29T03:24:52*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
