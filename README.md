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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196292 | 75501 | 41595 | 77926 | 2708 | 2026-07-13 02:49:58 |
| [transformers](https://github.com/huggingface/transformers) | 162552 | 33876 | 19173 | 27384 | 2492 | 2026-07-13 03:39:16 |
| [pytorch](https://github.com/pytorch/pytorch) | 101780 | 28485 | 59753 | 129293 | 18295 | 2026-07-13 03:29:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 100416 | 9597 | 3540 | 6074 | 100 | 2026-07-10 17:54:44 |
| [django](https://github.com/django/django) | 88177 | 34178 | 0 | 21543 | 460 | 2026-07-10 22:01:58 |
| [cpython](https://github.com/python/cpython) | 73772 | 35010 | 77158 | 74145 | 9407 | 2026-07-13 02:51:38 |
| [flask](https://github.com/pallets/flask) | 71917 | 16907 | 2755 | 2863 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66667 | 27175 | 12173 | 21109 | 2104 | 2026-07-11 05:42:37 |
| [keras](https://github.com/keras-team/keras) | 64166 | 19753 | 12820 | 9567 | 229 | 2026-07-07 17:53:38 |
| [pandas](https://github.com/pandas-dev/pandas) | 49177 | 20128 | 28383 | 37824 | 3029 | 2026-07-13 00:53:06 |
| [ray](https://github.com/ray-project/ray) | 43215 | 7787 | 22836 | 41477 | 3472 | 2026-07-12 23:48:32 |
| [gym](https://github.com/openai/gym) | 37251 | 8691 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33738 | 4691 | 5764 | 4101 | 221 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32356 | 12564 | 13997 | 17896 | 2403 | 2026-07-12 18:25:14 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30095 | 7075 | 3967 | 5026 | 84 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28681 | 5099 | 5287 | 4176 | 786 | 2026-07-09 14:31:55 |
| [dash](https://github.com/plotly/dash) | 24307 | 2307 | 2126 | 1644 | 543 | 2026-07-10 17:33:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22986 | 8387 | 11355 | 20619 | 1472 | 2026-07-11 04:57:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5536 | 1876 | 1791 | 242 | 2026-07-08 17:05:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 22171 | 1463 | 1370 | 6820 | 396 | 2026-07-12 12:35:01 |
| [micropython](https://github.com/micropython/micropython) | 21890 | 8916 | 6095 | 7946 | 1611 | 2026-07-13 03:40:50 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18678 | 2824 | 3367 | 2118 | 773 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1588 | 1468 | 1691 | 134 | 2026-07-12 07:17:35 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16508 | 2345 | 3222 | 9561 | 225 | 2026-07-13 00:26:54 |
| [httpx](https://github.com/encode/httpx) | 15360 | 1201 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14813 | 5802 | 11522 | 14070 | 1845 | 2026-07-13 01:54:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13947 | 2123 | 2655 | 1201 | 218 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13855 | 1903 | 5540 | 6650 | 1261 | 2026-07-09 15:44:54 |
| [starlette](https://github.com/Kludex/starlette) | 12471 | 1225 | 771 | 1977 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11991 | 1711 | 8240 | 1138 | 205 | 2026-07-12 22:57:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11854 | 610 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9792 | 1012 | 1133 | 1477 | 169 | 2026-07-08 16:24:46 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9129 | 600 | 1039 | 520 | 216 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1502 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7292 | 409 | 895 | 2570 | 327 | 2026-07-12 00:29:14 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5603 | 497 | 1262 | 870 | 528 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1029 | 919 | 312 | 203 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4251 | 349 | 1187 | 230 | 122 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 312 | 674 | 1335 | 311 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2502 | 219 | 452 | 690 | 89 | 2026-07-12 20:32:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 914 | 1084 | 1563 | 359 | 2026-07-11 08:25:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 366 | 1785 | 268 | 266 | 2026-07-06 17:55:11 |
| [pypy](https://github.com/pypy/pypy) | 1763 | 118 | 5234 | 271 | 737 | 2026-07-12 04:18:37 |
| [jython](https://github.com/jython/jython) | 1523 | 232 | 298 | 138 | 106 | 2026-07-10 06:45:13 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-13T03:42:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
