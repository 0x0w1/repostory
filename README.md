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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 192241 | 74932 | 40888 | 60060 | 1670 | 2025-10-29 02:02:15 |
| [transformers](https://github.com/huggingface/transformers) | 151769 | 30971 | 18121 | 23209 | 2112 | 2025-10-28 18:24:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 94343 | 25687 | 54526 | 111483 | 17018 | 2025-10-29 02:01:25 |
| [fastapi](https://github.com/fastapi/fastapi) | 91263 | 8138 | 3472 | 4810 | 198 | 2025-10-28 20:20:52 |
| [django](https://github.com/django/django) | 85581 | 33170 | 0 | 19950 | 355 | 2025-10-28 15:40:01 |
| [flask](https://github.com/pallets/flask) | 70670 | 16596 | 2700 | 2714 | 17 | 2025-10-14 20:26:26 |
| [cpython](https://github.com/python/cpython) | 69579 | 33249 | 74142 | 65648 | 9218 | 2025-10-28 20:05:32 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63845 | 26373 | 11785 | 19685 | 2158 | 2025-10-29 01:30:22 |
| [keras](https://github.com/keras-team/keras) | 63522 | 19637 | 12576 | 8431 | 266 | 2025-10-29 00:43:50 |
| [pandas](https://github.com/pandas-dev/pandas) | 46959 | 19203 | 27833 | 35016 | 3639 | 2025-10-29 00:42:18 |
| [ray](https://github.com/ray-project/ray) | 39568 | 6838 | 21744 | 36178 | 3192 | 2025-10-29 01:23:48 |
| [gym](https://github.com/openai/gym) | 36713 | 8715 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32727 | 4612 | 5728 | 4071 | 206 | 2025-10-28 08:43:48 |
| [numpy](https://github.com/numpy/numpy) | 30695 | 11631 | 13613 | 16415 | 2346 | 2025-10-29 00:33:56 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29624 | 7027 | 3945 | 4853 | 81 | 2025-10-28 07:47:29 |
| [celery](https://github.com/celery/celery) | 27429 | 4874 | 5174 | 3708 | 747 | 2025-10-28 22:07:46 |
| [dash](https://github.com/plotly/dash) | 24206 | 2225 | 2014 | 1355 | 577 | 2025-10-28 18:50:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22328 | 5538 | 1853 | 1674 | 205 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21890 | 8095 | 11023 | 19634 | 1634 | 2025-10-29 01:05:25 |
| [micropython](https://github.com/micropython/micropython) | 20996 | 8509 | 5861 | 7306 | 1779 | 2025-10-28 01:50:35 |
| [RustPython](https://github.com/RustPython/RustPython) | 20703 | 1356 | 1225 | 4937 | 441 | 2025-10-28 04:19:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18535 | 1581 | 1451 | 1629 | 148 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17895 | 2736 | 3267 | 1968 | 726 | 2025-10-28 14:59:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16058 | 2148 | 3158 | 8276 | 262 | 2025-10-28 22:47:11 |
| [httpx](https://github.com/encode/httpx) | 14682 | 972 | 919 | 1751 | 106 | 2025-10-16 09:04:38 |
| [scipy](https://github.com/scipy/scipy) | 14131 | 5522 | 11101 | 12765 | 1792 | 2025-10-28 21:23:24 |
| [dask](https://github.com/dask/dask) | 13559 | 1815 | 5446 | 6374 | 1193 | 2025-10-28 20:19:37 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13524 | 2039 | 2632 | 1149 | 193 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11592 | 1057 | 755 | 1727 | 47 | 2025-10-28 17:34:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11378 | 582 | 396 | 297 | 147 | 2025-10-16 22:58:21 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11061 | 1590 | 8108 | 995 | 217 | 2025-10-28 23:42:27 |
| [falcon](https://github.com/falconry/falcon) | 9743 | 970 | 1107 | 1382 | 167 | 2025-10-17 18:55:50 |
| [bottle](https://github.com/bottlepy/bottle) | 8682 | 1489 | 856 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8663 | 529 | 964 | 449 | 176 | 2025-10-23 07:16:59 |
| [trio](https://github.com/python-trio/trio) | 6918 | 373 | 872 | 2463 | 312 | 2025-10-28 21:52:27 |
| [hug](https://github.com/hugapi/hug) | 6904 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6736 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5627 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5349 | 442 | 1197 | 714 | 502 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5058 | 956 | 875 | 263 | 170 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4058 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3932 | 262 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3716 | 296 | 1163 | 198 | 115 | 2025-10-29 00:23:51 |
| [quart](https://github.com/pallets/quart) | 3511 | 191 | 277 | 123 | 63 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2699 | 304 | 653 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2316 | 133 | 427 | 392 | 21 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2266 | 171 | 411 | 537 | 71 | 2025-10-28 10:34:28 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 910 | 1077 | 1462 | 368 | 2025-10-22 10:50:47 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1926 | 370 | 1781 | 264 | 261 | 2025-10-27 17:37:16 |
| [pypy](https://github.com/pypy/pypy) | 1549 | 87 | 5153 | 171 | 740 | 2025-10-28 13:51:47 |
| [jython](https://github.com/jython/jython) | 1448 | 225 | 283 | 114 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 101 | 36 | 14 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-13 17:07:49 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-29T02:06:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
