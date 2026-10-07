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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200723 | 78550 | 41841 | 83131 | 3251 | 2026-10-07 05:36:33 |
| [transformers](https://github.com/huggingface/transformers) | 167005 | 34764 | 19575 | 29013 | 2354 | 2026-10-07 00:50:51 |
| [pytorch](https://github.com/pytorch/pytorch) | 103815 | 31592 | 61533 | 137800 | 17619 | 2026-10-07 05:32:04 |
| [fastapi](https://github.com/fastapi/fastapi) | 102849 | 10000 | 3556 | 6414 | 88 | 2026-10-06 17:31:16 |
| [django](https://github.com/django/django) | 91355 | 36468 | 0 | 22012 | 534 | 2026-10-07 01:54:57 |
| [cpython](https://github.com/python/cpython) | 77543 | 37537 | 78558 | 78025 | 9810 | 2026-10-07 05:35:17 |
| [flask](https://github.com/pallets/flask) | 74930 | 17044 | 2769 | 2912 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67485 | 27479 | 12312 | 21583 | 2157 | 2026-10-06 15:37:34 |
| [keras](https://github.com/keras-team/keras) | 64351 | 19803 | 12981 | 10007 | 235 | 2026-10-07 02:52:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 49926 | 20470 | 28586 | 39249 | 2400 | 2026-10-06 22:43:37 |
| [ray](https://github.com/ray-project/ray) | 43978 | 8122 | 23127 | 43248 | 3572 | 2026-10-07 05:00:07 |
| [gym](https://github.com/openai/gym) | 37245 | 8670 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33944 | 4732 | 5774 | 4129 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33038 | 12894 | 14123 | 18694 | 2250 | 2026-10-06 20:01:38 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30199 | 7088 | 3966 | 5084 | 53 | 2026-10-06 21:32:49 |
| [celery](https://github.com/celery/celery) | 28935 | 5206 | 5327 | 4524 | 728 | 2026-10-07 03:15:15 |
| [dash](https://github.com/plotly/dash) | 24442 | 2329 | 2166 | 1758 | 439 | 2026-10-06 16:14:49 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23332 | 8501 | 11432 | 20945 | 1493 | 2026-10-07 04:12:17 |
| [RustPython](https://github.com/RustPython/RustPython) | 22382 | 1497 | 1437 | 7458 | 297 | 2026-10-07 05:32:22 |
| [tornado](https://github.com/tornadoweb/tornado) | 22169 | 5566 | 1885 | 1861 | 214 | 2026-10-06 19:45:12 |
| [micropython](https://github.com/micropython/micropython) | 22107 | 8989 | 6135 | 8121 | 1535 | 2026-10-03 07:13:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18824 | 2861 | 3388 | 2213 | 732 | 2026-10-06 14:21:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1608 | 1470 | 1684 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16569 | 2439 | 3262 | 10363 | 216 | 2026-10-07 02:04:27 |
| [httpx](https://github.com/encode/httpx) | 15530 | 3198 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15086 | 5994 | 11680 | 14646 | 1854 | 2026-10-06 21:18:42 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14060 | 2142 | 2663 | 1228 | 239 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13932 | 1972 | 5563 | 6745 | 1351 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12654 | 1363 | 786 | 2195 | 56 | 2026-10-06 20:18:56 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12201 | 1806 | 8334 | 1221 | 213 | 2026-10-07 00:25:58 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11910 | 615 | 425 | 337 | 166 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1036 | 1146 | 1533 | 158 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9204 | 614 | 1047 | 558 | 222 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1514 | 867 | 651 | 289 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7343 | 441 | 902 | 2626 | 330 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5631 | 519 | 1271 | 917 | 524 | 2026-10-07 04:44:53 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5413 | 1045 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4431 | 382 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 893 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3987 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3669 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 676 | 1353 | 292 | 2026-10-07 03:07:02 |
| [anyio](https://github.com/agronholm/anyio) | 2553 | 298 | 487 | 823 | 134 | 2026-10-06 20:50:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 917 | 1085 | 1602 | 357 | 2026-10-06 11:55:04 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1808 | 128 | 5275 | 329 | 723 | 2026-10-06 04:31:07 |
| [jython](https://github.com/jython/jython) | 1547 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 116 | 77 | 2026-10-05 17:39:10 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-07T05:38:31*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
