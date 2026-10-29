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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201289 | 78732 | 41924 | 84132 | 3423 | 2026-10-29 05:18:57 |
| [transformers](https://github.com/huggingface/transformers) | 168318 | 35021 | 19714 | 29577 | 1024 | 2026-10-29 05:24:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 105161 | 31849 | 62072 | 139728 | 17780 | 2026-10-29 05:29:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 104268 | 10144 | 3556 | 6531 | 56 | 2026-10-27 04:56:28 |
| [django](https://github.com/django/django) | 91537 | 36540 | 0 | 22129 | 534 | 2026-10-28 12:53:14 |
| [cpython](https://github.com/python/cpython) | 77753 | 37685 | 78940 | 79388 | 9250 | 2026-10-29 04:08:22 |
| [flask](https://github.com/pallets/flask) | 74936 | 17192 | 2770 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67984 | 27597 | 12352 | 21705 | 2156 | 2026-10-28 13:07:43 |
| [keras](https://github.com/keras-team/keras) | 64395 | 19803 | 13047 | 10168 | 273 | 2026-10-27 23:29:20 |
| [pandas](https://github.com/pandas-dev/pandas) | 50338 | 20654 | 28656 | 39733 | 2091 | 2026-10-29 01:11:55 |
| [ray](https://github.com/ray-project/ray) | 44149 | 8217 | 23262 | 43817 | 3651 | 2026-10-29 04:40:27 |
| [gym](https://github.com/openai/gym) | 37233 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34003 | 4737 | 5781 | 4138 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33206 | 13027 | 14156 | 18915 | 2236 | 2026-10-28 22:04:40 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30218 | 7096 | 3966 | 5101 | 65 | 2026-10-28 07:03:26 |
| [celery](https://github.com/celery/celery) | 29096 | 5251 | 5355 | 4660 | 738 | 2026-10-28 22:12:57 |
| [dash](https://github.com/plotly/dash) | 24473 | 2331 | 2170 | 1799 | 433 | 2026-10-29 01:59:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23399 | 8532 | 11454 | 21033 | 1480 | 2026-10-29 04:35:35 |
| [RustPython](https://github.com/RustPython/RustPython) | 22431 | 1506 | 1446 | 7901 | 292 | 2026-10-29 05:26:04 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5592 | 1888 | 1903 | 234 | 2026-10-26 21:18:33 |
| [micropython](https://github.com/micropython/micropython) | 22164 | 9025 | 6151 | 8166 | 1555 | 2026-10-29 04:53:12 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18859 | 2882 | 3399 | 2257 | 745 | 2026-10-28 16:35:18 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16596 | 2493 | 3269 | 10558 | 264 | 2026-10-28 19:23:23 |
| [httpx](https://github.com/encode/httpx) | 15712 | 3252 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15165 | 6038 | 11729 | 14791 | 1884 | 2026-10-29 00:20:39 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14090 | 2151 | 2667 | 1247 | 257 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13937 | 2007 | 5580 | 6793 | 1410 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12690 | 1419 | 795 | 2282 | 53 | 2026-10-29 04:39:11 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12270 | 1834 | 8366 | 1250 | 218 | 2026-10-28 15:12:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11921 | 621 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9811 | 1050 | 1148 | 1559 | 160 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9224 | 621 | 1054 | 579 | 238 | 2026-10-28 17:08:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1516 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7357 | 464 | 906 | 2653 | 344 | 2026-10-24 14:32:28 |
| [hug](https://github.com/hugapi/hug) | 6873 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 537 | 1300 | 971 | 556 | 2026-10-25 16:05:18 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5437 | 1052 | 938 | 328 | 207 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4458 | 390 | 1210 | 259 | 118 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 677 | 1383 | 263 | 2026-10-29 00:07:04 |
| [anyio](https://github.com/agronholm/anyio) | 2562 | 338 | 493 | 874 | 143 | 2026-10-26 22:05:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1606 | 355 | 2026-10-26 14:24:50 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1791 | 277 | 278 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1821 | 130 | 5289 | 384 | 718 | 2026-10-28 22:01:49 |
| [jython](https://github.com/jython/jython) | 1551 | 232 | 305 | 155 | 101 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-29T05:30:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
