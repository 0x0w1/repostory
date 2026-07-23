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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196452 | 75694 | 41618 | 78620 | 2761 | 2026-07-23 03:33:19 |
| [transformers](https://github.com/huggingface/transformers) | 162850 | 33995 | 19221 | 27525 | 2402 | 2026-07-23 00:51:01 |
| [pytorch](https://github.com/pytorch/pytorch) | 101858 | 28456 | 59969 | 130233 | 18251 | 2026-07-23 03:32:34 |
| [fastapi](https://github.com/fastapi/fastapi) | 100778 | 9663 | 3541 | 6101 | 85 | 2026-07-21 21:28:20 |
| [django](https://github.com/django/django) | 88180 | 34144 | 0 | 21583 | 453 | 2026-07-22 21:21:10 |
| [cpython](https://github.com/python/cpython) | 73857 | 34973 | 77355 | 74814 | 9468 | 2026-07-22 23:03:26 |
| [flask](https://github.com/pallets/flask) | 71994 | 16913 | 2756 | 2870 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66755 | 27205 | 12196 | 21159 | 2113 | 2026-07-22 18:21:30 |
| [keras](https://github.com/keras-team/keras) | 64172 | 19743 | 12849 | 9604 | 208 | 2026-07-22 21:27:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 49289 | 20152 | 28410 | 37917 | 2908 | 2026-07-23 01:49:12 |
| [ray](https://github.com/ray-project/ray) | 43319 | 7821 | 22862 | 41685 | 3476 | 2026-07-23 03:31:55 |
| [gym](https://github.com/openai/gym) | 37237 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33765 | 4699 | 5768 | 4106 | 230 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32405 | 12585 | 14013 | 17957 | 2314 | 2026-07-23 00:38:17 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30102 | 7078 | 3967 | 5030 | 87 | 2026-07-22 08:03:04 |
| [celery](https://github.com/celery/celery) | 28716 | 5111 | 5288 | 4189 | 789 | 2026-07-22 22:12:38 |
| [dash](https://github.com/plotly/dash) | 24340 | 2309 | 2133 | 1657 | 536 | 2026-07-22 15:05:20 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23027 | 8414 | 11370 | 20666 | 1485 | 2026-07-23 02:19:17 |
| [RustPython](https://github.com/RustPython/RustPython) | 22214 | 1465 | 1390 | 6887 | 399 | 2026-07-22 11:34:20 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5546 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21922 | 8916 | 6104 | 7976 | 1576 | 2026-07-22 12:31:30 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18683 | 2827 | 3373 | 2116 | 777 | 2026-07-22 21:49:20 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1589 | 1469 | 1694 | 135 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16505 | 2356 | 3225 | 9645 | 215 | 2026-07-23 02:06:13 |
| [httpx](https://github.com/encode/httpx) | 15364 | 1214 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14837 | 5817 | 11542 | 14117 | 1860 | 2026-07-22 13:28:49 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13971 | 2129 | 2656 | 1205 | 223 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13864 | 1912 | 5543 | 6662 | 1271 | 2026-07-20 22:02:49 |
| [starlette](https://github.com/Kludex/starlette) | 12487 | 1234 | 771 | 1970 | 64 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12013 | 1722 | 8248 | 1147 | 202 | 2026-07-22 21:29:46 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11864 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 1021 | 1139 | 1491 | 171 | 2026-07-22 04:16:42 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9148 | 601 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7302 | 410 | 896 | 2575 | 328 | 2026-07-22 17:43:08 |
| [hug](https://github.com/hugapi/hug) | 6884 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5610 | 499 | 1265 | 875 | 534 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5589 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5329 | 1029 | 922 | 314 | 207 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4273 | 355 | 1189 | 234 | 126 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 203 | 284 | 132 | 56 | 2026-07-22 21:09:08 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2509 | 223 | 456 | 703 | 95 | 2026-07-22 20:11:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 914 | 1084 | 1579 | 360 | 2026-07-22 16:37:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-20 17:50:19 |
| [pypy](https://github.com/pypy/pypy) | 1767 | 120 | 5237 | 272 | 722 | 2026-07-22 19:47:32 |
| [jython](https://github.com/jython/jython) | 1529 | 231 | 298 | 144 | 106 | 2026-07-19 06:34:16 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-23T03:34:25*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
