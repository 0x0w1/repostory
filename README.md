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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195605 | 75182 | 41541 | 75914 | 3461 | 2026-06-12 04:48:03 |
| [transformers](https://github.com/huggingface/transformers) | 161515 | 33483 | 19057 | 26807 | 2417 | 2026-06-12 04:35:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 100663 | 27983 | 59204 | 127331 | 18410 | 2026-06-12 04:51:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 99122 | 9424 | 3533 | 5890 | 94 | 2026-06-10 23:14:27 |
| [django](https://github.com/django/django) | 87819 | 33859 | 0 | 21391 | 446 | 2026-06-11 20:27:10 |
| [cpython](https://github.com/python/cpython) | 73176 | 34725 | 76697 | 72359 | 9265 | 2026-06-12 01:47:01 |
| [flask](https://github.com/pallets/flask) | 71641 | 16873 | 2747 | 2836 | 4 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66296 | 27059 | 12131 | 20947 | 2052 | 2026-06-11 18:24:05 |
| [keras](https://github.com/keras-team/keras) | 64080 | 19733 | 12784 | 9438 | 174 | 2026-06-11 02:00:18 |
| [pandas](https://github.com/pandas-dev/pandas) | 48960 | 20007 | 28310 | 37458 | 3219 | 2026-06-11 22:16:14 |
| [ray](https://github.com/ray-project/ray) | 42846 | 7673 | 22737 | 40922 | 3454 | 2026-06-12 04:38:32 |
| [gym](https://github.com/openai/gym) | 37223 | 8705 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33652 | 4687 | 5758 | 4096 | 211 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32173 | 12439 | 13938 | 17589 | 2380 | 2026-06-11 19:57:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30065 | 7069 | 3967 | 5013 | 78 | 2026-06-10 05:40:50 |
| [celery](https://github.com/celery/celery) | 28576 | 5072 | 5280 | 4142 | 779 | 2026-06-11 14:47:38 |
| [dash](https://github.com/plotly/dash) | 24253 | 2297 | 2105 | 1583 | 541 | 2026-06-11 16:47:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22879 | 8350 | 11304 | 20511 | 1445 | 2026-06-11 23:22:12 |
| [tornado](https://github.com/tornadoweb/tornado) | 22183 | 5533 | 1872 | 1744 | 217 | 2026-06-08 18:22:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22115 | 1442 | 1355 | 6654 | 376 | 2026-06-12 02:10:50 |
| [micropython](https://github.com/micropython/micropython) | 21800 | 8859 | 6067 | 7868 | 1649 | 2026-06-11 13:43:24 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1591 | 1467 | 1689 | 132 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18597 | 2808 | 3360 | 2094 | 766 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16445 | 2325 | 3211 | 9355 | 223 | 2026-06-11 23:44:36 |
| [httpx](https://github.com/encode/httpx) | 15292 | 1169 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14747 | 5760 | 11474 | 13866 | 1807 | 2026-06-12 03:28:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13909 | 2117 | 2653 | 1183 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13848 | 1885 | 5538 | 6610 | 1242 | 2026-06-11 17:31:35 |
| [starlette](https://github.com/Kludex/starlette) | 12389 | 1196 | 770 | 1941 | 43 | 2026-06-11 15:32:10 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11905 | 1697 | 8227 | 1113 | 211 | 2026-06-11 21:21:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11817 | 609 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 1000 | 1128 | 1459 | 160 | 2026-06-11 21:05:18 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9090 | 598 | 1039 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8769 | 1501 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7281 | 399 | 892 | 2552 | 320 | 2026-06-09 06:57:17 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6739 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5593 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5577 | 486 | 1257 | 849 | 514 | 2026-06-10 08:36:34 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5291 | 1022 | 914 | 303 | 212 | 2026-06-09 07:01:02 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4190 | 339 | 1184 | 224 | 115 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4085 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4002 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3641 | 201 | 283 | 129 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2753 | 311 | 666 | 1320 | 306 | 2026-06-11 12:40:47 |
| [anyio](https://github.com/agronholm/anyio) | 2479 | 207 | 443 | 649 | 85 | 2026-06-11 22:12:33 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 912 | 1084 | 1544 | 367 | 2026-06-06 20:15:33 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 364 | 1785 | 268 | 266 | 2026-06-08 17:45:57 |
| [pypy](https://github.com/pypy/pypy) | 1748 | 115 | 5219 | 261 | 734 | 2026-06-11 07:52:24 |
| [jython](https://github.com/jython/jython) | 1515 | 230 | 297 | 135 | 109 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 113 | 78 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-12T04:51:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
