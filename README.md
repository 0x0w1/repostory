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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193674 | 75222 | 41151 | 66780 | 3380 | 2026-02-10 03:15:43 |
| [transformers](https://github.com/huggingface/transformers) | 156288 | 32015 | 18555 | 24716 | 2221 | 2026-02-10 03:08:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 97279 | 26799 | 56738 | 117400 | 18015 | 2026-02-10 03:19:13 |
| [fastapi](https://github.com/fastapi/fastapi) | 94953 | 8663 | 3502 | 5263 | 165 | 2026-02-09 17:39:12 |
| [django](https://github.com/django/django) | 86717 | 33638 | 0 | 20597 | 408 | 2026-02-09 22:46:33 |
| [cpython](https://github.com/python/cpython) | 71435 | 34047 | 75207 | 68439 | 9203 | 2026-02-10 03:04:52 |
| [flask](https://github.com/pallets/flask) | 71146 | 16701 | 2714 | 2766 | 2 | 2026-02-06 21:23:01 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64969 | 26670 | 11930 | 20181 | 2129 | 2026-02-09 09:24:55 |
| [keras](https://github.com/keras-team/keras) | 63759 | 19687 | 12629 | 8718 | 272 | 2026-02-10 00:16:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 47845 | 19635 | 28088 | 35948 | 3642 | 2026-02-09 23:34:36 |
| [ray](https://github.com/ray-project/ray) | 41195 | 7198 | 22298 | 38254 | 3363 | 2026-02-10 03:05:38 |
| [gym](https://github.com/openai/gym) | 37028 | 8711 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33182 | 4640 | 5739 | 4078 | 187 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31404 | 12035 | 13785 | 16962 | 2314 | 2026-02-09 13:25:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29866 | 7066 | 3946 | 4920 | 90 | 2026-02-07 13:26:13 |
| [celery](https://github.com/celery/celery) | 27990 | 4943 | 5191 | 3791 | 770 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24464 | 2254 | 2053 | 1431 | 559 | 2026-02-07 17:40:21 |
| [tornado](https://github.com/tornadoweb/tornado) | 22444 | 5546 | 1863 | 1699 | 214 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22316 | 8181 | 11140 | 19939 | 1532 | 2026-02-09 22:27:05 |
| [RustPython](https://github.com/RustPython/RustPython) | 21772 | 1400 | 1297 | 5703 | 371 | 2026-02-09 15:50:54 |
| [micropython](https://github.com/micropython/micropython) | 21449 | 8698 | 5951 | 7547 | 1842 | 2026-02-07 08:00:48 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1584 | 1465 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18241 | 2774 | 3321 | 2025 | 775 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16257 | 2188 | 3176 | 8562 | 286 | 2026-02-09 12:25:07 |
| [httpx](https://github.com/encode/httpx) | 14973 | 1029 | 925 | 1788 | 134 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14439 | 5613 | 11296 | 13237 | 1766 | 2026-02-10 02:33:47 |
| [dask](https://github.com/dask/dask) | 13736 | 1842 | 5504 | 6486 | 1224 | 2026-02-05 22:04:22 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13716 | 2079 | 2646 | 1160 | 204 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11904 | 1116 | 763 | 1785 | 54 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11638 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11484 | 1636 | 8152 | 1028 | 206 | 2026-02-09 14:28:51 |
| [falcon](https://github.com/falconry/falcon) | 9799 | 979 | 1119 | 1413 | 163 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8891 | 556 | 1005 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8747 | 1493 | 860 | 628 | 282 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7161 | 383 | 878 | 2496 | 316 | 2026-02-10 01:04:58 |
| [hug](https://github.com/hugapi/hug) | 6906 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5487 | 456 | 1224 | 763 | 486 | 2026-02-09 07:34:49 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5183 | 999 | 901 | 289 | 191 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3948 | 310 | 1181 | 209 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3593 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2725 | 308 | 658 | 1270 | 313 | 2026-02-08 01:14:02 |
| [anyio](https://github.com/agronholm/anyio) | 2381 | 180 | 423 | 569 | 74 | 2026-02-09 18:37:13 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 909 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1934 | 367 | 1785 | 266 | 266 | 2026-02-09 18:28:59 |
| [pypy](https://github.com/pypy/pypy) | 1649 | 98 | 5175 | 179 | 757 | 2026-02-09 08:46:09 |
| [jython](https://github.com/jython/jython) | 1479 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-10T03:19:28*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
