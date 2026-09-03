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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198363 | 76228 | 41744 | 81372 | 3015 | 2026-09-03 03:35:10 |
| [transformers](https://github.com/huggingface/transformers) | 164732 | 34430 | 19402 | 28337 | 2394 | 2026-09-03 04:06:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 102728 | 29093 | 60723 | 134424 | 17540 | 2026-09-03 04:06:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 102041 | 9837 | 3549 | 6306 | 81 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 89567 | 34219 | 0 | 21749 | 481 | 2026-09-02 17:25:36 |
| [cpython](https://github.com/python/cpython) | 75598 | 35318 | 77930 | 76583 | 9631 | 2026-09-02 21:41:55 |
| [flask](https://github.com/pallets/flask) | 72171 | 16957 | 2767 | 2900 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67141 | 27347 | 12262 | 21420 | 2150 | 2026-09-02 21:00:44 |
| [keras](https://github.com/keras-team/keras) | 64273 | 19773 | 12892 | 9788 | 221 | 2026-09-03 01:12:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 49624 | 20321 | 28511 | 38437 | 2710 | 2026-09-03 01:18:44 |
| [ray](https://github.com/ray-project/ray) | 43688 | 7996 | 23009 | 42455 | 3537 | 2026-09-03 03:54:00 |
| [gym](https://github.com/openai/gym) | 37244 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33869 | 4723 | 5771 | 4119 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32643 | 12707 | 14079 | 18310 | 2336 | 2026-09-03 02:56:24 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30155 | 7083 | 3966 | 5050 | 58 | 2026-09-01 19:20:21 |
| [celery](https://github.com/celery/celery) | 28855 | 5145 | 5296 | 4288 | 750 | 2026-09-03 03:43:48 |
| [dash](https://github.com/plotly/dash) | 24392 | 2317 | 2147 | 1693 | 530 | 2026-09-03 00:13:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23141 | 8467 | 11411 | 20801 | 1472 | 2026-09-01 19:20:29 |
| [RustPython](https://github.com/RustPython/RustPython) | 22328 | 1481 | 1423 | 7144 | 399 | 2026-09-02 23:13:53 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5553 | 1879 | 1809 | 253 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22038 | 8955 | 6121 | 8081 | 1534 | 2026-09-02 07:25:28 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18763 | 2838 | 3377 | 2148 | 701 | 2026-09-02 21:49:37 |
| [sanic](https://github.com/sanic-org/sanic) | 18646 | 1600 | 1471 | 1705 | 147 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16535 | 2392 | 3242 | 10027 | 217 | 2026-09-02 18:50:52 |
| [httpx](https://github.com/encode/httpx) | 15463 | 1268 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14983 | 5907 | 11622 | 14433 | 1826 | 2026-09-02 20:41:34 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14010 | 2128 | 2659 | 1216 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13910 | 1943 | 5554 | 6714 | 1324 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12588 | 1282 | 781 | 2072 | 64 | 2026-09-01 19:21:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12129 | 1771 | 8284 | 1199 | 205 | 2026-09-02 20:54:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 613 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1032 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9180 | 610 | 1044 | 542 | 223 | 2026-09-02 18:12:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1505 | 865 | 648 | 290 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7314 | 418 | 900 | 2595 | 324 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6881 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5623 | 503 | 1266 | 893 | 543 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5377 | 1037 | 933 | 323 | 201 | 2026-09-02 10:45:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4363 | 371 | 1199 | 248 | 127 | 2026-09-02 19:33:21 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3660 | 206 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 315 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 251 | 473 | 755 | 106 | 2026-09-02 21:45:54 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 274 | 272 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1786 | 125 | 5255 | 299 | 721 | 2026-09-02 21:10:48 |
| [jython](https://github.com/jython/jython) | 1539 | 231 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-03T04:07:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
