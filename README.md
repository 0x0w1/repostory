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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197329 | 76098 | 41703 | 80654 | 2932 | 2026-08-22 23:47:43 |
| [transformers](https://github.com/huggingface/transformers) | 164345 | 34326 | 19349 | 28131 | 2403 | 2026-08-23 01:43:22 |
| [pytorch](https://github.com/pytorch/pytorch) | 102547 | 28958 | 60477 | 133348 | 17274 | 2026-08-23 01:38:10 |
| [fastapi](https://github.com/fastapi/fastapi) | 101763 | 9806 | 3544 | 6259 | 78 | 2026-08-19 08:58:11 |
| [django](https://github.com/django/django) | 88718 | 34159 | 0 | 21699 | 467 | 2026-08-21 12:34:31 |
| [cpython](https://github.com/python/cpython) | 74670 | 35259 | 77789 | 76105 | 9572 | 2026-08-22 18:45:59 |
| [flask](https://github.com/pallets/flask) | 72140 | 16944 | 2762 | 2895 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67012 | 27300 | 12247 | 21357 | 2124 | 2026-08-21 08:56:47 |
| [keras](https://github.com/keras-team/keras) | 64248 | 19759 | 12879 | 9742 | 233 | 2026-08-21 23:10:41 |
| [pandas](https://github.com/pandas-dev/pandas) | 49547 | 20285 | 28483 | 38289 | 2791 | 2026-08-23 01:50:46 |
| [ray](https://github.com/ray-project/ray) | 43581 | 7952 | 22976 | 42294 | 3517 | 2026-08-22 15:55:13 |
| [gym](https://github.com/openai/gym) | 37247 | 8685 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33839 | 4712 | 5770 | 4115 | 237 | 2026-08-07 11:44:36 |
| [numpy](https://github.com/numpy/numpy) | 32583 | 12669 | 14057 | 18239 | 2333 | 2026-08-21 23:36:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30140 | 7078 | 3966 | 5046 | 57 | 2026-08-19 14:15:51 |
| [celery](https://github.com/celery/celery) | 28811 | 5143 | 5298 | 4254 | 794 | 2026-08-22 14:29:20 |
| [dash](https://github.com/plotly/dash) | 24380 | 2317 | 2144 | 1683 | 539 | 2026-08-21 19:57:31 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23108 | 8450 | 11401 | 20770 | 1474 | 2026-08-22 07:23:18 |
| [RustPython](https://github.com/RustPython/RustPython) | 22297 | 1476 | 1422 | 7086 | 395 | 2026-08-22 23:54:46 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5550 | 1878 | 1807 | 252 | 2026-08-07 15:34:25 |
| [micropython](https://github.com/micropython/micropython) | 22007 | 8940 | 6120 | 8060 | 1538 | 2026-08-18 14:36:09 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18751 | 2835 | 3378 | 2141 | 780 | 2026-08-21 23:12:12 |
| [sanic](https://github.com/sanic-org/sanic) | 18643 | 1598 | 1471 | 1703 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16525 | 2382 | 3241 | 9921 | 254 | 2026-08-22 19:11:47 |
| [httpx](https://github.com/encode/httpx) | 15429 | 1256 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14946 | 5876 | 11603 | 14367 | 1847 | 2026-08-22 13:06:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14008 | 2126 | 2659 | 1214 | 229 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13895 | 1933 | 5551 | 6703 | 1312 | 2026-08-17 14:33:18 |
| [starlette](https://github.com/Kludex/starlette) | 12561 | 1265 | 776 | 2040 | 68 | 2026-08-22 20:54:54 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12102 | 1755 | 8274 | 1186 | 212 | 2026-08-21 13:45:05 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11886 | 611 | 417 | 327 | 154 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1030 | 1139 | 1503 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9172 | 611 | 1042 | 538 | 223 | 2026-08-22 15:12:40 |
| [bottle](https://github.com/bottlepy/bottle) | 8776 | 1501 | 865 | 644 | 288 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7305 | 415 | 899 | 2590 | 322 | 2026-08-18 00:29:06 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5611 | 499 | 1265 | 887 | 540 | 2026-08-13 15:24:46 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5362 | 1034 | 930 | 318 | 195 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4335 | 364 | 1197 | 245 | 127 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4091 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3995 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 204 | 284 | 135 | 37 | 2026-08-19 19:52:39 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2535 | 247 | 469 | 740 | 105 | 2026-08-21 20:50:22 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 916 | 1084 | 1590 | 356 | 2026-08-21 10:16:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 368 | 1786 | 272 | 270 | 2026-08-17 23:26:03 |
| [pypy](https://github.com/pypy/pypy) | 1783 | 124 | 5254 | 295 | 727 | 2026-08-22 22:27:32 |
| [jython](https://github.com/jython/jython) | 1535 | 231 | 301 | 151 | 99 | 2026-08-16 08:58:23 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-23T01:51:06*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
