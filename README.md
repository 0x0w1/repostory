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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191178 | 74767 | 40719 | 56214 | 1522 | 2025-08-15 02:06:06 |
| [transformers](https://github.com/huggingface/transformers) | 148325 | 30026 | 17768 | 21843 | 1962 | 2025-08-14 21:41:01 |
| [pytorch](https://github.com/pytorch/pytorch) | 92368 | 24958 | 53093 | 107155 | 16788 | 2025-08-15 02:11:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 88386 | 7727 | 3466 | 4659 | 296 | 2025-08-12 16:49:35 |
| [django](https://github.com/django/django) | 84582 | 32822 | 0 | 19664 | 354 | 2025-08-15 00:53:14 |
| [flask](https://github.com/pallets/flask) | 70173 | 16522 | 2692 | 2686 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68364 | 32577 | 73276 | 63587 | 9291 | 2025-08-14 21:26:03 |
| [keras](https://github.com/keras-team/keras) | 63328 | 19612 | 12523 | 8277 | 295 | 2025-08-14 20:13:00 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63029 | 26134 | 11645 | 19180 | 2156 | 2025-08-14 08:52:01 |
| [pandas](https://github.com/pandas-dev/pandas) | 46292 | 18784 | 27651 | 34410 | 3690 | 2025-08-14 22:39:01 |
| [ray](https://github.com/ray-project/ray) | 38470 | 6704 | 20881 | 34407 | 2981 | 2025-08-15 01:59:54 |
| [gym](https://github.com/openai/gym) | 36377 | 8687 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32176 | 4561 | 5715 | 4064 | 196 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30150 | 11199 | 13485 | 16014 | 2341 | 2025-08-14 22:07:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29372 | 6995 | 3945 | 4825 | 98 | 2025-08-13 04:53:25 |
| [celery](https://github.com/celery/celery) | 27000 | 4824 | 5155 | 3638 | 758 | 2025-08-12 11:22:23 |
| [dash](https://github.com/plotly/dash) | 23933 | 2189 | 1973 | 1311 | 546 | 2025-08-13 21:59:01 |
| [tornado](https://github.com/tornadoweb/tornado) | 22097 | 5537 | 1851 | 1670 | 206 | 2025-08-12 13:28:52 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21553 | 7957 | 10941 | 19450 | 1655 | 2025-08-14 21:06:34 |
| [micropython](https://github.com/micropython/micropython) | 20723 | 8358 | 5779 | 7106 | 1769 | 2025-08-15 01:48:32 |
| [RustPython](https://github.com/RustPython/RustPython) | 20406 | 1339 | 1207 | 4822 | 442 | 2025-08-11 21:28:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18467 | 1578 | 1449 | 1625 | 143 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17596 | 2699 | 3239 | 1944 | 719 | 2025-08-14 15:14:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15911 | 2111 | 3142 | 7992 | 262 | 2025-08-14 11:28:18 |
| [httpx](https://github.com/encode/httpx) | 14462 | 941 | 913 | 1705 | 99 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13917 | 5440 | 10969 | 12480 | 1757 | 2025-08-11 12:56:38 |
| [dask](https://github.com/dask/dask) | 13406 | 1792 | 5421 | 6333 | 1191 | 2025-08-12 06:36:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13365 | 2027 | 2621 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11345 | 1029 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11138 | 569 | 387 | 287 | 140 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10776 | 1573 | 8066 | 975 | 237 | 2025-08-14 14:48:11 |
| [falcon](https://github.com/falconry/falcon) | 9703 | 959 | 1093 | 1358 | 161 | 2025-08-14 14:40:39 |
| [bottle](https://github.com/bottlepy/bottle) | 8646 | 1487 | 854 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8450 | 518 | 936 | 429 | 403 | 2025-08-11 21:00:03 |
| [hug](https://github.com/hugapi/hug) | 6893 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6727 | 746 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6697 | 362 | 863 | 2441 | 312 | 2025-08-12 16:35:03 |
| [vibora](https://github.com/vibora-io/vibora) | 5635 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5242 | 435 | 1183 | 708 | 492 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4939 | 924 | 861 | 258 | 157 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4041 | 891 | 1060 | 2715 | 85 | 2025-08-12 15:14:59 |
| [databases](https://github.com/encode/databases) | 3935 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3523 | 288 | 1152 | 194 | 116 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3394 | 185 | 277 | 121 | 62 | 2025-08-14 14:23:09 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2675 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2297 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2174 | 163 | 399 | 498 | 68 | 2025-08-13 13:44:30 |
| [web2py](https://github.com/web2py/web2py) | 2151 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1921 | 369 | 1779 | 264 | 260 | 2025-08-11 17:55:35 |
| [pypy](https://github.com/pypy/pypy) | 1469 | 83 | 5139 | 168 | 733 | 2025-08-14 05:35:41 |
| [jython](https://github.com/jython/jython) | 1420 | 216 | 279 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-15T02:11:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
