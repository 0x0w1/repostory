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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200320 | 77490 | 41809 | 82690 | 3322 | 2026-09-26 04:28:03 |
| [transformers](https://github.com/huggingface/transformers) | 166659 | 34677 | 19521 | 28812 | 2384 | 2026-09-26 01:45:27 |
| [pytorch](https://github.com/pytorch/pytorch) | 103334 | 30478 | 61264 | 136759 | 17551 | 2026-09-26 04:41:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 102622 | 9949 | 3553 | 6359 | 81 | 2026-09-25 18:27:31 |
| [django](https://github.com/django/django) | 91182 | 35455 | 0 | 21956 | 525 | 2026-09-24 08:59:37 |
| [cpython](https://github.com/python/cpython) | 77272 | 36503 | 78285 | 77567 | 9748 | 2026-09-26 02:33:21 |
| [flask](https://github.com/pallets/flask) | 74779 | 17004 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67371 | 27449 | 12298 | 21537 | 2153 | 2026-09-24 17:11:32 |
| [keras](https://github.com/keras-team/keras) | 64343 | 19806 | 12955 | 9942 | 262 | 2026-09-26 04:22:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 49819 | 20427 | 28565 | 38915 | 2566 | 2026-09-25 21:50:06 |
| [ray](https://github.com/ray-project/ray) | 43927 | 8089 | 23105 | 42978 | 3565 | 2026-09-26 02:33:04 |
| [gym](https://github.com/openai/gym) | 37235 | 8672 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33922 | 4725 | 5773 | 4125 | 246 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32840 | 12848 | 14111 | 18585 | 2262 | 2026-09-25 20:48:46 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30192 | 7085 | 3966 | 5072 | 48 | 2026-09-24 10:51:51 |
| [celery](https://github.com/celery/celery) | 28915 | 5184 | 5307 | 4437 | 734 | 2026-09-24 14:07:53 |
| [dash](https://github.com/plotly/dash) | 24428 | 2321 | 2158 | 1725 | 424 | 2026-09-24 19:27:16 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23272 | 8492 | 11429 | 20905 | 1489 | 2026-09-26 03:37:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22366 | 1488 | 1430 | 7322 | 401 | 2026-09-26 02:13:38 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5560 | 1883 | 1838 | 246 | 2026-09-25 19:17:31 |
| [micropython](https://github.com/micropython/micropython) | 22092 | 8979 | 6132 | 8106 | 1529 | 2026-09-21 13:34:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18806 | 2852 | 3387 | 2196 | 716 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18635 | 1603 | 1468 | 1678 | 150 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16561 | 2433 | 3256 | 10204 | 232 | 2026-09-25 11:17:30 |
| [httpx](https://github.com/encode/httpx) | 15509 | 2156 | 925 | 1805 | 140 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15044 | 5970 | 11663 | 14582 | 1853 | 2026-09-25 14:01:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14041 | 2141 | 2663 | 1224 | 236 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13927 | 1966 | 5560 | 6734 | 1343 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12636 | 1334 | 784 | 2146 | 65 | 2026-09-23 09:28:33 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12184 | 1794 | 8304 | 1213 | 207 | 2026-09-25 17:35:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11905 | 617 | 422 | 332 | 164 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9804 | 1037 | 1145 | 1529 | 158 | 2026-09-25 08:40:09 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9198 | 613 | 1047 | 553 | 224 | 2026-09-24 17:11:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8790 | 1513 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7338 | 436 | 902 | 2615 | 331 | 2026-09-21 22:04:23 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 517 | 1271 | 906 | 524 | 2026-09-18 21:32:05 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5409 | 1042 | 934 | 323 | 200 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4413 | 377 | 1202 | 250 | 117 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3990 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3673 | 207 | 288 | 136 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2763 | 316 | 675 | 1339 | 312 | 2026-09-23 01:15:44 |
| [anyio](https://github.com/agronholm/anyio) | 2549 | 279 | 480 | 791 | 123 | 2026-09-21 18:00:35 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2358 | 134 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1085 | 1598 | 355 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 275 | 272 | 2026-09-21 17:54:27 |
| [pypy](https://github.com/pypy/pypy) | 1800 | 126 | 5263 | 307 | 715 | 2026-09-24 05:31:55 |
| [jython](https://github.com/jython/jython) | 1542 | 232 | 302 | 152 | 99 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-26T04:42:43*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
