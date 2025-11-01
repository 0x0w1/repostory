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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192282 | 74944 | 40892 | 60442 | 1890 | 2025-11-01 01:46:21 |
| [transformers](https://github.com/huggingface/transformers) | 151910 | 31006 | 18134 | 23239 | 2116 | 2025-10-31 20:11:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 94432 | 25729 | 54593 | 111704 | 17038 | 2025-11-01 01:49:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 91380 | 8146 | 3474 | 4825 | 204 | 2025-10-31 18:36:42 |
| [django](https://github.com/django/django) | 85611 | 33187 | 0 | 19968 | 355 | 2025-10-31 13:33:27 |
| [flask](https://github.com/pallets/flask) | 70696 | 16599 | 2701 | 2717 | 17 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69615 | 33268 | 74187 | 65741 | 9210 | 2025-11-01 00:39:48 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63880 | 26382 | 11789 | 19704 | 2145 | 2025-10-31 15:54:00 |
| [keras](https://github.com/keras-team/keras) | 63524 | 19640 | 12582 | 8436 | 267 | 2025-10-31 02:33:06 |
| [pandas](https://github.com/pandas-dev/pandas) | 46990 | 19210 | 27846 | 35046 | 3628 | 2025-10-31 22:16:23 |
| [ray](https://github.com/ray-project/ray) | 39623 | 6849 | 21752 | 36250 | 3181 | 2025-11-01 01:23:35 |
| [gym](https://github.com/openai/gym) | 36731 | 8716 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32744 | 4613 | 5729 | 4071 | 207 | 2025-10-28 08:43:48 |
| [numpy](https://github.com/numpy/numpy) | 30717 | 11646 | 13625 | 16434 | 2353 | 2025-10-31 16:18:40 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29626 | 7031 | 3946 | 4855 | 78 | 2025-10-30 18:02:25 |
| [celery](https://github.com/celery/celery) | 27458 | 4882 | 5174 | 3712 | 750 | 2025-10-31 22:09:12 |
| [dash](https://github.com/plotly/dash) | 24214 | 2225 | 2016 | 1357 | 579 | 2025-10-29 15:00:09 |
| [tornado](https://github.com/tornadoweb/tornado) | 22326 | 5539 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21909 | 8103 | 11027 | 19641 | 1623 | 2025-10-31 12:09:03 |
| [micropython](https://github.com/micropython/micropython) | 21007 | 8512 | 5863 | 7315 | 1786 | 2025-10-31 00:34:54 |
| [RustPython](https://github.com/RustPython/RustPython) | 20732 | 1356 | 1225 | 4942 | 443 | 2025-10-30 15:08:04 |
| [sanic](https://github.com/sanic-org/sanic) | 18542 | 1584 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17904 | 2737 | 3269 | 1970 | 730 | 2025-10-31 21:10:16 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16060 | 2149 | 3159 | 8279 | 262 | 2025-10-29 10:52:58 |
| [httpx](https://github.com/encode/httpx) | 14686 | 970 | 919 | 1752 | 107 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14142 | 5527 | 11107 | 12780 | 1793 | 2025-11-01 00:49:45 |
| [dask](https://github.com/dask/dask) | 13562 | 1815 | 5449 | 6379 | 1189 | 2025-10-31 14:44:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13527 | 2041 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11609 | 1064 | 757 | 1731 | 53 | 2025-10-28 17:34:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11381 | 583 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11073 | 1591 | 8111 | 996 | 217 | 2025-10-31 22:59:49 |
| [falcon](https://github.com/falconry/falcon) | 9747 | 971 | 1107 | 1388 | 167 | 2025-10-30 08:18:07 |
| [bottle](https://github.com/bottlepy/bottle) | 8683 | 1490 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8673 | 531 | 964 | 449 | 176 | 2025-10-23 07:16:59 |
| [trio](https://github.com/python-trio/trio) | 6925 | 372 | 872 | 2465 | 311 | 2025-11-01 01:15:59 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5628 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5354 | 442 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5061 | 958 | 875 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4059 | 887 | 1061 | 2721 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3725 | 297 | 1164 | 198 | 116 | 2025-10-29 16:54:22 |
| [quart](https://github.com/pallets/quart) | 3511 | 191 | 277 | 124 | 64 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2701 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2316 | 133 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2270 | 172 | 411 | 537 | 71 | 2025-10-28 10:34:28 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 911 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 371 | 1781 | 264 | 261 | 2025-10-27 17:37:16 |
| [pypy](https://github.com/pypy/pypy) | 1555 | 87 | 5154 | 171 | 741 | 2025-10-28 13:51:47 |
| [jython](https://github.com/jython/jython) | 1449 | 225 | 283 | 114 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 83 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-11-01T02:06:16*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
