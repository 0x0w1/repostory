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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193273 | 75144 | 41064 | 64784 | 2733 | 2026-01-10 02:02:35 |
| [transformers](https://github.com/huggingface/transformers) | 154812 | 31668 | 18406 | 24195 | 2165 | 2026-01-09 21:46:46 |
| [pytorch](https://github.com/pytorch/pytorch) | 96474 | 26470 | 56234 | 115418 | 17905 | 2026-01-10 01:55:44 |
| [fastapi](https://github.com/fastapi/fastapi) | 93909 | 8498 | 3500 | 5094 | 221 | 2026-01-09 15:51:29 |
| [django](https://github.com/django/django) | 86416 | 33451 | 0 | 20455 | 382 | 2026-01-09 20:55:46 |
| [flask](https://github.com/pallets/flask) | 71031 | 16666 | 2708 | 2747 | 12 | 2026-01-05 16:50:56 |
| [cpython](https://github.com/python/cpython) | 71001 | 33859 | 74929 | 67716 | 9225 | 2026-01-09 23:18:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64570 | 26585 | 11878 | 20017 | 2110 | 2026-01-09 13:17:58 |
| [keras](https://github.com/keras-team/keras) | 63691 | 19670 | 12608 | 8591 | 240 | 2026-01-09 23:51:42 |
| [pandas](https://github.com/pandas-dev/pandas) | 47516 | 19490 | 28006 | 35555 | 3600 | 2026-01-09 17:57:53 |
| [ray](https://github.com/ray-project/ray) | 40694 | 7090 | 22130 | 37539 | 3269 | 2026-01-10 01:41:48 |
| [gym](https://github.com/openai/gym) | 36944 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33053 | 4632 | 5736 | 4077 | 185 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31184 | 11936 | 13737 | 16823 | 2335 | 2026-01-10 00:37:39 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29797 | 7049 | 3946 | 4897 | 82 | 2026-01-05 14:49:58 |
| [celery](https://github.com/celery/celery) | 27847 | 4926 | 5180 | 3764 | 760 | 2026-01-06 22:10:42 |
| [dash](https://github.com/plotly/dash) | 24392 | 2247 | 2040 | 1407 | 559 | 2026-01-08 15:55:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22413 | 5545 | 1862 | 1691 | 210 | 2026-01-08 06:35:07 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22198 | 8170 | 11100 | 19802 | 1538 | 2026-01-09 14:50:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 21631 | 1400 | 1277 | 5342 | 365 | 2026-01-10 01:27:47 |
| [micropython](https://github.com/micropython/micropython) | 21318 | 8638 | 5934 | 7472 | 1829 | 2026-01-09 04:23:13 |
| [sanic](https://github.com/sanic-org/sanic) | 18610 | 1585 | 1460 | 1662 | 110 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18162 | 2771 | 3313 | 1998 | 764 | 2026-01-09 17:00:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16193 | 2171 | 3171 | 8470 | 272 | 2026-01-09 20:38:06 |
| [httpx](https://github.com/encode/httpx) | 14887 | 1004 | 925 | 1776 | 124 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14328 | 5581 | 11233 | 13067 | 1751 | 2026-01-10 01:17:08 |
| [dask](https://github.com/dask/dask) | 13697 | 1834 | 5482 | 6445 | 1207 | 2026-01-08 16:18:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13667 | 2077 | 2644 | 1155 | 202 | 2025-12-24 15:21:17 |
| [starlette](https://github.com/Kludex/starlette) | 11827 | 1096 | 761 | 1758 | 54 | 2026-01-02 08:04:08 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11570 | 598 | 400 | 302 | 155 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11368 | 1618 | 8138 | 1019 | 209 | 2026-01-09 14:19:52 |
| [falcon](https://github.com/falconry/falcon) | 9777 | 975 | 1115 | 1405 | 163 | 2025-12-29 15:48:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8835 | 555 | 991 | 479 | 196 | 2026-01-04 16:26:13 |
| [bottle](https://github.com/bottlepy/bottle) | 8726 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7093 | 378 | 877 | 2486 | 312 | 2026-01-05 22:28:33 |
| [hug](https://github.com/hugapi/hug) | 6907 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5619 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5440 | 445 | 1215 | 735 | 512 | 2025-12-30 04:12:30 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5142 | 983 | 884 | 279 | 180 | 2026-01-07 13:28:38 |
| [pyramid](https://github.com/Pylons/pyramid) | 4073 | 888 | 1062 | 2723 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4024 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3877 | 305 | 1173 | 207 | 117 | 2026-01-09 21:22:57 |
| [quart](https://github.com/pallets/quart) | 3573 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2723 | 307 | 654 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 427 | 393 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2350 | 180 | 421 | 562 | 73 | 2026-01-06 11:46:43 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1078 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1930 | 368 | 1784 | 266 | 265 | 2025-12-22 17:40:03 |
| [pypy](https://github.com/pypy/pypy) | 1624 | 94 | 5169 | 174 | 755 | 2026-01-08 21:11:28 |
| [jython](https://github.com/jython/jython) | 1468 | 225 | 289 | 120 | 106 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2025-12-08 17:09:01 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-10T02:12:20*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
