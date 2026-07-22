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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196458 | 75652 | 41615 | 78537 | 2795 | 2026-07-22 03:28:22 |
| [transformers](https://github.com/huggingface/transformers) | 162817 | 33967 | 19212 | 27510 | 2437 | 2026-07-22 03:05:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 101842 | 28449 | 59955 | 130159 | 18279 | 2026-07-22 03:29:07 |
| [fastapi](https://github.com/fastapi/fastapi) | 100763 | 9655 | 3541 | 6100 | 86 | 2026-07-21 21:28:20 |
| [django](https://github.com/django/django) | 88212 | 34133 | 0 | 21574 | 450 | 2026-07-21 08:39:15 |
| [cpython](https://github.com/python/cpython) | 73879 | 34971 | 77333 | 74723 | 9460 | 2026-07-22 02:33:59 |
| [flask](https://github.com/pallets/flask) | 72012 | 16911 | 2756 | 2869 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66749 | 27200 | 12194 | 21153 | 2124 | 2026-07-21 20:22:26 |
| [keras](https://github.com/keras-team/keras) | 64174 | 19743 | 12847 | 9597 | 207 | 2026-07-22 01:39:36 |
| [pandas](https://github.com/pandas-dev/pandas) | 49285 | 20152 | 28409 | 37900 | 2901 | 2026-07-22 02:17:15 |
| [ray](https://github.com/ray-project/ray) | 43311 | 7813 | 22858 | 41666 | 3479 | 2026-07-22 02:03:38 |
| [gym](https://github.com/openai/gym) | 37241 | 8688 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33759 | 4696 | 5768 | 4105 | 229 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32406 | 12583 | 14009 | 17951 | 2375 | 2026-07-21 22:04:27 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30106 | 7078 | 3967 | 5030 | 88 | 2026-07-21 19:13:24 |
| [celery](https://github.com/celery/celery) | 28712 | 5110 | 5288 | 4185 | 785 | 2026-07-21 14:50:15 |
| [dash](https://github.com/plotly/dash) | 24339 | 2308 | 2130 | 1656 | 533 | 2026-07-22 02:19:11 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23026 | 8413 | 11368 | 20655 | 1487 | 2026-07-22 03:04:07 |
| [RustPython](https://github.com/RustPython/RustPython) | 22211 | 1464 | 1389 | 6882 | 399 | 2026-07-20 16:36:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5546 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21920 | 8915 | 6103 | 7973 | 1579 | 2026-07-22 00:30:22 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18684 | 2828 | 3372 | 2115 | 780 | 2026-07-20 16:37:01 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1589 | 1468 | 1694 | 134 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16504 | 2354 | 3225 | 9628 | 211 | 2026-07-21 21:59:24 |
| [httpx](https://github.com/encode/httpx) | 15362 | 1214 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14833 | 5811 | 11540 | 14112 | 1858 | 2026-07-22 00:50:30 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13972 | 2129 | 2656 | 1205 | 223 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13866 | 1913 | 5542 | 6662 | 1270 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12488 | 1234 | 771 | 1970 | 64 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12011 | 1721 | 8247 | 1145 | 203 | 2026-07-21 14:36:14 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11865 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9792 | 1021 | 1138 | 1489 | 169 | 2026-07-21 18:51:18 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9144 | 601 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8773 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7299 | 410 | 896 | 2574 | 328 | 2026-07-20 21:57:28 |
| [hug](https://github.com/hugapi/hug) | 6885 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5612 | 499 | 1264 | 875 | 533 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5328 | 1029 | 922 | 313 | 206 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4270 | 355 | 1189 | 234 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 204 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2511 | 223 | 456 | 703 | 95 | 2026-07-20 23:44:09 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 913 | 1084 | 1576 | 359 | 2026-07-21 09:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1767 | 119 | 5237 | 271 | 723 | 2026-07-21 19:13:37 |
| [jython](https://github.com/jython/jython) | 1530 | 231 | 298 | 143 | 105 | 2026-07-19 06:34:16 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-22T03:29:35*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
