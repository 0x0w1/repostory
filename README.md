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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198907 | 76289 | 41750 | 81609 | 3134 | 2026-09-07 04:06:15 |
| [transformers](https://github.com/huggingface/transformers) | 164923 | 34481 | 19417 | 28403 | 2414 | 2026-09-06 23:02:07 |
| [pytorch](https://github.com/pytorch/pytorch) | 102826 | 29144 | 60791 | 134731 | 17563 | 2026-09-07 03:56:06 |
| [fastapi](https://github.com/fastapi/fastapi) | 102163 | 9865 | 3549 | 6333 | 92 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 89984 | 34257 | 0 | 21790 | 492 | 2026-09-06 15:50:27 |
| [cpython](https://github.com/python/cpython) | 76032 | 35355 | 77971 | 76728 | 9642 | 2026-09-06 21:15:38 |
| [flask](https://github.com/pallets/flask) | 72204 | 16980 | 2765 | 2902 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67201 | 27376 | 12266 | 21433 | 2147 | 2026-09-04 20:55:21 |
| [keras](https://github.com/keras-team/keras) | 64319 | 19786 | 12896 | 9809 | 211 | 2026-09-05 05:37:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 49686 | 20350 | 28531 | 38573 | 2749 | 2026-09-06 18:47:22 |
| [ray](https://github.com/ray-project/ray) | 43721 | 8006 | 23022 | 42528 | 3565 | 2026-09-07 01:02:52 |
| [gym](https://github.com/openai/gym) | 37240 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33876 | 4723 | 5771 | 4120 | 239 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32694 | 12743 | 14084 | 18347 | 2312 | 2026-09-07 00:43:00 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30165 | 7084 | 3966 | 5054 | 53 | 2026-09-06 17:12:09 |
| [celery](https://github.com/celery/celery) | 28865 | 5152 | 5299 | 4303 | 734 | 2026-09-06 17:14:41 |
| [dash](https://github.com/plotly/dash) | 24398 | 2316 | 2150 | 1698 | 534 | 2026-09-04 16:25:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23198 | 8483 | 11412 | 20831 | 1469 | 2026-09-07 02:18:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 22336 | 1484 | 1423 | 7165 | 396 | 2026-09-07 01:19:04 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5555 | 1879 | 1811 | 254 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22046 | 8964 | 6123 | 8084 | 1526 | 2026-09-07 03:11:48 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18766 | 2837 | 3378 | 2150 | 700 | 2026-09-04 13:59:59 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1599 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16538 | 2396 | 3243 | 10040 | 214 | 2026-09-07 02:04:30 |
| [httpx](https://github.com/encode/httpx) | 15461 | 1280 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14992 | 5910 | 11626 | 14453 | 1832 | 2026-09-07 01:05:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14017 | 2130 | 2660 | 1217 | 232 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13911 | 1942 | 5555 | 6715 | 1326 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12597 | 1293 | 781 | 2097 | 42 | 2026-09-06 17:43:10 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12140 | 1777 | 8287 | 1200 | 203 | 2026-09-04 20:37:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 612 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9798 | 1032 | 1140 | 1514 | 156 | 2026-09-06 20:35:23 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9184 | 611 | 1044 | 543 | 223 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1506 | 866 | 649 | 290 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7316 | 420 | 900 | 2599 | 328 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5622 | 503 | 1268 | 893 | 545 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5379 | 1038 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4371 | 374 | 1201 | 249 | 127 | 2026-09-04 17:15:17 |
| [pyramid](https://github.com/Pylons/pyramid) | 4097 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3664 | 206 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 316 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 253 | 475 | 759 | 106 | 2026-09-06 19:40:33 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1786 | 274 | 272 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1788 | 125 | 5255 | 300 | 722 | 2026-09-06 20:34:15 |
| [jython](https://github.com/jython/jython) | 1540 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-07T04:17:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
