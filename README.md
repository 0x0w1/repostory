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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196804 | 75851 | 41649 | 79467 | 3016 | 2026-08-05 03:18:08 |
| [transformers](https://github.com/huggingface/transformers) | 163340 | 34120 | 19271 | 27774 | 2336 | 2026-08-05 02:27:45 |
| [pytorch](https://github.com/pytorch/pytorch) | 102186 | 28710 | 60177 | 131345 | 18464 | 2026-08-05 03:13:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 101309 | 9729 | 3543 | 6192 | 76 | 2026-08-04 16:21:33 |
| [django](https://github.com/django/django) | 88351 | 34101 | 0 | 21610 | 443 | 2026-08-04 18:57:56 |
| [cpython](https://github.com/python/cpython) | 74160 | 35137 | 77527 | 75322 | 9490 | 2026-08-04 22:02:49 |
| [flask](https://github.com/pallets/flask) | 72114 | 16924 | 2759 | 2884 | 7 | 2026-07-30 17:29:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66883 | 27257 | 12220 | 21240 | 2110 | 2026-08-04 15:06:09 |
| [keras](https://github.com/keras-team/keras) | 64220 | 19748 | 12860 | 9663 | 207 | 2026-08-05 00:55:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 49423 | 20229 | 28452 | 38062 | 2894 | 2026-08-05 00:29:49 |
| [ray](https://github.com/ray-project/ray) | 43447 | 7884 | 22895 | 41920 | 3478 | 2026-08-05 03:09:48 |
| [gym](https://github.com/openai/gym) | 37247 | 8685 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33802 | 4703 | 5768 | 4107 | 231 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32490 | 12611 | 14036 | 18066 | 2320 | 2026-08-04 21:05:41 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30119 | 7076 | 3965 | 5037 | 69 | 2026-07-31 18:52:20 |
| [celery](https://github.com/celery/celery) | 28761 | 5122 | 5290 | 4213 | 798 | 2026-08-04 06:44:28 |
| [dash](https://github.com/plotly/dash) | 24367 | 2312 | 2139 | 1675 | 543 | 2026-08-04 14:15:45 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23060 | 8424 | 11386 | 20716 | 1478 | 2026-08-05 01:17:53 |
| [RustPython](https://github.com/RustPython/RustPython) | 22243 | 1469 | 1408 | 6971 | 399 | 2026-08-04 17:15:28 |
| [tornado](https://github.com/tornadoweb/tornado) | 22191 | 5548 | 1878 | 1800 | 251 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21965 | 8922 | 6113 | 8011 | 1564 | 2026-08-01 08:22:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18717 | 2833 | 3376 | 2127 | 774 | 2026-08-01 12:45:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1595 | 1471 | 1700 | 143 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16508 | 2362 | 3228 | 9741 | 218 | 2026-08-04 11:39:05 |
| [httpx](https://github.com/encode/httpx) | 15391 | 1234 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14884 | 5845 | 11559 | 14221 | 1848 | 2026-08-04 19:35:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13987 | 2130 | 2655 | 1207 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13879 | 1923 | 5546 | 6680 | 1288 | 2026-08-03 22:03:26 |
| [starlette](https://github.com/Kludex/starlette) | 12517 | 1255 | 772 | 2000 | 77 | 2026-08-04 15:00:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12047 | 1737 | 8255 | 1166 | 212 | 2026-08-04 20:48:04 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11878 | 612 | 417 | 326 | 154 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1021 | 1139 | 1495 | 157 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9158 | 603 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1500 | 865 | 643 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7307 | 412 | 898 | 2585 | 323 | 2026-08-03 02:34:09 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 464 | 188 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 501 | 1265 | 882 | 540 | 2026-08-04 15:29:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5587 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5341 | 1029 | 925 | 316 | 200 | 2026-07-28 09:15:48 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4297 | 360 | 1190 | 238 | 123 | 2026-08-04 20:51:37 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 4001 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3654 | 202 | 284 | 133 | 42 | 2026-08-03 20:05:57 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2758 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2519 | 234 | 463 | 723 | 102 | 2026-08-04 21:21:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1084 | 1581 | 356 | 2026-07-29 16:59:19 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 270 | 268 | 2026-08-03 17:54:08 |
| [pypy](https://github.com/pypy/pypy) | 1779 | 122 | 5245 | 287 | 733 | 2026-08-04 11:44:15 |
| [jython](https://github.com/jython/jython) | 1531 | 230 | 299 | 148 | 101 | 2026-08-04 10:05:01 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 102 | 38 | 14 | 2026-08-02 09:46:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-05T03:20:59*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
