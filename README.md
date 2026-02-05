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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193616 | 75212 | 41147 | 66374 | 3171 | 2026-02-05 02:31:20 |
| [transformers](https://github.com/huggingface/transformers) | 156156 | 31961 | 18527 | 24621 | 2201 | 2026-02-04 21:37:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 97163 | 26754 | 56688 | 117150 | 17999 | 2026-02-05 02:33:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 94809 | 8629 | 3502 | 5216 | 202 | 2026-02-04 18:14:58 |
| [django](https://github.com/django/django) | 86681 | 33623 | 0 | 20577 | 404 | 2026-02-03 16:03:40 |
| [cpython](https://github.com/python/cpython) | 71354 | 34021 | 75174 | 68304 | 9212 | 2026-02-04 20:27:41 |
| [flask](https://github.com/pallets/flask) | 71136 | 16694 | 2713 | 2762 | 2 | 2026-02-03 18:22:23 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64904 | 26668 | 11914 | 20150 | 2124 | 2026-02-04 15:30:27 |
| [keras](https://github.com/keras-team/keras) | 63755 | 19687 | 12625 | 8693 | 258 | 2026-02-04 21:10:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 47786 | 19612 | 28076 | 35888 | 3627 | 2026-02-04 20:50:40 |
| [ray](https://github.com/ray-project/ray) | 41144 | 7184 | 22282 | 38128 | 3349 | 2026-02-05 02:44:29 |
| [gym](https://github.com/openai/gym) | 37010 | 8710 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33163 | 4636 | 5739 | 4077 | 186 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31381 | 12021 | 13774 | 16941 | 2295 | 2026-02-03 23:33:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29854 | 7062 | 3946 | 4912 | 87 | 2026-02-05 00:02:21 |
| [celery](https://github.com/celery/celery) | 27963 | 4937 | 5187 | 3787 | 762 | 2026-02-04 15:34:09 |
| [dash](https://github.com/plotly/dash) | 24446 | 2251 | 2053 | 1428 | 558 | 2026-02-04 19:43:39 |
| [tornado](https://github.com/tornadoweb/tornado) | 22437 | 5544 | 1863 | 1698 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22308 | 8180 | 11123 | 19911 | 1526 | 2026-02-04 22:28:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 21751 | 1400 | 1295 | 5637 | 372 | 2026-02-05 01:20:48 |
| [micropython](https://github.com/micropython/micropython) | 21427 | 8694 | 5949 | 7536 | 1846 | 2026-02-05 00:48:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1583 | 1465 | 1663 | 115 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18236 | 2777 | 3320 | 2007 | 771 | 2026-01-26 21:41:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16247 | 2185 | 3176 | 8545 | 280 | 2026-02-04 19:16:42 |
| [httpx](https://github.com/encode/httpx) | 14971 | 1027 | 925 | 1783 | 129 | 2026-02-01 16:43:53 |
| [scipy](https://github.com/scipy/scipy) | 14424 | 5608 | 11288 | 13210 | 1759 | 2026-02-03 20:48:11 |
| [dask](https://github.com/dask/dask) | 13729 | 1840 | 5504 | 6472 | 1226 | 2026-02-04 18:57:14 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13703 | 2079 | 2645 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11894 | 1104 | 763 | 1781 | 50 | 2026-02-01 19:56:56 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11628 | 600 | 403 | 312 | 149 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11466 | 1633 | 8150 | 1028 | 208 | 2026-02-04 15:36:12 |
| [falcon](https://github.com/falconry/falcon) | 9789 | 978 | 1119 | 1411 | 162 | 2026-01-25 20:14:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8885 | 556 | 1005 | 482 | 204 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8740 | 1492 | 860 | 624 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7149 | 381 | 878 | 2495 | 316 | 2026-02-01 01:14:41 |
| [hug](https://github.com/hugapi/hug) | 6905 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 737 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5474 | 453 | 1222 | 746 | 506 | 2026-02-03 19:53:01 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5178 | 1001 | 898 | 288 | 188 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4021 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3939 | 310 | 1181 | 208 | 115 | 2026-01-31 11:25:41 |
| [quart](https://github.com/pallets/quart) | 3589 | 192 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2724 | 308 | 657 | 1267 | 313 | 2026-02-03 05:21:34 |
| [anyio](https://github.com/agronholm/anyio) | 2376 | 178 | 423 | 565 | 75 | 2026-02-04 20:13:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 910 | 1079 | 1462 | 369 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1932 | 367 | 1785 | 266 | 266 | 2026-01-26 17:46:31 |
| [pypy](https://github.com/pypy/pypy) | 1644 | 97 | 5173 | 179 | 757 | 2026-02-04 21:15:04 |
| [jython](https://github.com/jython/jython) | 1479 | 225 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-05T02:46:29*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
