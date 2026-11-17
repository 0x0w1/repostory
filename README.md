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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201613 | 77968 | 41979 | 84822 | 3440 | 2026-11-17 07:34:06 |
| [transformers](https://github.com/huggingface/transformers) | 169107 | 35219 | 19894 | 30103 | 1114 | 2026-11-17 06:22:50 |
| [pytorch](https://github.com/pytorch/pytorch) | 105604 | 30734 | 62697 | 141822 | 18363 | 2026-11-17 07:39:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 104830 | 10325 | 3555 | 6643 | 49 | 2026-11-16 09:50:09 |
| [django](https://github.com/django/django) | 91827 | 35209 | 0 | 22213 | 534 | 2026-11-16 16:18:34 |
| [cpython](https://github.com/python/cpython) | 78296 | 36602 | 79313 | 80420 | 9304 | 2026-11-17 05:43:03 |
| [flask](https://github.com/pallets/flask) | 75193 | 17339 | 2781 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68208 | 27688 | 12387 | 21840 | 2175 | 2026-11-17 03:14:32 |
| [keras](https://github.com/keras-team/keras) | 64424 | 19815 | 13090 | 10283 | 244 | 2026-11-17 00:32:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 50546 | 20744 | 28694 | 40069 | 1855 | 2026-11-16 21:57:14 |
| [ray](https://github.com/ray-project/ray) | 44301 | 8287 | 23328 | 44422 | 3808 | 2026-11-17 07:35:09 |
| [gym](https://github.com/openai/gym) | 37239 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34062 | 4741 | 5785 | 4152 | 275 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33392 | 13105 | 14191 | 19059 | 2253 | 2026-11-16 22:53:15 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30242 | 7102 | 3966 | 5114 | 62 | 2026-11-16 15:59:11 |
| [celery](https://github.com/celery/celery) | 29213 | 5265 | 5398 | 4745 | 814 | 2026-11-16 17:04:01 |
| [dash](https://github.com/plotly/dash) | 24491 | 2348 | 2182 | 1841 | 439 | 2026-11-16 18:46:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23468 | 8551 | 11465 | 21082 | 1482 | 2026-11-15 20:03:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22489 | 1510 | 1468 | 8329 | 311 | 2026-11-17 04:53:51 |
| [micropython](https://github.com/micropython/micropython) | 22205 | 9062 | 6181 | 8268 | 1604 | 2026-11-17 05:53:39 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5610 | 1896 | 1935 | 221 | 2026-11-17 02:46:28 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18908 | 2897 | 3404 | 2285 | 757 | 2026-11-16 19:36:16 |
| [sanic](https://github.com/sanic-org/sanic) | 18634 | 1618 | 1474 | 1690 | 164 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16608 | 2528 | 3278 | 10742 | 323 | 2026-11-16 16:26:08 |
| [httpx](https://github.com/encode/httpx) | 15798 | 1977 | 925 | 1813 | 140 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15222 | 6096 | 11776 | 14927 | 1914 | 2026-11-17 05:59:10 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14113 | 2164 | 2669 | 1261 | 260 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13954 | 2029 | 5583 | 6842 | 1431 | 2026-11-17 00:50:22 |
| [starlette](https://github.com/Kludex/starlette) | 12726 | 1447 | 799 | 2304 | 35 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12289 | 1933 | 8408 | 1264 | 217 | 2026-11-16 21:02:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11940 | 623 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9818 | 1056 | 1154 | 1580 | 163 | 2026-11-16 21:28:35 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9245 | 626 | 1057 | 617 | 159 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8802 | 1511 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7365 | 477 | 911 | 2674 | 346 | 2026-11-17 07:15:29 |
| [hug](https://github.com/hugapi/hug) | 6870 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 546 | 1310 | 993 | 559 | 2026-11-16 17:48:02 |
| [vibora](https://github.com/vibora-io/vibora) | 5578 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5454 | 1054 | 939 | 335 | 202 | 2026-11-14 15:09:10 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4482 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3984 | 343 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3684 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1424 | 257 | 2026-11-17 03:48:10 |
| [anyio](https://github.com/agronholm/anyio) | 2571 | 357 | 505 | 908 | 165 | 2026-11-17 00:12:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1950 | 372 | 1791 | 283 | 279 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1825 | 133 | 5303 | 443 | 723 | 2026-11-17 06:55:52 |
| [jython](https://github.com/jython/jython) | 1550 | 236 | 307 | 163 | 107 | 2026-11-16 18:03:33 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-17T07:40:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
