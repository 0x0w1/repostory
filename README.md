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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 199339 | 76280 | 41755 | 81715 | 3125 | 2026-09-09 04:22:41 |
| [transformers](https://github.com/huggingface/transformers) | 165017 | 34483 | 19428 | 28436 | 2398 | 2026-09-09 02:23:40 |
| [pytorch](https://github.com/pytorch/pytorch) | 102867 | 29160 | 60840 | 134893 | 17599 | 2026-09-09 04:17:15 |
| [fastapi](https://github.com/fastapi/fastapi) | 102204 | 9867 | 3549 | 6319 | 80 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 90390 | 34245 | 0 | 21805 | 492 | 2026-09-08 19:01:03 |
| [cpython](https://github.com/python/cpython) | 76455 | 35356 | 78054 | 76791 | 9639 | 2026-09-09 00:20:26 |
| [flask](https://github.com/pallets/flask) | 73581 | 16979 | 2765 | 2903 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67220 | 27377 | 12272 | 21445 | 2153 | 2026-09-08 10:24:38 |
| [keras](https://github.com/keras-team/keras) | 64319 | 19786 | 12897 | 9824 | 206 | 2026-09-08 22:31:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 49705 | 20359 | 28532 | 38585 | 2730 | 2026-09-08 20:53:34 |
| [ray](https://github.com/ray-project/ray) | 43750 | 8015 | 23029 | 42568 | 3576 | 2026-09-09 03:52:43 |
| [gym](https://github.com/openai/gym) | 37236 | 8676 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33887 | 4721 | 5771 | 4120 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32704 | 12752 | 14087 | 18367 | 2299 | 2026-09-08 22:16:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30169 | 7081 | 3966 | 5057 | 53 | 2026-09-08 19:14:07 |
| [celery](https://github.com/celery/celery) | 28872 | 5152 | 5298 | 4315 | 735 | 2026-09-08 22:13:17 |
| [dash](https://github.com/plotly/dash) | 24401 | 2313 | 2150 | 1699 | 508 | 2026-09-08 21:04:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23205 | 8478 | 11417 | 20838 | 1472 | 2026-09-09 03:54:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 22342 | 1485 | 1423 | 7179 | 396 | 2026-09-09 02:47:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5555 | 1879 | 1811 | 254 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22051 | 8965 | 6123 | 8084 | 1522 | 2026-09-08 06:29:21 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18768 | 2837 | 3380 | 2150 | 702 | 2026-09-08 17:13:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1598 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16544 | 2397 | 3249 | 10069 | 218 | 2026-09-09 02:19:18 |
| [httpx](https://github.com/encode/httpx) | 15470 | 1282 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15002 | 5916 | 11630 | 14471 | 1833 | 2026-09-09 01:43:05 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14019 | 2129 | 2662 | 1217 | 232 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13911 | 1945 | 5556 | 6719 | 1327 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12611 | 1296 | 782 | 2101 | 44 | 2026-09-07 17:36:27 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12147 | 1777 | 8289 | 1201 | 200 | 2026-09-08 18:49:39 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11897 | 613 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 1032 | 1140 | 1513 | 155 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9186 | 611 | 1044 | 544 | 224 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8781 | 1506 | 866 | 649 | 290 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7315 | 421 | 900 | 2601 | 323 | 2026-09-07 22:29:47 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5625 | 506 | 1268 | 895 | 547 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5382 | 1038 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4379 | 374 | 1201 | 249 | 120 | 2026-09-08 19:06:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4098 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3668 | 205 | 285 | 135 | 26 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 316 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2537 | 256 | 475 | 762 | 108 | 2026-09-07 19:36:00 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 916 | 1085 | 1596 | 357 | 2026-09-08 02:20:54 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1786 | 274 | 272 | 2026-09-07 18:00:00 |
| [pypy](https://github.com/pypy/pypy) | 1789 | 125 | 5256 | 301 | 722 | 2026-09-08 19:46:17 |
| [jython](https://github.com/jython/jython) | 1540 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-09T04:23:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
