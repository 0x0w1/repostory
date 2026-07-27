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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196557 | 75601 | 41626 | 78846 | 2853 | 2026-07-27 03:45:24 |
| [transformers](https://github.com/huggingface/transformers) | 163015 | 34026 | 19235 | 27597 | 2358 | 2026-07-27 03:19:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 101989 | 28536 | 60017 | 130504 | 18314 | 2026-07-27 03:44:20 |
| [fastapi](https://github.com/fastapi/fastapi) | 100914 | 9694 | 3542 | 6131 | 85 | 2026-07-24 21:16:20 |
| [django](https://github.com/django/django) | 88227 | 33993 | 0 | 21601 | 452 | 2026-07-24 18:54:30 |
| [cpython](https://github.com/python/cpython) | 73945 | 35012 | 77416 | 74991 | 9485 | 2026-07-27 00:03:23 |
| [flask](https://github.com/pallets/flask) | 72020 | 16922 | 2757 | 2875 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66787 | 27215 | 12202 | 21182 | 2120 | 2026-07-25 04:36:01 |
| [keras](https://github.com/keras-team/keras) | 64180 | 19744 | 12851 | 9614 | 215 | 2026-07-24 17:51:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 49338 | 20175 | 28418 | 37951 | 2894 | 2026-07-26 19:09:17 |
| [ray](https://github.com/ray-project/ray) | 43360 | 7836 | 22873 | 41746 | 3470 | 2026-07-27 03:26:04 |
| [gym](https://github.com/openai/gym) | 37241 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33777 | 4698 | 5767 | 4106 | 229 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32435 | 12593 | 14022 | 17998 | 2323 | 2026-07-26 08:51:58 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30107 | 7077 | 3966 | 5034 | 74 | 2026-07-25 18:13:17 |
| [celery](https://github.com/celery/celery) | 28726 | 5113 | 5289 | 4199 | 788 | 2026-07-23 09:11:33 |
| [dash](https://github.com/plotly/dash) | 24352 | 2308 | 2132 | 1659 | 533 | 2026-07-27 01:04:09 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23034 | 8418 | 11374 | 20683 | 1480 | 2026-07-26 15:39:25 |
| [RustPython](https://github.com/RustPython/RustPython) | 22229 | 1467 | 1398 | 6914 | 407 | 2026-07-26 05:31:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5546 | 1876 | 1790 | 240 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21940 | 8916 | 6109 | 7984 | 1567 | 2026-07-27 03:48:47 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18689 | 2826 | 3371 | 2117 | 777 | 2026-07-24 17:29:44 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1591 | 1470 | 1696 | 138 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16508 | 2358 | 3225 | 9671 | 214 | 2026-07-26 21:49:12 |
| [httpx](https://github.com/encode/httpx) | 15372 | 1217 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14852 | 5827 | 11545 | 14142 | 1841 | 2026-07-26 23:04:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13977 | 2128 | 2655 | 1205 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13871 | 1915 | 5544 | 6665 | 1274 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12497 | 1239 | 772 | 1984 | 69 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12027 | 1724 | 8249 | 1153 | 207 | 2026-07-23 18:03:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11868 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9790 | 1021 | 1139 | 1493 | 163 | 2026-07-24 19:59:36 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9149 | 602 | 1040 | 525 | 221 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8773 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7307 | 410 | 897 | 2579 | 327 | 2026-07-27 00:34:37 |
| [hug](https://github.com/hugapi/hug) | 6884 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5606 | 499 | 1265 | 877 | 536 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5333 | 1029 | 923 | 314 | 201 | 2026-07-24 08:38:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4281 | 356 | 1190 | 235 | 124 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4092 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 202 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2757 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2513 | 226 | 458 | 708 | 93 | 2026-07-25 10:23:19 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1580 | 358 | 2026-07-24 11:00:35 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1771 | 121 | 5237 | 275 | 721 | 2026-07-27 02:33:58 |
| [jython](https://github.com/jython/jython) | 1528 | 231 | 299 | 146 | 104 | 2026-07-26 19:12:04 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-27T03:51:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
