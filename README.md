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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194861 | 75279 | 41328 | 72084 | 4708 | 2026-04-25 03:22:32 |
| [transformers](https://github.com/huggingface/transformers) | 159891 | 33004 | 18894 | 26099 | 2355 | 2026-04-25 02:13:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 99423 | 27588 | 58237 | 122705 | 18571 | 2026-04-25 03:22:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 97621 | 9150 | 3522 | 5659 | 171 | 2026-04-24 13:06:37 |
| [django](https://github.com/django/django) | 87323 | 33830 | 0 | 21103 | 433 | 2026-04-24 18:19:15 |
| [cpython](https://github.com/python/cpython) | 72443 | 34486 | 76097 | 70585 | 9419 | 2026-04-24 20:38:15 |
| [flask](https://github.com/pallets/flask) | 71447 | 16813 | 2735 | 2812 | 3 | 2026-04-09 04:04:09 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65915 | 26974 | 12052 | 20632 | 2044 | 2026-04-25 01:03:15 |
| [keras](https://github.com/keras-team/keras) | 64036 | 19763 | 12739 | 9233 | 260 | 2026-04-24 23:01:02 |
| [pandas](https://github.com/pandas-dev/pandas) | 48565 | 19876 | 28256 | 37028 | 3418 | 2026-04-25 02:49:46 |
| [ray](https://github.com/ray-project/ray) | 42295 | 7501 | 22607 | 39967 | 3578 | 2026-04-25 02:37:32 |
| [gym](https://github.com/openai/gym) | 37174 | 8706 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33506 | 4676 | 5755 | 4091 | 203 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31888 | 12315 | 13890 | 17363 | 2370 | 2026-04-24 18:40:44 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29990 | 7067 | 3968 | 5002 | 80 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28405 | 5019 | 5271 | 4088 | 775 | 2026-04-23 22:23:41 |
| [dash](https://github.com/plotly/dash) | 24149 | 2277 | 2091 | 1543 | 542 | 2026-04-24 20:51:14 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22732 | 8324 | 11248 | 20261 | 1492 | 2026-04-24 22:51:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22221 | 5542 | 1870 | 1728 | 217 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 22025 | 1429 | 1335 | 6272 | 374 | 2026-04-24 21:30:05 |
| [micropython](https://github.com/micropython/micropython) | 21654 | 8806 | 6039 | 7751 | 1884 | 2026-04-20 13:16:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1588 | 1465 | 1683 | 133 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18476 | 2803 | 3340 | 2078 | 763 | 2026-04-21 22:32:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16417 | 2260 | 3191 | 8903 | 281 | 2026-04-24 10:57:52 |
| [httpx](https://github.com/encode/httpx) | 15230 | 1128 | 0 | 1805 | 148 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14634 | 5709 | 11424 | 13625 | 1790 | 2026-04-23 07:15:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13827 | 2103 | 2652 | 1172 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13806 | 1867 | 5522 | 6532 | 1247 | 2026-04-22 10:20:36 |
| [starlette](https://github.com/Kludex/starlette) | 12235 | 1160 | 766 | 1880 | 56 | 2026-04-21 07:48:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11794 | 1676 | 8199 | 1064 | 217 | 2026-04-24 21:39:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11770 | 605 | 413 | 323 | 167 | 2026-01-30 14:24:05 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 988 | 1122 | 1434 | 154 | 2026-04-23 18:19:06 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9027 | 572 | 1032 | 506 | 203 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8753 | 1497 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7247 | 393 | 890 | 2536 | 320 | 2026-04-20 22:28:04 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6735 | 734 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5600 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5558 | 480 | 1249 | 824 | 509 | 2026-04-20 14:18:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5244 | 1008 | 911 | 291 | 201 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4092 | 330 | 1183 | 218 | 113 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4080 | 894 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4007 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3626 | 195 | 282 | 126 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2738 | 311 | 663 | 1308 | 305 | 2026-04-12 01:50:37 |
| [anyio](https://github.com/agronholm/anyio) | 2444 | 200 | 435 | 616 | 85 | 2026-04-24 10:56:29 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 905 | 1083 | 1477 | 364 | 2026-04-24 15:15:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 267 | 267 | 2026-04-20 17:39:29 |
| [pypy](https://github.com/pypy/pypy) | 1713 | 112 | 5200 | 226 | 746 | 2026-04-24 13:37:55 |
| [jython](https://github.com/jython/jython) | 1501 | 228 | 294 | 127 | 112 | 2026-04-18 11:58:26 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 192 | 41 | 2026-04-25 01:52:47 |

*Last Automatic Update: 2026-04-25T03:23:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
