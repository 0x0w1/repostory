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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195608 | 75319 | 41516 | 75532 | 3233 | 2026-06-08 04:50:24 |
| [transformers](https://github.com/huggingface/transformers) | 161404 | 33441 | 19040 | 26736 | 2428 | 2026-06-07 19:56:34 |
| [pytorch](https://github.com/pytorch/pytorch) | 100590 | 27963 | 59090 | 126874 | 18329 | 2026-06-08 04:38:50 |
| [fastapi](https://github.com/fastapi/fastapi) | 99019 | 9408 | 3528 | 5871 | 94 | 2026-06-05 19:20:50 |
| [django](https://github.com/django/django) | 87803 | 33967 | 0 | 21361 | 450 | 2026-06-05 21:11:32 |
| [cpython](https://github.com/python/cpython) | 73142 | 34704 | 76642 | 72091 | 9310 | 2026-06-07 18:37:10 |
| [flask](https://github.com/pallets/flask) | 71638 | 16853 | 2741 | 2835 | 4 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66281 | 27054 | 12125 | 20902 | 2042 | 2026-06-05 07:30:53 |
| [keras](https://github.com/keras-team/keras) | 64090 | 19744 | 12776 | 9420 | 179 | 2026-06-05 21:31:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 48923 | 19999 | 28303 | 37431 | 3227 | 2026-06-07 18:30:10 |
| [ray](https://github.com/ray-project/ray) | 42805 | 7661 | 22725 | 40803 | 3445 | 2026-06-08 03:10:06 |
| [gym](https://github.com/openai/gym) | 37213 | 8703 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33638 | 4686 | 5757 | 4095 | 209 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32162 | 12433 | 13932 | 17568 | 2374 | 2026-06-06 21:00:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30055 | 7068 | 3967 | 5009 | 77 | 2026-06-06 13:20:03 |
| [celery](https://github.com/celery/celery) | 28564 | 5070 | 5280 | 4132 | 785 | 2026-06-03 07:47:09 |
| [dash](https://github.com/plotly/dash) | 24240 | 2290 | 2103 | 1580 | 538 | 2026-06-06 11:56:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22873 | 8350 | 11301 | 20494 | 1460 | 2026-06-06 02:08:49 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5538 | 1872 | 1741 | 217 | 2026-06-05 15:54:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 22101 | 1440 | 1354 | 6630 | 390 | 2026-06-04 20:20:35 |
| [micropython](https://github.com/micropython/micropython) | 21789 | 8860 | 6067 | 7858 | 1684 | 2026-06-04 13:18:58 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1592 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18589 | 2806 | 3354 | 2094 | 761 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16441 | 2296 | 3211 | 9320 | 229 | 2026-06-08 01:53:30 |
| [httpx](https://github.com/encode/httpx) | 15282 | 1162 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14739 | 5753 | 11463 | 13843 | 1801 | 2026-06-07 19:26:29 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13902 | 2115 | 2653 | 1182 | 221 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13849 | 1880 | 5536 | 6602 | 1240 | 2026-06-06 20:15:44 |
| [starlette](https://github.com/Kludex/starlette) | 12369 | 1194 | 770 | 1937 | 59 | 2026-06-05 08:52:03 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11895 | 1695 | 8225 | 1106 | 212 | 2026-06-05 14:25:43 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11811 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 999 | 1127 | 1453 | 159 | 2026-06-01 11:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9082 | 597 | 1037 | 517 | 214 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7276 | 398 | 892 | 2550 | 320 | 2026-06-01 23:07:35 |
| [hug](https://github.com/hugapi/hug) | 6886 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5596 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5575 | 486 | 1257 | 849 | 517 | 2026-06-07 04:29:18 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5281 | 1018 | 914 | 300 | 212 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4179 | 337 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4003 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3639 | 200 | 283 | 128 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2748 | 311 | 666 | 1320 | 307 | 2026-06-06 13:02:09 |
| [anyio](https://github.com/agronholm/anyio) | 2478 | 207 | 441 | 647 | 83 | 2026-06-07 13:05:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 910 | 1084 | 1537 | 361 | 2026-06-06 20:15:33 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-01 17:59:42 |
| [pypy](https://github.com/pypy/pypy) | 1748 | 113 | 5215 | 258 | 735 | 2026-06-08 04:34:56 |
| [jython](https://github.com/jython/jython) | 1515 | 230 | 297 | 135 | 110 | 2026-06-03 08:15:01 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 113 | 78 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-08T04:52:52*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
