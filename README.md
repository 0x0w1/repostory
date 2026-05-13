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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195092 | 75286 | 41407 | 73398 | 5128 | 2026-05-13 04:00:59 |
| [transformers](https://github.com/huggingface/transformers) | 160539 | 33184 | 18951 | 26303 | 2354 | 2026-05-13 03:40:15 |
| [pytorch](https://github.com/pytorch/pytorch) | 99860 | 27765 | 58642 | 124310 | 18410 | 2026-05-13 03:59:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 98140 | 9251 | 3525 | 5721 | 195 | 2026-05-12 17:44:46 |
| [django](https://github.com/django/django) | 87467 | 33868 | 0 | 21211 | 429 | 2026-05-12 19:58:54 |
| [cpython](https://github.com/python/cpython) | 72665 | 34588 | 76343 | 71104 | 9302 | 2026-05-13 03:36:33 |
| [flask](https://github.com/pallets/flask) | 71524 | 16843 | 2736 | 2819 | 3 | 2026-05-02 13:14:04 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66052 | 27015 | 12082 | 20748 | 2024 | 2026-05-12 21:39:15 |
| [keras](https://github.com/keras-team/keras) | 64063 | 19776 | 12753 | 9307 | 194 | 2026-05-13 00:15:53 |
| [pandas](https://github.com/pandas-dev/pandas) | 48735 | 19943 | 28278 | 37260 | 3290 | 2026-05-13 01:23:00 |
| [ray](https://github.com/ray-project/ray) | 42513 | 7557 | 22668 | 40274 | 3535 | 2026-05-13 01:04:10 |
| [gym](https://github.com/openai/gym) | 37194 | 8700 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33571 | 4682 | 5755 | 4092 | 204 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 32022 | 12357 | 13911 | 17432 | 2367 | 2026-05-13 00:40:49 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30006 | 7066 | 3967 | 5005 | 78 | 2026-05-06 11:55:49 |
| [celery](https://github.com/celery/celery) | 28475 | 5039 | 5274 | 4107 | 771 | 2026-05-13 00:34:31 |
| [dash](https://github.com/plotly/dash) | 24175 | 2282 | 2095 | 1562 | 550 | 2026-05-12 20:12:23 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22790 | 8331 | 11264 | 20340 | 1487 | 2026-05-12 20:16:18 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5540 | 1871 | 1731 | 218 | 2026-05-12 15:07:09 |
| [RustPython](https://github.com/RustPython/RustPython) | 22046 | 1436 | 1341 | 6451 | 369 | 2026-05-13 03:16:33 |
| [micropython](https://github.com/micropython/micropython) | 21697 | 8821 | 6054 | 7790 | 1769 | 2026-05-13 04:02:03 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1588 | 1466 | 1683 | 134 | 2026-04-10 04:26:05 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18520 | 2804 | 3343 | 2083 | 763 | 2026-05-12 23:28:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16432 | 2261 | 3193 | 8993 | 255 | 2026-05-13 01:21:27 |
| [httpx](https://github.com/encode/httpx) | 15263 | 1141 | 0 | 1805 | 147 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14686 | 5721 | 11438 | 13671 | 1784 | 2026-05-12 22:44:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13867 | 2112 | 2653 | 1179 | 220 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13828 | 1869 | 5525 | 6555 | 1243 | 2026-05-12 20:38:53 |
| [starlette](https://github.com/Kludex/starlette) | 12305 | 1168 | 766 | 1891 | 58 | 2026-05-12 13:17:29 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11846 | 1684 | 8207 | 1080 | 220 | 2026-05-12 13:03:55 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11783 | 606 | 414 | 323 | 154 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 999 | 1125 | 1448 | 159 | 2026-05-03 09:55:26 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9050 | 579 | 1033 | 511 | 208 | 2026-04-21 06:23:04 |
| [bottle](https://github.com/bottlepy/bottle) | 8764 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7260 | 394 | 892 | 2542 | 320 | 2026-05-11 22:08:12 |
| [hug](https://github.com/hugapi/hug) | 6894 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6738 | 735 | 979 | 589 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5599 | 302 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5568 | 479 | 1251 | 826 | 503 | 2026-05-11 16:22:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5252 | 1013 | 912 | 298 | 208 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4132 | 332 | 1183 | 219 | 114 | 2026-04-24 21:28:44 |
| [pyramid](https://github.com/Pylons/pyramid) | 4084 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3633 | 196 | 282 | 127 | 67 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2743 | 311 | 663 | 1314 | 306 | 2026-05-13 00:38:23 |
| [anyio](https://github.com/agronholm/anyio) | 2463 | 206 | 438 | 633 | 83 | 2026-05-12 20:41:10 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2364 | 137 | 427 | 396 | 25 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 908 | 1084 | 1499 | 360 | 2026-05-12 12:19:17 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 267 | 266 | 2026-05-04 17:42:04 |
| [pypy](https://github.com/pypy/pypy) | 1726 | 112 | 5206 | 242 | 739 | 2026-05-12 11:37:19 |
| [jython](https://github.com/jython/jython) | 1508 | 229 | 294 | 129 | 113 | 2026-04-25 11:45:42 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-05-13T04:05:20*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
