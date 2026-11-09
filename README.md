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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201403 | 78177 | 41965 | 84521 | 3524 | 2026-11-09 05:44:57 |
| [transformers](https://github.com/huggingface/transformers) | 168673 | 35143 | 19813 | 29847 | 1071 | 2026-11-09 05:32:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 105270 | 31070 | 62397 | 140918 | 18133 | 2026-11-09 05:46:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 104582 | 10208 | 3555 | 6596 | 61 | 2026-11-08 18:01:45 |
| [django](https://github.com/django/django) | 91692 | 35695 | 0 | 22185 | 536 | 2026-11-06 22:17:53 |
| [cpython](https://github.com/python/cpython) | 78114 | 36973 | 79194 | 80067 | 9266 | 2026-11-09 04:40:56 |
| [flask](https://github.com/pallets/flask) | 75078 | 17289 | 2778 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68101 | 27658 | 12372 | 21776 | 2167 | 2026-11-06 12:37:21 |
| [keras](https://github.com/keras-team/keras) | 64417 | 19820 | 13070 | 10224 | 286 | 2026-11-06 21:43:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 50545 | 20732 | 28670 | 39864 | 1936 | 2026-11-09 05:30:22 |
| [ray](https://github.com/ray-project/ray) | 44240 | 8258 | 23297 | 44199 | 3746 | 2026-11-09 05:45:09 |
| [gym](https://github.com/openai/gym) | 37233 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34037 | 4740 | 5783 | 4145 | 267 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33405 | 13098 | 14171 | 18980 | 2246 | 2026-11-07 21:05:25 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30229 | 7098 | 3966 | 5107 | 64 | 2026-11-07 13:50:43 |
| [celery](https://github.com/celery/celery) | 29159 | 5260 | 5371 | 4706 | 760 | 2026-11-08 12:06:57 |
| [dash](https://github.com/plotly/dash) | 24481 | 2341 | 2178 | 1823 | 448 | 2026-11-06 15:40:44 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23435 | 8542 | 11456 | 21041 | 1472 | 2026-11-09 05:07:36 |
| [RustPython](https://github.com/RustPython/RustPython) | 22469 | 1510 | 1459 | 8198 | 318 | 2026-11-08 11:38:49 |
| [micropython](https://github.com/micropython/micropython) | 22182 | 9048 | 6174 | 8224 | 1579 | 2026-11-08 12:20:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22164 | 5607 | 1893 | 1917 | 230 | 2026-11-09 01:37:59 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18884 | 2894 | 3402 | 2280 | 755 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1616 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16606 | 2516 | 3274 | 10669 | 295 | 2026-11-09 00:59:17 |
| [httpx](https://github.com/encode/httpx) | 15759 | 2306 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15192 | 6071 | 11761 | 14868 | 1908 | 2026-11-08 22:38:02 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14100 | 2159 | 2668 | 1254 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13942 | 2017 | 5582 | 6812 | 1429 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12714 | 1442 | 797 | 2305 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12271 | 1849 | 8384 | 1262 | 209 | 2026-11-08 15:34:18 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11930 | 619 | 430 | 345 | 176 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9813 | 1053 | 1151 | 1569 | 163 | 2026-11-07 22:41:22 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9241 | 628 | 1057 | 615 | 160 | 2026-11-08 16:39:21 |
| [bottle](https://github.com/bottlepy/bottle) | 8797 | 1515 | 866 | 656 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7357 | 472 | 910 | 2664 | 343 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6869 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 736 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5647 | 543 | 1307 | 988 | 563 | 2026-11-07 04:17:10 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5447 | 1054 | 938 | 329 | 207 | 2026-11-07 09:09:52 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4471 | 392 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 896 | 1066 | 2743 | 92 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 279 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3681 | 211 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 319 | 681 | 1412 | 258 | 2026-11-08 22:25:11 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 349 | 498 | 888 | 148 | 2026-11-08 13:41:57 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 915 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 372 | 1791 | 280 | 280 | 2026-11-06 00:44:46 |
| [pypy](https://github.com/pypy/pypy) | 1823 | 131 | 5300 | 406 | 719 | 2026-11-08 22:23:38 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 159 | 104 | 2026-11-07 21:07:33 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-09T05:55:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
