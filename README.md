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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196118 | 75308 | 41585 | 77511 | 2655 | 2026-07-06 04:03:30 |
| [transformers](https://github.com/huggingface/transformers) | 162288 | 33782 | 19146 | 27219 | 2489 | 2026-07-06 04:13:16 |
| [pytorch](https://github.com/pytorch/pytorch) | 101523 | 28265 | 59630 | 128742 | 18253 | 2026-07-06 04:16:42 |
| [fastapi](https://github.com/fastapi/fastapi) | 100056 | 9546 | 3538 | 6053 | 96 | 2026-07-04 20:24:30 |
| [django](https://github.com/django/django) | 88102 | 34005 | 0 | 21510 | 456 | 2026-07-03 02:38:41 |
| [cpython](https://github.com/python/cpython) | 73598 | 34826 | 77054 | 73769 | 9397 | 2026-07-06 03:19:17 |
| [flask](https://github.com/pallets/flask) | 71919 | 16896 | 2754 | 2855 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66642 | 27157 | 12167 | 21084 | 2108 | 2026-07-03 16:15:55 |
| [keras](https://github.com/keras-team/keras) | 64178 | 19759 | 12809 | 9555 | 224 | 2026-07-01 17:25:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49140 | 20097 | 28358 | 37691 | 3023 | 2026-07-05 18:54:46 |
| [ray](https://github.com/ray-project/ray) | 43123 | 7762 | 22805 | 41340 | 3459 | 2026-07-06 03:33:45 |
| [gym](https://github.com/openai/gym) | 37245 | 8695 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33715 | 4691 | 5763 | 4099 | 219 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32318 | 12535 | 13981 | 17802 | 2407 | 2026-07-05 16:50:33 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30094 | 7074 | 3967 | 5026 | 85 | 2026-07-02 18:50:14 |
| [celery](https://github.com/celery/celery) | 28649 | 5094 | 5286 | 4169 | 790 | 2026-07-05 13:13:29 |
| [dash](https://github.com/plotly/dash) | 24289 | 2305 | 2124 | 1623 | 536 | 2026-07-03 18:30:44 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22964 | 8380 | 11345 | 20593 | 1475 | 2026-07-04 02:34:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22187 | 5530 | 1876 | 1787 | 240 | 2026-07-04 19:51:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22159 | 1450 | 1360 | 6777 | 383 | 2026-07-04 16:18:37 |
| [micropython](https://github.com/micropython/micropython) | 21870 | 8904 | 6089 | 7926 | 1633 | 2026-07-05 08:57:45 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18662 | 2820 | 3363 | 2102 | 769 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1590 | 1467 | 1691 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16481 | 2344 | 3222 | 9491 | 253 | 2026-07-03 21:24:24 |
| [httpx](https://github.com/encode/httpx) | 15338 | 1192 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14804 | 5792 | 11515 | 14035 | 1833 | 2026-07-05 17:40:35 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13937 | 2118 | 2655 | 1198 | 215 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13859 | 1896 | 5540 | 6637 | 1254 | 2026-07-01 16:46:02 |
| [starlette](https://github.com/Kludex/starlette) | 12454 | 1223 | 771 | 1971 | 56 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11968 | 1707 | 8237 | 1131 | 212 | 2026-06-27 22:33:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11849 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1011 | 1133 | 1475 | 171 | 2026-07-01 06:50:52 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9114 | 598 | 1038 | 518 | 215 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1500 | 865 | 637 | 285 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7285 | 403 | 895 | 2566 | 327 | 2026-07-04 05:52:00 |
| [hug](https://github.com/hugapi/hug) | 6884 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 740 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5598 | 494 | 1260 | 865 | 524 | 2026-07-03 15:44:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5313 | 1025 | 917 | 310 | 203 | 2026-07-02 05:35:42 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4237 | 347 | 1187 | 229 | 121 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4087 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3646 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2754 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2496 | 215 | 448 | 675 | 87 | 2026-06-29 23:43:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1084 | 1555 | 361 | 2026-07-03 11:15:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-29 17:47:29 |
| [pypy](https://github.com/pypy/pypy) | 1759 | 119 | 5230 | 268 | 741 | 2026-07-05 10:06:03 |
| [jython](https://github.com/jython/jython) | 1523 | 231 | 297 | 137 | 110 | 2026-06-30 12:03:48 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-06T04:18:39*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
