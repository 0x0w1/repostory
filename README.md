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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200219 | 77033 | 41785 | 82351 | 3225 | 2026-09-21 04:26:27 |
| [transformers](https://github.com/huggingface/transformers) | 166455 | 34648 | 19499 | 28698 | 2429 | 2026-09-21 04:07:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 103136 | 29999 | 61080 | 136087 | 17566 | 2026-09-21 04:36:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 102493 | 9916 | 3552 | 6343 | 83 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91146 | 34985 | 0 | 21878 | 503 | 2026-09-20 17:42:44 |
| [cpython](https://github.com/python/cpython) | 77235 | 36060 | 78208 | 77313 | 9708 | 2026-09-21 04:36:34 |
| [flask](https://github.com/pallets/flask) | 74758 | 16989 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67330 | 27428 | 12289 | 21515 | 2163 | 2026-09-19 19:07:47 |
| [keras](https://github.com/keras-team/keras) | 64324 | 19802 | 12920 | 9904 | 216 | 2026-09-19 20:46:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 49766 | 20408 | 28553 | 38856 | 2682 | 2026-09-21 00:45:48 |
| [ray](https://github.com/ray-project/ray) | 43881 | 8066 | 23089 | 42828 | 3612 | 2026-09-21 00:34:31 |
| [gym](https://github.com/openai/gym) | 37236 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33910 | 4723 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32794 | 12826 | 14105 | 18524 | 2291 | 2026-09-21 01:52:05 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7083 | 3966 | 5069 | 52 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28903 | 5171 | 5301 | 4404 | 723 | 2026-09-21 03:10:19 |
| [dash](https://github.com/plotly/dash) | 24419 | 2317 | 2152 | 1706 | 472 | 2026-09-18 20:02:03 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23241 | 8491 | 11425 | 20887 | 1490 | 2026-09-19 17:39:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 22354 | 1486 | 1425 | 7258 | 395 | 2026-09-21 03:19:14 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5557 | 1883 | 1833 | 259 | 2026-09-21 03:16:00 |
| [micropython](https://github.com/micropython/micropython) | 22075 | 8974 | 6131 | 8099 | 1533 | 2026-09-19 06:11:45 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18794 | 2849 | 3385 | 2190 | 714 | 2026-09-18 22:49:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1599 | 1468 | 1678 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16554 | 2419 | 3256 | 10146 | 227 | 2026-09-19 01:38:41 |
| [httpx](https://github.com/encode/httpx) | 15501 | 1763 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15032 | 5956 | 11650 | 14541 | 1839 | 2026-09-21 01:31:38 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14030 | 2135 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13921 | 1959 | 5559 | 6728 | 1337 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12623 | 1317 | 782 | 2132 | 55 | 2026-09-20 10:07:50 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12170 | 1791 | 8300 | 1211 | 209 | 2026-09-19 20:04:17 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11896 | 615 | 421 | 331 | 162 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1036 | 1144 | 1525 | 161 | 2026-09-20 05:52:31 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9193 | 612 | 1046 | 550 | 222 | 2026-09-19 05:35:44 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7333 | 432 | 901 | 2612 | 330 | 2026-09-17 02:12:00 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 517 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5400 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4405 | 375 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2546 | 270 | 477 | 777 | 109 | 2026-09-20 19:04:16 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1794 | 125 | 5260 | 303 | 714 | 2026-09-20 14:05:43 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-21T04:38:41*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
