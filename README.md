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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191627 | 74830 | 40787 | 57491 | 1724 | 2025-09-14 01:16:57 |
| [transformers](https://github.com/huggingface/transformers) | 149655 | 30379 | 17918 | 22377 | 1998 | 2025-09-13 14:27:17 |
| [pytorch](https://github.com/pytorch/pytorch) | 93149 | 25262 | 53725 | 108716 | 17092 | 2025-09-14 01:31:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 89452 | 7870 | 3467 | 4714 | 244 | 2025-09-12 08:21:56 |
| [django](https://github.com/django/django) | 84974 | 32948 | 0 | 19795 | 372 | 2025-09-13 22:28:51 |
| [flask](https://github.com/pallets/flask) | 70343 | 16530 | 2694 | 2702 | 8 | 2025-09-12 21:52:55 |
| [cpython](https://github.com/python/cpython) | 68860 | 32855 | 73585 | 64380 | 9337 | 2025-09-13 20:37:08 |
| [keras](https://github.com/keras-team/keras) | 63402 | 19625 | 12544 | 8334 | 269 | 2025-09-11 18:42:15 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63332 | 26228 | 11707 | 19344 | 2164 | 2025-09-12 12:39:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 46566 | 18906 | 27706 | 34579 | 3659 | 2025-09-13 06:22:04 |
| [ray](https://github.com/ray-project/ray) | 38913 | 6790 | 21087 | 35074 | 3054 | 2025-09-14 01:02:25 |
| [gym](https://github.com/openai/gym) | 36504 | 8692 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32471 | 4580 | 5721 | 4069 | 204 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30395 | 11345 | 13540 | 16149 | 2365 | 2025-09-13 18:16:21 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29463 | 7003 | 3945 | 4831 | 101 | 2025-09-08 19:44:29 |
| [celery](https://github.com/celery/celery) | 27182 | 4841 | 5161 | 3653 | 755 | 2025-09-09 12:10:28 |
| [dash](https://github.com/plotly/dash) | 24044 | 2200 | 1990 | 1329 | 559 | 2025-09-11 22:46:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5538 | 1852 | 1674 | 209 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21692 | 7996 | 10978 | 19532 | 1646 | 2025-09-11 21:18:41 |
| [micropython](https://github.com/micropython/micropython) | 20813 | 8425 | 5807 | 7173 | 1777 | 2025-09-11 04:26:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 20513 | 1343 | 1220 | 4864 | 441 | 2025-09-13 12:25:48 |
| [sanic](https://github.com/sanic-org/sanic) | 18494 | 1580 | 1450 | 1625 | 143 | 2025-09-08 03:48:03 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17725 | 2708 | 3250 | 1950 | 721 | 2025-09-12 15:13:22 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15980 | 2122 | 3145 | 8062 | 275 | 2025-09-12 10:28:26 |
| [httpx](https://github.com/encode/httpx) | 14544 | 954 | 918 | 1724 | 104 | 2025-09-12 11:19:51 |
| [scipy](https://github.com/scipy/scipy) | 14021 | 5472 | 11026 | 12570 | 1766 | 2025-09-13 21:42:49 |
| [dask](https://github.com/dask/dask) | 13481 | 1796 | 5436 | 6342 | 1202 | 2025-09-10 10:09:44 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13433 | 2033 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11452 | 1035 | 753 | 1703 | 49 | 2025-09-13 10:21:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11249 | 571 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10884 | 1579 | 8082 | 981 | 232 | 2025-09-13 13:55:32 |
| [falcon](https://github.com/falconry/falcon) | 9716 | 959 | 1099 | 1368 | 158 | 2025-09-10 04:12:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8658 | 1488 | 855 | 622 | 284 | 2025-09-13 12:31:44 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8531 | 522 | 942 | 434 | 410 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6894 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6855 | 367 | 867 | 2449 | 309 | 2025-09-10 06:28:43 |
| [eve](https://github.com/pyeve/eve) | 6734 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5286 | 437 | 1191 | 713 | 499 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4980 | 938 | 868 | 260 | 165 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4047 | 889 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3598 | 291 | 1157 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3445 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2684 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2305 | 131 | 426 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2206 | 163 | 400 | 506 | 66 | 2025-09-13 17:54:23 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-09-08 17:38:35 |
| [pypy](https://github.com/pypy/pypy) | 1496 | 85 | 5143 | 168 | 734 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1431 | 220 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-14T02:00:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
