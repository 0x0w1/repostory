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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194209 | 75255 | 41241 | 69336 | 3777 | 2026-03-19 02:19:27 |
| [transformers](https://github.com/huggingface/transformers) | 158045 | 32536 | 18733 | 25479 | 2286 | 2026-03-18 21:35:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 98367 | 27247 | 57364 | 119927 | 18042 | 2026-03-19 02:53:35 |
| [fastapi](https://github.com/fastapi/fastapi) | 96323 | 8878 | 3512 | 5465 | 171 | 2026-03-18 23:41:06 |
| [django](https://github.com/django/django) | 87067 | 33765 | 0 | 20875 | 431 | 2026-03-18 12:23:32 |
| [cpython](https://github.com/python/cpython) | 72018 | 34254 | 75623 | 69520 | 9324 | 2026-03-19 02:05:10 |
| [flask](https://github.com/pallets/flask) | 71346 | 16750 | 2724 | 2788 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65423 | 26807 | 12000 | 20419 | 2142 | 2026-03-18 17:45:39 |
| [keras](https://github.com/keras-team/keras) | 63914 | 19741 | 12674 | 8973 | 258 | 2026-03-18 19:52:56 |
| [pandas](https://github.com/pandas-dev/pandas) | 48171 | 19761 | 28183 | 36449 | 3651 | 2026-03-19 01:07:24 |
| [ray](https://github.com/ray-project/ray) | 41768 | 7358 | 22465 | 39033 | 3473 | 2026-03-19 02:49:49 |
| [gym](https://github.com/openai/gym) | 37102 | 8706 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33352 | 4659 | 5746 | 4083 | 196 | 2026-03-15 10:29:09 |
| [numpy](https://github.com/numpy/numpy) | 31620 | 12176 | 13837 | 17129 | 2342 | 2026-03-18 17:44:14 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29929 | 7078 | 3946 | 4946 | 78 | 2026-03-18 20:41:06 |
| [celery](https://github.com/celery/celery) | 28236 | 4994 | 5208 | 3869 | 769 | 2026-03-15 10:51:04 |
| [dash](https://github.com/plotly/dash) | 24466 | 2267 | 2074 | 1475 | 583 | 2026-03-16 17:39:59 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22596 | 8265 | 11204 | 20077 | 1545 | 2026-03-18 23:47:11 |
| [tornado](https://github.com/tornadoweb/tornado) | 22406 | 5549 | 1865 | 1715 | 215 | 2026-03-18 19:36:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 21891 | 1408 | 1317 | 6075 | 363 | 2026-03-19 00:51:57 |
| [micropython](https://github.com/micropython/micropython) | 21555 | 8749 | 5978 | 7634 | 1848 | 2026-03-18 22:37:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1586 | 1465 | 1672 | 123 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18362 | 2787 | 3330 | 2057 | 776 | 2026-03-18 22:10:07 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16362 | 2215 | 3182 | 8758 | 274 | 2026-03-19 01:09:08 |
| [httpx](https://github.com/encode/httpx) | 15138 | 1079 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14541 | 5662 | 11379 | 13463 | 1791 | 2026-03-18 15:42:57 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13770 | 2085 | 2648 | 1165 | 210 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13768 | 1859 | 5518 | 6508 | 1231 | 2026-03-16 22:03:09 |
| [starlette](https://github.com/Kludex/starlette) | 12032 | 1138 | 765 | 1833 | 46 | 2026-03-16 05:35:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11690 | 602 | 408 | 317 | 158 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11666 | 1654 | 8171 | 1048 | 214 | 2026-03-18 23:37:45 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 981 | 1119 | 1421 | 163 | 2026-03-10 12:58:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8953 | 565 | 1024 | 497 | 218 | 2026-03-18 20:06:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1503 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7206 | 392 | 882 | 2515 | 318 | 2026-03-19 02:55:44 |
| [hug](https://github.com/hugapi/hug) | 6905 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5606 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5524 | 467 | 1242 | 802 | 494 | 2026-03-18 13:29:05 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5212 | 1001 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1064 | 2733 | 83 | 2026-03-11 17:57:15 |
| [databases](https://github.com/encode/databases) | 4017 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4017 | 323 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3610 | 193 | 280 | 126 | 65 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2735 | 312 | 663 | 1302 | 310 | 2026-03-18 13:04:54 |
| [anyio](https://github.com/agronholm/anyio) | 2413 | 189 | 430 | 589 | 86 | 2026-03-16 20:33:51 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 905 | 1081 | 1464 | 369 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1939 | 368 | 1785 | 267 | 267 | 2026-03-16 17:53:47 |
| [pypy](https://github.com/pypy/pypy) | 1682 | 104 | 5180 | 185 | 758 | 2026-03-16 11:57:50 |
| [jython](https://github.com/jython/jython) | 1490 | 227 | 293 | 122 | 108 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-19T02:56:05*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
