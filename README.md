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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193609 | 75204 | 41144 | 66281 | 3120 | 2026-02-04 02:40:51 |
| [transformers](https://github.com/huggingface/transformers) | 156121 | 31941 | 18522 | 24598 | 2199 | 2026-02-03 23:33:20 |
| [pytorch](https://github.com/pytorch/pytorch) | 97140 | 26746 | 56663 | 117075 | 17996 | 2026-02-04 02:41:11 |
| [fastapi](https://github.com/fastapi/fastapi) | 94774 | 8623 | 3502 | 5202 | 224 | 2026-02-03 18:08:37 |
| [django](https://github.com/django/django) | 86673 | 33615 | 0 | 20572 | 402 | 2026-02-03 16:03:40 |
| [cpython](https://github.com/python/cpython) | 71343 | 34013 | 75167 | 68282 | 9221 | 2026-02-03 23:38:22 |
| [flask](https://github.com/pallets/flask) | 71137 | 16692 | 2713 | 2762 | 2 | 2026-02-03 18:22:23 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64890 | 26661 | 11911 | 20148 | 2123 | 2026-02-02 13:53:20 |
| [keras](https://github.com/keras-team/keras) | 63756 | 19686 | 12625 | 8687 | 258 | 2026-02-03 17:45:48 |
| [pandas](https://github.com/pandas-dev/pandas) | 47782 | 19603 | 28074 | 35876 | 3621 | 2026-02-04 02:24:45 |
| [ray](https://github.com/ray-project/ray) | 41127 | 7183 | 22278 | 38103 | 3349 | 2026-02-04 02:30:06 |
| [gym](https://github.com/openai/gym) | 37008 | 8711 | 1838 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33159 | 4636 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31377 | 12022 | 13772 | 16940 | 2292 | 2026-02-03 23:33:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29853 | 7063 | 3946 | 4912 | 89 | 2026-02-03 13:30:36 |
| [celery](https://github.com/celery/celery) | 27953 | 4937 | 5187 | 3780 | 764 | 2026-02-03 10:13:58 |
| [dash](https://github.com/plotly/dash) | 24442 | 2251 | 2052 | 1427 | 559 | 2026-02-03 19:47:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22437 | 5544 | 1863 | 1698 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22304 | 8179 | 11120 | 19905 | 1525 | 2026-02-03 10:10:36 |
| [RustPython](https://github.com/RustPython/RustPython) | 21750 | 1400 | 1295 | 5628 | 377 | 2026-02-04 01:35:46 |
| [micropython](https://github.com/micropython/micropython) | 21417 | 8693 | 5947 | 7531 | 1848 | 2026-02-03 02:26:46 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1583 | 1465 | 1663 | 115 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18235 | 2776 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16244 | 2185 | 3175 | 8540 | 276 | 2026-02-04 01:52:42 |
| [httpx](https://github.com/encode/httpx) | 14969 | 1028 | 925 | 1783 | 129 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14420 | 5607 | 11283 | 13204 | 1748 | 2026-02-03 20:48:11 |
| [dask](https://github.com/dask/dask) | 13727 | 1840 | 5503 | 6465 | 1223 | 2026-02-03 13:42:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13704 | 2079 | 2645 | 1157 | 204 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11894 | 1104 | 763 | 1781 | 51 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11626 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11456 | 1634 | 8149 | 1027 | 208 | 2026-02-04 00:03:46 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 978 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8880 | 556 | 1004 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8739 | 1491 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7141 | 381 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5472 | 453 | 1222 | 745 | 506 | 2026-02-03 19:53:01 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5176 | 1000 | 898 | 288 | 188 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3934 | 309 | 1181 | 208 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3588 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2724 | 308 | 657 | 1267 | 313 | 2026-02-03 05:21:34 |
| [anyio](https://github.com/agronholm/anyio) | 2374 | 178 | 423 | 565 | 76 | 2026-01-26 17:53:28 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1644 | 97 | 5172 | 178 | 756 | 2026-02-03 14:45:11 |
| [jython](https://github.com/jython/jython) | 1478 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-04T02:44:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
