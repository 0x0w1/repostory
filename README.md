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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 198353 | 76226 | 41743 | 81300 | 3022 | 2026-09-02 04:00:57 |
| [transformers](https://github.com/huggingface/transformers) | 164703 | 34421 | 19399 | 28313 | 2396 | 2026-09-02 00:38:55 |
| [pytorch](https://github.com/pytorch/pytorch) | 102710 | 29076 | 60702 | 134322 | 17554 | 2026-09-02 04:05:55 |
| [fastapi](https://github.com/fastapi/fastapi) | 102010 | 9836 | 3549 | 6305 | 81 | 2026-09-01 20:59:55 |
| [django](https://github.com/django/django) | 89565 | 34213 | 0 | 21744 | 484 | 2026-09-01 20:15:42 |
| [cpython](https://github.com/python/cpython) | 75587 | 35315 | 77913 | 76536 | 9630 | 2026-09-02 00:32:39 |
| [flask](https://github.com/pallets/flask) | 72168 | 16954 | 2767 | 2900 | 4 | 2026-08-16 18:35:35 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 67130 | 27342 | 12261 | 21413 | 2146 | 2026-09-01 14:29:23 |
| [keras](https://github.com/keras-team/keras) | 64271 | 19772 | 12892 | 9784 | 223 | 2026-09-02 01:20:05 |
| [pandas](https://github.com/pandas-dev/pandas) | 49620 | 20316 | 28510 | 38413 | 2707 | 2026-09-01 21:04:16 |
| [ray](https://github.com/ray-project/ray) | 43681 | 7987 | 23007 | 42434 | 3540 | 2026-09-02 02:57:47 |
| [gym](https://github.com/openai/gym) | 37246 | 8677 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33867 | 4723 | 5770 | 4119 | 238 | 2026-08-24 08:26:10 |
| [numpy](https://github.com/numpy/numpy) | 32642 | 12700 | 14077 | 18302 | 2340 | 2026-09-02 03:23:37 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30153 | 7080 | 3966 | 5050 | 58 | 2026-09-01 19:20:21 |
| [celery](https://github.com/celery/celery) | 28851 | 5144 | 5296 | 4283 | 745 | 2026-09-02 03:04:07 |
| [dash](https://github.com/plotly/dash) | 24389 | 2318 | 2147 | 1692 | 529 | 2026-09-01 21:23:41 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23136 | 8466 | 11410 | 20800 | 1472 | 2026-09-01 19:20:29 |
| [RustPython](https://github.com/RustPython/RustPython) | 22328 | 1481 | 1423 | 7138 | 397 | 2026-09-02 02:38:57 |
| [tornado](https://github.com/tornadoweb/tornado) | 22177 | 5553 | 1879 | 1809 | 255 | 2026-08-24 19:01:07 |
| [micropython](https://github.com/micropython/micropython) | 22036 | 8954 | 6121 | 8079 | 1534 | 2026-08-31 04:24:54 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18763 | 2838 | 3378 | 2146 | 722 | 2026-08-31 21:06:31 |
| [sanic](https://github.com/sanic-org/sanic) | 18647 | 1600 | 1471 | 1705 | 147 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16535 | 2392 | 3242 | 10026 | 217 | 2026-09-02 03:10:28 |
| [httpx](https://github.com/encode/httpx) | 15462 | 1265 | 0 | 1805 | 143 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14980 | 5905 | 11620 | 14425 | 1835 | 2026-09-02 03:46:11 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14010 | 2128 | 2659 | 1216 | 230 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13910 | 1943 | 5554 | 6713 | 1323 | 2026-08-24 18:46:39 |
| [starlette](https://github.com/Kludex/starlette) | 12584 | 1279 | 780 | 2071 | 62 | 2026-09-01 19:21:08 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12128 | 1769 | 8281 | 1199 | 206 | 2026-09-01 17:41:11 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11895 | 613 | 419 | 330 | 159 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1031 | 1139 | 1509 | 161 | 2026-07-31 07:09:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9178 | 610 | 1043 | 541 | 222 | 2026-08-30 17:48:51 |
| [bottle](https://github.com/bottlepy/bottle) | 8779 | 1505 | 865 | 648 | 290 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7311 | 418 | 900 | 2595 | 324 | 2026-09-01 03:20:14 |
| [hug](https://github.com/hugapi/hug) | 6882 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 740 | 979 | 592 | 29 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5621 | 501 | 1266 | 892 | 542 | 2026-09-01 00:07:28 |
| [vibora](https://github.com/vibora-io/vibora) | 5582 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5374 | 1038 | 932 | 321 | 200 | 2026-08-20 08:11:03 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4360 | 370 | 1199 | 247 | 129 | 2026-08-14 07:40:29 |
| [pyramid](https://github.com/Pylons/pyramid) | 4096 | 892 | 1065 | 2741 | 89 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3993 | 264 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3659 | 205 | 284 | 135 | 25 | 2026-08-29 18:41:13 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2759 | 315 | 675 | 1338 | 313 | 2026-08-31 12:23:46 |
| [anyio](https://github.com/agronholm/anyio) | 2536 | 250 | 473 | 754 | 105 | 2026-09-01 00:10:54 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 916 | 1085 | 1596 | 357 | 2026-08-25 17:27:13 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1947 | 370 | 1786 | 274 | 272 | 2026-08-31 18:04:55 |
| [pypy](https://github.com/pypy/pypy) | 1787 | 125 | 5255 | 299 | 721 | 2026-09-01 18:58:46 |
| [jython](https://github.com/jython/jython) | 1540 | 231 | 301 | 151 | 98 | 2026-09-01 09:11:37 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 102 | 38 | 14 | 2026-08-12 22:15:54 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 77 | 2026-08-05 12:08:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 149 | 196 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-09-02T04:11:08*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
