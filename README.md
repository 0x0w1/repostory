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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200572 | 77790 | 41814 | 82756 | 3386 | 2026-09-28 03:48:56 |
| [transformers](https://github.com/huggingface/transformers) | 166737 | 34697 | 19527 | 28831 | 2402 | 2026-09-28 00:24:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 103430 | 30792 | 61273 | 136874 | 17604 | 2026-09-28 05:01:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 102682 | 9963 | 3553 | 6360 | 82 | 2026-09-26 13:35:50 |
| [django](https://github.com/django/django) | 91220 | 35726 | 0 | 21962 | 525 | 2026-09-27 14:39:15 |
| [cpython](https://github.com/python/cpython) | 77318 | 36803 | 78314 | 77634 | 9762 | 2026-09-28 00:52:59 |
| [flask](https://github.com/pallets/flask) | 74803 | 17007 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67404 | 27449 | 12298 | 21540 | 2154 | 2026-09-24 17:11:32 |
| [keras](https://github.com/keras-team/keras) | 64346 | 19804 | 12958 | 9943 | 265 | 2026-09-26 21:33:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 49854 | 20438 | 28568 | 38980 | 2501 | 2026-09-28 00:06:50 |
| [ray](https://github.com/ray-project/ray) | 43938 | 8092 | 23106 | 42994 | 3569 | 2026-09-27 19:57:30 |
| [gym](https://github.com/openai/gym) | 37239 | 8671 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33925 | 4727 | 5773 | 4125 | 246 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32866 | 12850 | 14112 | 18591 | 2268 | 2026-09-25 20:48:46 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7083 | 3966 | 5073 | 49 | 2026-09-24 10:51:51 |
| [celery](https://github.com/celery/celery) | 28919 | 5185 | 5309 | 4447 | 723 | 2026-09-27 15:29:28 |
| [dash](https://github.com/plotly/dash) | 24438 | 2324 | 2158 | 1727 | 426 | 2026-09-24 19:27:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23297 | 8495 | 11429 | 20909 | 1491 | 2026-09-26 03:37:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22369 | 1488 | 1431 | 7369 | 407 | 2026-09-27 22:05:41 |
| [tornado](https://github.com/tornadoweb/tornado) | 22179 | 5561 | 1884 | 1839 | 248 | 2026-09-25 19:17:31 |
| [micropython](https://github.com/micropython/micropython) | 22097 | 8979 | 6132 | 8110 | 1533 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18810 | 2855 | 3387 | 2199 | 719 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18634 | 1603 | 1468 | 1678 | 150 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16565 | 2435 | 3257 | 10224 | 235 | 2026-09-28 03:48:56 |
| [httpx](https://github.com/encode/httpx) | 15517 | 2460 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15047 | 5973 | 11667 | 14593 | 1844 | 2026-09-27 18:15:14 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14046 | 2142 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13927 | 1967 | 5561 | 6734 | 1344 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12639 | 1338 | 784 | 2152 | 61 | 2026-09-27 10:57:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12189 | 1795 | 8307 | 1214 | 210 | 2026-09-25 17:35:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11907 | 617 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1037 | 1145 | 1530 | 159 | 2026-09-25 08:40:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9198 | 613 | 1047 | 554 | 222 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1512 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7340 | 436 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 519 | 1271 | 906 | 521 | 2026-09-27 09:32:15 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5412 | 1042 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4417 | 379 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3674 | 208 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1340 | 313 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2550 | 282 | 481 | 795 | 120 | 2026-09-27 20:47:08 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 275 | 272 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1803 | 127 | 5266 | 313 | 721 | 2026-09-28 04:48:25 |
| [jython](https://github.com/jython/jython) | 1543 | 231 | 303 | 152 | 100 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-28T05:06:11*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
