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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197006 | 76010 | 41678 | 80046 | 2857 | 2026-08-14 02:29:56 |
| [transformers](https://github.com/huggingface/transformers) | 164083 | 34242 | 19305 | 27911 | 2387 | 2026-08-13 23:55:53 |
| [pytorch](https://github.com/pytorch/pytorch) | 102361 | 28862 | 60330 | 132501 | 17245 | 2026-08-14 02:30:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 101579 | 9780 | 3544 | 6224 | 72 | 2026-08-12 07:19:26 |
| [django](https://github.com/django/django) | 88422 | 34127 | 0 | 21659 | 459 | 2026-08-13 06:03:19 |
| [cpython](https://github.com/python/cpython) | 74321 | 35203 | 77659 | 75754 | 9485 | 2026-08-13 20:20:32 |
| [flask](https://github.com/pallets/flask) | 72187 | 16945 | 2763 | 2892 | 3 | 2026-08-11 22:32:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66975 | 27288 | 12243 | 21313 | 2124 | 2026-08-13 22:04:45 |
| [keras](https://github.com/keras-team/keras) | 64228 | 19749 | 12867 | 9702 | 217 | 2026-08-13 19:27:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 49521 | 20279 | 28475 | 38172 | 2846 | 2026-08-14 01:53:16 |
| [ray](https://github.com/ray-project/ray) | 43514 | 7920 | 22944 | 42130 | 3495 | 2026-08-14 01:46:34 |
| [gym](https://github.com/openai/gym) | 37241 | 8685 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33817 | 4709 | 5770 | 4110 | 232 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32530 | 12631 | 14044 | 18148 | 2323 | 2026-08-13 23:46:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30129 | 7077 | 3966 | 5044 | 56 | 2026-08-12 11:26:08 |
| [celery](https://github.com/celery/celery) | 28785 | 5133 | 5293 | 4234 | 801 | 2026-08-13 14:19:13 |
| [dash](https://github.com/plotly/dash) | 24377 | 2312 | 2142 | 1678 | 536 | 2026-08-13 15:02:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23078 | 8434 | 11394 | 20746 | 1472 | 2026-08-13 18:40:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22280 | 1474 | 1421 | 7021 | 407 | 2026-08-13 18:30:51 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5551 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21990 | 8930 | 6116 | 8042 | 1528 | 2026-08-14 02:11:31 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18738 | 2833 | 3375 | 2137 | 774 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1596 | 1471 | 1701 | 144 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16522 | 2373 | 3236 | 9822 | 232 | 2026-08-14 02:16:42 |
| [httpx](https://github.com/encode/httpx) | 15417 | 1246 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14915 | 5862 | 11593 | 14302 | 1855 | 2026-08-13 14:19:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13998 | 2127 | 2658 | 1212 | 227 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13888 | 1926 | 5548 | 6692 | 1301 | 2026-08-10 22:03:29 |
| [starlette](https://github.com/Kludex/starlette) | 12540 | 1258 | 773 | 2027 | 63 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12080 | 1749 | 8265 | 1180 | 211 | 2026-08-13 21:03:13 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11884 | 612 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1025 | 1139 | 1498 | 159 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 605 | 1042 | 528 | 226 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8775 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7305 | 414 | 898 | 2589 | 321 | 2026-08-11 00:45:57 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5611 | 501 | 1265 | 886 | 539 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5348 | 1033 | 929 | 316 | 204 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4320 | 363 | 1197 | 244 | 130 | 2026-08-12 14:11:42 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3997 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3657 | 203 | 284 | 134 | 37 | 2026-08-09 20:23:31 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2524 | 242 | 469 | 732 | 106 | 2026-08-13 23:15:10 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1584 | 357 | 2026-08-11 15:13:53 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-10 17:58:57 |
| [pypy](https://github.com/pypy/pypy) | 1782 | 121 | 5247 | 290 | 731 | 2026-08-14 01:40:41 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 300 | 149 | 97 | 2026-08-10 15:30:18 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-14T02:32:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
