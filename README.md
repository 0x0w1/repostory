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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201285 | 78705 | 41922 | 84055 | 3405 | 2026-10-27 04:27:13 |
| [transformers](https://github.com/huggingface/transformers) | 168222 | 35003 | 19698 | 29503 | 1009 | 2026-10-27 03:18:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 105108 | 31800 | 62021 | 139469 | 17837 | 2026-10-27 04:35:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 104243 | 10134 | 3556 | 6530 | 58 | 2026-10-26 20:54:19 |
| [django](https://github.com/django/django) | 91678 | 36503 | 0 | 22121 | 534 | 2026-10-26 19:58:25 |
| [cpython](https://github.com/python/cpython) | 77778 | 37627 | 78910 | 79296 | 9244 | 2026-10-26 22:09:33 |
| [flask](https://github.com/pallets/flask) | 75105 | 17153 | 2769 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67945 | 27593 | 12347 | 21696 | 2173 | 2026-10-26 14:13:29 |
| [keras](https://github.com/keras-team/keras) | 64391 | 19803 | 13041 | 10159 | 271 | 2026-10-26 20:40:53 |
| [pandas](https://github.com/pandas-dev/pandas) | 50305 | 20620 | 28654 | 39720 | 2121 | 2026-10-27 00:45:07 |
| [ray](https://github.com/ray-project/ray) | 44129 | 8206 | 23256 | 43757 | 3638 | 2026-10-27 04:05:12 |
| [gym](https://github.com/openai/gym) | 37237 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33997 | 4736 | 5780 | 4137 | 261 | 2026-10-27 00:10:55 |
| [numpy](https://github.com/numpy/numpy) | 33176 | 12998 | 14151 | 18898 | 2241 | 2026-10-26 08:18:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30218 | 7098 | 3966 | 5100 | 65 | 2026-10-20 19:14:36 |
| [celery](https://github.com/celery/celery) | 29079 | 5252 | 5354 | 4651 | 741 | 2026-10-26 22:14:06 |
| [dash](https://github.com/plotly/dash) | 24471 | 2331 | 2168 | 1792 | 432 | 2026-10-26 17:44:54 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23395 | 8531 | 11452 | 21021 | 1480 | 2026-10-23 19:17:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 22428 | 1507 | 1446 | 7856 | 293 | 2026-10-27 04:29:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22168 | 5594 | 1888 | 1901 | 233 | 2026-10-26 21:18:33 |
| [micropython](https://github.com/micropython/micropython) | 22157 | 9017 | 6151 | 8161 | 1554 | 2026-10-26 01:04:23 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18855 | 2882 | 3397 | 2253 | 743 | 2026-10-23 23:43:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16594 | 2493 | 3269 | 10524 | 264 | 2026-10-26 23:03:52 |
| [httpx](https://github.com/encode/httpx) | 15818 | 3251 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15155 | 6034 | 11723 | 14769 | 1873 | 2026-10-26 22:58:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14087 | 2151 | 2667 | 1246 | 256 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13939 | 2005 | 5578 | 6791 | 1406 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12686 | 1413 | 794 | 2273 | 44 | 2026-10-24 17:17:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12266 | 1834 | 8362 | 1244 | 213 | 2026-10-26 21:20:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11916 | 621 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1049 | 1148 | 1558 | 159 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9222 | 621 | 1054 | 579 | 242 | 2026-10-26 15:23:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8800 | 1517 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7355 | 462 | 906 | 2649 | 341 | 2026-10-24 14:32:28 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 536 | 1300 | 970 | 555 | 2026-10-25 16:05:18 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5435 | 1052 | 938 | 327 | 206 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4458 | 390 | 1209 | 259 | 117 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 896 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 275 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 677 | 1379 | 264 | 2026-10-25 19:28:52 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 330 | 493 | 873 | 143 | 2026-10-26 22:05:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2357 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1606 | 355 | 2026-10-26 14:24:50 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 369 | 1791 | 276 | 277 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1821 | 131 | 5287 | 380 | 718 | 2026-10-26 18:04:14 |
| [jython](https://github.com/jython/jython) | 1551 | 231 | 305 | 155 | 101 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-27T04:45:13*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
