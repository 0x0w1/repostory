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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200298 | 77291 | 41806 | 82629 | 3320 | 2026-09-25 04:24:09 |
| [transformers](https://github.com/huggingface/transformers) | 166622 | 34669 | 19515 | 28796 | 2392 | 2026-09-25 00:53:11 |
| [pytorch](https://github.com/pytorch/pytorch) | 103274 | 30308 | 61239 | 136661 | 17585 | 2026-09-25 04:39:02 |
| [fastapi](https://github.com/fastapi/fastapi) | 102591 | 9943 | 3553 | 6356 | 82 | 2026-09-18 21:24:37 |
| [django](https://github.com/django/django) | 91172 | 35286 | 0 | 21946 | 520 | 2026-09-24 08:59:37 |
| [cpython](https://github.com/python/cpython) | 77255 | 36332 | 78265 | 77522 | 9720 | 2026-09-25 04:10:30 |
| [flask](https://github.com/pallets/flask) | 74774 | 17005 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67358 | 27444 | 12294 | 21535 | 2147 | 2026-09-24 17:11:32 |
| [keras](https://github.com/keras-team/keras) | 64339 | 19806 | 12952 | 9935 | 262 | 2026-09-25 00:27:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 49798 | 20424 | 28561 | 38899 | 2602 | 2026-09-24 22:25:16 |
| [ray](https://github.com/ray-project/ray) | 43919 | 8084 | 23100 | 42964 | 3619 | 2026-09-25 02:38:56 |
| [gym](https://github.com/openai/gym) | 37236 | 8673 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33919 | 4725 | 5773 | 4125 | 246 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32824 | 12843 | 14110 | 18579 | 2265 | 2026-09-24 22:48:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30189 | 7086 | 3966 | 5072 | 48 | 2026-09-24 10:51:51 |
| [celery](https://github.com/celery/celery) | 28913 | 5184 | 5307 | 4435 | 733 | 2026-09-24 14:07:53 |
| [dash](https://github.com/plotly/dash) | 24429 | 2322 | 2157 | 1725 | 423 | 2026-09-24 19:27:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23263 | 8494 | 11427 | 20898 | 1486 | 2026-09-25 01:42:19 |
| [RustPython](https://github.com/RustPython/RustPython) | 22364 | 1486 | 1430 | 7309 | 397 | 2026-09-25 00:45:19 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5558 | 1883 | 1836 | 259 | 2026-09-22 14:09:48 |
| [micropython](https://github.com/micropython/micropython) | 22091 | 8977 | 6132 | 8105 | 1528 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18804 | 2852 | 3387 | 2195 | 715 | 2026-09-24 15:43:59 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1602 | 1468 | 1678 | 151 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16560 | 2429 | 3256 | 10197 | 231 | 2026-09-25 01:37:16 |
| [httpx](https://github.com/encode/httpx) | 15506 | 1995 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15038 | 5970 | 11660 | 14573 | 1846 | 2026-09-25 03:19:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14041 | 2140 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13924 | 1965 | 5560 | 6732 | 1342 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12632 | 1330 | 784 | 2142 | 61 | 2026-09-23 09:28:33 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12181 | 1794 | 8304 | 1213 | 207 | 2026-09-24 21:08:22 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11904 | 616 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1037 | 1145 | 1528 | 159 | 2026-09-22 20:20:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9195 | 613 | 1047 | 553 | 224 | 2026-09-24 17:11:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8790 | 1510 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7337 | 435 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 738 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 517 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5407 | 1041 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4413 | 377 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 269 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 206 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1339 | 312 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2547 | 275 | 479 | 788 | 119 | 2026-09-21 18:00:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 275 | 272 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1799 | 126 | 5263 | 307 | 715 | 2026-09-24 05:31:55 |
| [jython](https://github.com/jython/jython) | 1542 | 232 | 302 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 315 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-25T04:40:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
