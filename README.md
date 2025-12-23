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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192990 | 75144 | 41048 | 63764 | 2423 | 2025-12-23 02:16:17 |
| [transformers](https://github.com/huggingface/transformers) | 154144 | 31509 | 18359 | 24047 | 2139 | 2025-12-22 19:02:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 96085 | 26335 | 56006 | 114645 | 17928 | 2025-12-23 02:17:39 |
| [fastapi](https://github.com/fastapi/fastapi) | 93336 | 8405 | 3499 | 5035 | 197 | 2025-12-21 18:24:52 |
| [django](https://github.com/django/django) | 86234 | 33409 | 0 | 20384 | 368 | 2025-12-23 02:04:49 |
| [flask](https://github.com/pallets/flask) | 70956 | 16667 | 2706 | 2737 | 13 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70426 | 33726 | 74788 | 67322 | 9247 | 2025-12-23 00:28:08 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64364 | 26520 | 11856 | 19935 | 2120 | 2025-12-22 19:33:00 |
| [keras](https://github.com/keras-team/keras) | 63658 | 19654 | 12606 | 8548 | 248 | 2025-12-22 22:52:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 47380 | 19428 | 27981 | 35424 | 3605 | 2025-12-22 21:51:39 |
| [ray](https://github.com/ray-project/ray) | 40435 | 7025 | 22041 | 37227 | 3200 | 2025-12-23 02:08:50 |
| [gym](https://github.com/openai/gym) | 36886 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32974 | 4630 | 5735 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31076 | 11877 | 13712 | 16731 | 2380 | 2025-12-22 19:27:16 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29758 | 7045 | 3946 | 4892 | 81 | 2025-12-23 00:43:52 |
| [celery](https://github.com/celery/celery) | 27758 | 4919 | 5179 | 3747 | 752 | 2025-12-22 17:26:19 |
| [dash](https://github.com/plotly/dash) | 24354 | 2246 | 2039 | 1395 | 553 | 2025-12-22 23:39:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22393 | 5544 | 1861 | 1690 | 209 | 2025-12-17 18:38:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22149 | 8146 | 11088 | 19758 | 1544 | 2025-12-22 19:03:21 |
| [micropython](https://github.com/micropython/micropython) | 21243 | 8597 | 5903 | 7451 | 1812 | 2025-12-19 06:12:00 |
| [RustPython](https://github.com/RustPython/RustPython) | 20932 | 1371 | 1248 | 5157 | 434 | 2025-12-22 23:57:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18604 | 1586 | 1456 | 1636 | 130 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18109 | 2764 | 3309 | 1994 | 758 | 2025-12-22 19:45:25 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16155 | 2168 | 3168 | 8395 | 269 | 2025-12-22 16:03:26 |
| [httpx](https://github.com/encode/httpx) | 14858 | 996 | 925 | 1773 | 122 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14281 | 5565 | 11211 | 12999 | 1780 | 2025-12-22 19:35:53 |
| [dask](https://github.com/dask/dask) | 13660 | 1827 | 5479 | 6428 | 1206 | 2025-12-17 09:40:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13629 | 2070 | 2642 | 1150 | 201 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11777 | 1092 | 760 | 1748 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11532 | 591 | 398 | 299 | 150 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11305 | 1607 | 8133 | 1016 | 209 | 2025-12-19 21:41:44 |
| [falcon](https://github.com/falconry/falcon) | 9770 | 975 | 1114 | 1404 | 163 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8804 | 550 | 985 | 474 | 192 | 2025-12-09 15:06:52 |
| [bottle](https://github.com/bottlepy/bottle) | 8717 | 1489 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7073 | 374 | 877 | 2483 | 314 | 2025-12-22 21:33:49 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 741 | 979 | 582 | 36 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5621 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5418 | 444 | 1211 | 732 | 510 | 2025-12-22 01:19:21 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5121 | 978 | 882 | 272 | 176 | 2025-12-11 12:41:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4018 | 259 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3833 | 303 | 1171 | 205 | 118 | 2025-12-22 19:47:52 |
| [quart](https://github.com/pallets/quart) | 3562 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2718 | 308 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2335 | 136 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2331 | 180 | 420 | 561 | 75 | 2025-12-22 17:46:05 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 911 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1929 | 369 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1608 | 92 | 5169 | 172 | 753 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1460 | 225 | 288 | 120 | 105 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-23T02:18:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
