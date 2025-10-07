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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191938 | 74902 | 40838 | 58882 | 1866 | 2025-10-07 01:50:34 |
| [transformers](https://github.com/huggingface/transformers) | 150692 | 30660 | 18017 | 22786 | 2028 | 2025-10-06 17:31:10 |
| [pytorch](https://github.com/pytorch/pytorch) | 93724 | 25488 | 54144 | 110200 | 16954 | 2025-10-07 01:48:22 |
| [fastapi](https://github.com/fastapi/fastapi) | 90432 | 8005 | 3470 | 4760 | 204 | 2025-10-06 19:08:45 |
| [django](https://github.com/django/django) | 85338 | 33061 | 0 | 19855 | 342 | 2025-10-03 21:12:58 |
| [flask](https://github.com/pallets/flask) | 70501 | 16551 | 2698 | 2705 | 9 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69165 | 33013 | 73799 | 64948 | 9317 | 2025-10-06 23:34:15 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63575 | 26300 | 11750 | 19532 | 2146 | 2025-10-07 00:53:23 |
| [keras](https://github.com/keras-team/keras) | 63455 | 19622 | 12562 | 8374 | 258 | 2025-10-06 16:19:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 46760 | 19090 | 27765 | 34789 | 3611 | 2025-10-06 22:13:38 |
| [ray](https://github.com/ray-project/ray) | 39208 | 6856 | 21290 | 35615 | 3170 | 2025-10-07 01:37:42 |
| [gym](https://github.com/openai/gym) | 36623 | 8705 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32592 | 4590 | 5722 | 4071 | 207 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30514 | 11519 | 13575 | 16248 | 2361 | 2025-10-06 11:07:07 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29536 | 7011 | 3945 | 4840 | 104 | 2025-09-25 12:59:12 |
| [celery](https://github.com/celery/celery) | 27298 | 4856 | 5169 | 3674 | 753 | 2025-10-06 16:54:19 |
| [dash](https://github.com/plotly/dash) | 24136 | 2209 | 2004 | 1347 | 574 | 2025-10-06 19:03:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22275 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21777 | 8058 | 11000 | 19595 | 1630 | 2025-10-06 19:03:07 |
| [micropython](https://github.com/micropython/micropython) | 20908 | 8464 | 5841 | 7252 | 1766 | 2025-10-06 04:13:46 |
| [RustPython](https://github.com/RustPython/RustPython) | 20574 | 1350 | 1221 | 4899 | 450 | 2025-10-06 13:41:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18504 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17808 | 2722 | 3259 | 1959 | 720 | 2025-10-03 19:12:17 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16025 | 2128 | 3146 | 8154 | 271 | 2025-10-07 01:34:18 |
| [httpx](https://github.com/encode/httpx) | 14603 | 958 | 918 | 1734 | 100 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14063 | 5492 | 11060 | 12662 | 1754 | 2025-10-06 13:13:40 |
| [dask](https://github.com/dask/dask) | 13515 | 1800 | 5440 | 6355 | 1198 | 2025-10-06 12:42:46 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13482 | 2037 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11519 | 1045 | 754 | 1717 | 47 | 2025-10-02 20:15:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11305 | 575 | 389 | 289 | 143 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10971 | 1584 | 8093 | 988 | 225 | 2025-10-03 19:08:54 |
| [falcon](https://github.com/falconry/falcon) | 9723 | 964 | 1103 | 1372 | 161 | 2025-09-20 19:45:11 |
| [bottle](https://github.com/bottlepy/bottle) | 8671 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8601 | 527 | 947 | 439 | 412 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6883 | 367 | 872 | 2458 | 311 | 2025-10-06 22:56:19 |
| [eve](https://github.com/pyeve/eve) | 6735 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5630 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5317 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5025 | 945 | 871 | 261 | 169 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3668 | 291 | 1162 | 196 | 117 | 2025-10-06 21:13:51 |
| [quart](https://github.com/pallets/quart) | 3478 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2690 | 303 | 651 | 1261 | 308 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2312 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2234 | 166 | 404 | 523 | 66 | 2025-10-06 18:05:50 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-10-06 17:57:17 |
| [pypy](https://github.com/pypy/pypy) | 1508 | 88 | 5149 | 171 | 737 | 2025-10-05 14:14:03 |
| [jython](https://github.com/jython/jython) | 1438 | 224 | 283 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-06 17:16:06 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-07T01:54:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
