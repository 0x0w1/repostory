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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195909 | 75190 | 41579 | 76938 | 3431 | 2026-06-26 04:21:08 |
| [transformers](https://github.com/huggingface/transformers) | 161927 | 33601 | 19108 | 27078 | 2445 | 2026-06-25 19:10:42 |
| [pytorch](https://github.com/pytorch/pytorch) | 101031 | 28124 | 59442 | 128182 | 18272 | 2026-06-26 04:11:01 |
| [fastapi](https://github.com/fastapi/fastapi) | 99667 | 9478 | 3535 | 5976 | 101 | 2026-06-25 15:40:10 |
| [django](https://github.com/django/django) | 87997 | 33872 | 0 | 21482 | 454 | 2026-06-25 20:50:40 |
| [cpython](https://github.com/python/cpython) | 73421 | 34781 | 76902 | 73009 | 9427 | 2026-06-26 03:49:16 |
| [flask](https://github.com/pallets/flask) | 71733 | 16875 | 2752 | 2841 | 6 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66457 | 27113 | 12161 | 21045 | 2101 | 2026-06-25 08:20:24 |
| [keras](https://github.com/keras-team/keras) | 64106 | 19742 | 12807 | 9507 | 230 | 2026-06-26 04:15:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49060 | 20040 | 28338 | 37599 | 3124 | 2026-06-25 21:25:54 |
| [ray](https://github.com/ray-project/ray) | 43024 | 7734 | 22778 | 41194 | 3480 | 2026-06-26 04:06:31 |
| [gym](https://github.com/openai/gym) | 37234 | 8701 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33699 | 4689 | 5762 | 4098 | 217 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32253 | 12490 | 13964 | 17711 | 2395 | 2026-06-26 00:04:50 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30087 | 7074 | 3967 | 5022 | 83 | 2026-06-25 23:24:23 |
| [celery](https://github.com/celery/celery) | 28627 | 5084 | 5282 | 4158 | 790 | 2026-06-24 15:07:52 |
| [dash](https://github.com/plotly/dash) | 24274 | 2301 | 2119 | 1602 | 553 | 2026-06-25 22:04:23 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22931 | 8359 | 11328 | 20557 | 1461 | 2026-06-25 11:37:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5531 | 1873 | 1755 | 214 | 2026-06-26 00:55:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22144 | 1448 | 1358 | 6738 | 385 | 2026-06-25 13:35:04 |
| [micropython](https://github.com/micropython/micropython) | 21834 | 8886 | 6073 | 7899 | 1632 | 2026-06-26 00:59:52 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18632 | 2815 | 3362 | 2098 | 767 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18626 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16465 | 2334 | 3215 | 9439 | 222 | 2026-06-25 21:53:44 |
| [httpx](https://github.com/encode/httpx) | 15318 | 1180 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14777 | 5774 | 11500 | 13974 | 1826 | 2026-06-25 11:58:27 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13934 | 2115 | 2655 | 1186 | 227 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13856 | 1893 | 5539 | 6628 | 1249 | 2026-06-23 14:17:10 |
| [starlette](https://github.com/Kludex/starlette) | 12432 | 1210 | 770 | 1955 | 49 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11950 | 1701 | 8234 | 1120 | 205 | 2026-06-25 13:13:14 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11832 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1004 | 1130 | 1467 | 164 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9105 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1501 | 864 | 636 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7277 | 398 | 893 | 2556 | 321 | 2026-06-22 22:13:40 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5593 | 490 | 1259 | 860 | 519 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5300 | 1024 | 916 | 307 | 210 | 2026-06-19 16:35:32 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4221 | 343 | 1186 | 226 | 118 | 2026-06-25 15:21:25 |
| [pyramid](https://github.com/Pylons/pyramid) | 4087 | 890 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2754 | 312 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2487 | 212 | 446 | 665 | 89 | 2026-06-25 22:07:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 910 | 1084 | 1548 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-22 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1759 | 118 | 5226 | 265 | 737 | 2026-06-25 16:18:48 |
| [jython](https://github.com/jython/jython) | 1519 | 230 | 297 | 137 | 111 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-26T04:22:05*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
