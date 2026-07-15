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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196359 | 75560 | 41600 | 78091 | 2705 | 2026-07-15 03:12:55 |
| [transformers](https://github.com/huggingface/transformers) | 162612 | 33880 | 19181 | 27414 | 2481 | 2026-07-15 03:08:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 101815 | 28493 | 59804 | 129536 | 18322 | 2026-07-15 03:16:48 |
| [fastapi](https://github.com/fastapi/fastapi) | 100516 | 9610 | 3540 | 6080 | 96 | 2026-07-14 18:45:13 |
| [django](https://github.com/django/django) | 88225 | 34176 | 0 | 21554 | 454 | 2026-07-14 20:38:32 |
| [cpython](https://github.com/python/cpython) | 73820 | 35008 | 77179 | 74211 | 9421 | 2026-07-15 03:06:24 |
| [flask](https://github.com/pallets/flask) | 71946 | 16905 | 2756 | 2865 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66679 | 27170 | 12177 | 21117 | 2108 | 2026-07-14 02:41:34 |
| [keras](https://github.com/keras-team/keras) | 64170 | 19739 | 12823 | 9570 | 220 | 2026-07-15 03:08:34 |
| [pandas](https://github.com/pandas-dev/pandas) | 49193 | 20119 | 28385 | 37841 | 2987 | 2026-07-15 02:58:59 |
| [ray](https://github.com/ray-project/ray) | 43247 | 7794 | 22843 | 41521 | 3467 | 2026-07-15 02:09:09 |
| [gym](https://github.com/openai/gym) | 37248 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33742 | 4691 | 5767 | 4102 | 225 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32367 | 12560 | 14000 | 17909 | 2402 | 2026-07-15 01:38:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30101 | 7075 | 3967 | 5026 | 84 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28685 | 5101 | 5287 | 4181 | 788 | 2026-07-15 01:25:43 |
| [dash](https://github.com/plotly/dash) | 24315 | 2306 | 2127 | 1646 | 541 | 2026-07-14 17:31:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22999 | 8392 | 11356 | 20622 | 1475 | 2026-07-15 02:52:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5540 | 1876 | 1796 | 246 | 2026-07-08 17:05:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 22189 | 1465 | 1372 | 6839 | 408 | 2026-07-13 14:11:23 |
| [micropython](https://github.com/micropython/micropython) | 21894 | 8902 | 6097 | 7950 | 1592 | 2026-07-15 03:04:38 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18678 | 2821 | 3368 | 2106 | 774 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1588 | 1467 | 1691 | 132 | 2026-07-12 07:17:35 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16504 | 2345 | 3222 | 9575 | 218 | 2026-07-14 14:09:03 |
| [httpx](https://github.com/encode/httpx) | 15355 | 1203 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14820 | 5804 | 11527 | 14077 | 1847 | 2026-07-14 12:11:53 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13957 | 2125 | 2656 | 1202 | 220 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13856 | 1905 | 5540 | 6654 | 1264 | 2026-07-14 13:22:10 |
| [starlette](https://github.com/Kludex/starlette) | 12474 | 1227 | 771 | 1975 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11990 | 1712 | 8243 | 1139 | 210 | 2026-07-12 22:57:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11856 | 610 | 416 | 324 | 153 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 1014 | 1134 | 1480 | 172 | 2026-07-13 14:45:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9134 | 601 | 1039 | 522 | 218 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1501 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7295 | 409 | 895 | 2571 | 327 | 2026-07-13 23:34:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5606 | 496 | 1263 | 871 | 529 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1028 | 920 | 312 | 203 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4258 | 349 | 1188 | 230 | 122 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 312 | 675 | 1335 | 312 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2504 | 219 | 453 | 693 | 92 | 2026-07-14 15:06:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 913 | 1084 | 1566 | 359 | 2026-07-14 13:49:41 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 266 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1763 | 118 | 5235 | 271 | 736 | 2026-07-14 06:33:40 |
| [jython](https://github.com/jython/jython) | 1524 | 231 | 298 | 139 | 103 | 2026-07-13 11:30:52 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-15T03:17:38*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
