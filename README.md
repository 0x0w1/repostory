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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195871 | 75233 | 41584 | 77280 | 2709 | 2026-07-01 04:44:39 |
| [transformers](https://github.com/huggingface/transformers) | 162060 | 33685 | 19121 | 27134 | 2453 | 2026-07-01 03:24:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 100998 | 28185 | 59516 | 128497 | 18267 | 2026-07-01 04:43:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 99834 | 9512 | 3538 | 5997 | 103 | 2026-07-01 04:39:56 |
| [django](https://github.com/django/django) | 87917 | 33915 | 0 | 21492 | 458 | 2026-07-01 01:17:33 |
| [cpython](https://github.com/python/cpython) | 73393 | 34798 | 76989 | 73400 | 9438 | 2026-07-01 03:29:45 |
| [flask](https://github.com/pallets/flask) | 71785 | 16887 | 2753 | 2842 | 6 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66513 | 27131 | 12166 | 21070 | 2108 | 2026-06-30 15:40:38 |
| [keras](https://github.com/keras-team/keras) | 64100 | 19746 | 12808 | 9534 | 216 | 2026-07-01 03:07:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 49098 | 20065 | 28353 | 37648 | 2999 | 2026-06-30 21:51:48 |
| [ray](https://github.com/ray-project/ray) | 43067 | 7744 | 22795 | 41275 | 3480 | 2026-07-01 04:23:41 |
| [gym](https://github.com/openai/gym) | 37244 | 8698 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33705 | 4690 | 5763 | 4098 | 218 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32292 | 12519 | 13976 | 17756 | 2411 | 2026-06-30 23:35:42 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30089 | 7072 | 3967 | 5024 | 85 | 2026-06-30 19:13:18 |
| [celery](https://github.com/celery/celery) | 28630 | 5087 | 5284 | 4162 | 789 | 2026-07-01 04:36:29 |
| [dash](https://github.com/plotly/dash) | 24279 | 2302 | 2121 | 1614 | 549 | 2026-07-01 01:20:54 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22943 | 8361 | 11338 | 20575 | 1459 | 2026-06-30 23:13:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22187 | 5530 | 1875 | 1762 | 220 | 2026-06-26 00:55:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22151 | 1449 | 1359 | 6770 | 388 | 2026-06-30 14:49:27 |
| [micropython](https://github.com/micropython/micropython) | 21851 | 8892 | 6078 | 7911 | 1636 | 2026-06-30 13:28:16 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18645 | 2816 | 3362 | 2100 | 769 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16463 | 2336 | 3221 | 9456 | 236 | 2026-06-30 19:21:59 |
| [httpx](https://github.com/encode/httpx) | 15325 | 1185 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14792 | 5784 | 11510 | 14008 | 1828 | 2026-06-30 09:30:24 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13934 | 2115 | 2655 | 1187 | 228 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13857 | 1894 | 5539 | 6631 | 1251 | 2026-06-29 22:02:52 |
| [starlette](https://github.com/Kludex/starlette) | 12442 | 1214 | 770 | 1963 | 51 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11951 | 1704 | 8236 | 1126 | 212 | 2026-06-27 22:33:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11839 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1004 | 1132 | 1468 | 167 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9109 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8768 | 1499 | 864 | 636 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7280 | 403 | 894 | 2564 | 325 | 2026-07-01 02:15:04 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5594 | 492 | 1259 | 864 | 523 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5303 | 1025 | 916 | 310 | 205 | 2026-06-30 12:40:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4230 | 345 | 1186 | 228 | 119 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 890 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3646 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2493 | 214 | 448 | 673 | 85 | 2026-06-29 23:43:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 909 | 1084 | 1547 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-29 17:47:29 |
| [pypy](https://github.com/pypy/pypy) | 1757 | 118 | 5229 | 265 | 740 | 2026-06-30 04:10:00 |
| [jython](https://github.com/jython/jython) | 1518 | 230 | 297 | 137 | 110 | 2026-06-30 12:03:48 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-01T04:45:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
