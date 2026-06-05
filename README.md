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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195418 | 75352 | 41512 | 75341 | 3159 | 2026-06-05 04:33:08 |
| [transformers](https://github.com/huggingface/transformers) | 161297 | 33416 | 19031 | 26688 | 2410 | 2026-06-04 17:30:26 |
| [pytorch](https://github.com/pytorch/pytorch) | 100388 | 27935 | 59056 | 126653 | 18278 | 2026-06-05 04:35:17 |
| [fastapi](https://github.com/fastapi/fastapi) | 98917 | 9397 | 3528 | 5865 | 91 | 2026-06-04 12:45:14 |
| [django](https://github.com/django/django) | 87635 | 33999 | 0 | 21349 | 446 | 2026-06-04 19:12:13 |
| [cpython](https://github.com/python/cpython) | 72988 | 34702 | 76614 | 71994 | 9314 | 2026-06-04 20:45:28 |
| [flask](https://github.com/pallets/flask) | 71644 | 16850 | 2740 | 2834 | 4 | 2026-05-31 14:42:51 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66248 | 27047 | 12124 | 20897 | 2039 | 2026-06-03 15:45:52 |
| [keras](https://github.com/keras-team/keras) | 64087 | 19747 | 12776 | 9410 | 173 | 2026-06-04 21:40:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 48909 | 19985 | 28302 | 37419 | 3220 | 2026-06-05 00:09:16 |
| [ray](https://github.com/ray-project/ray) | 42775 | 7637 | 22719 | 40764 | 3450 | 2026-06-05 04:00:36 |
| [gym](https://github.com/openai/gym) | 37209 | 8700 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33635 | 4686 | 5757 | 4094 | 208 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32151 | 12419 | 13931 | 17556 | 2371 | 2026-06-04 18:44:18 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30050 | 7069 | 3967 | 5009 | 77 | 2026-06-04 16:46:46 |
| [celery](https://github.com/celery/celery) | 28556 | 5066 | 5280 | 4129 | 783 | 2026-06-03 07:47:09 |
| [dash](https://github.com/plotly/dash) | 24232 | 2287 | 2103 | 1579 | 538 | 2026-06-04 03:26:41 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22862 | 8347 | 11300 | 20466 | 1469 | 2026-06-05 04:32:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5540 | 1872 | 1741 | 218 | 2026-06-02 20:08:23 |
| [RustPython](https://github.com/RustPython/RustPython) | 22095 | 1443 | 1351 | 6624 | 381 | 2026-06-04 20:20:35 |
| [micropython](https://github.com/micropython/micropython) | 21780 | 8854 | 6065 | 7851 | 1686 | 2026-06-04 13:18:58 |
| [sanic](https://github.com/sanic-org/sanic) | 18628 | 1591 | 1467 | 1689 | 133 | 2026-05-31 19:42:26 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18576 | 2805 | 3349 | 2094 | 757 | 2026-06-03 20:10:01 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16440 | 2290 | 3210 | 9267 | 236 | 2026-06-04 23:57:03 |
| [httpx](https://github.com/encode/httpx) | 15277 | 1164 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14729 | 5747 | 11460 | 13822 | 1791 | 2026-06-04 23:57:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13900 | 2117 | 2653 | 1182 | 222 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13847 | 1881 | 5534 | 6599 | 1241 | 2026-06-04 18:24:23 |
| [starlette](https://github.com/Kludex/starlette) | 12361 | 1190 | 770 | 1935 | 59 | 2026-06-03 20:44:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11886 | 1697 | 8223 | 1106 | 213 | 2026-06-04 21:26:38 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11811 | 608 | 415 | 323 | 155 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 998 | 1126 | 1452 | 158 | 2026-06-01 11:19:07 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9079 | 596 | 1037 | 517 | 214 | 2026-05-28 09:04:02 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 864 | 635 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7276 | 397 | 892 | 2549 | 319 | 2026-06-01 23:07:35 |
| [hug](https://github.com/hugapi/hug) | 6887 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6737 | 736 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5595 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5573 | 485 | 1257 | 846 | 516 | 2026-06-04 17:20:19 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5276 | 1017 | 914 | 300 | 212 | 2026-02-03 07:13:13 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4175 | 336 | 1184 | 223 | 114 | 2026-05-31 16:51:24 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 892 | 1065 | 2736 | 86 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4004 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3639 | 198 | 283 | 127 | 68 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2748 | 311 | 665 | 1318 | 307 | 2026-05-28 19:17:32 |
| [anyio](https://github.com/agronholm/anyio) | 2477 | 207 | 441 | 647 | 83 | 2026-06-04 21:38:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2362 | 138 | 428 | 400 | 30 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 909 | 1084 | 1533 | 361 | 2026-06-03 17:35:39 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 365 | 1785 | 268 | 266 | 2026-06-01 17:59:42 |
| [pypy](https://github.com/pypy/pypy) | 1745 | 113 | 5215 | 258 | 735 | 2026-06-04 14:41:00 |
| [jython](https://github.com/jython/jython) | 1513 | 230 | 297 | 135 | 110 | 2026-06-03 08:15:01 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 82 | 102 | 38 | 16 | 2026-06-04 08:45:38 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 447 | 113 | 77 | 2026-05-25 17:10:04 |
| [circuits](https://github.com/circuits/circuits) | 316 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-05T04:38:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
