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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191643 | 74828 | 40791 | 57530 | 1662 | 2025-09-16 01:44:04 |
| [transformers](https://github.com/huggingface/transformers) | 149835 | 30406 | 17922 | 22401 | 1992 | 2025-09-16 00:47:48 |
| [pytorch](https://github.com/pytorch/pytorch) | 93199 | 25291 | 53761 | 108820 | 17119 | 2025-09-16 01:53:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 89496 | 7874 | 3468 | 4716 | 246 | 2025-09-15 17:36:07 |
| [django](https://github.com/django/django) | 85000 | 32966 | 0 | 19803 | 373 | 2025-09-16 01:14:50 |
| [flask](https://github.com/pallets/flask) | 70362 | 16532 | 2695 | 2702 | 9 | 2025-09-12 21:52:55 |
| [cpython](https://github.com/python/cpython) | 68878 | 32874 | 73607 | 64437 | 9337 | 2025-09-15 22:53:51 |
| [keras](https://github.com/keras-team/keras) | 63406 | 19622 | 12546 | 8336 | 267 | 2025-09-15 21:01:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63350 | 26236 | 11710 | 19355 | 2167 | 2025-09-15 08:31:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 46585 | 18924 | 27712 | 34586 | 3656 | 2025-09-15 22:05:54 |
| [ray](https://github.com/ray-project/ray) | 38945 | 6800 | 21098 | 35120 | 3083 | 2025-09-16 01:12:28 |
| [gym](https://github.com/openai/gym) | 36510 | 8692 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32480 | 4579 | 5722 | 4069 | 205 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30402 | 11351 | 13541 | 16154 | 2360 | 2025-09-15 23:54:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29467 | 7003 | 3945 | 4831 | 100 | 2025-09-15 19:45:43 |
| [celery](https://github.com/celery/celery) | 27194 | 4842 | 5161 | 3655 | 756 | 2025-09-15 16:48:26 |
| [dash](https://github.com/plotly/dash) | 24051 | 2200 | 1993 | 1330 | 560 | 2025-09-15 23:23:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22183 | 5538 | 1852 | 1674 | 209 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21694 | 8000 | 10982 | 19537 | 1627 | 2025-09-15 19:02:31 |
| [micropython](https://github.com/micropython/micropython) | 20820 | 8427 | 5811 | 7183 | 1785 | 2025-09-16 01:31:20 |
| [RustPython](https://github.com/RustPython/RustPython) | 20518 | 1344 | 1220 | 4868 | 443 | 2025-09-16 00:35:08 |
| [sanic](https://github.com/sanic-org/sanic) | 18491 | 1579 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17728 | 2708 | 3251 | 1951 | 720 | 2025-09-15 14:11:49 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15988 | 2123 | 3145 | 8068 | 273 | 2025-09-15 12:57:39 |
| [httpx](https://github.com/encode/httpx) | 14550 | 955 | 918 | 1724 | 104 | 2025-09-12 11:19:51 |
| [scipy](https://github.com/scipy/scipy) | 14024 | 5475 | 11026 | 12583 | 1768 | 2025-09-15 23:24:09 |
| [dask](https://github.com/dask/dask) | 13484 | 1797 | 5437 | 6344 | 1201 | 2025-09-15 22:03:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13434 | 2033 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11457 | 1038 | 753 | 1704 | 49 | 2025-09-13 10:21:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11251 | 573 | 388 | 289 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10892 | 1580 | 8084 | 982 | 231 | 2025-09-15 21:56:02 |
| [falcon](https://github.com/falconry/falcon) | 9717 | 959 | 1099 | 1368 | 158 | 2025-09-10 04:12:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8658 | 1486 | 855 | 622 | 284 | 2025-09-13 12:31:44 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8536 | 523 | 942 | 434 | 409 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6895 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6858 | 367 | 867 | 2450 | 309 | 2025-09-15 21:35:35 |
| [eve](https://github.com/pyeve/eve) | 6734 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5632 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5290 | 437 | 1192 | 713 | 500 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4982 | 938 | 869 | 260 | 166 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4046 | 889 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3606 | 291 | 1157 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3449 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2686 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2307 | 131 | 426 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2210 | 163 | 401 | 509 | 67 | 2025-09-15 17:46:56 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 909 | 1077 | 1458 | 369 | 2025-09-13 16:04:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1780 | 264 | 261 | 2025-09-15 17:40:35 |
| [pypy](https://github.com/pypy/pypy) | 1497 | 86 | 5143 | 168 | 734 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1431 | 220 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-16T01:53:42*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
