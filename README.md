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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200668 | 78132 | 41831 | 83009 | 3242 | 2026-10-03 04:18:42 |
| [transformers](https://github.com/huggingface/transformers) | 166911 | 34741 | 19554 | 28931 | 2360 | 2026-10-03 03:54:50 |
| [pytorch](https://github.com/pytorch/pytorch) | 103632 | 31176 | 61456 | 137482 | 17576 | 2026-10-03 05:02:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 102772 | 9982 | 3556 | 6402 | 84 | 2026-10-02 11:36:38 |
| [django](https://github.com/django/django) | 91221 | 36050 | 0 | 21979 | 525 | 2026-10-02 21:29:29 |
| [cpython](https://github.com/python/cpython) | 77392 | 37161 | 78389 | 77881 | 9739 | 2026-10-02 22:34:39 |
| [flask](https://github.com/pallets/flask) | 74796 | 17037 | 2769 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67456 | 27471 | 12308 | 21564 | 2165 | 2026-10-02 13:23:25 |
| [keras](https://github.com/keras-team/keras) | 64348 | 19805 | 12973 | 9983 | 255 | 2026-10-02 22:17:14 |
| [pandas](https://github.com/pandas-dev/pandas) | 49901 | 20457 | 28579 | 39141 | 2456 | 2026-10-03 00:11:18 |
| [ray](https://github.com/ray-project/ray) | 43965 | 8109 | 23117 | 43147 | 3544 | 2026-10-03 00:52:29 |
| [gym](https://github.com/openai/gym) | 37240 | 8671 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33933 | 4734 | 5774 | 4128 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 32900 | 12870 | 14120 | 18645 | 2251 | 2026-10-02 18:41:57 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30201 | 7086 | 3966 | 5076 | 50 | 2026-09-30 06:38:50 |
| [celery](https://github.com/celery/celery) | 28931 | 5200 | 5319 | 4488 | 739 | 2026-10-03 03:54:09 |
| [dash](https://github.com/plotly/dash) | 24439 | 2328 | 2164 | 1748 | 431 | 2026-10-02 15:22:38 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23317 | 8500 | 11431 | 20930 | 1496 | 2026-10-03 02:47:06 |
| [RustPython](https://github.com/RustPython/RustPython) | 22375 | 1492 | 1433 | 7416 | 403 | 2026-10-02 09:59:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22170 | 5563 | 1885 | 1847 | 213 | 2026-10-02 17:33:28 |
| [micropython](https://github.com/micropython/micropython) | 22104 | 8984 | 6133 | 8119 | 1532 | 2026-10-02 07:05:46 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18819 | 2858 | 3387 | 2208 | 728 | 2026-10-01 07:39:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1606 | 1469 | 1682 | 154 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16567 | 2437 | 3261 | 10303 | 217 | 2026-10-02 23:32:05 |
| [httpx](https://github.com/encode/httpx) | 15524 | 2797 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15072 | 5985 | 11678 | 14629 | 1862 | 2026-10-02 12:07:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14053 | 2144 | 2663 | 1227 | 239 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13930 | 1971 | 5563 | 6740 | 1350 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12646 | 1353 | 785 | 2170 | 61 | 2026-10-01 19:45:03 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12197 | 1801 | 8321 | 1217 | 211 | 2026-10-02 22:57:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11907 | 616 | 422 | 335 | 163 | 2026-10-01 15:38:19 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1038 | 1145 | 1532 | 156 | 2026-09-30 18:05:10 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9204 | 615 | 1047 | 557 | 225 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1514 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7340 | 440 | 902 | 2622 | 331 | 2026-10-01 07:30:18 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 519 | 1270 | 908 | 521 | 2026-10-01 05:56:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5413 | 1045 | 934 | 325 | 202 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4425 | 383 | 1202 | 252 | 118 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3988 | 272 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3674 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2766 | 316 | 675 | 1343 | 307 | 2026-10-03 02:26:40 |
| [anyio](https://github.com/agronholm/anyio) | 2550 | 296 | 484 | 814 | 134 | 2026-10-02 21:20:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 916 | 1085 | 1601 | 357 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1786 | 276 | 273 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1806 | 127 | 5268 | 319 | 716 | 2026-10-02 12:11:28 |
| [jython](https://github.com/jython/jython) | 1546 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-10-03T05:03:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
