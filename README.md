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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 200645 | 77990 | 41818 | 82945 | 3232 | 2026-10-01 05:31:05 |
| [transformers](https://github.com/huggingface/transformers) | 166878 | 34735 | 19540 | 28887 | 2362 | 2026-10-01 05:11:54 |
| [pytorch](https://github.com/pytorch/pytorch) | 103574 | 31024 | 61369 | 137197 | 17563 | 2026-10-01 05:32:32 |
| [fastapi](https://github.com/fastapi/fastapi) | 102735 | 9975 | 3555 | 6387 | 96 | 2026-10-01 05:17:15 |
| [django](https://github.com/django/django) | 91238 | 35919 | 0 | 21974 | 525 | 2026-09-30 21:36:59 |
| [cpython](https://github.com/python/cpython) | 77370 | 37040 | 78363 | 77821 | 9730 | 2026-10-01 01:20:23 |
| [flask](https://github.com/pallets/flask) | 74800 | 17030 | 2768 | 2910 | 4 | 2026-09-08 16:40:53 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67435 | 27464 | 12304 | 21552 | 2157 | 2026-09-30 12:08:03 |
| [keras](https://github.com/keras-team/keras) | 64342 | 19807 | 12968 | 9969 | 252 | 2026-10-01 05:08:26 |
| [pandas](https://github.com/pandas-dev/pandas) | 49884 | 20451 | 28573 | 39057 | 2469 | 2026-10-01 00:29:05 |
| [ray](https://github.com/ray-project/ray) | 43956 | 8107 | 23113 | 43083 | 3540 | 2026-10-01 04:10:58 |
| [gym](https://github.com/openai/gym) | 37236 | 8672 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33931 | 4731 | 5774 | 4127 | 247 | 2026-09-30 08:13:41 |
| [numpy](https://github.com/numpy/numpy) | 32887 | 12862 | 14118 | 18629 | 2254 | 2026-10-01 02:06:34 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30197 | 7086 | 3966 | 5075 | 49 | 2026-09-30 06:38:50 |
| [celery](https://github.com/celery/celery) | 28928 | 5191 | 5313 | 4472 | 722 | 2026-10-01 04:02:31 |
| [dash](https://github.com/plotly/dash) | 24448 | 2327 | 2159 | 1740 | 423 | 2026-09-30 19:59:48 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23310 | 8496 | 11430 | 20914 | 1493 | 2026-09-30 03:22:33 |
| [RustPython](https://github.com/RustPython/RustPython) | 22372 | 1492 | 1433 | 7407 | 397 | 2026-10-01 02:32:32 |
| [tornado](https://github.com/tornadoweb/tornado) | 22178 | 5560 | 1884 | 1842 | 246 | 2026-09-30 20:46:50 |
| [micropython](https://github.com/micropython/micropython) | 22104 | 8982 | 6133 | 8112 | 1526 | 2026-09-30 06:13:17 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18817 | 2858 | 3386 | 2205 | 724 | 2026-09-25 07:35:35 |
| [sanic](https://github.com/sanic-org/sanic) | 18638 | 1604 | 1469 | 1680 | 152 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16567 | 2435 | 3260 | 10274 | 234 | 2026-09-30 22:53:41 |
| [httpx](https://github.com/encode/httpx) | 15524 | 2662 | 925 | 1805 | 139 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 15060 | 5978 | 11673 | 14616 | 1853 | 2026-09-30 23:18:48 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14053 | 2144 | 2663 | 1227 | 239 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13927 | 1971 | 5562 | 6735 | 1345 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12643 | 1348 | 784 | 2160 | 59 | 2026-09-29 07:31:18 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12192 | 1798 | 8314 | 1215 | 208 | 2026-09-30 23:39:25 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11909 | 616 | 422 | 334 | 164 | 2026-10-01 03:26:23 |
| [falcon](https://github.com/falconry/falcon) | 9806 | 1038 | 1145 | 1531 | 155 | 2026-09-30 18:05:10 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9204 | 615 | 1047 | 556 | 224 | 2026-09-27 17:46:43 |
| [bottle](https://github.com/bottlepy/bottle) | 8795 | 1511 | 868 | 651 | 290 | 2026-09-18 09:07:00 |
| [trio](https://github.com/python-trio/trio) | 7342 | 438 | 902 | 2620 | 330 | 2026-10-01 05:29:26 |
| [hug](https://github.com/hugapi/hug) | 6880 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 592 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5634 | 520 | 1270 | 907 | 521 | 2026-10-01 03:35:06 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5413 | 1044 | 934 | 325 | 202 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4424 | 382 | 1202 | 252 | 118 | 2026-09-18 17:57:22 |
| [pyramid](https://github.com/Pylons/pyramid) | 4100 | 894 | 1065 | 2742 | 90 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3989 | 271 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3674 | 208 | 289 | 136 | 28 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2766 | 316 | 675 | 1342 | 309 | 2026-10-01 04:58:59 |
| [anyio](https://github.com/agronholm/anyio) | 2550 | 291 | 484 | 810 | 131 | 2026-09-29 18:41:32 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 135 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 917 | 1085 | 1600 | 356 | 2026-09-14 17:25:22 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1948 | 371 | 1786 | 276 | 273 | 2026-09-28 18:11:20 |
| [pypy](https://github.com/pypy/pypy) | 1805 | 127 | 5267 | 317 | 716 | 2026-09-30 10:58:34 |
| [jython](https://github.com/jython/jython) | 1544 | 231 | 303 | 152 | 100 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 812 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 115 | 78 | 2026-09-28 17:22:28 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-10-01T05:32:48*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
