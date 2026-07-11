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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196282 | 75467 | 41594 | 77859 | 2647 | 2026-07-11 03:26:43 |
| [transformers](https://github.com/huggingface/transformers) | 162461 | 33859 | 19166 | 27363 | 2476 | 2026-07-10 22:00:52 |
| [pytorch](https://github.com/pytorch/pytorch) | 101721 | 28469 | 59741 | 129243 | 18302 | 2026-07-11 03:25:37 |
| [fastapi](https://github.com/fastapi/fastapi) | 100335 | 9584 | 3539 | 6070 | 98 | 2026-07-10 17:54:44 |
| [django](https://github.com/django/django) | 88148 | 34146 | 0 | 21541 | 457 | 2026-07-10 22:01:58 |
| [cpython](https://github.com/python/cpython) | 73733 | 34985 | 77135 | 74062 | 9399 | 2026-07-10 22:25:22 |
| [flask](https://github.com/pallets/flask) | 71910 | 16906 | 2754 | 2863 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66685 | 27170 | 12172 | 21103 | 2100 | 2026-07-10 16:18:03 |
| [keras](https://github.com/keras-team/keras) | 64187 | 19754 | 12816 | 9567 | 232 | 2026-07-07 17:53:38 |
| [pandas](https://github.com/pandas-dev/pandas) | 49167 | 20121 | 28380 | 37803 | 3047 | 2026-07-11 00:11:48 |
| [ray](https://github.com/ray-project/ray) | 43189 | 7784 | 22828 | 41464 | 3458 | 2026-07-11 00:20:18 |
| [gym](https://github.com/openai/gym) | 37248 | 8693 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33736 | 4689 | 5764 | 4099 | 220 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32351 | 12559 | 13989 | 17881 | 2400 | 2026-07-10 23:35:53 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30092 | 7073 | 3967 | 5026 | 85 | 2026-07-08 20:30:28 |
| [celery](https://github.com/celery/celery) | 28670 | 5097 | 5287 | 4174 | 784 | 2026-07-09 14:31:55 |
| [dash](https://github.com/plotly/dash) | 24310 | 2305 | 2126 | 1644 | 543 | 2026-07-10 17:33:35 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22980 | 8385 | 11354 | 20618 | 1472 | 2026-07-10 19:17:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5534 | 1876 | 1789 | 240 | 2026-07-08 17:05:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 22166 | 1455 | 1367 | 6808 | 383 | 2026-07-10 00:58:33 |
| [micropython](https://github.com/micropython/micropython) | 21886 | 8913 | 6095 | 7945 | 1630 | 2026-07-10 01:27:42 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18672 | 2822 | 3366 | 2117 | 771 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1588 | 1467 | 1691 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16492 | 2346 | 3223 | 9552 | 243 | 2026-07-10 14:57:09 |
| [httpx](https://github.com/encode/httpx) | 15344 | 1197 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14810 | 5799 | 11519 | 14059 | 1845 | 2026-07-10 11:22:10 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13944 | 2119 | 2655 | 1198 | 215 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13855 | 1902 | 5540 | 6647 | 1259 | 2026-07-09 15:44:54 |
| [starlette](https://github.com/Kludex/starlette) | 12468 | 1225 | 771 | 1975 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11981 | 1709 | 8240 | 1137 | 211 | 2026-07-09 20:32:01 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11853 | 610 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9793 | 1013 | 1133 | 1477 | 170 | 2026-07-08 16:24:46 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9126 | 600 | 1039 | 520 | 216 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7290 | 408 | 895 | 2569 | 327 | 2026-07-06 22:45:42 |
| [hug](https://github.com/hugapi/hug) | 6884 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5603 | 497 | 1262 | 870 | 528 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1028 | 919 | 312 | 203 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4250 | 349 | 1187 | 229 | 121 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4089 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 312 | 674 | 1335 | 311 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2499 | 219 | 452 | 687 | 92 | 2026-07-10 22:50:46 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 914 | 1084 | 1562 | 359 | 2026-07-10 14:57:18 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 365 | 1785 | 268 | 266 | 2026-07-06 17:55:11 |
| [pypy](https://github.com/pypy/pypy) | 1763 | 118 | 5234 | 271 | 737 | 2026-07-10 14:20:19 |
| [jython](https://github.com/jython/jython) | 1523 | 232 | 298 | 138 | 107 | 2026-07-10 06:45:13 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-11T03:29:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
