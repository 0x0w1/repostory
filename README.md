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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 194575 | 75258 | 41293 | 70630 | 4210 | 2026-04-08 03:04:50 |
| [transformers](https://github.com/huggingface/transformers) | 158995 | 32779 | 18836 | 25828 | 2386 | 2026-04-07 21:59:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 98906 | 27432 | 57693 | 121439 | 18241 | 2026-04-08 03:22:58 |
| [fastapi](https://github.com/fastapi/fastapi) | 96947 | 9027 | 3513 | 5561 | 166 | 2026-04-07 09:50:22 |
| [django](https://github.com/django/django) | 87196 | 33809 | 0 | 21003 | 427 | 2026-04-07 19:38:35 |
| [cpython](https://github.com/python/cpython) | 72203 | 34391 | 75854 | 70094 | 9324 | 2026-04-07 21:37:46 |
| [flask](https://github.com/pallets/flask) | 71383 | 16774 | 2727 | 2798 | 3 | 2026-04-05 19:32:20 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65698 | 26899 | 12023 | 20519 | 2062 | 2026-04-07 10:32:39 |
| [keras](https://github.com/keras-team/keras) | 63938 | 19738 | 12727 | 9123 | 267 | 2026-04-07 23:54:09 |
| [pandas](https://github.com/pandas-dev/pandas) | 48406 | 19856 | 28232 | 36803 | 3476 | 2026-04-07 17:21:35 |
| [ray](https://github.com/ray-project/ray) | 42007 | 7417 | 22542 | 39517 | 3568 | 2026-04-08 03:09:46 |
| [gym](https://github.com/openai/gym) | 37145 | 8707 | 1840 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33427 | 4669 | 5750 | 4089 | 197 | 2026-03-28 20:59:29 |
| [numpy](https://github.com/numpy/numpy) | 31766 | 12271 | 13866 | 17245 | 2347 | 2026-04-07 20:07:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29953 | 7071 | 3968 | 4997 | 77 | 2026-04-07 22:54:03 |
| [celery](https://github.com/celery/celery) | 28308 | 5002 | 5266 | 4063 | 780 | 2026-04-07 12:54:55 |
| [dash](https://github.com/plotly/dash) | 24442 | 2272 | 2086 | 1520 | 548 | 2026-04-07 22:50:57 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22688 | 8311 | 11233 | 20179 | 1537 | 2026-04-08 00:14:40 |
| [tornado](https://github.com/tornadoweb/tornado) | 22390 | 5544 | 1869 | 1727 | 215 | 2026-03-31 00:51:40 |
| [RustPython](https://github.com/RustPython/RustPython) | 21984 | 1422 | 1326 | 6171 | 371 | 2026-04-06 14:30:16 |
| [micropython](https://github.com/micropython/micropython) | 21614 | 8784 | 6011 | 7692 | 1870 | 2026-04-07 11:57:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18640 | 1587 | 1465 | 1677 | 128 | 2026-04-07 17:45:16 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18428 | 2793 | 3340 | 2065 | 777 | 2026-04-07 20:15:10 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16378 | 2242 | 3187 | 8821 | 274 | 2026-04-07 13:13:55 |
| [httpx](https://github.com/encode/httpx) | 15156 | 1105 | 0 | 1805 | 149 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14585 | 5686 | 11404 | 13561 | 1788 | 2026-04-07 21:08:23 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13797 | 2094 | 2650 | 1170 | 214 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13792 | 1861 | 5520 | 6523 | 1242 | 2026-04-07 15:43:50 |
| [starlette](https://github.com/Kludex/starlette) | 12181 | 1153 | 766 | 1857 | 53 | 2026-04-05 13:21:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11743 | 607 | 411 | 321 | 164 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11706 | 1665 | 8185 | 1053 | 212 | 2026-04-03 19:20:05 |
| [falcon](https://github.com/falconry/falcon) | 9805 | 987 | 1120 | 1429 | 163 | 2026-04-07 15:03:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8990 | 566 | 1025 | 500 | 219 | 2026-04-05 18:24:55 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1499 | 864 | 634 | 283 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7234 | 396 | 887 | 2528 | 319 | 2026-04-07 23:01:36 |
| [hug](https://github.com/hugapi/hug) | 6896 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6740 | 735 | 979 | 588 | 26 | 2026-03-24 09:19:21 |
| [vibora](https://github.com/vibora-io/vibora) | 5602 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5542 | 473 | 1245 | 819 | 506 | 2026-04-07 08:46:20 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5229 | 1006 | 909 | 291 | 199 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4082 | 894 | 1064 | 2736 | 86 | 2026-03-11 17:57:15 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4057 | 327 | 1181 | 215 | 114 | 2026-03-06 16:36:10 |
| [databases](https://github.com/encode/databases) | 4010 | 259 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3618 | 194 | 281 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2735 | 311 | 664 | 1306 | 305 | 2026-04-03 22:07:14 |
| [anyio](https://github.com/agronholm/anyio) | 2433 | 193 | 431 | 603 | 86 | 2026-04-07 22:16:53 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 427 | 395 | 24 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2172 | 905 | 1082 | 1465 | 365 | 2026-04-07 11:19:41 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1941 | 367 | 1785 | 267 | 267 | 2026-04-06 17:51:41 |
| [pypy](https://github.com/pypy/pypy) | 1699 | 109 | 5190 | 201 | 755 | 2026-04-07 18:18:27 |
| [jython](https://github.com/jython/jython) | 1500 | 228 | 294 | 123 | 109 | 2026-03-02 17:11:39 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 81 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 20 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-03-16 17:12:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-04-08T03:23:49*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
