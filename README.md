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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192880 | 75161 | 41048 | 63677 | 2411 | 2025-12-21 00:29:33 |
| [transformers](https://github.com/huggingface/transformers) | 154095 | 31498 | 18351 | 24022 | 2141 | 2025-12-20 18:27:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 96042 | 26308 | 55970 | 114499 | 17915 | 2025-12-21 02:23:01 |
| [fastapi](https://github.com/fastapi/fastapi) | 93275 | 8399 | 3499 | 5023 | 193 | 2025-12-20 17:40:29 |
| [django](https://github.com/django/django) | 86212 | 33442 | 0 | 20369 | 366 | 2025-12-19 20:10:12 |
| [flask](https://github.com/pallets/flask) | 70950 | 16667 | 2706 | 2736 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70399 | 33715 | 74770 | 67285 | 9248 | 2025-12-21 00:25:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64344 | 26512 | 11854 | 19934 | 2127 | 2025-12-18 23:08:39 |
| [keras](https://github.com/keras-team/keras) | 63653 | 19654 | 12606 | 8546 | 247 | 2025-12-20 00:20:41 |
| [pandas](https://github.com/pandas-dev/pandas) | 47366 | 19421 | 27978 | 35405 | 3605 | 2025-12-20 20:30:45 |
| [ray](https://github.com/ray-project/ray) | 40420 | 7020 | 22037 | 37220 | 3205 | 2025-12-20 20:25:35 |
| [gym](https://github.com/openai/gym) | 36884 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32973 | 4631 | 5734 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31056 | 11871 | 13708 | 16720 | 2379 | 2025-12-20 20:32:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29752 | 7043 | 3946 | 4890 | 81 | 2025-12-15 16:01:56 |
| [celery](https://github.com/celery/celery) | 27746 | 4918 | 5179 | 3745 | 752 | 2025-12-18 05:06:57 |
| [dash](https://github.com/plotly/dash) | 24350 | 2247 | 2039 | 1395 | 553 | 2025-12-18 16:31:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22390 | 5542 | 1861 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22145 | 8146 | 11087 | 19754 | 1546 | 2025-12-19 19:34:09 |
| [micropython](https://github.com/micropython/micropython) | 21237 | 8595 | 5903 | 7451 | 1813 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 20929 | 1372 | 1248 | 5153 | 435 | 2025-12-20 23:25:17 |
| [sanic](https://github.com/sanic-org/sanic) | 18603 | 1586 | 1456 | 1636 | 130 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18102 | 2764 | 3309 | 1993 | 758 | 2025-12-10 17:07:05 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16153 | 2167 | 3168 | 8388 | 273 | 2025-12-20 00:09:59 |
| [httpx](https://github.com/encode/httpx) | 14851 | 995 | 925 | 1772 | 121 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14276 | 5563 | 11205 | 12990 | 1777 | 2025-12-21 00:34:55 |
| [dask](https://github.com/dask/dask) | 13659 | 1826 | 5479 | 6428 | 1206 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13625 | 2070 | 2641 | 1150 | 200 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11771 | 1093 | 760 | 1748 | 53 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11527 | 591 | 398 | 299 | 150 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11293 | 1607 | 8132 | 1015 | 207 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9770 | 975 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8796 | 550 | 985 | 474 | 192 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8713 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7072 | 374 | 877 | 2482 | 314 | 2025-12-15 22:18:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 741 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5417 | 444 | 1210 | 732 | 510 | 2025-12-20 05:59:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5117 | 977 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4018 | 258 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3823 | 304 | 1170 | 205 | 119 | 2025-12-18 06:57:55 |
| [quart](https://github.com/pallets/quart) | 3561 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2720 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2334 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2331 | 180 | 420 | 560 | 75 | 2025-12-17 13:22:00 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-15 17:49:12 |
| [pypy](https://github.com/pypy/pypy) | 1608 | 92 | 5168 | 172 | 752 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-21T02:24:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
