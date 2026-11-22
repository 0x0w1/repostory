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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201700 | 77415 | 41991 | 84964 | 3475 | 2026-11-22 04:04:43 |
| [transformers](https://github.com/huggingface/transformers) | 169339 | 35262 | 19937 | 30277 | 1117 | 2026-11-22 01:37:19 |
| [pytorch](https://github.com/pytorch/pytorch) | 105753 | 30694 | 62883 | 142440 | 18514 | 2026-11-22 06:11:47 |
| [fastapi](https://github.com/fastapi/fastapi) | 104968 | 10364 | 3555 | 6646 | 49 | 2026-11-18 19:14:19 |
| [django](https://github.com/django/django) | 91879 | 35115 | 0 | 22239 | 541 | 2026-11-21 16:52:56 |
| [cpython](https://github.com/python/cpython) | 78417 | 36559 | 79379 | 80623 | 9380 | 2026-11-22 02:35:10 |
| [flask](https://github.com/pallets/flask) | 75294 | 17282 | 2782 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68285 | 27681 | 12402 | 21879 | 2176 | 2026-11-21 14:45:13 |
| [keras](https://github.com/keras-team/keras) | 64448 | 19805 | 13106 | 10320 | 253 | 2026-11-20 23:54:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 50595 | 20706 | 28705 | 40137 | 1798 | 2026-11-22 04:17:32 |
| [ray](https://github.com/ray-project/ray) | 44354 | 8296 | 23359 | 44599 | 3844 | 2026-11-22 02:59:10 |
| [gym](https://github.com/openai/gym) | 37237 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34082 | 4750 | 5785 | 4155 | 276 | 2026-11-21 10:00:45 |
| [numpy](https://github.com/numpy/numpy) | 33454 | 13059 | 14204 | 19093 | 2261 | 2026-11-21 19:39:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30253 | 7107 | 3966 | 5119 | 58 | 2026-11-19 09:00:18 |
| [celery](https://github.com/celery/celery) | 29257 | 5274 | 5404 | 4753 | 812 | 2026-11-19 19:15:56 |
| [dash](https://github.com/plotly/dash) | 24502 | 2348 | 2185 | 1852 | 427 | 2026-11-20 20:30:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23495 | 8572 | 11466 | 21103 | 1480 | 2026-11-22 04:03:58 |
| [RustPython](https://github.com/RustPython/RustPython) | 22499 | 1509 | 1473 | 8409 | 326 | 2026-11-22 02:15:47 |
| [micropython](https://github.com/micropython/micropython) | 22217 | 9075 | 6185 | 8280 | 1597 | 2026-11-21 05:26:55 |
| [tornado](https://github.com/tornadoweb/tornado) | 22171 | 5615 | 1901 | 1953 | 204 | 2026-11-21 03:23:15 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18918 | 2903 | 3408 | 2295 | 737 | 2026-11-19 23:40:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1618 | 1475 | 1696 | 167 | 2026-11-20 17:16:24 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16620 | 2538 | 3280 | 10763 | 338 | 2026-11-22 01:35:55 |
| [httpx](https://github.com/encode/httpx) | 15833 | 2021 | 925 | 1827 | 153 | 2026-11-16 19:43:14 |
| [scipy](https://github.com/scipy/scipy) | 15237 | 6114 | 11787 | 14962 | 1931 | 2026-11-21 20:39:15 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14120 | 2169 | 2669 | 1266 | 265 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13959 | 2032 | 5583 | 6851 | 1436 | 2026-11-21 20:29:45 |
| [starlette](https://github.com/Kludex/starlette) | 12751 | 1453 | 800 | 2304 | 36 | 2026-11-14 06:11:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12302 | 1961 | 8409 | 1263 | 218 | 2026-11-19 21:09:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11947 | 624 | 431 | 349 | 178 | 2026-11-20 01:08:10 |
| [falcon](https://github.com/falconry/falcon) | 9821 | 1055 | 1154 | 1583 | 164 | 2026-11-21 22:54:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9250 | 624 | 1059 | 622 | 163 | 2026-11-17 12:36:08 |
| [bottle](https://github.com/bottlepy/bottle) | 8803 | 1512 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7368 | 480 | 911 | 2678 | 344 | 2026-11-18 11:55:16 |
| [hug](https://github.com/hugapi/hug) | 6868 | 390 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5641 | 549 | 1311 | 995 | 559 | 2026-11-21 06:36:45 |
| [vibora](https://github.com/vibora-io/vibora) | 5576 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5458 | 1054 | 939 | 336 | 196 | 2026-11-17 12:47:23 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4482 | 395 | 1212 | 259 | 118 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4108 | 898 | 1067 | 2752 | 83 | 2026-11-22 03:16:11 |
| [databases](https://github.com/encode/databases) | 3984 | 368 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3683 | 214 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2761 | 320 | 682 | 1430 | 256 | 2026-11-22 04:25:10 |
| [anyio](https://github.com/agronholm/anyio) | 2572 | 360 | 507 | 914 | 165 | 2026-11-21 14:17:49 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2353 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 373 | 1791 | 284 | 280 | 2026-11-16 18:02:38 |
| [pypy](https://github.com/pypy/pypy) | 1827 | 133 | 5305 | 472 | 724 | 2026-11-21 20:14:35 |
| [jython](https://github.com/jython/jython) | 1549 | 238 | 306 | 165 | 110 | 2026-11-21 09:13:28 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 394 | 41 | 449 | 118 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 315 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-22T06:23:36*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
