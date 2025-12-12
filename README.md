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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192757 | 75044 | 41034 | 62945 | 2759 | 2025-12-12 02:03:32 |
| [transformers](https://github.com/huggingface/transformers) | 153761 | 31395 | 18321 | 23903 | 2161 | 2025-12-11 23:41:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 95796 | 26187 | 55812 | 113964 | 17862 | 2025-12-12 02:11:50 |
| [fastapi](https://github.com/fastapi/fastapi) | 93001 | 8350 | 3499 | 4960 | 184 | 2025-12-11 21:25:28 |
| [django](https://github.com/django/django) | 86124 | 33301 | 0 | 20329 | 365 | 2025-12-11 17:59:59 |
| [flask](https://github.com/pallets/flask) | 70920 | 16648 | 2704 | 2732 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70255 | 33645 | 74642 | 66991 | 9250 | 2025-12-12 01:37:47 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64261 | 26504 | 11845 | 19908 | 2123 | 2025-12-11 02:07:51 |
| [keras](https://github.com/keras-team/keras) | 63630 | 19651 | 12604 | 8524 | 260 | 2025-12-11 23:41:35 |
| [pandas](https://github.com/pandas-dev/pandas) | 47299 | 19386 | 27949 | 35327 | 3586 | 2025-12-11 02:22:05 |
| [ray](https://github.com/ray-project/ray) | 40271 | 6995 | 22007 | 37041 | 3204 | 2025-12-12 01:53:11 |
| [gym](https://github.com/openai/gym) | 36859 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32943 | 4635 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30992 | 11826 | 13694 | 16664 | 2382 | 2025-12-12 00:14:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29723 | 7041 | 3946 | 4884 | 79 | 2025-12-09 17:27:43 |
| [celery](https://github.com/celery/celery) | 27704 | 4914 | 5179 | 3740 | 753 | 2025-12-09 10:17:07 |
| [dash](https://github.com/plotly/dash) | 24330 | 2243 | 2035 | 1386 | 556 | 2025-12-05 17:17:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22382 | 5544 | 1858 | 1687 | 207 | 2025-12-11 14:59:09 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22108 | 8138 | 11072 | 19724 | 1577 | 2025-12-12 00:09:43 |
| [micropython](https://github.com/micropython/micropython) | 21193 | 8582 | 5893 | 7426 | 1799 | 2025-12-09 14:49:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 20881 | 1370 | 1244 | 5101 | 443 | 2025-12-12 01:37:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18595 | 1584 | 1454 | 1635 | 128 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18076 | 2761 | 3305 | 1992 | 754 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16140 | 2167 | 3165 | 8363 | 271 | 2025-12-11 10:32:39 |
| [httpx](https://github.com/encode/httpx) | 14830 | 988 | 923 | 1763 | 112 | 2025-12-10 15:17:09 |
| [scipy](https://github.com/scipy/scipy) | 14252 | 5557 | 11181 | 12947 | 1769 | 2025-12-12 00:22:05 |
| [dask](https://github.com/dask/dask) | 13647 | 1824 | 5476 | 6418 | 1204 | 2025-12-10 19:44:34 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13613 | 2063 | 2640 | 1150 | 199 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11750 | 1089 | 760 | 1746 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11515 | 589 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11247 | 1606 | 8128 | 1010 | 205 | 2025-12-10 20:45:00 |
| [falcon](https://github.com/falconry/falcon) | 9768 | 971 | 1114 | 1403 | 162 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8769 | 547 | 983 | 467 | 184 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8713 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7048 | 372 | 877 | 2481 | 314 | 2025-12-09 00:42:38 |
| [hug](https://github.com/hugapi/hug) | 6908 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 743 | 979 | 581 | 35 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5410 | 445 | 1204 | 726 | 508 | 2025-12-09 01:00:15 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5110 | 971 | 880 | 268 | 171 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3812 | 301 | 1170 | 203 | 119 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3559 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2716 | 307 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2332 | 135 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2324 | 180 | 419 | 555 | 74 | 2025-12-08 17:56:30 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-08 17:49:38 |
| [pypy](https://github.com/pypy/pypy) | 1598 | 91 | 5166 | 172 | 751 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-12T02:12:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
