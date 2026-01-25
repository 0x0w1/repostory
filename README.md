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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193473 | 75205 | 41117 | 65563 | 2733 | 2026-01-25 01:33:50 |
| [transformers](https://github.com/huggingface/transformers) | 155661 | 31849 | 18459 | 24409 | 2188 | 2026-01-24 18:26:11 |
| [pytorch](https://github.com/pytorch/pytorch) | 96881 | 26620 | 56454 | 116340 | 17961 | 2026-01-25 02:26:00 |
| [fastapi](https://github.com/fastapi/fastapi) | 94421 | 8579 | 3500 | 5171 | 211 | 2026-01-24 21:29:42 |
| [django](https://github.com/django/django) | 86560 | 33545 | 0 | 20518 | 395 | 2026-01-23 23:33:38 |
| [cpython](https://github.com/python/cpython) | 71209 | 33957 | 75095 | 68126 | 9253 | 2026-01-24 16:09:29 |
| [flask](https://github.com/pallets/flask) | 71086 | 16680 | 2711 | 2756 | 10 | 2026-01-25 02:25:31 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 64761 | 26626 | 11899 | 20088 | 2121 | 2026-01-24 22:29:32 |
| [keras](https://github.com/keras-team/keras) | 63742 | 19676 | 12618 | 8642 | 249 | 2026-01-24 01:17:28 |
| [pandas](https://github.com/pandas-dev/pandas) | 47688 | 19568 | 28047 | 35744 | 3625 | 2026-01-24 18:14:04 |
| [ray](https://github.com/ray-project/ray) | 40966 | 7153 | 22221 | 37907 | 3303 | 2026-01-24 22:10:50 |
| [gym](https://github.com/openai/gym) | 36974 | 8714 | 1837 | 1467 | 126 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33104 | 4635 | 5737 | 4077 | 184 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31314 | 11985 | 13758 | 16901 | 2297 | 2026-01-24 20:09:51 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29822 | 7058 | 3946 | 4908 | 86 | 2026-01-24 14:33:27 |
| [celery](https://github.com/celery/celery) | 27908 | 4931 | 5184 | 3771 | 758 | 2026-01-22 11:20:35 |
| [dash](https://github.com/plotly/dash) | 24415 | 2251 | 2048 | 1422 | 559 | 2026-01-24 14:42:43 |
| [tornado](https://github.com/tornadoweb/tornado) | 22432 | 5542 | 1862 | 1696 | 210 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22266 | 8175 | 11116 | 19870 | 1530 | 2026-01-24 16:53:12 |
| [RustPython](https://github.com/RustPython/RustPython) | 21720 | 1399 | 1294 | 5508 | 372 | 2026-01-24 16:40:58 |
| [micropython](https://github.com/micropython/micropython) | 21377 | 8668 | 5939 | 7500 | 1843 | 2026-01-23 23:25:29 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1583 | 1463 | 1662 | 113 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18210 | 2776 | 3317 | 2005 | 767 | 2026-01-14 21:23:50 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16224 | 2183 | 3174 | 8515 | 276 | 2026-01-24 15:52:14 |
| [httpx](https://github.com/encode/httpx) | 14936 | 1015 | 925 | 1779 | 126 | 2025-12-17 13:57:57 |
| [scipy](https://github.com/scipy/scipy) | 14393 | 5595 | 11267 | 13148 | 1762 | 2026-01-24 08:33:08 |
| [dask](https://github.com/dask/dask) | 13727 | 1837 | 5497 | 6455 | 1215 | 2026-01-24 20:45:59 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13693 | 2082 | 2644 | 1157 | 203 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11864 | 1098 | 763 | 1772 | 47 | 2026-01-24 09:41:28 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11610 | 601 | 403 | 309 | 152 | 2026-01-19 17:03:12 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11421 | 1627 | 8143 | 1024 | 206 | 2026-01-24 19:22:06 |
| [falcon](https://github.com/falconry/falcon) | 9780 | 976 | 1119 | 1411 | 164 | 2026-01-24 23:24:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8856 | 556 | 998 | 482 | 199 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8735 | 1492 | 860 | 625 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7110 | 379 | 878 | 2490 | 314 | 2026-01-20 02:39:49 |
| [hug](https://github.com/hugapi/hug) | 6906 | 390 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6744 | 739 | 979 | 583 | 37 | 2026-01-01 01:43:32 |
| [vibora](https://github.com/vibora-io/vibora) | 5618 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5457 | 447 | 1221 | 736 | 512 | 2026-01-24 23:53:20 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5166 | 995 | 891 | 284 | 185 | 2026-01-22 06:45:33 |
| [pyramid](https://github.com/Pylons/pyramid) | 4072 | 890 | 1063 | 2724 | 91 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4022 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3911 | 307 | 1177 | 207 | 119 | 2026-01-14 18:53:49 |
| [quart](https://github.com/pallets/quart) | 3579 | 191 | 279 | 125 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2722 | 307 | 657 | 1261 | 312 | 2025-07-17 01:58:34 |
| [anyio](https://github.com/agronholm/anyio) | 2368 | 179 | 423 | 564 | 75 | 2026-01-24 16:46:44 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 134 | 428 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2173 | 910 | 1078 | 1462 | 368 | 2025-12-20 07:29:06 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1931 | 367 | 1785 | 266 | 266 | 2026-01-19 17:53:24 |
| [pypy](https://github.com/pypy/pypy) | 1635 | 96 | 5172 | 177 | 755 | 2026-01-19 10:28:14 |
| [jython](https://github.com/jython/jython) | 1473 | 225 | 291 | 120 | 108 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 814 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-01-25T02:35:14*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
