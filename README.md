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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197049 | 76059 | 41699 | 80322 | 3014 | 2026-08-19 01:43:06 |
| [transformers](https://github.com/huggingface/transformers) | 164229 | 34270 | 19327 | 28003 | 2367 | 2026-08-18 23:32:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 102468 | 28911 | 60422 | 132941 | 17115 | 2026-08-19 01:37:39 |
| [fastapi](https://github.com/fastapi/fastapi) | 101681 | 9793 | 3544 | 6247 | 86 | 2026-08-18 19:46:42 |
| [django](https://github.com/django/django) | 88476 | 34144 | 0 | 21682 | 456 | 2026-08-18 18:09:39 |
| [cpython](https://github.com/python/cpython) | 74405 | 35234 | 77722 | 75961 | 9540 | 2026-08-18 22:01:36 |
| [flask](https://github.com/pallets/flask) | 72140 | 16935 | 2762 | 2893 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66972 | 27292 | 12245 | 21340 | 2127 | 2026-08-18 13:49:34 |
| [keras](https://github.com/keras-team/keras) | 64239 | 19750 | 12874 | 9716 | 227 | 2026-08-18 18:47:41 |
| [pandas](https://github.com/pandas-dev/pandas) | 49516 | 20277 | 28479 | 38241 | 2798 | 2026-08-19 00:11:06 |
| [ray](https://github.com/ray-project/ray) | 43547 | 7934 | 22961 | 42210 | 3520 | 2026-08-19 01:36:19 |
| [gym](https://github.com/openai/gym) | 37240 | 8687 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33827 | 4710 | 5770 | 4114 | 236 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32552 | 12646 | 14053 | 18190 | 2331 | 2026-08-18 23:41:48 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30131 | 7075 | 3966 | 5045 | 56 | 2026-08-18 15:15:53 |
| [celery](https://github.com/celery/celery) | 28792 | 5137 | 5296 | 4248 | 802 | 2026-08-18 15:56:43 |
| [dash](https://github.com/plotly/dash) | 24374 | 2316 | 2143 | 1683 | 539 | 2026-08-18 20:52:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23088 | 8445 | 11400 | 20760 | 1481 | 2026-08-16 07:40:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 22290 | 1473 | 1422 | 7056 | 405 | 2026-08-18 15:30:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5552 | 1878 | 1807 | 252 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21992 | 8931 | 6118 | 8056 | 1533 | 2026-08-18 14:36:09 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18746 | 2833 | 3378 | 2139 | 779 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18642 | 1597 | 1471 | 1703 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16527 | 2379 | 3239 | 9898 | 245 | 2026-08-19 01:30:53 |
| [httpx](https://github.com/encode/httpx) | 15429 | 1248 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14935 | 5867 | 11597 | 14334 | 1850 | 2026-08-19 01:14:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14000 | 2128 | 2659 | 1214 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13891 | 1931 | 5549 | 6700 | 1308 | 2026-08-17 14:33:18 |
| [starlette](https://github.com/Kludex/starlette) | 12549 | 1262 | 773 | 2030 | 65 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12092 | 1755 | 8273 | 1185 | 214 | 2026-08-18 22:24:47 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11885 | 611 | 417 | 327 | 154 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1027 | 1139 | 1500 | 160 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9164 | 610 | 1042 | 538 | 227 | 2026-08-17 17:39:58 |
| [bottle](https://github.com/bottlepy/bottle) | 8775 | 1502 | 865 | 644 | 288 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7303 | 415 | 899 | 2590 | 322 | 2026-08-18 00:29:06 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5608 | 500 | 1265 | 887 | 540 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5586 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5358 | 1032 | 929 | 316 | 198 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4328 | 363 | 1197 | 244 | 127 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3996 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 204 | 284 | 135 | 37 | 2026-08-14 14:43:56 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2532 | 245 | 469 | 737 | 104 | 2026-08-18 19:13:04 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 915 | 1084 | 1589 | 356 | 2026-08-18 15:39:26 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 368 | 1786 | 272 | 270 | 2026-08-17 23:26:03 |
| [pypy](https://github.com/pypy/pypy) | 1783 | 123 | 5252 | 292 | 731 | 2026-08-18 18:55:23 |
| [jython](https://github.com/jython/jython) | 1533 | 231 | 300 | 151 | 98 | 2026-08-16 08:58:23 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-19T01:44:01*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
