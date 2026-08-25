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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197561 | 76115 | 41707 | 80742 | 2929 | 2026-08-25 01:38:17 |
| [transformers](https://github.com/huggingface/transformers) | 164404 | 34344 | 19357 | 28159 | 2397 | 2026-08-24 23:25:06 |
| [pytorch](https://github.com/pytorch/pytorch) | 102578 | 28969 | 60508 | 133523 | 17317 | 2026-08-25 01:41:57 |
| [fastapi](https://github.com/fastapi/fastapi) | 101824 | 9811 | 3545 | 6262 | 77 | 2026-08-19 08:58:11 |
| [django](https://github.com/django/django) | 88922 | 34171 | 0 | 21708 | 472 | 2026-08-23 19:39:31 |
| [cpython](https://github.com/python/cpython) | 74896 | 35267 | 77808 | 76177 | 9584 | 2026-08-25 00:39:52 |
| [flask](https://github.com/pallets/flask) | 72147 | 16946 | 2763 | 2896 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67057 | 27309 | 12248 | 21369 | 2128 | 2026-08-24 15:38:18 |
| [keras](https://github.com/keras-team/keras) | 64249 | 19760 | 12883 | 9750 | 245 | 2026-08-24 18:42:25 |
| [pandas](https://github.com/pandas-dev/pandas) | 49560 | 20288 | 28484 | 38301 | 2771 | 2026-08-24 21:20:23 |
| [ray](https://github.com/ray-project/ray) | 43602 | 7962 | 22986 | 42319 | 3519 | 2026-08-25 01:08:13 |
| [gym](https://github.com/openai/gym) | 37251 | 8685 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33840 | 4716 | 5770 | 4117 | 237 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32597 | 12672 | 14063 | 18264 | 2339 | 2026-08-24 23:11:48 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30143 | 7076 | 3966 | 5046 | 56 | 2026-08-19 14:15:51 |
| [celery](https://github.com/celery/celery) | 28821 | 5143 | 5300 | 4259 | 798 | 2026-08-24 22:14:16 |
| [dash](https://github.com/plotly/dash) | 24381 | 2319 | 2144 | 1686 | 536 | 2026-08-24 17:29:25 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23105 | 8452 | 11402 | 20771 | 1473 | 2026-08-23 09:43:53 |
| [RustPython](https://github.com/RustPython/RustPython) | 22303 | 1476 | 1422 | 7094 | 394 | 2026-08-25 00:52:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22180 | 5550 | 1878 | 1807 | 252 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22009 | 8941 | 6120 | 8062 | 1539 | 2026-08-24 13:50:59 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18754 | 2836 | 3378 | 2143 | 779 | 2026-08-24 22:31:43 |
| [sanic](https://github.com/sanic-org/sanic) | 18644 | 1598 | 1471 | 1703 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16528 | 2383 | 3242 | 9947 | 239 | 2026-08-25 00:46:07 |
| [httpx](https://github.com/encode/httpx) | 15433 | 1257 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14950 | 5879 | 11607 | 14385 | 1845 | 2026-08-24 22:48:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14006 | 2126 | 2659 | 1214 | 229 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13895 | 1933 | 5551 | 6703 | 1312 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12564 | 1271 | 779 | 2051 | 69 | 2026-08-23 20:56:13 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12104 | 1756 | 8277 | 1189 | 206 | 2026-08-24 19:56:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11885 | 612 | 417 | 328 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9794 | 1030 | 1139 | 1504 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9174 | 611 | 1042 | 540 | 220 | 2026-08-24 14:12:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8776 | 1500 | 865 | 644 | 288 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7306 | 416 | 899 | 2592 | 324 | 2026-08-24 22:05:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5611 | 500 | 1266 | 888 | 541 | 2026-08-24 16:57:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5364 | 1035 | 930 | 320 | 197 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4336 | 365 | 1198 | 245 | 128 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4093 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3995 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 204 | 284 | 135 | 34 | 2026-08-24 19:55:28 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2535 | 247 | 471 | 742 | 104 | 2026-08-24 23:44:40 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1084 | 1593 | 359 | 2026-08-21 10:16:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 368 | 1786 | 272 | 270 | 2026-08-24 17:57:48 |
| [pypy](https://github.com/pypy/pypy) | 1783 | 125 | 5254 | 296 | 727 | 2026-08-24 20:59:17 |
| [jython](https://github.com/jython/jython) | 1535 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-25T01:42:52*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
