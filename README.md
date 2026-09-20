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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200199 | 76951 | 41785 | 82322 | 3202 | 2026-09-20 04:18:35 |
| [transformers](https://github.com/huggingface/transformers) | 166414 | 34636 | 19493 | 28690 | 2422 | 2026-09-19 23:27:24 |
| [pytorch](https://github.com/pytorch/pytorch) | 103112 | 29900 | 61065 | 136037 | 17579 | 2026-09-20 04:38:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 102470 | 9913 | 3552 | 6342 | 82 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91142 | 34911 | 0 | 21872 | 502 | 2026-09-19 22:39:58 |
| [cpython](https://github.com/python/cpython) | 77228 | 35977 | 78196 | 77277 | 9688 | 2026-09-20 03:32:24 |
| [flask](https://github.com/pallets/flask) | 74755 | 16988 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67318 | 27423 | 12288 | 21512 | 2163 | 2026-09-19 19:07:47 |
| [keras](https://github.com/keras-team/keras) | 64321 | 19802 | 12919 | 9903 | 214 | 2026-09-19 20:46:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 49759 | 20403 | 28551 | 38831 | 2685 | 2026-09-20 04:26:05 |
| [ray](https://github.com/ray-project/ray) | 43873 | 8064 | 23084 | 42817 | 3597 | 2026-09-20 03:58:15 |
| [gym](https://github.com/openai/gym) | 37237 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33911 | 4723 | 5773 | 4124 | 245 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32785 | 12818 | 14103 | 18505 | 2285 | 2026-09-19 17:26:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7082 | 3966 | 5068 | 51 | 2026-09-15 18:18:15 |
| [celery](https://github.com/celery/celery) | 28902 | 5168 | 5301 | 4402 | 727 | 2026-09-19 17:19:41 |
| [dash](https://github.com/plotly/dash) | 24418 | 2317 | 2152 | 1706 | 472 | 2026-09-18 20:02:03 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23237 | 8489 | 11425 | 20885 | 1490 | 2026-09-19 17:39:11 |
| [RustPython](https://github.com/RustPython/RustPython) | 22355 | 1486 | 1425 | 7246 | 396 | 2026-09-20 01:34:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5557 | 1883 | 1828 | 259 | 2026-09-19 20:47:10 |
| [micropython](https://github.com/micropython/micropython) | 22074 | 8974 | 6130 | 8099 | 1532 | 2026-09-19 06:11:45 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18793 | 2848 | 3385 | 2190 | 714 | 2026-09-18 22:49:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1598 | 1468 | 1677 | 150 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16553 | 2415 | 3254 | 10143 | 222 | 2026-09-19 01:38:41 |
| [httpx](https://github.com/encode/httpx) | 15502 | 1684 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15027 | 5952 | 11650 | 14538 | 1841 | 2026-09-19 16:41:44 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14026 | 2134 | 2663 | 1223 | 235 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13921 | 1957 | 5559 | 6728 | 1337 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12622 | 1315 | 782 | 2130 | 54 | 2026-09-19 20:08:07 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12168 | 1789 | 8300 | 1211 | 209 | 2026-09-19 20:04:17 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11896 | 615 | 421 | 331 | 162 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 1036 | 1143 | 1523 | 159 | 2026-09-18 17:07:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9194 | 612 | 1046 | 550 | 222 | 2026-09-19 05:35:44 |
| [bottle](https://github.com/bottlepy/bottle) | 8789 | 1509 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7332 | 432 | 901 | 2611 | 330 | 2026-09-17 02:12:00 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 517 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5399 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4403 | 375 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3991 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2546 | 269 | 477 | 776 | 111 | 2026-09-19 15:40:31 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 403 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1786 | 274 | 271 | 2026-09-14 18:01:11 |
| [pypy](https://github.com/pypy/pypy) | 1795 | 125 | 5257 | 303 | 711 | 2026-09-19 19:48:09 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 302 | 151 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-20T04:40:17*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
