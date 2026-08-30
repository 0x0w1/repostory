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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198021 | 76182 | 41730 | 81116 | 2980 | 2026-08-30 04:52:43 |
| [transformers](https://github.com/huggingface/transformers) | 164619 | 34387 | 19390 | 28266 | 2404 | 2026-08-30 00:01:28 |
| [pytorch](https://github.com/pytorch/pytorch) | 102661 | 29034 | 60610 | 134045 | 17439 | 2026-08-30 04:53:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 101929 | 9828 | 3548 | 6283 | 80 | 2026-08-26 17:54:56 |
| [django](https://github.com/django/django) | 89287 | 34204 | 0 | 21735 | 480 | 2026-08-29 17:52:42 |
| [cpython](https://github.com/python/cpython) | 75283 | 35296 | 77871 | 76395 | 9614 | 2026-08-30 05:06:53 |
| [flask](https://github.com/pallets/flask) | 72148 | 16955 | 2764 | 2898 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67098 | 27334 | 12256 | 21395 | 2135 | 2026-08-28 21:28:28 |
| [keras](https://github.com/keras-team/keras) | 64269 | 19772 | 12889 | 9774 | 234 | 2026-08-29 23:14:53 |
| [pandas](https://github.com/pandas-dev/pandas) | 49592 | 20305 | 28500 | 38383 | 2741 | 2026-08-30 04:24:56 |
| [ray](https://github.com/ray-project/ray) | 43648 | 7978 | 22997 | 42379 | 3537 | 2026-08-29 21:58:04 |
| [gym](https://github.com/openai/gym) | 37244 | 8680 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33864 | 4721 | 5770 | 4117 | 236 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32630 | 12690 | 14072 | 18292 | 2341 | 2026-08-28 23:23:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30149 | 7080 | 3966 | 5048 | 58 | 2026-08-25 19:14:08 |
| [celery](https://github.com/celery/celery) | 28837 | 5143 | 5296 | 4274 | 761 | 2026-08-29 13:37:56 |
| [dash](https://github.com/plotly/dash) | 24389 | 2319 | 2146 | 1690 | 535 | 2026-08-28 22:53:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23122 | 8459 | 11405 | 20787 | 1467 | 2026-08-30 00:52:59 |
| [RustPython](https://github.com/RustPython/RustPython) | 22313 | 1480 | 1422 | 7114 | 398 | 2026-08-30 04:45:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5555 | 1878 | 1808 | 254 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22021 | 8945 | 6118 | 8073 | 1535 | 2026-08-28 08:29:56 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18761 | 2838 | 3378 | 2146 | 770 | 2026-08-27 16:46:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18646 | 1600 | 1471 | 1704 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16535 | 2390 | 3242 | 9983 | 229 | 2026-08-29 16:23:42 |
| [httpx](https://github.com/encode/httpx) | 15455 | 1265 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14968 | 5898 | 11617 | 14411 | 1832 | 2026-08-29 13:30:33 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14008 | 2127 | 2659 | 1213 | 228 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13904 | 1942 | 5551 | 6712 | 1319 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12579 | 1281 | 780 | 2062 | 66 | 2026-08-26 10:51:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12120 | 1764 | 8280 | 1199 | 207 | 2026-08-29 14:42:19 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11894 | 611 | 418 | 328 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1030 | 1139 | 1508 | 160 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9179 | 610 | 1043 | 540 | 221 | 2026-08-24 14:12:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8777 | 1502 | 865 | 645 | 289 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7308 | 417 | 899 | 2592 | 322 | 2026-08-27 03:44:56 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5620 | 499 | 1266 | 889 | 542 | 2026-08-24 16:57:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5370 | 1037 | 932 | 320 | 199 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4355 | 367 | 1199 | 245 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4095 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3659 | 205 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 316 | 675 | 1338 | 314 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 249 | 472 | 749 | 106 | 2026-08-29 18:21:15 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1595 | 356 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 368 | 1786 | 272 | 270 | 2026-08-24 17:57:48 |
| [pypy](https://github.com/pypy/pypy) | 1784 | 125 | 5254 | 297 | 726 | 2026-08-29 19:16:54 |
| [jython](https://github.com/jython/jython) | 1536 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-30T05:07:12*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
