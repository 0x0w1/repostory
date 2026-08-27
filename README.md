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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197716 | 76153 | 41724 | 80930 | 2943 | 2026-08-27 08:49:24 |
| [transformers](https://github.com/huggingface/transformers) | 164489 | 34383 | 19381 | 28227 | 2405 | 2026-08-27 08:36:34 |
| [pytorch](https://github.com/pytorch/pytorch) | 102611 | 29003 | 60571 | 133769 | 17372 | 2026-08-27 08:54:31 |
| [fastapi](https://github.com/fastapi/fastapi) | 101871 | 9818 | 3548 | 6270 | 79 | 2026-08-26 17:54:56 |
| [django](https://github.com/django/django) | 89025 | 34186 | 0 | 21712 | 474 | 2026-08-23 19:39:31 |
| [cpython](https://github.com/python/cpython) | 75007 | 35282 | 77840 | 76248 | 9614 | 2026-08-27 02:17:13 |
| [flask](https://github.com/pallets/flask) | 72139 | 16949 | 2763 | 2895 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67068 | 27319 | 12252 | 21378 | 2126 | 2026-08-26 13:46:35 |
| [keras](https://github.com/keras-team/keras) | 64254 | 19764 | 12886 | 9761 | 247 | 2026-08-26 22:12:59 |
| [pandas](https://github.com/pandas-dev/pandas) | 49565 | 20291 | 28490 | 38326 | 2776 | 2026-08-26 22:27:09 |
| [ray](https://github.com/ray-project/ray) | 43618 | 7968 | 22989 | 42347 | 3536 | 2026-08-27 03:55:07 |
| [gym](https://github.com/openai/gym) | 37248 | 8682 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33853 | 4718 | 5770 | 4117 | 237 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32607 | 12680 | 14066 | 18285 | 2340 | 2026-08-27 01:32:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30146 | 7077 | 3966 | 5047 | 57 | 2026-08-25 19:14:08 |
| [celery](https://github.com/celery/celery) | 28825 | 5142 | 5295 | 4262 | 776 | 2026-08-26 22:12:46 |
| [dash](https://github.com/plotly/dash) | 24388 | 2319 | 2144 | 1688 | 535 | 2026-08-25 23:31:08 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23110 | 8453 | 11403 | 20774 | 1471 | 2026-08-27 05:41:34 |
| [RustPython](https://github.com/RustPython/RustPython) | 22306 | 1476 | 1422 | 7101 | 394 | 2026-08-26 14:38:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5551 | 1878 | 1806 | 252 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22012 | 8945 | 6117 | 8068 | 1536 | 2026-08-27 05:42:12 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18755 | 2837 | 3378 | 2145 | 771 | 2026-08-26 18:54:07 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1598 | 1471 | 1703 | 145 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16526 | 2383 | 3241 | 9953 | 222 | 2026-08-26 14:47:04 |
| [httpx](https://github.com/encode/httpx) | 15444 | 1261 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14955 | 5881 | 11613 | 14392 | 1846 | 2026-08-26 13:16:45 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14005 | 2126 | 2659 | 1214 | 229 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13897 | 1937 | 5551 | 6706 | 1313 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12572 | 1275 | 779 | 2056 | 61 | 2026-08-26 10:51:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12111 | 1756 | 8278 | 1191 | 209 | 2026-08-26 16:47:23 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11887 | 612 | 417 | 328 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1030 | 1139 | 1505 | 162 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9176 | 610 | 1042 | 540 | 220 | 2026-08-24 14:12:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1500 | 865 | 644 | 288 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7307 | 416 | 899 | 2592 | 322 | 2026-08-27 03:44:56 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5614 | 498 | 1266 | 888 | 541 | 2026-08-24 16:57:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5366 | 1035 | 930 | 320 | 197 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4343 | 365 | 1199 | 245 | 129 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4095 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3994 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 205 | 284 | 135 | 27 | 2026-08-25 19:06:37 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2537 | 247 | 471 | 745 | 105 | 2026-08-25 16:28:26 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1085 | 1595 | 356 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 368 | 1786 | 272 | 270 | 2026-08-24 17:57:48 |
| [pypy](https://github.com/pypy/pypy) | 1783 | 125 | 5254 | 297 | 726 | 2026-08-27 08:09:13 |
| [jython](https://github.com/jython/jython) | 1535 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-27T08:55:55*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
