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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200487 | 77658 | 41811 | 82728 | 3357 | 2026-09-27 05:03:48 |
| [transformers](https://github.com/huggingface/transformers) | 166704 | 34690 | 19522 | 28816 | 2385 | 2026-09-27 02:09:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 103382 | 30649 | 61269 | 136801 | 17574 | 2026-09-27 04:38:49 |
| [fastapi](https://github.com/fastapi/fastapi) | 102646 | 9954 | 3553 | 6360 | 82 | 2026-09-26 13:35:50 |
| [django](https://github.com/django/django) | 91202 | 35624 | 0 | 21958 | 525 | 2026-09-26 05:15:52 |
| [cpython](https://github.com/python/cpython) | 77293 | 36686 | 78303 | 77606 | 9758 | 2026-09-27 04:03:51 |
| [flask](https://github.com/pallets/flask) | 74788 | 17006 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67389 | 27451 | 12298 | 21539 | 2154 | 2026-09-24 17:11:32 |
| [keras](https://github.com/keras-team/keras) | 64345 | 19805 | 12958 | 9943 | 265 | 2026-09-26 21:33:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 49835 | 20430 | 28566 | 38941 | 2564 | 2026-09-27 04:27:28 |
| [ray](https://github.com/ray-project/ray) | 43934 | 8090 | 23106 | 42988 | 3567 | 2026-09-26 17:29:28 |
| [gym](https://github.com/openai/gym) | 37237 | 8671 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33924 | 4727 | 5773 | 4125 | 246 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32854 | 12849 | 14112 | 18587 | 2264 | 2026-09-25 20:48:46 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30193 | 7084 | 3966 | 5072 | 48 | 2026-09-24 10:51:51 |
| [celery](https://github.com/celery/celery) | 28918 | 5186 | 5308 | 4440 | 730 | 2026-09-26 17:18:40 |
| [dash](https://github.com/plotly/dash) | 24430 | 2321 | 2158 | 1726 | 425 | 2026-09-24 19:27:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23282 | 8493 | 11429 | 20907 | 1490 | 2026-09-26 03:37:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22369 | 1489 | 1431 | 7342 | 404 | 2026-09-27 04:40:51 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5560 | 1883 | 1838 | 246 | 2026-09-25 19:17:31 |
| [micropython](https://github.com/micropython/micropython) | 22095 | 8978 | 6132 | 8109 | 1532 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18808 | 2852 | 3387 | 2196 | 716 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1603 | 1468 | 1678 | 150 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16563 | 2433 | 3256 | 10208 | 232 | 2026-09-26 23:42:53 |
| [httpx](https://github.com/encode/httpx) | 15513 | 2331 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15046 | 5970 | 11664 | 14586 | 1842 | 2026-09-26 21:51:02 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14043 | 2141 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13928 | 1967 | 5560 | 6734 | 1343 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12639 | 1335 | 784 | 2148 | 63 | 2026-09-26 10:06:52 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12186 | 1794 | 8307 | 1213 | 210 | 2026-09-25 17:35:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11907 | 617 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1037 | 1145 | 1529 | 158 | 2026-09-25 08:40:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9198 | 613 | 1047 | 553 | 221 | 2026-09-26 14:05:20 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1513 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7339 | 436 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 519 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5410 | 1042 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4414 | 379 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 207 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1339 | 312 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2549 | 280 | 480 | 794 | 120 | 2026-09-26 12:50:08 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 275 | 272 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1801 | 126 | 5265 | 310 | 720 | 2026-09-27 00:19:08 |
| [jython](https://github.com/jython/jython) | 1542 | 231 | 302 | 152 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-27T05:04:15*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
