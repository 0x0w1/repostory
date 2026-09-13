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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 199741 | 76311 | 41776 | 81923 | 3112 | 2026-09-12 22:44:53 |
| [transformers](https://github.com/huggingface/transformers) | 165224 | 34535 | 19457 | 28526 | 2419 | 2026-09-13 03:31:49 |
| [pytorch](https://github.com/pytorch/pytorch) | 102961 | 29210 | 60923 | 135300 | 17731 | 2026-09-13 04:29:46 |
| [fastapi](https://github.com/fastapi/fastapi) | 102294 | 9874 | 3551 | 6323 | 83 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 90764 | 34252 | 0 | 21840 | 502 | 2026-09-08 19:01:03 |
| [cpython](https://github.com/python/cpython) | 76863 | 35375 | 78093 | 76950 | 9646 | 2026-09-13 04:20:58 |
| [flask](https://github.com/pallets/flask) | 74278 | 16984 | 2767 | 2909 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67235 | 27390 | 12279 | 21476 | 2161 | 2026-09-12 17:11:44 |
| [keras](https://github.com/keras-team/keras) | 64318 | 19787 | 12903 | 9849 | 188 | 2026-09-12 03:20:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 49725 | 20373 | 28541 | 38723 | 2750 | 2026-09-13 04:25:33 |
| [ray](https://github.com/ray-project/ray) | 43785 | 8029 | 23057 | 42662 | 3605 | 2026-09-12 23:11:07 |
| [gym](https://github.com/openai/gym) | 37238 | 8675 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33894 | 4721 | 5772 | 4120 | 240 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32731 | 12773 | 14093 | 18414 | 2299 | 2026-09-12 17:21:50 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30175 | 7082 | 3966 | 5062 | 51 | 2026-09-12 17:52:41 |
| [celery](https://github.com/celery/celery) | 28878 | 5162 | 5299 | 4353 | 728 | 2026-09-13 04:22:01 |
| [dash](https://github.com/plotly/dash) | 24404 | 2313 | 2151 | 1700 | 486 | 2026-09-11 17:00:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23213 | 8479 | 11423 | 20857 | 1481 | 2026-09-12 13:10:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 22342 | 1486 | 1424 | 7197 | 399 | 2026-09-13 00:41:58 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5555 | 1879 | 1814 | 255 | 2026-09-13 02:29:44 |
| [micropython](https://github.com/micropython/micropython) | 22060 | 8963 | 6124 | 8089 | 1524 | 2026-09-11 14:21:56 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18778 | 2838 | 3382 | 2152 | 700 | 2026-09-12 22:16:00 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1597 | 1467 | 1676 | 148 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16547 | 2406 | 3250 | 10085 | 220 | 2026-09-11 22:22:56 |
| [httpx](https://github.com/encode/httpx) | 15477 | 1288 | 0 | 1805 | 142 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15010 | 5927 | 11641 | 14495 | 1835 | 2026-09-12 21:00:33 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14022 | 2130 | 2662 | 1221 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13915 | 1954 | 5557 | 6723 | 1332 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12616 | 1302 | 782 | 2111 | 44 | 2026-09-12 12:06:46 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12153 | 1780 | 8298 | 1207 | 212 | 2026-09-12 05:02:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11898 | 614 | 420 | 330 | 160 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9800 | 1034 | 1142 | 1517 | 160 | 2026-09-07 10:34:33 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9189 | 612 | 1045 | 545 | 226 | 2026-09-03 16:41:54 |
| [bottle](https://github.com/bottlepy/bottle) | 8785 | 1506 | 866 | 649 | 290 | 2026-09-06 11:21:32 |
| [trio](https://github.com/python-trio/trio) | 7322 | 426 | 900 | 2605 | 326 | 2026-09-07 22:29:47 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 739 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5627 | 509 | 1269 | 899 | 531 | 2026-09-12 16:33:57 |
| [vibora](https://github.com/vibora-io/vibora) | 5581 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5386 | 1041 | 934 | 323 | 201 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4389 | 375 | 1202 | 249 | 118 | 2026-09-11 19:10:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 891 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3992 | 268 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 205 | 286 | 135 | 25 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2760 | 316 | 675 | 1339 | 314 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2540 | 260 | 477 | 766 | 109 | 2026-09-12 12:27:17 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1596 | 356 | 2026-09-12 16:42:08 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1786 | 274 | 272 | 2026-09-07 18:00:00 |
| [pypy](https://github.com/pypy/pypy) | 1793 | 125 | 5257 | 303 | 722 | 2026-09-11 11:55:49 |
| [jython](https://github.com/jython/jython) | 1541 | 232 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-13T04:32:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
