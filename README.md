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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196535 | 75570 | 41625 | 78804 | 2823 | 2026-07-26 03:22:56 |
| [transformers](https://github.com/huggingface/transformers) | 162979 | 34015 | 19232 | 27591 | 2389 | 2026-07-26 00:53:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 101954 | 28504 | 60012 | 130469 | 18306 | 2026-07-26 03:39:41 |
| [fastapi](https://github.com/fastapi/fastapi) | 100882 | 9690 | 3543 | 6130 | 88 | 2026-07-24 21:16:20 |
| [django](https://github.com/django/django) | 88214 | 33980 | 0 | 21596 | 450 | 2026-07-24 18:54:30 |
| [cpython](https://github.com/python/cpython) | 73920 | 35005 | 77399 | 74955 | 9478 | 2026-07-25 15:17:12 |
| [flask](https://github.com/pallets/flask) | 72016 | 16918 | 2756 | 2874 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66785 | 27212 | 12200 | 21179 | 2115 | 2026-07-25 04:36:01 |
| [keras](https://github.com/keras-team/keras) | 64180 | 19742 | 12853 | 9612 | 215 | 2026-07-24 17:51:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 49327 | 20176 | 28417 | 37950 | 2893 | 2026-07-25 15:29:17 |
| [ray](https://github.com/ray-project/ray) | 43352 | 7831 | 22874 | 41734 | 3462 | 2026-07-25 23:08:06 |
| [gym](https://github.com/openai/gym) | 37240 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33772 | 4699 | 5770 | 4106 | 232 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32429 | 12593 | 14021 | 17996 | 2322 | 2026-07-25 16:31:30 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30107 | 7078 | 3967 | 5034 | 79 | 2026-07-25 18:13:17 |
| [celery](https://github.com/celery/celery) | 28727 | 5113 | 5288 | 4198 | 787 | 2026-07-23 09:11:33 |
| [dash](https://github.com/plotly/dash) | 24351 | 2308 | 2133 | 1658 | 532 | 2026-07-24 14:34:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23033 | 8417 | 11372 | 20681 | 1478 | 2026-07-25 18:56:43 |
| [RustPython](https://github.com/RustPython/RustPython) | 22222 | 1467 | 1391 | 6907 | 406 | 2026-07-25 11:41:31 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5547 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21936 | 8915 | 6109 | 7983 | 1571 | 2026-07-25 02:01:24 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18687 | 2826 | 3373 | 2117 | 778 | 2026-07-24 17:29:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1591 | 1470 | 1696 | 138 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16506 | 2357 | 3225 | 9667 | 217 | 2026-07-25 12:18:11 |
| [httpx](https://github.com/encode/httpx) | 15373 | 1216 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14849 | 5823 | 11545 | 14131 | 1834 | 2026-07-25 18:56:40 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13974 | 2128 | 2656 | 1205 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13871 | 1914 | 5546 | 6663 | 1274 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12498 | 1237 | 772 | 1982 | 67 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12024 | 1722 | 8249 | 1150 | 204 | 2026-07-23 18:03:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11867 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9792 | 1021 | 1139 | 1492 | 162 | 2026-07-24 19:59:36 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9148 | 602 | 1040 | 525 | 221 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8773 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7304 | 410 | 896 | 2575 | 327 | 2026-07-24 05:14:45 |
| [hug](https://github.com/hugapi/hug) | 6885 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5606 | 500 | 1265 | 879 | 538 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5333 | 1029 | 923 | 314 | 201 | 2026-07-24 08:38:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4279 | 356 | 1190 | 235 | 124 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 202 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2757 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2513 | 226 | 457 | 708 | 91 | 2026-07-25 10:23:19 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 915 | 1084 | 1580 | 358 | 2026-07-24 11:00:35 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1771 | 121 | 5237 | 275 | 723 | 2026-07-25 19:27:15 |
| [jython](https://github.com/jython/jython) | 1528 | 231 | 298 | 145 | 104 | 2026-07-24 07:02:59 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-26T03:41:42*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
