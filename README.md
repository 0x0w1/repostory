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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196423 | 75631 | 41615 | 78462 | 2856 | 2026-07-21 03:28:00 |
| [transformers](https://github.com/huggingface/transformers) | 162785 | 33955 | 19207 | 27493 | 2442 | 2026-07-21 02:54:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 101819 | 28437 | 59927 | 130058 | 18290 | 2026-07-21 03:30:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 100707 | 9649 | 3541 | 6098 | 94 | 2026-07-20 14:37:07 |
| [django](https://github.com/django/django) | 88188 | 34128 | 0 | 21572 | 452 | 2026-07-20 17:32:09 |
| [cpython](https://github.com/python/cpython) | 73839 | 34960 | 77310 | 74659 | 9469 | 2026-07-21 01:05:05 |
| [flask](https://github.com/pallets/flask) | 71988 | 16910 | 2756 | 2868 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66739 | 27197 | 12192 | 21147 | 2131 | 2026-07-20 17:04:06 |
| [keras](https://github.com/keras-team/keras) | 64170 | 19744 | 12847 | 9595 | 218 | 2026-07-21 02:06:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49261 | 20151 | 28405 | 37890 | 2904 | 2026-07-21 01:14:58 |
| [ray](https://github.com/ray-project/ray) | 43299 | 7809 | 22858 | 41638 | 3478 | 2026-07-21 02:53:57 |
| [gym](https://github.com/openai/gym) | 37240 | 8689 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33756 | 4696 | 5768 | 4104 | 228 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32401 | 12579 | 14008 | 17945 | 2373 | 2026-07-20 18:43:43 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30106 | 7077 | 3967 | 5027 | 85 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28704 | 5108 | 5288 | 4183 | 785 | 2026-07-20 22:12:58 |
| [dash](https://github.com/plotly/dash) | 24336 | 2308 | 2130 | 1652 | 533 | 2026-07-20 19:16:05 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23022 | 8409 | 11367 | 20651 | 1486 | 2026-07-19 02:37:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 22210 | 1464 | 1388 | 6880 | 396 | 2026-07-20 16:36:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22191 | 5546 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21916 | 8914 | 6103 | 7969 | 1582 | 2026-07-21 02:21:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18684 | 2827 | 3372 | 2114 | 779 | 2026-07-20 16:37:01 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1589 | 1468 | 1694 | 134 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16502 | 2355 | 3225 | 9621 | 209 | 2026-07-20 20:45:06 |
| [httpx](https://github.com/encode/httpx) | 15356 | 1213 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14832 | 5808 | 11539 | 14105 | 1852 | 2026-07-21 01:49:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13972 | 2127 | 2656 | 1204 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13865 | 1910 | 5542 | 6659 | 1267 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12489 | 1234 | 771 | 1970 | 64 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12009 | 1720 | 8246 | 1145 | 203 | 2026-07-20 19:57:34 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11864 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9792 | 1021 | 1138 | 1487 | 171 | 2026-07-20 21:36:57 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9142 | 602 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7297 | 409 | 896 | 2574 | 328 | 2026-07-20 21:57:28 |
| [hug](https://github.com/hugapi/hug) | 6884 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5610 | 499 | 1264 | 875 | 533 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5325 | 1029 | 922 | 313 | 206 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4265 | 355 | 1189 | 234 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 266 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 204 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2510 | 224 | 455 | 703 | 94 | 2026-07-20 23:44:09 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 913 | 1084 | 1575 | 359 | 2026-07-20 10:21:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1768 | 119 | 5237 | 271 | 723 | 2026-07-19 20:20:02 |
| [jython](https://github.com/jython/jython) | 1529 | 232 | 298 | 142 | 103 | 2026-07-19 06:34:16 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-21T03:30:58*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
