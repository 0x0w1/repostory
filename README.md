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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196313 | 75510 | 41609 | 78248 | 2690 | 2026-07-17 03:21:50 |
| [transformers](https://github.com/huggingface/transformers) | 162668 | 33900 | 19190 | 27458 | 2481 | 2026-07-17 02:31:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 101716 | 28421 | 59885 | 129781 | 18364 | 2026-07-17 03:26:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 100587 | 9631 | 3541 | 6105 | 94 | 2026-07-16 20:17:03 |
| [django](https://github.com/django/django) | 88140 | 34081 | 0 | 21561 | 454 | 2026-07-16 20:15:59 |
| [cpython](https://github.com/python/cpython) | 73778 | 34918 | 77204 | 74273 | 9443 | 2026-07-17 02:52:52 |
| [flask](https://github.com/pallets/flask) | 71963 | 16903 | 2756 | 2867 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66704 | 27182 | 12180 | 21129 | 2113 | 2026-07-16 07:46:28 |
| [keras](https://github.com/keras-team/keras) | 64169 | 19741 | 12826 | 9580 | 211 | 2026-07-16 20:38:43 |
| [pandas](https://github.com/pandas-dev/pandas) | 49209 | 20134 | 28390 | 37856 | 2984 | 2026-07-17 00:48:52 |
| [ray](https://github.com/ray-project/ray) | 43257 | 7799 | 22849 | 41582 | 3468 | 2026-07-17 03:23:21 |
| [gym](https://github.com/openai/gym) | 37245 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33746 | 4692 | 5767 | 4102 | 225 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32383 | 12565 | 14004 | 17932 | 2371 | 2026-07-16 21:03:52 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30101 | 7074 | 3967 | 5027 | 85 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28697 | 5105 | 5288 | 4184 | 782 | 2026-07-16 06:44:39 |
| [dash](https://github.com/plotly/dash) | 24322 | 2308 | 2129 | 1646 | 539 | 2026-07-15 18:26:57 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23009 | 8396 | 11357 | 20631 | 1471 | 2026-07-16 19:40:57 |
| [RustPython](https://github.com/RustPython/RustPython) | 22198 | 1465 | 1374 | 6850 | 386 | 2026-07-17 02:51:36 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5540 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21902 | 8908 | 6099 | 7959 | 1596 | 2026-07-17 03:21:39 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18682 | 2823 | 3369 | 2109 | 773 | 2026-07-16 19:56:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1587 | 1467 | 1692 | 133 | 2026-07-15 18:25:33 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16499 | 2347 | 3223 | 9585 | 223 | 2026-07-16 11:25:09 |
| [httpx](https://github.com/encode/httpx) | 15353 | 1206 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14825 | 5805 | 11532 | 14087 | 1840 | 2026-07-16 19:12:26 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13962 | 2127 | 2656 | 1203 | 221 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13860 | 1905 | 5541 | 6655 | 1265 | 2026-07-14 13:22:10 |
| [starlette](https://github.com/Kludex/starlette) | 12483 | 1230 | 771 | 1978 | 62 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12000 | 1715 | 8243 | 1142 | 206 | 2026-07-16 12:43:13 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11861 | 611 | 417 | 325 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9789 | 1014 | 1135 | 1481 | 172 | 2026-07-16 16:56:59 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9137 | 602 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1501 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7297 | 408 | 896 | 2573 | 327 | 2026-07-16 04:09:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5608 | 499 | 1263 | 875 | 532 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1028 | 921 | 312 | 204 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4262 | 351 | 1189 | 233 | 125 | 2026-07-16 17:14:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2506 | 222 | 453 | 697 | 96 | 2026-07-16 21:48:33 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 913 | 1084 | 1569 | 359 | 2026-07-16 11:37:11 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 266 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1765 | 118 | 5237 | 271 | 732 | 2026-07-15 17:57:42 |
| [jython](https://github.com/jython/jython) | 1526 | 231 | 298 | 139 | 103 | 2026-07-13 11:30:52 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-17T03:27:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
