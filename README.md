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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192182 | 74913 | 40882 | 59912 | 1640 | 2025-10-25 01:52:47 |
| [transformers](https://github.com/huggingface/transformers) | 151565 | 30930 | 18097 | 23164 | 2081 | 2025-10-24 18:52:45 |
| [pytorch](https://github.com/pytorch/pytorch) | 94226 | 25662 | 54473 | 111262 | 17008 | 2025-10-25 01:55:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 91112 | 8110 | 3472 | 4799 | 198 | 2025-10-23 20:55:59 |
| [django](https://github.com/django/django) | 85539 | 33140 | 0 | 19934 | 349 | 2025-10-24 19:51:39 |
| [flask](https://github.com/pallets/flask) | 70641 | 16596 | 2699 | 2714 | 16 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69511 | 33205 | 74095 | 65540 | 9208 | 2025-10-24 20:53:38 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63793 | 26359 | 11779 | 19658 | 2151 | 2025-10-24 17:22:16 |
| [keras](https://github.com/keras-team/keras) | 63505 | 19631 | 12572 | 8417 | 258 | 2025-10-24 23:11:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 46922 | 19184 | 27818 | 34957 | 3633 | 2025-10-24 23:52:45 |
| [ray](https://github.com/ray-project/ray) | 39490 | 6824 | 21703 | 36107 | 3318 | 2025-10-25 01:35:13 |
| [gym](https://github.com/openai/gym) | 36713 | 8713 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32699 | 4608 | 5727 | 4071 | 211 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30665 | 11620 | 13607 | 16402 | 2344 | 2025-10-24 22:28:51 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29601 | 7026 | 3945 | 4853 | 85 | 2025-10-22 12:47:30 |
| [celery](https://github.com/celery/celery) | 27408 | 4866 | 5174 | 3700 | 753 | 2025-10-23 12:38:38 |
| [dash](https://github.com/plotly/dash) | 24196 | 2220 | 2013 | 1355 | 577 | 2025-10-24 22:59:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22323 | 5535 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21870 | 8085 | 11021 | 19615 | 1629 | 2025-10-23 19:34:39 |
| [micropython](https://github.com/micropython/micropython) | 20990 | 8503 | 5857 | 7298 | 1773 | 2025-10-24 19:18:55 |
| [RustPython](https://github.com/RustPython/RustPython) | 20681 | 1355 | 1225 | 4925 | 441 | 2025-10-24 12:41:28 |
| [sanic](https://github.com/sanic-org/sanic) | 18532 | 1580 | 1450 | 1629 | 147 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17885 | 2732 | 3266 | 1966 | 725 | 2025-10-22 18:58:42 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16051 | 2141 | 3157 | 8256 | 263 | 2025-10-24 19:30:30 |
| [httpx](https://github.com/encode/httpx) | 14668 | 963 | 919 | 1747 | 102 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14121 | 5516 | 11097 | 12744 | 1789 | 2025-10-24 22:53:45 |
| [dask](https://github.com/dask/dask) | 13554 | 1808 | 5444 | 6370 | 1194 | 2025-10-24 18:00:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13514 | 2036 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11580 | 1050 | 755 | 1725 | 49 | 2025-10-21 19:01:09 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11366 | 581 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11042 | 1589 | 8106 | 995 | 218 | 2025-10-24 23:36:21 |
| [falcon](https://github.com/falconry/falcon) | 9742 | 969 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8681 | 1487 | 855 | 624 | 283 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8655 | 528 | 961 | 447 | 171 | 2025-10-23 07:16:59 |
| [trio](https://github.com/python-trio/trio) | 6912 | 371 | 872 | 2462 | 312 | 2025-10-24 13:13:16 |
| [hug](https://github.com/hugapi/hug) | 6902 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5345 | 440 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5052 | 950 | 874 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4055 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3709 | 294 | 1163 | 196 | 118 | 2025-10-18 20:09:08 |
| [quart](https://github.com/pallets/quart) | 3507 | 190 | 277 | 123 | 63 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2697 | 303 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2317 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2260 | 167 | 408 | 532 | 68 | 2025-10-24 23:00:58 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 909 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 369 | 1780 | 264 | 260 | 2025-10-20 20:06:23 |
| [pypy](https://github.com/pypy/pypy) | 1545 | 87 | 5153 | 171 | 740 | 2025-10-20 16:20:39 |
| [jython](https://github.com/jython/jython) | 1447 | 225 | 282 | 114 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-25T01:56:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
