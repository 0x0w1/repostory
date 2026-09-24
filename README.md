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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200268 | 77110 | 41804 | 82567 | 3394 | 2026-09-24 04:21:42 |
| [transformers](https://github.com/huggingface/transformers) | 166576 | 34661 | 19509 | 28773 | 2390 | 2026-09-24 04:13:12 |
| [pytorch](https://github.com/pytorch/pytorch) | 103224 | 30100 | 61201 | 136567 | 17561 | 2026-09-24 04:26:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 102562 | 9940 | 3553 | 6356 | 82 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91168 | 35088 | 0 | 21892 | 511 | 2026-09-23 11:46:48 |
| [cpython](https://github.com/python/cpython) | 77242 | 36151 | 78242 | 77450 | 9704 | 2026-09-24 04:17:38 |
| [flask](https://github.com/pallets/flask) | 74766 | 17003 | 2767 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67354 | 27443 | 12293 | 21534 | 2153 | 2026-09-23 17:44:25 |
| [keras](https://github.com/keras-team/keras) | 64334 | 19807 | 12943 | 9929 | 251 | 2026-09-24 03:55:48 |
| [pandas](https://github.com/pandas-dev/pandas) | 49788 | 20423 | 28556 | 38886 | 2605 | 2026-09-24 01:35:00 |
| [ray](https://github.com/ray-project/ray) | 43913 | 8075 | 23097 | 42927 | 3617 | 2026-09-24 04:22:28 |
| [gym](https://github.com/openai/gym) | 37236 | 8674 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33918 | 4724 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32809 | 12840 | 14109 | 18566 | 2271 | 2026-09-24 02:23:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7084 | 3966 | 5071 | 48 | 2026-09-23 22:25:53 |
| [celery](https://github.com/celery/celery) | 28912 | 5178 | 5305 | 4422 | 724 | 2026-09-23 03:18:40 |
| [dash](https://github.com/plotly/dash) | 24426 | 2322 | 2154 | 1724 | 422 | 2026-09-23 16:56:59 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23254 | 8494 | 11426 | 20895 | 1488 | 2026-09-24 03:30:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22359 | 1486 | 1430 | 7297 | 400 | 2026-09-24 03:21:27 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5558 | 1883 | 1835 | 259 | 2026-09-22 14:09:48 |
| [micropython](https://github.com/micropython/micropython) | 22091 | 8979 | 6132 | 8102 | 1525 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18800 | 2851 | 3386 | 2194 | 715 | 2026-09-22 21:25:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1602 | 1468 | 1678 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16558 | 2429 | 3256 | 10180 | 233 | 2026-09-23 16:37:59 |
| [httpx](https://github.com/encode/httpx) | 15504 | 1845 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15037 | 5965 | 11655 | 14560 | 1844 | 2026-09-23 20:00:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14039 | 2140 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13924 | 1965 | 5560 | 6731 | 1341 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12627 | 1326 | 783 | 2138 | 56 | 2026-09-23 09:28:33 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12176 | 1794 | 8303 | 1213 | 212 | 2026-09-21 17:07:32 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11903 | 616 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9803 | 1036 | 1144 | 1527 | 158 | 2026-09-22 20:20:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9196 | 612 | 1046 | 552 | 223 | 2026-09-23 14:23:20 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7336 | 434 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 516 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5407 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4412 | 376 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4101 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 269 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1339 | 312 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2547 | 274 | 479 | 786 | 119 | 2026-09-21 18:00:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1798 | 126 | 5263 | 307 | 715 | 2026-09-23 17:35:33 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-24T04:28:32*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
