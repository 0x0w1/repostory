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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193542 | 75203 | 41132 | 65913 | 2929 | 2026-01-30 02:22:15 |
| [transformers](https://github.com/huggingface/transformers) | 155908 | 31898 | 18492 | 24515 | 2203 | 2026-01-29 21:27:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 97046 | 26688 | 56579 | 116789 | 17993 | 2026-01-30 02:29:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 94614 | 8599 | 3500 | 5180 | 212 | 2026-01-29 08:23:49 |
| [django](https://github.com/django/django) | 86624 | 33569 | 0 | 20547 | 400 | 2026-01-29 14:20:12 |
| [cpython](https://github.com/python/cpython) | 71267 | 33975 | 75133 | 68185 | 9213 | 2026-01-30 00:35:30 |
| [flask](https://github.com/pallets/flask) | 71109 | 16679 | 2712 | 2760 | 2 | 2026-01-28 15:43:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64822 | 26645 | 11905 | 20109 | 2113 | 2026-01-29 10:48:33 |
| [keras](https://github.com/keras-team/keras) | 63752 | 19681 | 12623 | 8666 | 256 | 2026-01-30 01:03:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 47735 | 19590 | 28063 | 35816 | 3640 | 2026-01-29 23:56:52 |
| [ray](https://github.com/ray-project/ray) | 41042 | 7166 | 22247 | 37998 | 3318 | 2026-01-30 02:33:59 |
| [gym](https://github.com/openai/gym) | 36990 | 8710 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33137 | 4637 | 5738 | 4077 | 185 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31352 | 12005 | 13764 | 16916 | 2286 | 2026-01-29 17:25:14 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29841 | 7060 | 3946 | 4910 | 88 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27935 | 4932 | 5185 | 3776 | 760 | 2026-01-29 12:37:15 |
| [dash](https://github.com/plotly/dash) | 24428 | 2252 | 2050 | 1424 | 559 | 2026-01-27 22:05:26 |
| [tornado](https://github.com/tornadoweb/tornado) | 22436 | 5542 | 1862 | 1696 | 210 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22293 | 8178 | 11117 | 19886 | 1529 | 2026-01-30 00:47:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 21737 | 1400 | 1295 | 5537 | 377 | 2026-01-29 22:48:29 |
| [micropython](https://github.com/micropython/micropython) | 21396 | 8682 | 5945 | 7509 | 1844 | 2026-01-28 22:18:10 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1584 | 1464 | 1663 | 114 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18224 | 2774 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16235 | 2184 | 3174 | 8531 | 277 | 2026-01-29 18:52:34 |
| [httpx](https://github.com/encode/httpx) | 14952 | 1023 | 925 | 1781 | 128 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14407 | 5603 | 11273 | 13170 | 1749 | 2026-01-30 01:26:57 |
| [dask](https://github.com/dask/dask) | 13725 | 1837 | 5498 | 6459 | 1215 | 2026-01-29 20:34:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13698 | 2081 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11877 | 1099 | 763 | 1776 | 48 | 2026-01-27 08:14:03 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11616 | 601 | 403 | 311 | 150 | 2026-01-30 00:58:01 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11445 | 1633 | 8145 | 1027 | 208 | 2026-01-29 19:53:55 |
| [falcon](https://github.com/falconry/falcon) | 9784 | 977 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8873 | 556 | 999 | 482 | 200 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8736 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7118 | 380 | 878 | 2493 | 315 | 2026-01-29 06:38:14 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5616 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5459 | 447 | 1221 | 742 | 508 | 2026-01-29 22:36:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5169 | 997 | 895 | 285 | 187 | 2026-01-27 13:50:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3925 | 308 | 1180 | 207 | 115 | 2026-01-29 20:24:57 |
| [quart](https://github.com/pallets/quart) | 3584 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2726 | 308 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2373 | 179 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1643 | 97 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1477 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-30T02:43:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
