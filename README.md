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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201210 | 79839 | 41912 | 83817 | 3438 | 2026-10-20 04:31:16 |
| [transformers](https://github.com/huggingface/transformers) | 167877 | 34912 | 19659 | 29300 | 2300 | 2026-10-20 04:19:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 104945 | 32921 | 61852 | 138967 | 17659 | 2026-10-20 04:31:52 |
| [fastapi](https://github.com/fastapi/fastapi) | 103267 | 10063 | 3555 | 6463 | 72 | 2026-10-19 22:39:29 |
| [django](https://github.com/django/django) | 91535 | 37624 | 0 | 22095 | 544 | 2026-10-19 09:46:16 |
| [cpython](https://github.com/python/cpython) | 77778 | 38768 | 78785 | 78685 | 9779 | 2026-10-20 04:00:42 |
| [flask](https://github.com/pallets/flask) | 74966 | 17109 | 2768 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67855 | 27554 | 12336 | 21644 | 2161 | 2026-10-20 03:32:15 |
| [keras](https://github.com/keras-team/keras) | 64373 | 19801 | 13030 | 10104 | 247 | 2026-10-19 19:14:48 |
| [pandas](https://github.com/pandas-dev/pandas) | 50256 | 20560 | 28632 | 39540 | 2128 | 2026-10-19 21:34:19 |
| [ray](https://github.com/ray-project/ray) | 44081 | 8174 | 23206 | 43533 | 3606 | 2026-10-20 03:39:10 |
| [gym](https://github.com/openai/gym) | 37239 | 8666 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33973 | 4735 | 5776 | 4132 | 253 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33053 | 12951 | 14144 | 18855 | 2239 | 2026-10-19 18:26:22 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30210 | 7092 | 3966 | 5092 | 57 | 2026-10-14 22:32:27 |
| [celery](https://github.com/celery/celery) | 29015 | 5230 | 5340 | 4594 | 731 | 2026-10-19 22:14:09 |
| [dash](https://github.com/plotly/dash) | 24460 | 2326 | 2167 | 1775 | 433 | 2026-10-19 16:57:50 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23384 | 8517 | 11442 | 20997 | 1476 | 2026-10-19 07:32:38 |
| [RustPython](https://github.com/RustPython/RustPython) | 22410 | 1501 | 1440 | 7696 | 299 | 2026-10-20 04:00:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22166 | 5583 | 1888 | 1875 | 230 | 2026-10-19 17:44:01 |
| [micropython](https://github.com/micropython/micropython) | 22136 | 9009 | 6147 | 8142 | 1539 | 2026-10-19 03:10:08 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18847 | 2875 | 3393 | 2241 | 737 | 2026-10-16 17:21:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1612 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16579 | 2462 | 3263 | 10432 | 236 | 2026-10-19 16:25:49 |
| [httpx](https://github.com/encode/httpx) | 15643 | 4403 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15128 | 6018 | 11706 | 14718 | 1873 | 2026-10-19 17:19:17 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14079 | 2148 | 2667 | 1242 | 253 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13935 | 1986 | 5569 | 6767 | 1374 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12676 | 1385 | 793 | 2225 | 47 | 2026-10-18 21:09:43 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12250 | 1826 | 8351 | 1235 | 213 | 2026-10-19 22:48:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11913 | 619 | 426 | 344 | 171 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9810 | 1040 | 1147 | 1548 | 158 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9215 | 619 | 1054 | 569 | 235 | 2026-10-13 12:52:56 |
| [bottle](https://github.com/bottlepy/bottle) | 8797 | 1517 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7350 | 459 | 904 | 2640 | 338 | 2026-10-19 23:00:19 |
| [hug](https://github.com/hugapi/hug) | 6875 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 531 | 1289 | 952 | 559 | 2026-10-19 17:54:04 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5429 | 1049 | 936 | 325 | 204 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4452 | 386 | 1207 | 257 | 120 | 2026-10-15 21:56:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 895 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 273 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3677 | 210 | 289 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2764 | 317 | 677 | 1363 | 265 | 2026-10-18 20:57:47 |
| [anyio](https://github.com/agronholm/anyio) | 2560 | 319 | 491 | 859 | 134 | 2026-10-19 20:23:23 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 917 | 1085 | 1603 | 356 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 369 | 1791 | 276 | 277 | 2026-10-19 18:13:34 |
| [pypy](https://github.com/pypy/pypy) | 1814 | 131 | 5285 | 364 | 716 | 2026-10-19 20:23:33 |
| [jython](https://github.com/jython/jython) | 1549 | 231 | 303 | 155 | 102 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-20T04:33:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
