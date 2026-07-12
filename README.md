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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196317 | 75484 | 41594 | 77897 | 2678 | 2026-07-12 03:37:37 |
| [transformers](https://github.com/huggingface/transformers) | 162514 | 33869 | 19167 | 27372 | 2481 | 2026-07-12 00:55:33 |
| [pytorch](https://github.com/pytorch/pytorch) | 101759 | 28478 | 59742 | 129267 | 18286 | 2026-07-12 02:28:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 100390 | 9593 | 3540 | 6074 | 103 | 2026-07-10 17:54:44 |
| [django](https://github.com/django/django) | 88197 | 34162 | 0 | 21543 | 460 | 2026-07-10 22:01:58 |
| [cpython](https://github.com/python/cpython) | 73783 | 35000 | 77149 | 74118 | 9399 | 2026-07-11 22:26:16 |
| [flask](https://github.com/pallets/flask) | 71940 | 16908 | 2754 | 2863 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66693 | 27170 | 12173 | 21105 | 2101 | 2026-07-11 05:42:37 |
| [keras](https://github.com/keras-team/keras) | 64191 | 19751 | 12819 | 9567 | 228 | 2026-07-07 17:53:38 |
| [pandas](https://github.com/pandas-dev/pandas) | 49167 | 20123 | 28382 | 37810 | 3032 | 2026-07-11 23:32:23 |
| [ray](https://github.com/ray-project/ray) | 43210 | 7784 | 22834 | 41473 | 3469 | 2026-07-12 00:56:38 |
| [gym](https://github.com/openai/gym) | 37248 | 8693 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33735 | 4689 | 5764 | 4101 | 221 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32349 | 12564 | 13992 | 17890 | 2406 | 2026-07-10 23:35:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30092 | 7073 | 3967 | 5026 | 85 | 2026-07-08 20:30:28 |
| [celery](https://github.com/celery/celery) | 28679 | 5099 | 5287 | 4176 | 786 | 2026-07-09 14:31:55 |
| [dash](https://github.com/plotly/dash) | 24307 | 2306 | 2126 | 1644 | 543 | 2026-07-10 17:33:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22980 | 8385 | 11354 | 20619 | 1471 | 2026-07-11 04:57:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22189 | 5534 | 1876 | 1789 | 240 | 2026-07-08 17:05:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 22165 | 1458 | 1369 | 6814 | 391 | 2026-07-11 05:06:21 |
| [micropython](https://github.com/micropython/micropython) | 21887 | 8914 | 6095 | 7945 | 1619 | 2026-07-10 01:27:42 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18672 | 2824 | 3367 | 2118 | 773 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18630 | 1588 | 1468 | 1691 | 134 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16507 | 2346 | 3223 | 9555 | 242 | 2026-07-10 14:57:09 |
| [httpx](https://github.com/encode/httpx) | 15356 | 1200 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14809 | 5801 | 11521 | 14066 | 1852 | 2026-07-11 07:56:32 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13946 | 2121 | 2655 | 1200 | 217 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13855 | 1903 | 5540 | 6649 | 1261 | 2026-07-09 15:44:54 |
| [starlette](https://github.com/Kludex/starlette) | 12469 | 1225 | 771 | 1977 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11988 | 1711 | 8240 | 1138 | 205 | 2026-07-11 21:42:54 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11853 | 610 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9793 | 1013 | 1133 | 1477 | 170 | 2026-07-08 16:24:46 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9128 | 599 | 1039 | 520 | 216 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7291 | 408 | 895 | 2569 | 326 | 2026-07-12 00:29:14 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5602 | 497 | 1262 | 870 | 528 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1028 | 919 | 312 | 203 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4249 | 349 | 1187 | 229 | 121 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 312 | 674 | 1335 | 311 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2502 | 219 | 452 | 689 | 93 | 2026-07-11 23:32:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 914 | 1084 | 1563 | 359 | 2026-07-11 08:25:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 366 | 1785 | 268 | 266 | 2026-07-06 17:55:11 |
| [pypy](https://github.com/pypy/pypy) | 1762 | 118 | 5234 | 271 | 737 | 2026-07-12 03:29:18 |
| [jython](https://github.com/jython/jython) | 1523 | 232 | 298 | 138 | 106 | 2026-07-10 06:45:13 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-12T03:40:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
