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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 197634 | 76131 | 41720 | 80826 | 2938 | 2026-08-26 01:45:22 |
| [transformers](https://github.com/huggingface/transformers) | 164443 | 34363 | 19375 | 28190 | 2413 | 2026-08-26 01:19:56 |
| [pytorch](https://github.com/pytorch/pytorch) | 102597 | 28983 | 60546 | 133641 | 17370 | 2026-08-26 01:39:40 |
| [fastapi](https://github.com/fastapi/fastapi) | 101854 | 9816 | 3546 | 6268 | 78 | 2026-08-25 13:19:29 |
| [django](https://github.com/django/django) | 88968 | 34180 | 0 | 21704 | 472 | 2026-08-23 19:39:31 |
| [cpython](https://github.com/python/cpython) | 74934 | 35277 | 77826 | 76216 | 9598 | 2026-08-26 01:35:50 |
| [flask](https://github.com/pallets/flask) | 72149 | 16947 | 2763 | 2896 | 3 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67061 | 27313 | 12250 | 21374 | 2124 | 2026-08-25 15:28:57 |
| [keras](https://github.com/keras-team/keras) | 64250 | 19764 | 12884 | 9758 | 249 | 2026-08-25 22:53:58 |
| [pandas](https://github.com/pandas-dev/pandas) | 49563 | 20289 | 28484 | 38311 | 2771 | 2026-08-25 23:18:56 |
| [ray](https://github.com/ray-project/ray) | 43611 | 7965 | 22987 | 42338 | 3529 | 2026-08-26 00:26:48 |
| [gym](https://github.com/openai/gym) | 37250 | 8682 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33848 | 4718 | 5770 | 4117 | 237 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32602 | 12676 | 14065 | 18280 | 2342 | 2026-08-25 22:48:48 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30144 | 7076 | 3966 | 5047 | 57 | 2026-08-25 19:14:08 |
| [celery](https://github.com/celery/celery) | 28824 | 5142 | 5295 | 4261 | 799 | 2026-08-24 22:14:16 |
| [dash](https://github.com/plotly/dash) | 24384 | 2319 | 2144 | 1687 | 535 | 2026-08-25 23:31:08 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23105 | 8452 | 11402 | 20774 | 1473 | 2026-08-25 14:43:10 |
| [RustPython](https://github.com/RustPython/RustPython) | 22304 | 1476 | 1422 | 7100 | 396 | 2026-08-25 15:50:30 |
| [tornado](https://github.com/tornadoweb/tornado) | 22181 | 5551 | 1878 | 1807 | 252 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22010 | 8947 | 6116 | 8062 | 1533 | 2026-08-25 05:06:29 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18754 | 2836 | 3378 | 2145 | 778 | 2026-08-25 17:41:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18645 | 1598 | 1471 | 1703 | 146 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16526 | 2383 | 3242 | 9952 | 226 | 2026-08-26 01:46:11 |
| [httpx](https://github.com/encode/httpx) | 15438 | 1258 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14952 | 5879 | 11610 | 14389 | 1841 | 2026-08-25 21:24:12 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14006 | 2126 | 2659 | 1214 | 229 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13897 | 1935 | 5551 | 6704 | 1312 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12570 | 1271 | 779 | 2052 | 59 | 2026-08-25 20:19:24 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12110 | 1756 | 8278 | 1191 | 209 | 2026-08-24 19:56:29 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11887 | 612 | 417 | 328 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1030 | 1139 | 1504 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9174 | 611 | 1042 | 540 | 220 | 2026-08-24 14:12:22 |
| [bottle](https://github.com/bottlepy/bottle) | 8778 | 1500 | 865 | 644 | 288 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7308 | 416 | 899 | 2592 | 324 | 2026-08-24 22:05:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5612 | 500 | 1266 | 888 | 541 | 2026-08-24 16:57:01 |
| [vibora](https://github.com/vibora-io/vibora) | 5583 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5365 | 1035 | 930 | 320 | 197 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4338 | 364 | 1199 | 245 | 129 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4094 | 893 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3995 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3658 | 204 | 284 | 135 | 27 | 2026-08-25 19:06:37 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 314 | 675 | 1337 | 313 | 2026-08-17 12:33:36 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 248 | 471 | 745 | 103 | 2026-08-25 16:28:26 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 916 | 1085 | 1595 | 356 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1946 | 368 | 1786 | 272 | 270 | 2026-08-24 17:57:48 |
| [pypy](https://github.com/pypy/pypy) | 1782 | 125 | 5254 | 297 | 726 | 2026-08-25 17:19:22 |
| [jython](https://github.com/jython/jython) | 1535 | 231 | 301 | 151 | 99 | 2026-08-24 06:50:54 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-08-26T01:48:27*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
