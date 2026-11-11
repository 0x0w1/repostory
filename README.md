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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201460 | 77835 | 41969 | 84600 | 3429 | 2026-11-11 05:48:14 |
| [transformers](https://github.com/huggingface/transformers) | 168772 | 35166 | 19840 | 29929 | 1072 | 2026-11-11 03:43:41 |
| [pytorch](https://github.com/pytorch/pytorch) | 105342 | 30639 | 62474 | 141169 | 18156 | 2026-11-11 05:50:36 |
| [fastapi](https://github.com/fastapi/fastapi) | 104640 | 10216 | 3555 | 6603 | 54 | 2026-11-10 19:24:34 |
| [django](https://github.com/django/django) | 91722 | 35217 | 0 | 22192 | 535 | 2026-11-10 12:53:00 |
| [cpython](https://github.com/python/cpython) | 78181 | 36551 | 79236 | 80162 | 9284 | 2026-11-11 05:35:27 |
| [flask](https://github.com/pallets/flask) | 75114 | 17306 | 2778 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68140 | 27669 | 12376 | 21798 | 2172 | 2026-11-11 00:00:27 |
| [keras](https://github.com/keras-team/keras) | 64422 | 19818 | 13079 | 10247 | 245 | 2026-11-11 02:10:55 |
| [pandas](https://github.com/pandas-dev/pandas) | 50579 | 20745 | 28681 | 39913 | 1880 | 2026-11-11 02:20:40 |
| [ray](https://github.com/ray-project/ray) | 44253 | 8271 | 23302 | 44273 | 3759 | 2026-11-11 05:33:49 |
| [gym](https://github.com/openai/gym) | 37236 | 8663 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34040 | 4739 | 5783 | 4145 | 266 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33428 | 13107 | 14179 | 19001 | 2253 | 2026-11-11 02:45:19 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30230 | 7099 | 3966 | 5110 | 63 | 2026-11-11 03:20:21 |
| [celery](https://github.com/celery/celery) | 29172 | 5259 | 5378 | 4716 | 773 | 2026-11-11 03:25:06 |
| [dash](https://github.com/plotly/dash) | 24484 | 2343 | 2180 | 1833 | 440 | 2026-11-10 18:47:32 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23448 | 8547 | 11459 | 21061 | 1477 | 2026-11-09 12:38:47 |
| [RustPython](https://github.com/RustPython/RustPython) | 22474 | 1511 | 1460 | 8231 | 316 | 2026-11-11 02:41:35 |
| [micropython](https://github.com/micropython/micropython) | 22188 | 9052 | 6177 | 8239 | 1590 | 2026-11-11 05:13:44 |
| [tornado](https://github.com/tornadoweb/tornado) | 22167 | 5609 | 1893 | 1922 | 226 | 2026-11-09 22:44:01 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18889 | 2895 | 3402 | 2281 | 753 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1615 | 1474 | 1688 | 162 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16605 | 2517 | 3275 | 10702 | 302 | 2026-11-11 04:54:08 |
| [httpx](https://github.com/encode/httpx) | 15773 | 1865 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15203 | 6077 | 11763 | 14885 | 1900 | 2026-11-10 11:23:46 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14106 | 2160 | 2668 | 1255 | 255 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13944 | 2018 | 5582 | 6812 | 1429 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12720 | 1442 | 797 | 2305 | 33 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12273 | 1848 | 8388 | 1263 | 207 | 2026-11-10 19:42:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11933 | 620 | 430 | 347 | 178 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9814 | 1054 | 1151 | 1573 | 164 | 2026-11-10 01:11:55 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9242 | 626 | 1057 | 616 | 158 | 2026-11-10 15:00:37 |
| [bottle](https://github.com/bottlepy/bottle) | 8799 | 1513 | 866 | 656 | 288 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7360 | 473 | 910 | 2666 | 344 | 2026-11-10 01:52:37 |
| [hug](https://github.com/hugapi/hug) | 6870 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6751 | 736 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5647 | 544 | 1307 | 989 | 556 | 2026-11-11 03:10:19 |
| [vibora](https://github.com/vibora-io/vibora) | 5579 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5448 | 1053 | 938 | 330 | 206 | 2026-11-09 13:12:20 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4473 | 390 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4106 | 898 | 1066 | 2744 | 88 | 2026-11-10 23:11:48 |
| [databases](https://github.com/encode/databases) | 3985 | 279 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3681 | 212 | 291 | 137 | 27 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 320 | 682 | 1414 | 258 | 2026-11-11 03:41:03 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 498 | 891 | 149 | 2026-11-10 12:48:02 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 915 | 1085 | 1611 | 356 | 2026-11-07 20:21:36 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 281 | 279 | 2026-11-09 18:05:48 |
| [pypy](https://github.com/pypy/pypy) | 1824 | 133 | 5300 | 408 | 718 | 2026-11-10 21:29:41 |
| [jython](https://github.com/jython/jython) | 1551 | 236 | 305 | 162 | 106 | 2026-11-10 16:57:51 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 84 | 104 | 39 | 17 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 41 | 449 | 118 | 79 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 317 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-11T05:51:59*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
