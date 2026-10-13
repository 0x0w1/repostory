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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200908 | 79209 | 41890 | 83535 | 3424 | 2026-10-13 06:18:53 |
| [transformers](https://github.com/huggingface/transformers) | 167618 | 34853 | 19617 | 29142 | 2348 | 2026-10-13 06:34:29 |
| [pytorch](https://github.com/pytorch/pytorch) | 104755 | 32200 | 61682 | 138374 | 17723 | 2026-10-13 06:27:47 |
| [fastapi](https://github.com/fastapi/fastapi) | 103067 | 10029 | 3556 | 6421 | 88 | 2026-10-08 12:29:28 |
| [django](https://github.com/django/django) | 91408 | 37011 | 0 | 22059 | 541 | 2026-10-12 15:23:19 |
| [cpython](https://github.com/python/cpython) | 77631 | 38113 | 78662 | 78261 | 9716 | 2026-10-13 06:15:21 |
| [flask](https://github.com/pallets/flask) | 75029 | 17067 | 2769 | 2913 | 4 | 2026-10-07 14:02:59 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67569 | 27517 | 12322 | 21617 | 2162 | 2026-10-12 13:38:16 |
| [keras](https://github.com/keras-team/keras) | 64367 | 19794 | 13002 | 10056 | 237 | 2026-10-13 03:23:32 |
| [pandas](https://github.com/pandas-dev/pandas) | 50043 | 20498 | 28600 | 39426 | 2281 | 2026-10-13 03:26:07 |
| [ray](https://github.com/ray-project/ray) | 44018 | 8134 | 23158 | 43351 | 3572 | 2026-10-13 05:27:55 |
| [gym](https://github.com/openai/gym) | 37244 | 8668 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33952 | 4731 | 5774 | 4129 | 250 | 2026-10-12 06:36:31 |
| [numpy](https://github.com/numpy/numpy) | 33083 | 12905 | 14126 | 18769 | 2239 | 2026-10-13 03:49:03 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30205 | 7094 | 3966 | 5090 | 56 | 2026-10-08 02:57:13 |
| [celery](https://github.com/celery/celery) | 28965 | 5216 | 5331 | 4558 | 747 | 2026-10-13 06:30:23 |
| [dash](https://github.com/plotly/dash) | 24448 | 2327 | 2166 | 1759 | 434 | 2026-10-09 21:04:04 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23359 | 8508 | 11437 | 20964 | 1499 | 2026-10-13 02:18:43 |
| [RustPython](https://github.com/RustPython/RustPython) | 22393 | 1501 | 1438 | 7550 | 292 | 2026-10-13 06:26:35 |
| [tornado](https://github.com/tornadoweb/tornado) | 22168 | 5573 | 1889 | 1886 | 224 | 2026-10-12 17:13:21 |
| [micropython](https://github.com/micropython/micropython) | 22117 | 8999 | 6141 | 8126 | 1532 | 2026-10-13 03:41:31 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18838 | 2869 | 3389 | 2226 | 730 | 2026-10-09 16:12:55 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1610 | 1471 | 1685 | 157 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16574 | 2455 | 3264 | 10417 | 248 | 2026-10-13 06:34:52 |
| [httpx](https://github.com/encode/httpx) | 15640 | 3818 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15104 | 6010 | 11687 | 14675 | 1866 | 2026-10-13 03:25:16 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14064 | 2148 | 2663 | 1239 | 249 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13934 | 1978 | 5568 | 6755 | 1362 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12660 | 1375 | 787 | 2207 | 59 | 2026-10-09 14:25:06 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12230 | 1812 | 8338 | 1225 | 215 | 2026-10-12 17:12:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11912 | 616 | 426 | 339 | 169 | 2026-10-06 14:14:25 |
| [falcon](https://github.com/falconry/falcon) | 9807 | 1038 | 1147 | 1543 | 163 | 2026-10-12 05:29:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9209 | 616 | 1050 | 560 | 227 | 2026-10-05 09:53:29 |
| [bottle](https://github.com/bottlepy/bottle) | 8795 | 1516 | 867 | 655 | 289 | 2026-10-10 12:56:15 |
| [trio](https://github.com/python-trio/trio) | 7346 | 450 | 903 | 2631 | 334 | 2026-10-13 02:31:46 |
| [hug](https://github.com/hugapi/hug) | 6877 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 737 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 526 | 1275 | 926 | 533 | 2026-10-11 14:57:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5424 | 1048 | 935 | 325 | 203 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4444 | 383 | 1204 | 253 | 120 | 2026-10-05 12:11:01 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 893 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3672 | 209 | 289 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2766 | 317 | 677 | 1358 | 270 | 2026-10-13 02:33:06 |
| [anyio](https://github.com/agronholm/anyio) | 2556 | 311 | 489 | 847 | 136 | 2026-10-12 18:21:01 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1602 | 355 | 2026-10-08 17:48:24 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 370 | 1791 | 276 | 277 | 2026-10-12 18:14:09 |
| [pypy](https://github.com/pypy/pypy) | 1811 | 129 | 5280 | 345 | 712 | 2026-10-13 06:20:57 |
| [jython](https://github.com/jython/jython) | 1547 | 231 | 303 | 154 | 101 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 84 | 102 | 38 | 14 | 2026-10-12 21:07:24 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-10-13T06:36:03*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
