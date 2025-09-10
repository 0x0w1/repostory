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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191559 | 74820 | 40777 | 57195 | 1625 | 2025-09-10 01:52:12 |
| [transformers](https://github.com/huggingface/transformers) | 149371 | 30326 | 17899 | 22306 | 1985 | 2025-09-09 21:46:57 |
| [pytorch](https://github.com/pytorch/pytorch) | 93056 | 25204 | 53623 | 108484 | 17091 | 2025-09-10 01:50:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 89333 | 7853 | 3466 | 4698 | 235 | 2025-09-09 09:14:41 |
| [django](https://github.com/django/django) | 84936 | 32919 | 0 | 19772 | 366 | 2025-09-09 06:24:25 |
| [flask](https://github.com/pallets/flask) | 70321 | 16524 | 2694 | 2696 | 6 | 2025-08-19 21:10:21 |
| [cpython](https://github.com/python/cpython) | 68772 | 32808 | 73546 | 64265 | 9327 | 2025-09-10 01:17:00 |
| [keras](https://github.com/keras-team/keras) | 63400 | 19627 | 12541 | 8326 | 270 | 2025-09-10 01:48:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63289 | 26213 | 11691 | 19323 | 2154 | 2025-09-09 16:58:12 |
| [pandas](https://github.com/pandas-dev/pandas) | 46523 | 18885 | 27698 | 34557 | 3662 | 2025-09-09 18:36:09 |
| [ray](https://github.com/ray-project/ray) | 38867 | 6782 | 21068 | 34987 | 3060 | 2025-09-10 01:38:52 |
| [gym](https://github.com/openai/gym) | 36482 | 8692 | 1840 | 1466 | 130 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32447 | 4581 | 5720 | 4069 | 203 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30366 | 11327 | 13536 | 16131 | 2367 | 2025-09-09 19:39:26 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29447 | 7001 | 3945 | 4831 | 101 | 2025-09-08 19:44:29 |
| [celery](https://github.com/celery/celery) | 27162 | 4841 | 5159 | 3652 | 752 | 2025-09-09 12:10:28 |
| [dash](https://github.com/plotly/dash) | 24023 | 2199 | 1986 | 1327 | 555 | 2025-09-09 21:04:29 |
| [tornado](https://github.com/tornadoweb/tornado) | 22157 | 5536 | 1852 | 1673 | 208 | 2025-08-21 14:14:13 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21677 | 7991 | 10973 | 19524 | 1642 | 2025-09-09 14:56:26 |
| [micropython](https://github.com/micropython/micropython) | 20798 | 8413 | 5805 | 7165 | 1787 | 2025-09-09 01:00:44 |
| [RustPython](https://github.com/RustPython/RustPython) | 20485 | 1342 | 1217 | 4861 | 442 | 2025-09-08 13:25:33 |
| [sanic](https://github.com/sanic-org/sanic) | 18493 | 1581 | 1449 | 1625 | 143 | 2025-09-08 03:48:03 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17708 | 2708 | 3250 | 1947 | 722 | 2025-09-09 15:07:21 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15975 | 2121 | 3144 | 8047 | 269 | 2025-09-09 10:35:44 |
| [httpx](https://github.com/encode/httpx) | 14537 | 952 | 917 | 1723 | 104 | 2025-09-05 15:15:17 |
| [scipy](https://github.com/scipy/scipy) | 14005 | 5472 | 11016 | 12558 | 1774 | 2025-09-09 21:00:23 |
| [dask](https://github.com/dask/dask) | 13473 | 1796 | 5434 | 6341 | 1199 | 2025-09-09 07:59:24 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13425 | 2033 | 2626 | 1148 | 187 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11442 | 1033 | 751 | 1692 | 48 | 2025-09-06 10:49:37 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11244 | 571 | 388 | 288 | 142 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10872 | 1578 | 8079 | 979 | 230 | 2025-09-07 13:28:02 |
| [falcon](https://github.com/falconry/falcon) | 9714 | 959 | 1098 | 1367 | 158 | 2025-09-08 14:42:41 |
| [bottle](https://github.com/bottlepy/bottle) | 8658 | 1487 | 855 | 621 | 284 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8525 | 520 | 939 | 434 | 408 | 2025-09-01 14:55:27 |
| [hug](https://github.com/hugapi/hug) | 6894 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6842 | 367 | 866 | 2449 | 310 | 2025-09-09 15:37:50 |
| [eve](https://github.com/pyeve/eve) | 6733 | 746 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5633 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5277 | 436 | 1190 | 713 | 498 | 2025-08-27 04:27:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4972 | 937 | 867 | 258 | 162 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4046 | 890 | 1061 | 2719 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3933 | 263 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3584 | 292 | 1156 | 196 | 116 | 2025-09-08 12:14:54 |
| [quart](https://github.com/pallets/quart) | 3445 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2683 | 303 | 649 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2307 | 131 | 426 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2199 | 163 | 400 | 505 | 69 | 2025-09-09 20:08:00 |
| [web2py](https://github.com/web2py/web2py) | 2153 | 908 | 1077 | 1458 | 369 | 2025-09-07 03:45:02 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1923 | 369 | 1780 | 264 | 261 | 2025-09-08 17:38:35 |
| [pypy](https://github.com/pypy/pypy) | 1494 | 85 | 5143 | 168 | 736 | 2025-08-25 15:57:04 |
| [jython](https://github.com/jython/jython) | 1431 | 219 | 281 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 81 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-09-10T01:53:31*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
