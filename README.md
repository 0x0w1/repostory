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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195812 | 75198 | 41563 | 76607 | 3514 | 2026-06-22 04:30:05 |
| [transformers](https://github.com/huggingface/transformers) | 161783 | 33565 | 19093 | 26992 | 2457 | 2026-06-21 21:28:37 |
| [pytorch](https://github.com/pytorch/pytorch) | 100943 | 28078 | 59352 | 127846 | 18320 | 2026-06-22 05:16:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 99493 | 9465 | 3535 | 5956 | 95 | 2026-06-21 19:39:50 |
| [django](https://github.com/django/django) | 87933 | 33874 | 0 | 21454 | 452 | 2026-06-19 16:43:45 |
| [cpython](https://github.com/python/cpython) | 73360 | 34752 | 76822 | 72748 | 9390 | 2026-06-22 04:21:01 |
| [flask](https://github.com/pallets/flask) | 71692 | 16876 | 2751 | 2838 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66391 | 27086 | 12155 | 21025 | 2099 | 2026-06-21 16:52:37 |
| [keras](https://github.com/keras-team/keras) | 64100 | 19738 | 12805 | 9474 | 211 | 2026-06-18 23:13:32 |
| [pandas](https://github.com/pandas-dev/pandas) | 49033 | 20024 | 28332 | 37504 | 3170 | 2026-06-21 19:45:34 |
| [ray](https://github.com/ray-project/ray) | 42964 | 7709 | 22758 | 41101 | 3492 | 2026-06-22 03:22:17 |
| [gym](https://github.com/openai/gym) | 37226 | 8703 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33679 | 4688 | 5759 | 4098 | 214 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32231 | 12466 | 13953 | 17672 | 2395 | 2026-06-22 00:07:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30080 | 7070 | 3967 | 5019 | 83 | 2026-06-16 19:13:19 |
| [celery](https://github.com/celery/celery) | 28615 | 5083 | 5282 | 4154 | 789 | 2026-06-20 17:30:01 |
| [dash](https://github.com/plotly/dash) | 24270 | 2300 | 2117 | 1593 | 554 | 2026-06-19 20:04:40 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22912 | 8355 | 11324 | 20549 | 1463 | 2026-06-19 19:16:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22182 | 5532 | 1873 | 1751 | 225 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22127 | 1448 | 1357 | 6707 | 389 | 2026-06-22 04:17:55 |
| [micropython](https://github.com/micropython/micropython) | 21821 | 8877 | 6071 | 7888 | 1633 | 2026-06-22 03:44:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18623 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18617 | 2813 | 3363 | 2098 | 770 | 2026-06-19 16:03:47 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16458 | 2333 | 3215 | 9417 | 219 | 2026-06-21 00:57:32 |
| [httpx](https://github.com/encode/httpx) | 15311 | 1181 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14765 | 5769 | 11492 | 13951 | 1819 | 2026-06-21 23:36:49 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13921 | 2115 | 2654 | 1185 | 225 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13851 | 1889 | 5539 | 6622 | 1245 | 2026-06-19 13:46:52 |
| [starlette](https://github.com/Kludex/starlette) | 12414 | 1205 | 770 | 1952 | 46 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11938 | 1700 | 8231 | 1119 | 209 | 2026-06-18 18:13:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11825 | 609 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9793 | 1002 | 1130 | 1465 | 162 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9101 | 600 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1502 | 864 | 635 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7280 | 397 | 892 | 2553 | 319 | 2026-06-16 05:03:49 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5587 | 489 | 1259 | 857 | 517 | 2026-06-18 15:20:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5298 | 1023 | 914 | 307 | 208 | 2026-06-19 16:35:32 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4213 | 341 | 1185 | 225 | 117 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 891 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 312 | 671 | 1334 | 307 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2484 | 211 | 446 | 660 | 87 | 2026-06-21 14:42:02 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 912 | 1084 | 1548 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1942 | 364 | 1785 | 268 | 266 | 2026-06-15 17:49:21 |
| [pypy](https://github.com/pypy/pypy) | 1753 | 116 | 5225 | 263 | 735 | 2026-06-21 20:30:39 |
| [jython](https://github.com/jython/jython) | 1519 | 230 | 297 | 136 | 110 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-22T05:18:50*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
