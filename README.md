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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200578 | 78817 | 41853 | 83277 | 3264 | 2026-10-10 04:58:44 |
| [transformers](https://github.com/huggingface/transformers) | 166955 | 34782 | 19594 | 29087 | 2337 | 2026-10-10 02:22:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 104011 | 31829 | 61617 | 138198 | 17697 | 2026-10-10 05:29:33 |
| [fastapi](https://github.com/fastapi/fastapi) | 102958 | 10014 | 3555 | 6418 | 87 | 2026-10-08 12:29:28 |
| [django](https://github.com/django/django) | 91358 | 36716 | 0 | 22042 | 535 | 2026-10-10 01:48:43 |
| [cpython](https://github.com/python/cpython) | 77601 | 37785 | 78602 | 78125 | 9806 | 2026-10-10 00:32:59 |
| [flask](https://github.com/pallets/flask) | 74992 | 17065 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67512 | 27493 | 12320 | 21599 | 2164 | 2026-10-10 04:40:09 |
| [keras](https://github.com/keras-team/keras) | 64360 | 19800 | 12993 | 10031 | 233 | 2026-10-10 01:28:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 49985 | 20483 | 28590 | 39335 | 2370 | 2026-10-10 01:48:34 |
| [ray](https://github.com/ray-project/ray) | 44000 | 8123 | 23149 | 43327 | 3564 | 2026-10-10 03:18:48 |
| [gym](https://github.com/openai/gym) | 37248 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33951 | 4732 | 5775 | 4129 | 249 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33049 | 12899 | 14124 | 18742 | 2246 | 2026-10-09 22:50:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30198 | 7094 | 3966 | 5090 | 56 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28937 | 5209 | 5329 | 4539 | 739 | 2026-10-10 02:16:58 |
| [dash](https://github.com/plotly/dash) | 24447 | 2329 | 2166 | 1759 | 434 | 2026-10-09 21:04:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23348 | 8502 | 11433 | 20955 | 1491 | 2026-10-10 01:01:27 |
| [RustPython](https://github.com/RustPython/RustPython) | 22393 | 1499 | 1437 | 7490 | 292 | 2026-10-10 00:25:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22163 | 5568 | 1888 | 1872 | 219 | 2026-10-07 21:34:52 |
| [micropython](https://github.com/micropython/micropython) | 22106 | 8993 | 6139 | 8122 | 1540 | 2026-10-03 07:13:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18827 | 2864 | 3388 | 2220 | 723 | 2026-10-09 16:12:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18637 | 1610 | 1470 | 1684 | 156 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16570 | 2445 | 3263 | 10383 | 221 | 2026-10-09 11:05:40 |
| [httpx](https://github.com/encode/httpx) | 15594 | 3471 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15100 | 5998 | 11681 | 14663 | 1859 | 2026-10-09 00:28:33 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14060 | 2142 | 2663 | 1230 | 240 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1977 | 5563 | 6750 | 1354 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12655 | 1367 | 787 | 2202 | 59 | 2026-10-09 14:25:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12210 | 1807 | 8335 | 1223 | 212 | 2026-10-09 16:52:33 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11910 | 616 | 425 | 337 | 166 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 1038 | 1146 | 1536 | 161 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9207 | 615 | 1050 | 559 | 226 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8792 | 1515 | 867 | 652 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7347 | 449 | 902 | 2629 | 332 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6878 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5632 | 523 | 1273 | 921 | 529 | 2026-10-07 04:44:53 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5420 | 1046 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4438 | 383 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 893 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3670 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 676 | 1357 | 288 | 2026-10-08 18:45:59 |
| [anyio](https://github.com/agronholm/anyio) | 2554 | 302 | 489 | 835 | 143 | 2026-10-09 23:02:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1811 | 129 | 5276 | 335 | 724 | 2026-10-09 18:30:05 |
| [jython](https://github.com/jython/jython) | 1548 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 117 | 78 | 2026-10-09 17:56:47 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-10T05:34:07*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
