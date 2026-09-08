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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 199338 | 76296 | 41750 | 81646 | 3159 | 2026-09-08 04:16:37 |
| [transformers](https://github.com/huggingface/transformers) | 164972 | 34486 | 19423 | 28422 | 2407 | 2026-09-07 23:10:23 |
| [pytorch](https://github.com/pytorch/pytorch) | 102846 | 29156 | 60819 | 134798 | 17592 | 2026-09-08 04:17:19 |
| [fastapi](https://github.com/fastapi/fastapi) | 102183 | 9863 | 3549 | 6318 | 80 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 90393 | 34259 | 0 | 21794 | 488 | 2026-09-07 20:38:44 |
| [cpython](https://github.com/python/cpython) | 76470 | 35361 | 78038 | 76763 | 9639 | 2026-09-08 04:04:21 |
| [flask](https://github.com/pallets/flask) | 73583 | 16979 | 2765 | 2902 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67212 | 27377 | 12269 | 21440 | 2153 | 2026-09-08 01:26:50 |
| [keras](https://github.com/keras-team/keras) | 64321 | 19788 | 12896 | 9816 | 212 | 2026-09-05 05:37:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 49696 | 20353 | 28531 | 38575 | 2733 | 2026-09-08 00:52:55 |
| [ray](https://github.com/ray-project/ray) | 43733 | 8012 | 23022 | 42536 | 3567 | 2026-09-08 01:32:42 |
| [gym](https://github.com/openai/gym) | 37238 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33882 | 4722 | 5771 | 4120 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32702 | 12750 | 14087 | 18357 | 2302 | 2026-09-07 18:41:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30167 | 7082 | 3966 | 5055 | 51 | 2026-09-07 18:03:04 |
| [celery](https://github.com/celery/celery) | 28868 | 5153 | 5299 | 4310 | 731 | 2026-09-07 22:13:08 |
| [dash](https://github.com/plotly/dash) | 24400 | 2316 | 2150 | 1699 | 535 | 2026-09-07 16:46:56 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23202 | 8481 | 11415 | 20831 | 1472 | 2026-09-07 02:18:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 22340 | 1484 | 1423 | 7177 | 398 | 2026-09-07 16:35:58 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5555 | 1879 | 1811 | 254 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22049 | 8966 | 6123 | 8084 | 1525 | 2026-09-08 01:30:40 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18768 | 2838 | 3378 | 2150 | 700 | 2026-09-04 13:59:59 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1599 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16543 | 2397 | 3249 | 10054 | 215 | 2026-09-08 01:37:17 |
| [httpx](https://github.com/encode/httpx) | 15468 | 1282 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14996 | 5915 | 11629 | 14464 | 1840 | 2026-09-07 18:58:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14019 | 2129 | 2662 | 1217 | 234 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13911 | 1944 | 5555 | 6716 | 1327 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12603 | 1294 | 781 | 2099 | 41 | 2026-09-07 17:36:27 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12147 | 1776 | 8289 | 1200 | 202 | 2026-09-07 16:17:41 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11896 | 612 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 1032 | 1140 | 1514 | 155 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9185 | 611 | 1044 | 543 | 223 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8781 | 1506 | 866 | 649 | 290 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7316 | 420 | 900 | 2600 | 326 | 2026-09-07 22:29:47 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5622 | 503 | 1268 | 894 | 546 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5382 | 1038 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4374 | 374 | 1201 | 249 | 127 | 2026-09-04 17:15:17 |
| [pyramid](https://github.com/Pylons/pyramid) | 4098 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3668 | 206 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 316 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 254 | 475 | 760 | 106 | 2026-09-07 19:36:00 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-09-08 02:20:54 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1786 | 274 | 272 | 2026-09-07 18:00:00 |
| [pypy](https://github.com/pypy/pypy) | 1789 | 125 | 5255 | 300 | 721 | 2026-09-07 20:18:03 |
| [jython](https://github.com/jython/jython) | 1540 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-08T04:17:59*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
