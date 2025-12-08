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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192708 | 75031 | 41025 | 62663 | 2729 | 2025-12-08 02:00:07 |
| [transformers](https://github.com/huggingface/transformers) | 153560 | 31335 | 18288 | 23798 | 2137 | 2025-12-07 20:28:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 95670 | 26125 | 55701 | 113601 | 17821 | 2025-12-08 02:08:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 92818 | 8338 | 3483 | 4941 | 191 | 2025-12-06 13:10:45 |
| [django](https://github.com/django/django) | 86076 | 33299 | 0 | 20312 | 364 | 2025-12-07 14:08:01 |
| [flask](https://github.com/pallets/flask) | 70888 | 16644 | 2704 | 2730 | 12 | 2025-11-28 19:06:04 |
| [cpython](https://github.com/python/cpython) | 70167 | 33610 | 74572 | 66850 | 9239 | 2025-12-08 00:51:52 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64223 | 26487 | 11837 | 19882 | 2116 | 2025-12-05 16:59:36 |
| [keras](https://github.com/keras-team/keras) | 63628 | 19651 | 12601 | 8508 | 257 | 2025-12-07 02:35:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 47275 | 19366 | 27938 | 35295 | 3571 | 2025-12-07 14:01:28 |
| [ray](https://github.com/ray-project/ray) | 40197 | 6979 | 21977 | 36918 | 3209 | 2025-12-07 23:28:26 |
| [gym](https://github.com/openai/gym) | 36846 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32917 | 4635 | 5733 | 4075 | 183 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 30963 | 11805 | 13688 | 16638 | 2381 | 2025-12-07 20:20:06 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29712 | 7039 | 3946 | 4880 | 82 | 2025-12-05 12:11:42 |
| [celery](https://github.com/celery/celery) | 27690 | 4911 | 5177 | 3737 | 751 | 2025-12-05 12:28:43 |
| [dash](https://github.com/plotly/dash) | 24320 | 2242 | 2034 | 1386 | 557 | 2025-12-05 17:17:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22384 | 5543 | 1857 | 1678 | 207 | 2025-12-06 04:51:33 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22096 | 8138 | 11064 | 19711 | 1594 | 2025-12-07 17:47:41 |
| [micropython](https://github.com/micropython/micropython) | 21181 | 8575 | 5889 | 7412 | 1786 | 2025-12-08 01:16:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 20877 | 1365 | 1242 | 5035 | 443 | 2025-12-08 01:39:15 |
| [sanic](https://github.com/sanic-org/sanic) | 18592 | 1585 | 1454 | 1635 | 128 | 2025-12-04 05:51:33 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18061 | 2757 | 3304 | 1990 | 755 | 2025-12-05 23:04:44 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16132 | 2165 | 3164 | 8343 | 270 | 2025-12-07 18:00:16 |
| [httpx](https://github.com/encode/httpx) | 14816 | 983 | 923 | 1759 | 117 | 2025-12-01 17:39:25 |
| [scipy](https://github.com/scipy/scipy) | 14245 | 5553 | 11172 | 12924 | 1764 | 2025-12-08 00:02:04 |
| [dask](https://github.com/dask/dask) | 13643 | 1825 | 5472 | 6412 | 1199 | 2025-12-05 11:49:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13602 | 2058 | 2637 | 1149 | 195 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11738 | 1088 | 760 | 1746 | 52 | 2025-12-04 11:24:48 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11501 | 589 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11228 | 1603 | 8128 | 1009 | 212 | 2025-12-07 14:16:25 |
| [falcon](https://github.com/falconry/falcon) | 9767 | 971 | 1114 | 1403 | 162 | 2025-12-07 23:04:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8762 | 545 | 980 | 464 | 179 | 2025-12-04 11:35:16 |
| [bottle](https://github.com/bottlepy/bottle) | 8709 | 1488 | 859 | 625 | 285 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 7044 | 371 | 876 | 2478 | 313 | 2025-12-06 01:51:15 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 744 | 979 | 581 | 35 | 2025-12-04 09:43:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5624 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5405 | 445 | 1203 | 725 | 509 | 2025-12-06 18:23:28 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5107 | 971 | 879 | 264 | 174 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4068 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4022 | 259 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3805 | 301 | 1169 | 202 | 117 | 2025-11-30 16:42:39 |
| [quart](https://github.com/pallets/quart) | 3554 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2715 | 305 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2331 | 135 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2320 | 180 | 418 | 554 | 72 | 2025-12-01 20:04:08 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1078 | 1462 | 369 | 2025-11-28 05:33:05 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 369 | 1784 | 266 | 265 | 2025-12-01 17:53:21 |
| [pypy](https://github.com/pypy/pypy) | 1592 | 91 | 5166 | 172 | 750 | 2025-12-03 20:52:04 |
| [jython](https://github.com/jython/jython) | 1462 | 225 | 286 | 115 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-11-24 17:09:55 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-12-08T02:09:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
