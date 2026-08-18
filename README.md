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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196990 | 76044 | 41684 | 80223 | 2921 | 2026-08-18 01:37:42 |
| [transformers](https://github.com/huggingface/transformers) | 164196 | 34260 | 19320 | 27978 | 2388 | 2026-08-18 00:29:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 102441 | 28895 | 60398 | 132825 | 17055 | 2026-08-18 01:41:33 |
| [fastapi](https://github.com/fastapi/fastapi) | 101659 | 9784 | 3544 | 6245 | 85 | 2026-08-17 20:15:06 |
| [django](https://github.com/django/django) | 88420 | 34142 | 0 | 21676 | 457 | 2026-08-17 17:21:54 |
| [cpython](https://github.com/python/cpython) | 74338 | 35221 | 77713 | 75918 | 9527 | 2026-08-17 19:39:17 |
| [flask](https://github.com/pallets/flask) | 72125 | 16937 | 2762 | 2893 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66963 | 27291 | 12244 | 21329 | 2126 | 2026-08-17 12:13:05 |
| [keras](https://github.com/keras-team/keras) | 64238 | 19750 | 12869 | 9711 | 222 | 2026-08-14 17:42:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 49509 | 20273 | 28478 | 38219 | 2810 | 2026-08-17 22:36:38 |
| [ray](https://github.com/ray-project/ray) | 43537 | 7930 | 22957 | 42185 | 3507 | 2026-08-18 01:36:56 |
| [gym](https://github.com/openai/gym) | 37236 | 8686 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33827 | 4709 | 5770 | 4112 | 234 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32547 | 12640 | 14053 | 18180 | 2336 | 2026-08-17 21:00:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30136 | 7076 | 3966 | 5044 | 56 | 2026-08-12 11:26:08 |
| [celery](https://github.com/celery/celery) | 28788 | 5136 | 5296 | 4245 | 803 | 2026-08-17 22:14:50 |
| [dash](https://github.com/plotly/dash) | 24372 | 2315 | 2143 | 1680 | 538 | 2026-08-17 20:39:36 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23083 | 8441 | 11399 | 20754 | 1478 | 2026-08-16 07:40:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 22288 | 1474 | 1422 | 7049 | 410 | 2026-08-17 13:35:50 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5551 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21987 | 8930 | 6117 | 8055 | 1535 | 2026-08-17 13:15:56 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18743 | 2833 | 3378 | 2139 | 779 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1597 | 1471 | 1703 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16526 | 2377 | 3238 | 9836 | 240 | 2026-08-18 01:11:54 |
| [httpx](https://github.com/encode/httpx) | 15427 | 1247 | 0 | 1802 | 141 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14935 | 5867 | 11596 | 14329 | 1851 | 2026-08-17 20:31:10 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13998 | 2128 | 2658 | 1214 | 229 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13891 | 1932 | 5549 | 6700 | 1309 | 2026-08-17 14:33:18 |
| [starlette](https://github.com/Kludex/starlette) | 12549 | 1261 | 773 | 2028 | 63 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12091 | 1755 | 8269 | 1184 | 213 | 2026-08-17 18:16:02 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11885 | 611 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1027 | 1139 | 1500 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 610 | 1042 | 537 | 226 | 2026-08-17 17:39:58 |
| [bottle](https://github.com/bottlepy/bottle) | 8775 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7301 | 415 | 899 | 2590 | 322 | 2026-08-18 00:29:06 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5608 | 500 | 1265 | 887 | 540 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5586 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5355 | 1032 | 929 | 316 | 198 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4325 | 363 | 1197 | 244 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3997 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3657 | 204 | 284 | 135 | 37 | 2026-08-14 14:43:56 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2529 | 245 | 469 | 737 | 106 | 2026-08-17 23:45:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 915 | 1084 | 1587 | 356 | 2026-08-17 16:22:18 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 367 | 1786 | 272 | 270 | 2026-08-17 23:26:03 |
| [pypy](https://github.com/pypy/pypy) | 1782 | 123 | 5250 | 292 | 729 | 2026-08-17 18:42:52 |
| [jython](https://github.com/jython/jython) | 1533 | 231 | 300 | 151 | 98 | 2026-08-16 08:58:23 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-18T01:42:11*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
