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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201585 | 77952 | 41976 | 84694 | 3440 | 2026-11-13 06:12:38 |
| [transformers](https://github.com/huggingface/transformers) | 168938 | 35234 | 19859 | 29989 | 1085 | 2026-11-13 05:49:32 |
| [pytorch](https://github.com/pytorch/pytorch) | 105462 | 30713 | 62557 | 141439 | 18214 | 2026-11-13 06:16:52 |
| [fastapi](https://github.com/fastapi/fastapi) | 104678 | 10239 | 3555 | 6605 | 53 | 2026-11-11 22:29:35 |
| [django](https://github.com/django/django) | 91731 | 35224 | 0 | 22196 | 533 | 2026-11-12 22:10:38 |
| [cpython](https://github.com/python/cpython) | 78201 | 36583 | 79256 | 80254 | 9287 | 2026-11-13 01:30:16 |
| [flask](https://github.com/pallets/flask) | 75112 | 17317 | 2780 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68159 | 27673 | 12381 | 21806 | 2171 | 2026-11-13 04:05:00 |
| [keras](https://github.com/keras-team/keras) | 64424 | 19819 | 13083 | 10250 | 239 | 2026-11-13 03:35:46 |
| [pandas](https://github.com/pandas-dev/pandas) | 50506 | 20737 | 28686 | 39974 | 1888 | 2026-11-12 22:19:26 |
| [ray](https://github.com/ray-project/ray) | 44277 | 8278 | 23317 | 44321 | 3766 | 2026-11-13 04:46:33 |
| [gym](https://github.com/openai/gym) | 37233 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34050 | 4740 | 5783 | 4147 | 268 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33353 | 13100 | 14185 | 19027 | 2248 | 2026-11-13 04:17:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30232 | 7100 | 3966 | 5113 | 64 | 2026-11-12 10:27:24 |
| [celery](https://github.com/celery/celery) | 29185 | 5262 | 5392 | 4730 | 801 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24490 | 2348 | 2181 | 1836 | 440 | 2026-11-12 20:54:45 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23455 | 8546 | 11460 | 21062 | 1474 | 2026-11-12 20:24:22 |
| [RustPython](https://github.com/RustPython/RustPython) | 22479 | 1510 | 1463 | 8258 | 311 | 2026-11-13 05:56:18 |
| [micropython](https://github.com/micropython/micropython) | 22196 | 9060 | 6179 | 8249 | 1597 | 2026-11-12 12:22:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22163 | 5607 | 1894 | 1925 | 228 | 2026-11-12 19:00:40 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18897 | 2895 | 3402 | 2281 | 752 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1618 | 1474 | 1689 | 163 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16605 | 2522 | 3275 | 10709 | 303 | 2026-11-13 04:05:00 |
| [httpx](https://github.com/encode/httpx) | 15803 | 1869 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15210 | 6082 | 11766 | 14895 | 1909 | 2026-11-12 22:30:21 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14109 | 2161 | 2668 | 1255 | 254 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13948 | 2023 | 5583 | 6830 | 1436 | 2026-11-12 17:57:54 |
| [starlette](https://github.com/Kludex/starlette) | 12731 | 1442 | 798 | 2303 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12280 | 1848 | 8393 | 1264 | 211 | 2026-11-11 20:51:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11935 | 620 | 431 | 348 | 180 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9814 | 1056 | 1152 | 1576 | 163 | 2026-11-11 09:13:34 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9244 | 626 | 1057 | 616 | 158 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1512 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7362 | 475 | 911 | 2670 | 344 | 2026-11-13 05:54:06 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 737 | 979 | 595 | 30 | 2026-11-12 09:41:56 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5643 | 545 | 1307 | 989 | 554 | 2026-11-12 09:12:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5450 | 1054 | 938 | 333 | 204 | 2026-11-12 07:01:24 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4476 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4107 | 898 | 1067 | 2748 | 91 | 2026-11-11 07:22:34 |
| [databases](https://github.com/encode/databases) | 3985 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3682 | 213 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 320 | 682 | 1416 | 257 | 2026-11-12 22:25:01 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 499 | 893 | 147 | 2026-11-12 07:54:18 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 913 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 281 | 279 | 2026-11-09 18:05:48 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 133 | 5302 | 427 | 728 | 2026-11-13 05:40:57 |
| [jython](https://github.com/jython/jython) | 1551 | 236 | 306 | 163 | 108 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-13T06:18:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
