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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194136 | 75241 | 41225 | 69023 | 3728 | 2026-03-15 03:04:41 |
| [transformers](https://github.com/huggingface/transformers) | 157818 | 32477 | 18712 | 25396 | 2306 | 2026-03-14 21:09:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 98255 | 27209 | 57310 | 119638 | 18054 | 2026-03-15 02:49:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 96207 | 8859 | 3511 | 5431 | 158 | 2026-03-14 15:02:04 |
| [django](https://github.com/django/django) | 87042 | 33748 | 0 | 20843 | 429 | 2026-03-14 18:11:27 |
| [cpython](https://github.com/python/cpython) | 71945 | 34225 | 75560 | 69393 | 9304 | 2026-03-15 03:05:38 |
| [flask](https://github.com/pallets/flask) | 71333 | 16743 | 2724 | 2782 | 4 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65393 | 26792 | 11992 | 20391 | 2146 | 2026-03-14 22:27:36 |
| [keras](https://github.com/keras-team/keras) | 63905 | 19737 | 12671 | 8964 | 266 | 2026-03-13 23:34:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 48137 | 19740 | 28172 | 36359 | 3673 | 2026-03-14 21:52:47 |
| [ray](https://github.com/ray-project/ray) | 41725 | 7339 | 22449 | 38947 | 3472 | 2026-03-15 02:03:01 |
| [gym](https://github.com/openai/gym) | 37097 | 8707 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33328 | 4659 | 5744 | 4083 | 196 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31605 | 12166 | 13830 | 17121 | 2333 | 2026-03-15 00:16:26 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29929 | 7078 | 3946 | 4942 | 78 | 2026-03-11 04:08:31 |
| [celery](https://github.com/celery/celery) | 28211 | 4988 | 5207 | 3862 | 769 | 2026-03-14 04:56:02 |
| [dash](https://github.com/plotly/dash) | 24460 | 2263 | 2070 | 1470 | 579 | 2026-03-13 22:51:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22577 | 8264 | 11200 | 20058 | 1540 | 2026-03-13 19:28:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22411 | 5546 | 1864 | 1711 | 218 | 2026-03-12 20:53:26 |
| [RustPython](https://github.com/RustPython/RustPython) | 21880 | 1406 | 1314 | 6048 | 361 | 2026-03-14 11:27:32 |
| [micropython](https://github.com/micropython/micropython) | 21542 | 8744 | 5974 | 7621 | 1852 | 2026-03-11 05:40:49 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18342 | 2787 | 3329 | 2055 | 777 | 2026-03-12 18:15:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16374 | 2212 | 3182 | 8743 | 277 | 2026-03-12 10:47:02 |
| [httpx](https://github.com/encode/httpx) | 15138 | 1063 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14535 | 5657 | 11373 | 13440 | 1795 | 2026-03-14 21:55:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13771 | 2084 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13765 | 1857 | 5516 | 6506 | 1229 | 2026-03-12 11:13:54 |
| [starlette](https://github.com/Kludex/starlette) | 12025 | 1134 | 764 | 1830 | 46 | 2026-03-14 06:00:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11688 | 602 | 408 | 316 | 157 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11658 | 1652 | 8167 | 1045 | 215 | 2026-03-09 22:58:15 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1419 | 162 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8947 | 564 | 1021 | 495 | 221 | 2026-03-13 12:05:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1501 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7204 | 391 | 880 | 2512 | 318 | 2026-03-11 03:55:14 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5607 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5516 | 466 | 1240 | 799 | 495 | 2026-03-14 23:23:43 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5207 | 1000 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 894 | 1064 | 2732 | 82 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4018 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4010 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3606 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 312 | 662 | 1298 | 308 | 2026-03-14 14:21:41 |
| [anyio](https://github.com/agronholm/anyio) | 2408 | 187 | 429 | 584 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1681 | 103 | 5179 | 184 | 758 | 2026-03-13 10:47:43 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-15T03:23:02*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
