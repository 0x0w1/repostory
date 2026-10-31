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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201236 | 78752 | 41933 | 84226 | 3461 | 2026-10-31 05:13:26 |
| [transformers](https://github.com/huggingface/transformers) | 168377 | 35056 | 19739 | 29648 | 1028 | 2026-10-31 03:23:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 105027 | 31884 | 62144 | 140026 | 17838 | 2026-10-31 05:08:19 |
| [fastapi](https://github.com/fastapi/fastapi) | 104300 | 10156 | 3556 | 6538 | 58 | 2026-10-30 20:31:56 |
| [django](https://github.com/django/django) | 91480 | 36556 | 0 | 22146 | 540 | 2026-10-31 02:48:02 |
| [cpython](https://github.com/python/cpython) | 77732 | 37725 | 79027 | 79575 | 9241 | 2026-10-31 01:56:21 |
| [flask](https://github.com/pallets/flask) | 74939 | 17225 | 2770 | 2913 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67943 | 27605 | 12354 | 21727 | 2165 | 2026-10-30 14:47:07 |
| [keras](https://github.com/keras-team/keras) | 64400 | 19813 | 13053 | 10180 | 271 | 2026-10-30 22:56:18 |
| [pandas](https://github.com/pandas-dev/pandas) | 50267 | 20690 | 28662 | 39761 | 2083 | 2026-10-30 19:04:51 |
| [ray](https://github.com/ray-project/ray) | 44170 | 8227 | 23273 | 43930 | 3699 | 2026-10-31 01:15:00 |
| [gym](https://github.com/openai/gym) | 37232 | 8664 | 1837 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34004 | 4739 | 5781 | 4139 | 261 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33210 | 13057 | 14158 | 18929 | 2235 | 2026-10-30 16:05:35 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30224 | 7093 | 3966 | 5103 | 66 | 2026-10-28 07:03:26 |
| [celery](https://github.com/celery/celery) | 29096 | 5254 | 5356 | 4667 | 744 | 2026-10-28 22:12:57 |
| [dash](https://github.com/plotly/dash) | 24473 | 2332 | 2170 | 1805 | 434 | 2026-10-30 16:13:22 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23401 | 8536 | 11456 | 21037 | 1481 | 2026-10-30 22:20:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22440 | 1506 | 1446 | 7943 | 294 | 2026-10-31 00:40:05 |
| [micropython](https://github.com/micropython/micropython) | 22174 | 9031 | 6152 | 8173 | 1549 | 2026-10-31 01:01:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5595 | 1888 | 1903 | 234 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18865 | 2884 | 3399 | 2262 | 745 | 2026-10-30 22:37:41 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16597 | 2496 | 3269 | 10572 | 268 | 2026-10-30 11:59:48 |
| [httpx](https://github.com/encode/httpx) | 15722 | 3243 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15168 | 6051 | 11737 | 14806 | 1894 | 2026-10-31 01:01:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14093 | 2153 | 2667 | 1247 | 257 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13941 | 2008 | 5580 | 6797 | 1414 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12698 | 1425 | 795 | 2292 | 61 | 2026-10-29 12:47:59 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12275 | 1838 | 8369 | 1253 | 213 | 2026-10-30 20:51:38 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11926 | 621 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9811 | 1049 | 1148 | 1559 | 160 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9229 | 622 | 1054 | 588 | 225 | 2026-10-30 18:52:47 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1515 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7358 | 464 | 906 | 2655 | 341 | 2026-10-30 17:17:14 |
| [hug](https://github.com/hugapi/hug) | 6873 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5639 | 540 | 1300 | 976 | 553 | 2026-10-31 04:22:39 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5439 | 1053 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4460 | 391 | 1211 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3679 | 209 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 678 | 1385 | 263 | 2026-10-30 18:39:53 |
| [anyio](https://github.com/agronholm/anyio) | 2566 | 341 | 493 | 875 | 143 | 2026-10-30 08:11:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1608 | 355 | 2026-10-30 11:34:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1791 | 278 | 279 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1822 | 130 | 5291 | 392 | 722 | 2026-10-30 07:28:57 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 155 | 101 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-31T05:16:00*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
