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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196777 | 75832 | 41648 | 79399 | 2991 | 2026-08-04 03:22:57 |
| [transformers](https://github.com/huggingface/transformers) | 163303 | 34112 | 19269 | 27746 | 2343 | 2026-08-04 02:46:41 |
| [pytorch](https://github.com/pytorch/pytorch) | 102166 | 28701 | 60160 | 131214 | 18428 | 2026-08-04 03:21:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 101288 | 9727 | 3542 | 6190 | 79 | 2026-08-03 20:17:29 |
| [django](https://github.com/django/django) | 88325 | 34093 | 0 | 21607 | 444 | 2026-08-03 15:11:31 |
| [cpython](https://github.com/python/cpython) | 74130 | 35126 | 77515 | 75280 | 9520 | 2026-08-03 21:21:12 |
| [flask](https://github.com/pallets/flask) | 72096 | 16923 | 2758 | 2884 | 7 | 2026-07-30 17:29:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66866 | 27254 | 12217 | 21238 | 2118 | 2026-08-03 19:05:04 |
| [keras](https://github.com/keras-team/keras) | 64217 | 19747 | 12859 | 9661 | 210 | 2026-08-04 00:52:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 49409 | 20226 | 28450 | 38054 | 2912 | 2026-08-03 22:34:52 |
| [ray](https://github.com/ray-project/ray) | 43426 | 7880 | 22891 | 41897 | 3480 | 2026-08-04 03:06:02 |
| [gym](https://github.com/openai/gym) | 37247 | 8686 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33800 | 4701 | 5768 | 4107 | 231 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32480 | 12614 | 14033 | 18059 | 2318 | 2026-08-03 22:09:05 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30115 | 7074 | 3965 | 5036 | 68 | 2026-07-31 18:52:20 |
| [celery](https://github.com/celery/celery) | 28756 | 5122 | 5289 | 4212 | 798 | 2026-08-03 22:14:11 |
| [dash](https://github.com/plotly/dash) | 24366 | 2313 | 2138 | 1673 | 542 | 2026-08-03 17:29:00 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23061 | 8426 | 11386 | 20712 | 1478 | 2026-08-03 03:00:30 |
| [RustPython](https://github.com/RustPython/RustPython) | 22240 | 1469 | 1407 | 6966 | 398 | 2026-08-03 22:31:06 |
| [tornado](https://github.com/tornadoweb/tornado) | 22191 | 5548 | 1877 | 1800 | 250 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21960 | 8918 | 6112 | 8009 | 1561 | 2026-08-01 08:22:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18713 | 2833 | 3376 | 2126 | 773 | 2026-08-01 12:45:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1594 | 1471 | 1700 | 143 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16510 | 2362 | 3228 | 9735 | 217 | 2026-08-03 13:41:32 |
| [httpx](https://github.com/encode/httpx) | 15391 | 1233 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14881 | 5843 | 11557 | 14208 | 1849 | 2026-08-03 21:03:32 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13987 | 2129 | 2655 | 1207 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13880 | 1922 | 5546 | 6679 | 1287 | 2026-08-03 22:03:26 |
| [starlette](https://github.com/Kludex/starlette) | 12516 | 1256 | 772 | 1993 | 75 | 2026-08-02 08:07:42 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12047 | 1738 | 8254 | 1165 | 211 | 2026-08-04 02:24:40 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11876 | 613 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1021 | 1139 | 1495 | 157 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9157 | 603 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1499 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 412 | 898 | 2585 | 323 | 2026-08-03 02:34:09 |
| [hug](https://github.com/hugapi/hug) | 6885 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5607 | 501 | 1265 | 880 | 539 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5340 | 1030 | 924 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4296 | 359 | 1190 | 238 | 123 | 2026-08-04 00:45:16 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 891 | 1065 | 2740 | 89 | 2026-08-02 21:27:46 |
| [databases](https://github.com/encode/databases) | 4001 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 202 | 284 | 133 | 42 | 2026-08-03 20:05:57 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2757 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2519 | 234 | 462 | 722 | 100 | 2026-08-03 23:44:36 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1084 | 1581 | 357 | 2026-07-29 16:59:19 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-08-03 17:54:08 |
| [pypy](https://github.com/pypy/pypy) | 1779 | 121 | 5244 | 285 | 730 | 2026-08-03 09:52:45 |
| [jython](https://github.com/jython/jython) | 1529 | 230 | 299 | 148 | 104 | 2026-08-03 09:19:56 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-02 09:46:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-04T03:25:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
