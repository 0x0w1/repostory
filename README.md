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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198130 | 76229 | 41733 | 81210 | 2999 | 2026-09-01 04:46:00 |
| [transformers](https://github.com/huggingface/transformers) | 164676 | 34411 | 19396 | 28291 | 2399 | 2026-09-01 04:46:05 |
| [pytorch](https://github.com/pytorch/pytorch) | 102697 | 29064 | 60658 | 134222 | 17497 | 2026-09-01 04:41:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 101984 | 9838 | 3548 | 6293 | 80 | 2026-08-26 17:54:56 |
| [django](https://github.com/django/django) | 89347 | 34216 | 0 | 21739 | 481 | 2026-08-31 20:40:48 |
| [cpython](https://github.com/python/cpython) | 75342 | 35319 | 77902 | 76496 | 9611 | 2026-08-31 22:19:06 |
| [flask](https://github.com/pallets/flask) | 72167 | 16952 | 2765 | 2899 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67115 | 27341 | 12259 | 21408 | 2140 | 2026-08-31 12:23:54 |
| [keras](https://github.com/keras-team/keras) | 64269 | 19771 | 12890 | 9782 | 236 | 2026-09-01 01:46:34 |
| [pandas](https://github.com/pandas-dev/pandas) | 49613 | 20314 | 28501 | 38403 | 2709 | 2026-09-01 02:09:55 |
| [ray](https://github.com/ray-project/ray) | 43669 | 7984 | 23000 | 42409 | 3546 | 2026-09-01 02:52:33 |
| [gym](https://github.com/openai/gym) | 37244 | 8680 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33865 | 4723 | 5770 | 4119 | 238 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32641 | 12701 | 14075 | 18297 | 2339 | 2026-08-31 18:30:34 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30151 | 7080 | 3966 | 5049 | 59 | 2026-08-25 19:14:08 |
| [celery](https://github.com/celery/celery) | 28845 | 5145 | 5296 | 4281 | 755 | 2026-08-31 22:13:40 |
| [dash](https://github.com/plotly/dash) | 24389 | 2318 | 2146 | 1691 | 528 | 2026-08-31 22:50:29 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23131 | 8467 | 11410 | 20798 | 1473 | 2026-09-01 04:14:31 |
| [RustPython](https://github.com/RustPython/RustPython) | 22324 | 1481 | 1422 | 7137 | 400 | 2026-09-01 01:03:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5553 | 1879 | 1809 | 255 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22034 | 8950 | 6120 | 8079 | 1533 | 2026-08-31 04:24:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18762 | 2838 | 3378 | 2146 | 734 | 2026-08-31 21:06:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18647 | 1600 | 1471 | 1705 | 147 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16535 | 2392 | 3242 | 10011 | 231 | 2026-09-01 04:03:18 |
| [httpx](https://github.com/encode/httpx) | 15463 | 1266 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14973 | 5904 | 11619 | 14418 | 1836 | 2026-08-31 18:30:42 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14009 | 2128 | 2659 | 1216 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13910 | 1942 | 5552 | 6713 | 1321 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12584 | 1281 | 780 | 2069 | 60 | 2026-08-30 13:22:00 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12122 | 1766 | 8281 | 1199 | 206 | 2026-08-31 22:17:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 612 | 419 | 329 | 158 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1031 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9178 | 610 | 1043 | 540 | 221 | 2026-08-30 17:48:51 |
| [bottle](https://github.com/bottlepy/bottle) | 8778 | 1504 | 865 | 647 | 289 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7310 | 418 | 900 | 2595 | 324 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5621 | 500 | 1266 | 891 | 541 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5373 | 1038 | 933 | 320 | 199 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4358 | 369 | 1199 | 246 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3659 | 205 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 315 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 251 | 472 | 754 | 104 | 2026-09-01 00:10:54 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 917 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 368 | 1786 | 272 | 270 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1786 | 125 | 5255 | 297 | 722 | 2026-08-31 20:23:23 |
| [jython](https://github.com/jython/jython) | 1538 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-01T04:50:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
