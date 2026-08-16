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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197047 | 76042 | 41685 | 80133 | 2860 | 2026-08-16 00:19:54 |
| [transformers](https://github.com/huggingface/transformers) | 164124 | 34249 | 19311 | 27941 | 2382 | 2026-08-15 22:28:12 |
| [pytorch](https://github.com/pytorch/pytorch) | 102395 | 28878 | 60352 | 132698 | 17327 | 2026-08-16 01:48:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 101615 | 9785 | 3544 | 6243 | 87 | 2026-08-15 05:17:14 |
| [django](https://github.com/django/django) | 88428 | 34139 | 0 | 21673 | 459 | 2026-08-15 15:55:33 |
| [cpython](https://github.com/python/cpython) | 74326 | 35210 | 77685 | 75843 | 9514 | 2026-08-15 20:47:07 |
| [flask](https://github.com/pallets/flask) | 72161 | 16934 | 2762 | 2892 | 3 | 2026-08-11 22:32:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66960 | 27290 | 12243 | 21320 | 2129 | 2026-08-13 22:04:45 |
| [keras](https://github.com/keras-team/keras) | 64232 | 19746 | 12869 | 9703 | 216 | 2026-08-14 17:42:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 49503 | 20268 | 28477 | 38198 | 2815 | 2026-08-16 01:05:14 |
| [ray](https://github.com/ray-project/ray) | 43523 | 7928 | 22947 | 42150 | 3472 | 2026-08-16 00:26:16 |
| [gym](https://github.com/openai/gym) | 37239 | 8685 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33823 | 4709 | 5770 | 4110 | 232 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32544 | 12634 | 14050 | 18162 | 2332 | 2026-08-14 23:22:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30133 | 7076 | 3966 | 5044 | 56 | 2026-08-12 11:26:08 |
| [celery](https://github.com/celery/celery) | 28786 | 5135 | 5294 | 4237 | 805 | 2026-08-14 17:52:08 |
| [dash](https://github.com/plotly/dash) | 24377 | 2314 | 2143 | 1679 | 538 | 2026-08-13 15:02:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23082 | 8436 | 11395 | 20753 | 1475 | 2026-08-16 01:02:52 |
| [RustPython](https://github.com/RustPython/RustPython) | 22281 | 1474 | 1422 | 7039 | 409 | 2026-08-15 12:05:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5551 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21992 | 8927 | 6117 | 8049 | 1535 | 2026-08-14 03:00:27 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18740 | 2832 | 3376 | 2137 | 775 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1597 | 1471 | 1702 | 145 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16523 | 2375 | 3236 | 9836 | 238 | 2026-08-15 17:18:52 |
| [httpx](https://github.com/encode/httpx) | 15423 | 1246 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14924 | 5866 | 11593 | 14318 | 1851 | 2026-08-15 17:11:55 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14002 | 2128 | 2658 | 1213 | 228 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13889 | 1930 | 5549 | 6696 | 1306 | 2026-08-10 22:03:29 |
| [starlette](https://github.com/Kludex/starlette) | 12547 | 1259 | 773 | 2027 | 63 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12086 | 1754 | 8267 | 1183 | 213 | 2026-08-14 13:03:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11884 | 611 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 1026 | 1139 | 1499 | 160 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9163 | 607 | 1042 | 532 | 230 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8775 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 415 | 899 | 2589 | 322 | 2026-08-11 00:45:57 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 500 | 1265 | 886 | 539 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5586 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5351 | 1032 | 929 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4322 | 363 | 1197 | 244 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4092 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3997 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 204 | 284 | 135 | 37 | 2026-08-14 14:43:56 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2525 | 245 | 469 | 735 | 106 | 2026-08-16 00:31:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 915 | 1084 | 1585 | 357 | 2026-08-14 23:59:43 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-10 17:58:57 |
| [pypy](https://github.com/pypy/pypy) | 1781 | 121 | 5248 | 292 | 732 | 2026-08-15 19:42:58 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 300 | 151 | 99 | 2026-08-10 15:30:18 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-16T01:49:18*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
