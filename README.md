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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194125 | 75246 | 41224 | 68989 | 3711 | 2026-03-14 02:43:00 |
| [transformers](https://github.com/huggingface/transformers) | 157772 | 32464 | 18708 | 25370 | 2282 | 2026-03-13 23:15:04 |
| [pytorch](https://github.com/pytorch/pytorch) | 98217 | 27194 | 57309 | 119614 | 18054 | 2026-03-14 02:33:47 |
| [fastapi](https://github.com/fastapi/fastapi) | 96183 | 8853 | 3509 | 5427 | 159 | 2026-03-13 19:53:13 |
| [django](https://github.com/django/django) | 87034 | 33749 | 0 | 20838 | 426 | 2026-03-13 20:29:10 |
| [cpython](https://github.com/python/cpython) | 71929 | 34221 | 75556 | 69371 | 9304 | 2026-03-13 18:44:51 |
| [flask](https://github.com/pallets/flask) | 71326 | 16743 | 2723 | 2782 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65378 | 26785 | 11989 | 20388 | 2146 | 2026-03-13 17:56:36 |
| [keras](https://github.com/keras-team/keras) | 63905 | 19736 | 12664 | 8957 | 253 | 2026-03-13 23:34:27 |
| [pandas](https://github.com/pandas-dev/pandas) | 48130 | 19740 | 28171 | 36352 | 3681 | 2026-03-13 20:32:53 |
| [ray](https://github.com/ray-project/ray) | 41718 | 7333 | 22448 | 38933 | 3463 | 2026-03-14 02:35:51 |
| [gym](https://github.com/openai/gym) | 37094 | 8707 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33322 | 4657 | 5744 | 4083 | 196 | 2026-03-09 15:12:34 |
| [numpy](https://github.com/numpy/numpy) | 31600 | 12158 | 13830 | 17119 | 2334 | 2026-03-13 19:26:08 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29932 | 7078 | 3946 | 4942 | 78 | 2026-03-11 04:08:31 |
| [celery](https://github.com/celery/celery) | 28208 | 4987 | 5205 | 3861 | 772 | 2026-03-12 14:51:00 |
| [dash](https://github.com/plotly/dash) | 24459 | 2263 | 2070 | 1470 | 579 | 2026-03-13 22:51:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22574 | 8260 | 11200 | 20056 | 1538 | 2026-03-13 19:28:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22411 | 5546 | 1864 | 1711 | 218 | 2026-03-12 20:53:26 |
| [RustPython](https://github.com/RustPython/RustPython) | 21880 | 1405 | 1314 | 6039 | 361 | 2026-03-14 00:45:44 |
| [micropython](https://github.com/micropython/micropython) | 21536 | 8741 | 5973 | 7620 | 1850 | 2026-03-11 05:40:49 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18334 | 2787 | 3329 | 2055 | 777 | 2026-03-12 18:15:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16372 | 2212 | 3182 | 8741 | 275 | 2026-03-12 10:47:02 |
| [httpx](https://github.com/encode/httpx) | 15134 | 1063 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14532 | 5657 | 11370 | 13434 | 1794 | 2026-03-14 00:17:33 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13771 | 2081 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13764 | 1856 | 5514 | 6506 | 1227 | 2026-03-12 11:13:54 |
| [starlette](https://github.com/Kludex/starlette) | 12026 | 1134 | 764 | 1828 | 47 | 2026-03-12 21:11:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11684 | 602 | 407 | 316 | 156 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11657 | 1652 | 8167 | 1045 | 217 | 2026-03-09 22:58:15 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 979 | 1119 | 1419 | 162 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8946 | 563 | 1021 | 493 | 219 | 2026-03-13 12:05:27 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7203 | 391 | 880 | 2512 | 318 | 2026-03-11 03:55:14 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5607 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5516 | 466 | 1240 | 799 | 495 | 2026-03-13 21:16:34 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5205 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 894 | 1064 | 2732 | 82 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4018 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4008 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3606 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2734 | 312 | 661 | 1293 | 308 | 2026-03-13 20:48:11 |
| [anyio](https://github.com/agronholm/anyio) | 2407 | 187 | 429 | 584 | 83 | 2026-03-09 18:22:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1080 | 1464 | 368 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-09 18:00:27 |
| [pypy](https://github.com/pypy/pypy) | 1681 | 103 | 5178 | 184 | 757 | 2026-03-13 10:47:43 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-09 17:14:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-14T02:44:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
