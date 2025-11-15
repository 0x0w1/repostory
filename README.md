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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192427 | 74990 | 40995 | 61343 | 2301 | 2025-11-15 01:55:18 |
| [transformers](https://github.com/huggingface/transformers) | 152518 | 31143 | 18193 | 23425 | 2126 | 2025-11-14 23:34:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 95062 | 25906 | 54874 | 112538 | 17082 | 2025-11-15 01:59:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 91932 | 8226 | 3477 | 4873 | 215 | 2025-11-13 17:05:28 |
| [django](https://github.com/django/django) | 85788 | 33223 | 0 | 20032 | 353 | 2025-11-14 14:26:05 |
| [flask](https://github.com/pallets/flask) | 70781 | 16620 | 2701 | 2724 | 15 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69866 | 33415 | 74349 | 66282 | 9191 | 2025-11-15 01:25:19 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64028 | 26435 | 11811 | 19767 | 2114 | 2025-11-14 17:04:02 |
| [keras](https://github.com/keras-team/keras) | 63551 | 19650 | 12591 | 8470 | 264 | 2025-11-14 19:35:13 |
| [pandas](https://github.com/pandas-dev/pandas) | 47108 | 19298 | 27882 | 35181 | 3617 | 2025-11-14 23:32:49 |
| [ray](https://github.com/ray-project/ray) | 39825 | 6902 | 21821 | 36481 | 3200 | 2025-11-15 01:33:39 |
| [gym](https://github.com/openai/gym) | 36770 | 8710 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32817 | 4621 | 5731 | 4072 | 196 | 2025-11-13 13:25:50 |
| [numpy](https://github.com/numpy/numpy) | 30825 | 11701 | 13648 | 16508 | 2354 | 2025-11-14 18:36:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29665 | 7036 | 3946 | 4867 | 87 | 2025-11-06 16:05:46 |
| [celery](https://github.com/celery/celery) | 27551 | 4890 | 5176 | 3723 | 754 | 2025-11-14 11:29:11 |
| [dash](https://github.com/plotly/dash) | 24252 | 2231 | 2024 | 1369 | 578 | 2025-11-14 15:14:45 |
| [tornado](https://github.com/tornadoweb/tornado) | 22346 | 5544 | 1853 | 1675 | 206 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21984 | 8113 | 11044 | 19661 | 1623 | 2025-11-13 20:19:41 |
| [micropython](https://github.com/micropython/micropython) | 21092 | 8532 | 5873 | 7346 | 1804 | 2025-11-13 03:40:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 20793 | 1358 | 1228 | 4973 | 451 | 2025-11-14 22:27:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18559 | 1582 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17971 | 2747 | 3291 | 1978 | 748 | 2025-11-14 19:08:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16090 | 2155 | 3161 | 8298 | 282 | 2025-11-13 10:33:58 |
| [httpx](https://github.com/encode/httpx) | 14742 | 976 | 921 | 1755 | 111 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14190 | 5538 | 11136 | 12836 | 1796 | 2025-11-14 00:36:39 |
| [dask](https://github.com/dask/dask) | 13594 | 1822 | 5458 | 6401 | 1193 | 2025-11-14 13:49:23 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13557 | 2044 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11659 | 1079 | 759 | 1744 | 51 | 2025-11-04 07:29:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11423 | 584 | 396 | 298 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11130 | 1596 | 8116 | 1000 | 210 | 2025-11-14 17:46:35 |
| [falcon](https://github.com/falconry/falcon) | 9757 | 973 | 1111 | 1401 | 164 | 2025-11-13 20:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8709 | 536 | 967 | 453 | 173 | 2025-11-14 16:27:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8690 | 1488 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [trio](https://github.com/python-trio/trio) | 6996 | 371 | 873 | 2469 | 313 | 2025-11-11 03:51:31 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5376 | 444 | 1197 | 715 | 503 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5083 | 963 | 876 | 263 | 171 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4061 | 887 | 1062 | 2721 | 90 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3934 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3752 | 300 | 1166 | 200 | 116 | 2025-11-14 20:35:35 |
| [quart](https://github.com/pallets/quart) | 3540 | 190 | 278 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2706 | 306 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2320 | 134 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2294 | 176 | 414 | 546 | 75 | 2025-11-14 16:10:07 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1927 | 371 | 1783 | 265 | 263 | 2025-11-14 03:49:17 |
| [pypy](https://github.com/pypy/pypy) | 1568 | 89 | 5162 | 171 | 747 | 2025-11-12 10:52:05 |
| [jython](https://github.com/jython/jython) | 1456 | 225 | 285 | 114 | 103 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 112 | 75 | 2025-11-14 15:44:44 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-15T02:00:50*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
