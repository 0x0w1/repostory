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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201279 | 78194 | 41952 | 84322 | 3498 | 2026-11-03 06:08:48 |
| [transformers](https://github.com/huggingface/transformers) | 168472 | 35093 | 19763 | 29718 | 1051 | 2026-11-03 05:30:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 105104 | 31321 | 62215 | 140277 | 17933 | 2026-11-03 06:10:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 104363 | 10182 | 3557 | 6567 | 67 | 2026-11-02 14:05:20 |
| [django](https://github.com/django/django) | 91489 | 36017 | 0 | 22156 | 543 | 2026-11-02 17:00:37 |
| [cpython](https://github.com/python/cpython) | 77799 | 37188 | 79091 | 79750 | 9234 | 2026-11-03 06:21:40 |
| [flask](https://github.com/pallets/flask) | 74943 | 17291 | 2771 | 2913 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67987 | 27631 | 12359 | 21747 | 2158 | 2026-11-03 05:50:32 |
| [keras](https://github.com/keras-team/keras) | 64414 | 19823 | 13063 | 10194 | 288 | 2026-11-01 11:13:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 50305 | 20734 | 28667 | 39792 | 2033 | 2026-11-02 22:10:44 |
| [ray](https://github.com/ray-project/ray) | 44188 | 8238 | 23276 | 44001 | 3722 | 2026-11-03 06:03:41 |
| [gym](https://github.com/openai/gym) | 37231 | 8666 | 1837 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34015 | 4741 | 5781 | 4140 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33240 | 13114 | 14159 | 18943 | 2236 | 2026-11-02 19:23:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30225 | 7097 | 3966 | 5104 | 67 | 2026-10-28 07:03:26 |
| [celery](https://github.com/celery/celery) | 29126 | 5255 | 5358 | 4680 | 743 | 2026-11-03 06:02:49 |
| [dash](https://github.com/plotly/dash) | 24478 | 2336 | 2170 | 1813 | 437 | 2026-11-02 19:56:57 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23416 | 8542 | 11456 | 21045 | 1476 | 2026-11-03 00:21:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 22456 | 1507 | 1454 | 8004 | 308 | 2026-11-03 06:02:08 |
| [micropython](https://github.com/micropython/micropython) | 22179 | 9039 | 6154 | 8190 | 1551 | 2026-11-03 03:35:46 |
| [tornado](https://github.com/tornadoweb/tornado) | 22162 | 5603 | 1890 | 1899 | 232 | 2026-10-26 21:18:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18873 | 2890 | 3402 | 2271 | 753 | 2026-11-01 07:37:22 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16604 | 2504 | 3269 | 10610 | 299 | 2026-11-02 16:26:46 |
| [httpx](https://github.com/encode/httpx) | 15732 | 2619 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15179 | 6057 | 11745 | 14822 | 1895 | 2026-11-02 11:28:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14099 | 2156 | 2668 | 1249 | 259 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13943 | 2015 | 5581 | 6802 | 1420 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12706 | 1430 | 795 | 2301 | 36 | 2026-11-01 20:39:28 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12276 | 1840 | 8376 | 1254 | 212 | 2026-11-02 22:26:46 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11928 | 619 | 428 | 344 | 173 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9811 | 1052 | 1150 | 1563 | 166 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9229 | 624 | 1055 | 596 | 194 | 2026-11-01 18:39:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1515 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7359 | 467 | 906 | 2660 | 339 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6872 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5640 | 542 | 1302 | 981 | 560 | 2026-10-31 04:22:39 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5443 | 1054 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4464 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 681 | 1392 | 267 | 2026-11-02 22:04:09 |
| [anyio](https://github.com/agronholm/anyio) | 2567 | 346 | 496 | 880 | 139 | 2026-11-02 18:31:53 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1608 | 355 | 2026-10-30 11:34:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1791 | 278 | 279 | 2026-11-02 18:22:13 |
| [pypy](https://github.com/pypy/pypy) | 1823 | 130 | 5296 | 397 | 720 | 2026-11-03 06:17:43 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 104 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 103 | 39 | 16 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-03T06:24:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
