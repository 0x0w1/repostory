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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194050 | 75223 | 41199 | 68555 | 3716 | 2026-03-09 01:32:45 |
| [transformers](https://github.com/huggingface/transformers) | 157576 | 32328 | 18678 | 25245 | 2293 | 2026-03-08 21:04:36 |
| [pytorch](https://github.com/pytorch/pytorch) | 98056 | 27116 | 57174 | 119159 | 18064 | 2026-03-09 02:47:38 |
| [fastapi](https://github.com/fastapi/fastapi) | 96015 | 8806 | 3506 | 5412 | 149 | 2026-03-07 09:29:24 |
| [django](https://github.com/django/django) | 87011 | 33727 | 0 | 20802 | 432 | 2026-03-08 11:08:27 |
| [cpython](https://github.com/python/cpython) | 71896 | 34202 | 75473 | 69177 | 9302 | 2026-03-09 02:25:21 |
| [flask](https://github.com/pallets/flask) | 71337 | 16745 | 2723 | 2782 | 3 | 2026-03-08 23:24:17 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65341 | 26751 | 11983 | 20344 | 2141 | 2026-03-07 05:58:51 |
| [keras](https://github.com/keras-team/keras) | 63911 | 19714 | 12658 | 8930 | 289 | 2026-03-08 23:22:33 |
| [pandas](https://github.com/pandas-dev/pandas) | 48082 | 19717 | 28162 | 36252 | 3703 | 2026-03-08 21:32:02 |
| [ray](https://github.com/ray-project/ray) | 41648 | 7305 | 22425 | 38803 | 3449 | 2026-03-08 23:49:52 |
| [gym](https://github.com/openai/gym) | 37077 | 8709 | 1840 | 1467 | 128 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33284 | 4642 | 5742 | 4082 | 193 | 2026-03-03 08:56:07 |
| [numpy](https://github.com/numpy/numpy) | 31579 | 12133 | 13824 | 17086 | 2326 | 2026-03-09 02:19:42 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29929 | 7077 | 3946 | 4940 | 79 | 2026-03-04 15:27:11 |
| [celery](https://github.com/celery/celery) | 28204 | 4986 | 5201 | 3855 | 773 | 2026-03-08 14:01:48 |
| [dash](https://github.com/plotly/dash) | 24446 | 2262 | 2069 | 1456 | 572 | 2026-03-06 19:02:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22539 | 8240 | 11189 | 20020 | 1536 | 2026-03-08 21:10:10 |
| [tornado](https://github.com/tornadoweb/tornado) | 22404 | 5545 | 1864 | 1704 | 219 | 2026-01-23 01:16:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 21864 | 1406 | 1312 | 6005 | 365 | 2026-03-09 02:47:24 |
| [micropython](https://github.com/micropython/micropython) | 21517 | 8733 | 5972 | 7605 | 1848 | 2026-03-08 13:41:27 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1586 | 1465 | 1671 | 124 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18314 | 2779 | 3326 | 2053 | 777 | 2026-03-06 19:04:59 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16381 | 2210 | 3181 | 8721 | 275 | 2026-03-09 02:17:24 |
| [httpx](https://github.com/encode/httpx) | 15143 | 1057 | 0 | 1804 | 149 | 2026-03-01 16:44:00 |
| [scipy](https://github.com/scipy/scipy) | 14513 | 5644 | 11353 | 13398 | 1780 | 2026-03-09 01:08:17 |
| [dask](https://github.com/dask/dask) | 13761 | 1853 | 5512 | 6503 | 1226 | 2026-03-05 10:51:36 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13758 | 2080 | 2647 | 1163 | 207 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 12010 | 1131 | 763 | 1824 | 47 | 2026-03-07 11:57:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11678 | 600 | 406 | 314 | 154 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11676 | 1650 | 8164 | 1041 | 212 | 2026-03-06 21:58:36 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 980 | 1119 | 1418 | 164 | 2026-03-06 07:42:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8934 | 560 | 1019 | 492 | 217 | 2026-03-06 14:12:06 |
| [bottle](https://github.com/bottlepy/bottle) | 8763 | 1500 | 863 | 632 | 285 | 2026-02-17 10:24:31 |
| [trio](https://github.com/python-trio/trio) | 7189 | 388 | 880 | 2511 | 319 | 2026-03-01 01:52:41 |
| [hug](https://github.com/hugapi/hug) | 6908 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6747 | 735 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5608 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5514 | 465 | 1237 | 793 | 490 | 2026-03-08 17:01:54 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5203 | 1000 | 908 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4077 | 895 | 1063 | 2731 | 81 | 2026-03-05 21:21:24 |
| [databases](https://github.com/encode/databases) | 4019 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3995 | 321 | 1181 | 214 | 113 | 2026-03-06 16:36:10 |
| [quart](https://github.com/pallets/quart) | 3604 | 193 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2733 | 311 | 660 | 1285 | 308 | 2026-03-06 21:26:00 |
| [anyio](https://github.com/agronholm/anyio) | 2405 | 184 | 429 | 580 | 83 | 2026-03-04 20:45:48 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2365 | 135 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 905 | 1079 | 1464 | 367 | 2026-03-03 06:12:03 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1938 | 368 | 1785 | 267 | 267 | 2026-03-02 18:13:20 |
| [pypy](https://github.com/pypy/pypy) | 1669 | 101 | 5177 | 182 | 758 | 2026-03-06 11:02:10 |
| [jython](https://github.com/jython/jython) | 1490 | 226 | 292 | 122 | 107 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-03-09T02:51:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
