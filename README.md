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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201315 | 78721 | 41924 | 84099 | 3436 | 2026-10-28 04:09:21 |
| [transformers](https://github.com/huggingface/transformers) | 168266 | 35013 | 19708 | 29547 | 1007 | 2026-10-28 04:30:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 105138 | 31823 | 62041 | 139605 | 17793 | 2026-10-28 05:12:05 |
| [fastapi](https://github.com/fastapi/fastapi) | 104203 | 10133 | 3556 | 6530 | 57 | 2026-10-27 04:56:28 |
| [django](https://github.com/django/django) | 91567 | 36511 | 0 | 22125 | 532 | 2026-10-28 01:29:44 |
| [cpython](https://github.com/python/cpython) | 77792 | 37650 | 78922 | 79341 | 9253 | 2026-10-28 04:15:21 |
| [flask](https://github.com/pallets/flask) | 74968 | 17172 | 2770 | 2912 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67970 | 27591 | 12350 | 21701 | 2162 | 2026-10-27 14:46:33 |
| [keras](https://github.com/keras-team/keras) | 64392 | 19807 | 13046 | 10167 | 269 | 2026-10-27 23:29:20 |
| [pandas](https://github.com/pandas-dev/pandas) | 50328 | 20640 | 28657 | 39726 | 2099 | 2026-10-27 22:13:49 |
| [ray](https://github.com/ray-project/ray) | 44140 | 8213 | 23260 | 43790 | 3644 | 2026-10-28 05:16:50 |
| [gym](https://github.com/openai/gym) | 37234 | 8664 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33998 | 4738 | 5781 | 4137 | 262 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33189 | 13014 | 14153 | 18907 | 2240 | 2026-10-28 01:20:00 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30218 | 7096 | 3966 | 5101 | 66 | 2026-10-27 19:13:44 |
| [celery](https://github.com/celery/celery) | 29088 | 5249 | 5355 | 4655 | 745 | 2026-10-28 05:03:00 |
| [dash](https://github.com/plotly/dash) | 24472 | 2332 | 2170 | 1795 | 434 | 2026-10-27 19:29:15 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23395 | 8531 | 11454 | 21025 | 1486 | 2026-10-23 19:17:21 |
| [RustPython](https://github.com/RustPython/RustPython) | 22427 | 1506 | 1446 | 7872 | 302 | 2026-10-28 01:11:59 |
| [tornado](https://github.com/tornadoweb/tornado) | 22165 | 5592 | 1888 | 1902 | 233 | 2026-10-26 21:18:33 |
| [micropython](https://github.com/micropython/micropython) | 22164 | 9014 | 6151 | 8162 | 1552 | 2026-10-28 05:12:49 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18857 | 2883 | 3399 | 2256 | 746 | 2026-10-23 23:43:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1615 | 1472 | 1687 | 160 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16594 | 2493 | 3269 | 10550 | 268 | 2026-10-28 03:21:58 |
| [httpx](https://github.com/encode/httpx) | 15702 | 3251 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15159 | 6037 | 11728 | 14780 | 1881 | 2026-10-28 05:05:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14088 | 2152 | 2667 | 1247 | 257 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13937 | 2006 | 5579 | 6792 | 1408 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12687 | 1416 | 794 | 2276 | 46 | 2026-10-24 17:17:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12267 | 1833 | 8366 | 1246 | 217 | 2026-10-27 22:56:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11917 | 621 | 428 | 345 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9809 | 1050 | 1148 | 1559 | 160 | 2026-10-24 19:47:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9223 | 621 | 1054 | 579 | 242 | 2026-10-26 15:23:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8801 | 1516 | 867 | 655 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7356 | 464 | 906 | 2653 | 344 | 2026-10-24 14:32:28 |
| [hug](https://github.com/hugapi/hug) | 6873 | 392 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5638 | 536 | 1300 | 970 | 555 | 2026-10-25 16:05:18 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5436 | 1052 | 938 | 328 | 207 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4458 | 391 | 1210 | 259 | 118 | 2026-10-22 03:25:05 |
| [pyramid](https://github.com/Pylons/pyramid) | 4103 | 896 | 1073 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3984 | 277 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3678 | 210 | 288 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 317 | 677 | 1381 | 265 | 2026-10-27 17:14:06 |
| [anyio](https://github.com/agronholm/anyio) | 2561 | 330 | 493 | 873 | 142 | 2026-10-26 22:05:41 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1606 | 355 | 2026-10-26 14:24:50 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 370 | 1791 | 277 | 278 | 2026-10-26 23:16:58 |
| [pypy](https://github.com/pypy/pypy) | 1821 | 130 | 5288 | 382 | 718 | 2026-10-27 17:14:38 |
| [jython](https://github.com/jython/jython) | 1551 | 231 | 305 | 155 | 101 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-28T05:19:21*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
