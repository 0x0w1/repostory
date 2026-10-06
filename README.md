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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200711 | 78423 | 41841 | 83085 | 3263 | 2026-10-06 05:54:06 |
| [transformers](https://github.com/huggingface/transformers) | 166987 | 34757 | 19570 | 28978 | 2362 | 2026-10-06 01:15:21 |
| [pytorch](https://github.com/pytorch/pytorch) | 103787 | 31468 | 61498 | 137704 | 17605 | 2026-10-06 06:01:52 |
| [fastapi](https://github.com/fastapi/fastapi) | 102832 | 9994 | 3557 | 6408 | 86 | 2026-10-05 20:21:37 |
| [django](https://github.com/django/django) | 91329 | 36330 | 0 | 21999 | 530 | 2026-10-05 23:02:29 |
| [cpython](https://github.com/python/cpython) | 77513 | 37427 | 78538 | 77990 | 9781 | 2026-10-06 00:06:10 |
| [flask](https://github.com/pallets/flask) | 74905 | 17042 | 2769 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67479 | 27479 | 12310 | 21579 | 2155 | 2026-10-06 05:21:43 |
| [keras](https://github.com/keras-team/keras) | 64354 | 19804 | 12974 | 9998 | 244 | 2026-10-06 05:05:01 |
| [pandas](https://github.com/pandas-dev/pandas) | 49919 | 20468 | 28584 | 39212 | 2410 | 2026-10-06 01:31:32 |
| [ray](https://github.com/ray-project/ray) | 43972 | 8119 | 23124 | 43218 | 3566 | 2026-10-06 05:14:15 |
| [gym](https://github.com/openai/gym) | 37245 | 8669 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33940 | 4731 | 5774 | 4129 | 248 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 33018 | 12889 | 14123 | 18674 | 2250 | 2026-10-06 04:44:12 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30201 | 7086 | 3966 | 5076 | 49 | 2026-10-05 05:21:15 |
| [celery](https://github.com/celery/celery) | 28936 | 5205 | 5327 | 4516 | 737 | 2026-10-05 22:13:17 |
| [dash](https://github.com/plotly/dash) | 24441 | 2328 | 2166 | 1756 | 437 | 2026-10-05 18:29:00 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23328 | 8501 | 11433 | 20940 | 1494 | 2026-10-05 15:23:52 |
| [RustPython](https://github.com/RustPython/RustPython) | 22380 | 1495 | 1434 | 7443 | 402 | 2026-10-05 17:24:51 |
| [tornado](https://github.com/tornadoweb/tornado) | 22168 | 5564 | 1885 | 1854 | 214 | 2026-10-06 01:10:40 |
| [micropython](https://github.com/micropython/micropython) | 22108 | 8985 | 6135 | 8120 | 1534 | 2026-10-03 07:13:43 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18824 | 2860 | 3388 | 2211 | 731 | 2026-10-06 01:51:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18636 | 1608 | 1470 | 1684 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16569 | 2439 | 3261 | 10352 | 221 | 2026-10-05 23:36:50 |
| [httpx](https://github.com/encode/httpx) | 15526 | 3096 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15077 | 5991 | 11680 | 14639 | 1861 | 2026-10-05 09:28:45 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14060 | 2143 | 2663 | 1228 | 239 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13934 | 1971 | 5563 | 6744 | 1351 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12655 | 1361 | 786 | 2186 | 58 | 2026-10-05 16:52:32 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12201 | 1805 | 8330 | 1221 | 214 | 2026-10-06 00:00:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11909 | 615 | 425 | 336 | 165 | 2026-10-01 15:38:19 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1037 | 1146 | 1533 | 158 | 2026-10-04 16:52:48 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9207 | 614 | 1047 | 558 | 222 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8793 | 1513 | 868 | 651 | 289 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7341 | 441 | 902 | 2626 | 330 | 2026-10-06 00:39:25 |
| [hug](https://github.com/hugapi/hug) | 6879 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6749 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5633 | 519 | 1271 | 912 | 523 | 2026-10-05 18:09:48 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5414 | 1045 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4431 | 382 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4099 | 893 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3988 | 270 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3671 | 209 | 289 | 137 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2765 | 316 | 676 | 1351 | 298 | 2026-10-06 01:00:03 |
| [anyio](https://github.com/agronholm/anyio) | 2550 | 297 | 486 | 822 | 133 | 2026-10-05 18:47:43 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2170 | 917 | 1085 | 1601 | 357 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-05 18:36:02 |
| [pypy](https://github.com/pypy/pypy) | 1807 | 127 | 5274 | 328 | 721 | 2026-10-06 04:31:07 |
| [jython](https://github.com/jython/jython) | 1547 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 116 | 77 | 2026-10-05 17:39:10 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-06T06:03:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
