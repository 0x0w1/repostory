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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191257 | 74787 | 40735 | 56430 | 1511 | 2025-08-21 01:56:44 |
| [transformers](https://github.com/huggingface/transformers) | 148579 | 30115 | 17807 | 21946 | 1958 | 2025-08-20 20:59:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 92547 | 25032 | 53232 | 107439 | 16850 | 2025-08-21 01:59:10 |
| [fastapi](https://github.com/fastapi/fastapi) | 88591 | 7749 | 3466 | 4664 | 280 | 2025-08-20 09:12:14 |
| [django](https://github.com/django/django) | 84635 | 32834 | 0 | 19690 | 364 | 2025-08-20 08:29:07 |
| [flask](https://github.com/pallets/flask) | 70196 | 16524 | 2692 | 2688 | 4 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68458 | 32673 | 73347 | 63732 | 9292 | 2025-08-20 21:59:40 |
| [keras](https://github.com/keras-team/keras) | 63352 | 19613 | 12527 | 8290 | 295 | 2025-08-21 01:42:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63085 | 26162 | 11655 | 19199 | 2157 | 2025-08-20 15:08:21 |
| [pandas](https://github.com/pandas-dev/pandas) | 46349 | 18837 | 27665 | 34447 | 3706 | 2025-08-20 20:30:48 |
| [ray](https://github.com/ray-project/ray) | 38563 | 6728 | 20917 | 34531 | 2984 | 2025-08-21 01:48:33 |
| [gym](https://github.com/openai/gym) | 36406 | 8687 | 1838 | 1464 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32209 | 4564 | 5717 | 4064 | 198 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30193 | 11233 | 13494 | 16045 | 2344 | 2025-08-21 00:23:52 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29390 | 6994 | 3945 | 4827 | 98 | 2025-08-16 07:10:06 |
| [celery](https://github.com/celery/celery) | 27046 | 4829 | 5156 | 3640 | 760 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23960 | 2190 | 1976 | 1314 | 551 | 2025-08-20 19:56:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22105 | 5539 | 1851 | 1670 | 207 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21583 | 7968 | 10946 | 19460 | 1648 | 2025-08-20 23:39:09 |
| [micropython](https://github.com/micropython/micropython) | 20743 | 8371 | 5788 | 7125 | 1769 | 2025-08-19 12:06:34 |
| [RustPython](https://github.com/RustPython/RustPython) | 20421 | 1342 | 1208 | 4830 | 445 | 2025-08-20 08:34:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18476 | 1579 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17624 | 2703 | 3241 | 1944 | 721 | 2025-08-19 14:08:55 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15927 | 2113 | 3143 | 8003 | 264 | 2025-08-20 11:43:42 |
| [httpx](https://github.com/encode/httpx) | 14483 | 945 | 915 | 1708 | 103 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13935 | 5448 | 10976 | 12495 | 1764 | 2025-08-20 17:28:56 |
| [dask](https://github.com/dask/dask) | 13423 | 1792 | 5425 | 6333 | 1192 | 2025-08-18 17:01:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13374 | 2027 | 2623 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11367 | 1031 | 750 | 1680 | 48 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11156 | 569 | 388 | 287 | 141 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10795 | 1575 | 8068 | 977 | 237 | 2025-08-19 17:26:41 |
| [falcon](https://github.com/falconry/falcon) | 9703 | 959 | 1093 | 1359 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8646 | 1488 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8458 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6892 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6727 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6722 | 363 | 863 | 2442 | 312 | 2025-08-18 22:06:52 |
| [vibora](https://github.com/vibora-io/vibora) | 5634 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5251 | 436 | 1186 | 711 | 496 | 2025-08-20 19:50:16 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4949 | 926 | 864 | 257 | 158 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1061 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3534 | 288 | 1153 | 194 | 117 | 2025-08-16 13:58:56 |
| [quart](https://github.com/pallets/quart) | 3403 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2677 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2302 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2178 | 164 | 399 | 499 | 68 | 2025-08-18 17:55:01 |
| [web2py](https://github.com/web2py/web2py) | 2154 | 906 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-08-18 17:39:32 |
| [pypy](https://github.com/pypy/pypy) | 1474 | 83 | 5141 | 168 | 735 | 2025-08-19 15:10:36 |
| [jython](https://github.com/jython/jython) | 1426 | 217 | 280 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 99 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-21T02:01:11*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
