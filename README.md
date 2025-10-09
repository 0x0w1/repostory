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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191955 | 74902 | 40839 | 59032 | 1875 | 2025-10-09 01:49:56 |
| [transformers](https://github.com/huggingface/transformers) | 150773 | 30688 | 18024 | 22843 | 2050 | 2025-10-08 18:13:23 |
| [pytorch](https://github.com/pytorch/pytorch) | 93763 | 25501 | 54181 | 110370 | 16981 | 2025-10-09 01:55:01 |
| [fastapi](https://github.com/fastapi/fastapi) | 90508 | 8013 | 3470 | 4766 | 199 | 2025-10-08 20:57:19 |
| [django](https://github.com/django/django) | 85349 | 33066 | 0 | 19867 | 346 | 2025-10-08 21:33:13 |
| [flask](https://github.com/pallets/flask) | 70512 | 16551 | 2699 | 2706 | 10 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69220 | 33040 | 73836 | 65048 | 9149 | 2025-10-08 23:24:30 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63594 | 26307 | 11753 | 19562 | 2134 | 2025-10-08 16:38:18 |
| [keras](https://github.com/keras-team/keras) | 63459 | 19625 | 12562 | 8379 | 258 | 2025-10-08 08:34:47 |
| [pandas](https://github.com/pandas-dev/pandas) | 46770 | 19097 | 27769 | 34811 | 3618 | 2025-10-07 22:51:26 |
| [ray](https://github.com/ray-project/ray) | 39239 | 6862 | 21541 | 35695 | 3194 | 2025-10-09 00:36:49 |
| [gym](https://github.com/openai/gym) | 36640 | 8706 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32606 | 4591 | 5723 | 4071 | 208 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30533 | 11528 | 13580 | 16259 | 2367 | 2025-10-09 01:02:14 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29542 | 7012 | 3945 | 4843 | 106 | 2025-10-08 12:47:05 |
| [celery](https://github.com/celery/celery) | 27304 | 4856 | 5171 | 3675 | 755 | 2025-10-08 04:57:58 |
| [dash](https://github.com/plotly/dash) | 24141 | 2212 | 2006 | 1348 | 575 | 2025-10-08 21:30:16 |
| [tornado](https://github.com/tornadoweb/tornado) | 22287 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21788 | 8060 | 11002 | 19596 | 1630 | 2025-10-08 23:01:10 |
| [micropython](https://github.com/micropython/micropython) | 20921 | 8465 | 5843 | 7259 | 1770 | 2025-10-08 23:40:14 |
| [RustPython](https://github.com/RustPython/RustPython) | 20582 | 1350 | 1221 | 4900 | 451 | 2025-10-06 13:41:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18508 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17812 | 2722 | 3260 | 1962 | 721 | 2025-10-08 17:44:09 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16026 | 2130 | 3149 | 8165 | 269 | 2025-10-08 18:37:46 |
| [httpx](https://github.com/encode/httpx) | 14610 | 959 | 919 | 1740 | 101 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14068 | 5493 | 11061 | 12666 | 1756 | 2025-10-07 04:13:50 |
| [dask](https://github.com/dask/dask) | 13517 | 1801 | 5441 | 6357 | 1194 | 2025-10-08 10:44:23 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13484 | 2037 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11528 | 1044 | 754 | 1717 | 47 | 2025-10-02 20:15:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11312 | 577 | 390 | 289 | 143 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10981 | 1584 | 8096 | 988 | 222 | 2025-10-08 16:22:24 |
| [falcon](https://github.com/falconry/falcon) | 9727 | 966 | 1105 | 1376 | 165 | 2025-10-08 07:26:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8670 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8607 | 527 | 949 | 440 | 415 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6896 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6887 | 368 | 872 | 2458 | 311 | 2025-10-06 22:56:19 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5629 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5319 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5028 | 945 | 871 | 261 | 168 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3931 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3670 | 291 | 1162 | 196 | 117 | 2025-10-07 02:53:39 |
| [quart](https://github.com/pallets/quart) | 3484 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2691 | 303 | 652 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2312 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2239 | 166 | 405 | 524 | 67 | 2025-10-08 12:15:25 |
| [web2py](https://github.com/web2py/web2py) | 2165 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-10-06 17:57:17 |
| [pypy](https://github.com/pypy/pypy) | 1511 | 88 | 5149 | 171 | 737 | 2025-10-08 06:58:26 |
| [jython](https://github.com/jython/jython) | 1439 | 224 | 283 | 113 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-06 17:16:06 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-09T01:55:40*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
