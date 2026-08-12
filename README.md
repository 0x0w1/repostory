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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196955 | 75988 | 41678 | 79859 | 2831 | 2026-08-12 02:27:46 |
| [transformers](https://github.com/huggingface/transformers) | 163834 | 34205 | 19295 | 27879 | 2369 | 2026-08-11 22:54:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 102326 | 28837 | 60294 | 132135 | 17116 | 2026-08-12 02:30:38 |
| [fastapi](https://github.com/fastapi/fastapi) | 101508 | 9770 | 3544 | 6224 | 73 | 2026-08-11 21:03:36 |
| [django](https://github.com/django/django) | 88406 | 34132 | 0 | 21643 | 455 | 2026-08-11 21:16:13 |
| [cpython](https://github.com/python/cpython) | 74289 | 35197 | 77628 | 75620 | 9532 | 2026-08-12 00:15:34 |
| [flask](https://github.com/pallets/flask) | 72180 | 16942 | 2763 | 2892 | 3 | 2026-08-11 22:32:54 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66953 | 27282 | 12237 | 21303 | 2118 | 2026-08-10 14:26:12 |
| [keras](https://github.com/keras-team/keras) | 64222 | 19752 | 12866 | 9685 | 209 | 2026-08-11 21:38:10 |
| [pandas](https://github.com/pandas-dev/pandas) | 49494 | 20263 | 28469 | 38149 | 2841 | 2026-08-12 02:18:32 |
| [ray](https://github.com/ray-project/ray) | 43498 | 7913 | 22930 | 42074 | 3462 | 2026-08-12 02:30:44 |
| [gym](https://github.com/openai/gym) | 37243 | 8685 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33813 | 4709 | 5770 | 4109 | 232 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32523 | 12624 | 14040 | 18121 | 2327 | 2026-08-11 22:22:09 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30127 | 7077 | 3966 | 5043 | 57 | 2026-08-11 19:13:44 |
| [celery](https://github.com/celery/celery) | 28784 | 5130 | 5293 | 4231 | 800 | 2026-08-10 16:55:09 |
| [dash](https://github.com/plotly/dash) | 24372 | 2314 | 2142 | 1677 | 538 | 2026-08-11 13:29:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23075 | 8432 | 11392 | 20742 | 1474 | 2026-08-10 22:32:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 22273 | 1474 | 1420 | 7005 | 412 | 2026-08-11 14:22:20 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5552 | 1878 | 1807 | 253 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 21986 | 8930 | 6115 | 8031 | 1551 | 2026-08-11 05:29:21 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18732 | 2835 | 3375 | 2137 | 775 | 2026-08-07 20:07:14 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1596 | 1471 | 1701 | 144 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16520 | 2372 | 3235 | 9808 | 232 | 2026-08-12 01:33:12 |
| [httpx](https://github.com/encode/httpx) | 15410 | 1242 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14903 | 5860 | 11589 | 14274 | 1854 | 2026-08-11 17:25:08 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13991 | 2130 | 2658 | 1210 | 226 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13886 | 1925 | 5548 | 6688 | 1298 | 2026-08-10 22:03:29 |
| [starlette](https://github.com/Kludex/starlette) | 12537 | 1256 | 773 | 2024 | 63 | 2026-08-11 08:54:49 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12065 | 1746 | 8262 | 1179 | 215 | 2026-08-11 19:07:44 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11883 | 613 | 417 | 327 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1024 | 1139 | 1498 | 159 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9165 | 605 | 1042 | 528 | 226 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1501 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 413 | 898 | 2588 | 321 | 2026-08-11 00:45:57 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5611 | 500 | 1266 | 885 | 541 | 2026-08-10 10:46:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5347 | 1032 | 928 | 316 | 203 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4312 | 362 | 1195 | 243 | 129 | 2026-08-10 22:28:26 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3998 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3656 | 202 | 284 | 133 | 37 | 2026-08-09 20:23:31 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2523 | 238 | 467 | 727 | 102 | 2026-08-11 21:20:09 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1583 | 356 | 2026-08-11 15:13:53 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1786 | 272 | 270 | 2026-08-10 17:58:57 |
| [pypy](https://github.com/pypy/pypy) | 1781 | 121 | 5247 | 290 | 731 | 2026-08-12 01:38:45 |
| [jython](https://github.com/jython/jython) | 1532 | 231 | 300 | 149 | 97 | 2026-08-10 15:30:18 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-02 09:46:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-12T02:32:07*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
