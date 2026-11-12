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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201571 | 77907 | 41973 | 84643 | 3441 | 2026-11-12 06:50:37 |
| [transformers](https://github.com/huggingface/transformers) | 168888 | 35220 | 19849 | 29955 | 1085 | 2026-11-12 06:51:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 105447 | 30695 | 62512 | 141333 | 18191 | 2026-11-12 06:50:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 104646 | 10237 | 3555 | 6606 | 53 | 2026-11-11 22:29:35 |
| [django](https://github.com/django/django) | 91719 | 35223 | 0 | 22191 | 533 | 2026-11-11 17:52:42 |
| [cpython](https://github.com/python/cpython) | 78175 | 36570 | 79244 | 80199 | 9286 | 2026-11-12 06:45:14 |
| [flask](https://github.com/pallets/flask) | 75103 | 17314 | 2779 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68149 | 27669 | 12380 | 21802 | 2175 | 2026-11-11 20:16:46 |
| [keras](https://github.com/keras-team/keras) | 64422 | 19820 | 13082 | 10262 | 247 | 2026-11-12 00:33:17 |
| [pandas](https://github.com/pandas-dev/pandas) | 50493 | 20735 | 28683 | 39959 | 1904 | 2026-11-12 01:48:58 |
| [ray](https://github.com/ray-project/ray) | 44269 | 8275 | 23308 | 44300 | 3768 | 2026-11-12 06:38:47 |
| [gym](https://github.com/openai/gym) | 37236 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34046 | 4739 | 5783 | 4146 | 267 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33342 | 13097 | 14180 | 19013 | 2245 | 2026-11-12 02:01:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30231 | 7101 | 3966 | 5113 | 65 | 2026-11-11 13:18:12 |
| [celery](https://github.com/celery/celery) | 29175 | 5260 | 5381 | 4720 | 780 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24488 | 2346 | 2181 | 1834 | 441 | 2026-11-10 18:47:32 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23453 | 8545 | 11460 | 21061 | 1475 | 2026-11-11 20:45:25 |
| [RustPython](https://github.com/RustPython/RustPython) | 22479 | 1509 | 1463 | 8248 | 313 | 2026-11-12 05:28:03 |
| [micropython](https://github.com/micropython/micropython) | 22191 | 9054 | 6178 | 8244 | 1592 | 2026-11-11 05:13:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5608 | 1894 | 1922 | 227 | 2026-11-09 22:44:01 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18896 | 2895 | 3402 | 2281 | 753 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1617 | 1474 | 1689 | 163 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16607 | 2520 | 3275 | 10706 | 303 | 2026-11-11 19:50:11 |
| [httpx](https://github.com/encode/httpx) | 15789 | 1869 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15207 | 6079 | 11763 | 14890 | 1904 | 2026-11-10 11:23:46 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14108 | 2160 | 2668 | 1255 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13948 | 2019 | 5582 | 6814 | 1431 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12727 | 1442 | 797 | 2305 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12276 | 1848 | 8390 | 1263 | 208 | 2026-11-11 20:51:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11935 | 620 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9814 | 1056 | 1151 | 1576 | 163 | 2026-11-11 09:13:34 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9243 | 626 | 1057 | 616 | 158 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1512 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7361 | 475 | 911 | 2670 | 346 | 2026-11-10 01:52:37 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 31 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5645 | 544 | 1307 | 989 | 556 | 2026-11-11 03:10:19 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5448 | 1054 | 938 | 333 | 206 | 2026-11-11 12:33:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4473 | 390 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4106 | 898 | 1066 | 2748 | 90 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3985 | 278 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 212 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 320 | 682 | 1414 | 257 | 2026-11-11 13:24:56 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 498 | 892 | 146 | 2026-11-11 16:14:18 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 281 | 279 | 2026-11-09 18:05:48 |
| [pypy](https://github.com/pypy/pypy) | 1823 | 133 | 5301 | 414 | 722 | 2026-11-12 06:33:05 |
| [jython](https://github.com/jython/jython) | 1551 | 236 | 305 | 162 | 106 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-12T06:56:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
