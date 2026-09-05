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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198832 | 76245 | 41745 | 81512 | 3119 | 2026-09-05 04:08:48 |
| [transformers](https://github.com/huggingface/transformers) | 164799 | 34448 | 19408 | 28366 | 2385 | 2026-09-05 03:11:14 |
| [pytorch](https://github.com/pytorch/pytorch) | 102761 | 29110 | 60774 | 134661 | 17530 | 2026-09-05 04:07:23 |
| [fastapi](https://github.com/fastapi/fastapi) | 102082 | 9848 | 3549 | 6310 | 83 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 89939 | 34236 | 0 | 21770 | 487 | 2026-09-04 21:24:26 |
| [cpython](https://github.com/python/cpython) | 75981 | 35330 | 77955 | 76656 | 9641 | 2026-09-04 21:08:37 |
| [flask](https://github.com/pallets/flask) | 72167 | 16958 | 2765 | 2899 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67161 | 27359 | 12265 | 21430 | 2146 | 2026-09-04 20:55:21 |
| [keras](https://github.com/keras-team/keras) | 64278 | 19773 | 12895 | 9805 | 212 | 2026-09-04 23:11:23 |
| [pandas](https://github.com/pandas-dev/pandas) | 49636 | 20325 | 28529 | 38523 | 2733 | 2026-09-05 04:01:33 |
| [ray](https://github.com/ray-project/ray) | 43702 | 8001 | 23022 | 42518 | 3564 | 2026-09-05 02:10:59 |
| [gym](https://github.com/openai/gym) | 37242 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33874 | 4723 | 5771 | 4120 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32653 | 12713 | 14082 | 18331 | 2334 | 2026-09-05 02:38:27 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30159 | 7085 | 3966 | 5051 | 58 | 2026-09-03 16:07:55 |
| [celery](https://github.com/celery/celery) | 28860 | 5149 | 5298 | 4298 | 746 | 2026-09-03 22:13:17 |
| [dash](https://github.com/plotly/dash) | 24397 | 2317 | 2150 | 1696 | 532 | 2026-09-04 16:25:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23146 | 8468 | 11411 | 20822 | 1467 | 2026-09-05 02:31:08 |
| [RustPython](https://github.com/RustPython/RustPython) | 22334 | 1482 | 1423 | 7152 | 394 | 2026-09-05 02:43:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22174 | 5553 | 1879 | 1809 | 253 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22043 | 8960 | 6122 | 8081 | 1523 | 2026-09-04 13:17:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18761 | 2837 | 3378 | 2150 | 700 | 2026-09-04 13:59:59 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1599 | 1467 | 1675 | 147 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16531 | 2394 | 3243 | 10037 | 215 | 2026-09-05 03:05:17 |
| [httpx](https://github.com/encode/httpx) | 15459 | 1272 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14987 | 5907 | 11624 | 14444 | 1830 | 2026-09-04 22:13:09 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14010 | 2129 | 2659 | 1216 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13910 | 1941 | 5555 | 6714 | 1325 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12591 | 1293 | 781 | 2080 | 67 | 2026-09-04 06:10:10 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12132 | 1774 | 8287 | 1200 | 203 | 2026-09-04 20:37:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11897 | 613 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 1032 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9180 | 610 | 1044 | 543 | 223 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8778 | 1505 | 865 | 648 | 290 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7315 | 419 | 900 | 2597 | 326 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6881 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5622 | 504 | 1266 | 893 | 543 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5377 | 1037 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4370 | 373 | 1200 | 248 | 126 | 2026-09-04 17:15:17 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3664 | 206 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 315 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 252 | 475 | 757 | 110 | 2026-09-04 23:02:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 274 | 272 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1788 | 125 | 5255 | 299 | 721 | 2026-09-04 20:32:29 |
| [jython](https://github.com/jython/jython) | 1540 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-05T04:10:03*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
