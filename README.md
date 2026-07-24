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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196486 | 75505 | 41618 | 78698 | 2768 | 2026-07-24 03:24:07 |
| [transformers](https://github.com/huggingface/transformers) | 162897 | 34007 | 19224 | 27556 | 2381 | 2026-07-24 03:20:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 101899 | 28473 | 59991 | 130339 | 18269 | 2026-07-24 03:28:53 |
| [fastapi](https://github.com/fastapi/fastapi) | 100812 | 9675 | 3542 | 6120 | 85 | 2026-07-24 00:09:13 |
| [django](https://github.com/django/django) | 88188 | 33967 | 0 | 21592 | 450 | 2026-07-23 17:16:09 |
| [cpython](https://github.com/python/cpython) | 73873 | 34976 | 77373 | 74849 | 9486 | 2026-07-23 17:28:40 |
| [flask](https://github.com/pallets/flask) | 71998 | 16913 | 2756 | 2872 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66767 | 27209 | 12197 | 21177 | 2116 | 2026-07-23 13:22:21 |
| [keras](https://github.com/keras-team/keras) | 64175 | 19744 | 12851 | 9607 | 211 | 2026-07-23 04:48:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 49300 | 20165 | 28414 | 37928 | 2882 | 2026-07-23 18:19:51 |
| [ray](https://github.com/ray-project/ray) | 43329 | 7827 | 22868 | 41713 | 3469 | 2026-07-24 03:23:23 |
| [gym](https://github.com/openai/gym) | 37239 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33768 | 4699 | 5768 | 4106 | 230 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32411 | 12590 | 14015 | 17985 | 2315 | 2026-07-24 01:01:13 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30105 | 7078 | 3967 | 5030 | 87 | 2026-07-22 08:03:04 |
| [celery](https://github.com/celery/celery) | 28719 | 5113 | 5288 | 4198 | 787 | 2026-07-23 09:11:33 |
| [dash](https://github.com/plotly/dash) | 24342 | 2308 | 2133 | 1657 | 533 | 2026-07-23 18:31:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23030 | 8416 | 11371 | 20672 | 1480 | 2026-07-24 03:16:17 |
| [RustPython](https://github.com/RustPython/RustPython) | 22217 | 1466 | 1391 | 6891 | 399 | 2026-07-23 17:43:31 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5546 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21926 | 8918 | 6105 | 7980 | 1577 | 2026-07-22 12:31:30 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18684 | 2827 | 3372 | 2117 | 777 | 2026-07-23 20:48:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1589 | 1470 | 1694 | 136 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16505 | 2357 | 3225 | 9657 | 216 | 2026-07-23 11:28:14 |
| [httpx](https://github.com/encode/httpx) | 15366 | 1214 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14841 | 5818 | 11543 | 14121 | 1843 | 2026-07-23 22:57:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13971 | 2129 | 2656 | 1205 | 223 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13865 | 1912 | 5543 | 6662 | 1271 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12490 | 1235 | 771 | 1981 | 65 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12021 | 1722 | 8249 | 1148 | 202 | 2026-07-23 18:03:16 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11865 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 1021 | 1139 | 1492 | 169 | 2026-07-23 19:40:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9148 | 601 | 1040 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8773 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7303 | 410 | 896 | 2575 | 328 | 2026-07-23 16:50:11 |
| [hug](https://github.com/hugapi/hug) | 6884 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 499 | 1265 | 875 | 534 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5332 | 1029 | 922 | 314 | 206 | 2026-07-23 11:26:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4276 | 355 | 1189 | 234 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4089 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3651 | 203 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2511 | 224 | 456 | 704 | 94 | 2026-07-23 06:49:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1579 | 358 | 2026-07-23 10:01:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1770 | 120 | 5237 | 273 | 721 | 2026-07-24 01:21:35 |
| [jython](https://github.com/jython/jython) | 1529 | 231 | 298 | 144 | 106 | 2026-07-19 06:34:16 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-24T03:30:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
