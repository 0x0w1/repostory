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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 193743 | 75234 | 41162 | 67267 | 3604 | 2026-02-17 01:49:45 |
| [transformers](https://github.com/huggingface/transformers) | 156554 | 32098 | 18586 | 24875 | 2265 | 2026-02-16 22:06:35 |
| [pytorch](https://github.com/pytorch/pytorch) | 97446 | 26886 | 56811 | 117788 | 18014 | 2026-02-17 02:38:27 |
| [fastapi](https://github.com/fastapi/fastapi) | 95157 | 8691 | 3503 | 5301 | 139 | 2026-02-14 08:57:26 |
| [django](https://github.com/django/django) | 86774 | 33646 | 0 | 20652 | 416 | 2026-02-16 19:37:49 |
| [cpython](https://github.com/python/cpython) | 71506 | 34082 | 75265 | 68632 | 9228 | 2026-02-17 02:28:21 |
| [flask](https://github.com/pallets/flask) | 71161 | 16714 | 2717 | 2769 | 3 | 2026-02-12 21:59:25 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 65040 | 26699 | 11941 | 20211 | 2130 | 2026-02-17 00:38:10 |
| [keras](https://github.com/keras-team/keras) | 63764 | 19697 | 12633 | 8766 | 290 | 2026-02-17 01:09:03 |
| [pandas](https://github.com/pandas-dev/pandas) | 47894 | 19659 | 28100 | 36014 | 3651 | 2026-02-17 00:45:11 |
| [ray](https://github.com/ray-project/ray) | 41278 | 7225 | 22330 | 38411 | 3366 | 2026-02-17 01:13:40 |
| [gym](https://github.com/openai/gym) | 37041 | 8712 | 1839 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 33210 | 4637 | 5740 | 4079 | 189 | 2025-11-27 18:55:46 |
| [numpy](https://github.com/numpy/numpy) | 31447 | 12060 | 13793 | 16986 | 2318 | 2026-02-16 18:05:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29875 | 7066 | 3946 | 4922 | 88 | 2026-02-16 10:51:07 |
| [celery](https://github.com/celery/celery) | 28026 | 4948 | 5195 | 3806 | 771 | 2026-02-16 22:14:00 |
| [dash](https://github.com/plotly/dash) | 24489 | 2255 | 2054 | 1437 | 558 | 2026-02-16 15:50:03 |
| [tornado](https://github.com/tornadoweb/tornado) | 22439 | 5546 | 1863 | 1699 | 213 | 2026-01-23 01:16:27 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22426 | 8192 | 11154 | 19967 | 1542 | 2026-02-16 19:40:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 21794 | 1400 | 1300 | 5810 | 378 | 2026-02-17 01:31:15 |
| [micropython](https://github.com/micropython/micropython) | 21469 | 8713 | 5957 | 7565 | 1857 | 2026-02-14 08:06:39 |
| [sanic](https://github.com/sanic-org/sanic) | 18639 | 1584 | 1464 | 1667 | 119 | 2026-01-07 11:11:51 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18254 | 2774 | 3323 | 2036 | 781 | 2026-02-16 19:57:19 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16262 | 2192 | 3177 | 8594 | 279 | 2026-02-16 15:29:00 |
| [httpx](https://github.com/encode/httpx) | 15002 | 1035 | 925 | 1790 | 135 | 2026-02-11 02:30:01 |
| [scipy](https://github.com/scipy/scipy) | 14455 | 5620 | 11310 | 13279 | 1771 | 2026-02-16 22:37:55 |
| [dask](https://github.com/dask/dask) | 13743 | 1843 | 5504 | 6489 | 1222 | 2026-02-16 22:55:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13725 | 2079 | 2646 | 1162 | 206 | 2026-01-22 13:03:07 |
| [starlette](https://github.com/Kludex/starlette) | 11926 | 1117 | 763 | 1802 | 48 | 2026-02-15 13:37:42 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11645 | 601 | 403 | 313 | 150 | 2026-01-30 14:24:05 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11516 | 1640 | 8152 | 1031 | 207 | 2026-02-16 15:27:59 |
| [falcon](https://github.com/falconry/falcon) | 9801 | 979 | 1119 | 1414 | 163 | 2026-02-16 10:48:02 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8899 | 558 | 1014 | 486 | 215 | 2026-01-23 15:02:05 |
| [bottle](https://github.com/bottlepy/bottle) | 8756 | 1496 | 861 | 629 | 283 | 2026-01-02 10:28:46 |
| [trio](https://github.com/python-trio/trio) | 7168 | 384 | 879 | 2501 | 314 | 2026-02-16 21:37:51 |
| [hug](https://github.com/hugapi/hug) | 6907 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 738 | 979 | 585 | 38 | 2026-02-11 11:19:09 |
| [vibora](https://github.com/vibora-io/vibora) | 5614 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5496 | 460 | 1230 | 777 | 484 | 2026-02-16 22:05:53 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5187 | 999 | 904 | 289 | 194 | 2026-02-03 07:13:13 |
| [pyramid](https://github.com/Pylons/pyramid) | 4071 | 891 | 1063 | 2725 | 92 | 2025-11-21 08:06:01 |
| [databases](https://github.com/encode/databases) | 4020 | 261 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3958 | 312 | 1181 | 210 | 116 | 2026-02-10 16:01:22 |
| [quart](https://github.com/pallets/quart) | 3597 | 192 | 279 | 126 | 66 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2726 | 309 | 658 | 1274 | 311 | 2026-02-17 02:10:23 |
| [anyio](https://github.com/agronholm/anyio) | 2388 | 181 | 426 | 571 | 77 | 2026-02-15 00:48:12 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2359 | 134 | 427 | 394 | 23 | 2025-03-25 15:52:44 |
| [web2py](https://github.com/web2py/web2py) | 2171 | 908 | 1079 | 1463 | 368 | 2026-02-11 14:23:25 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1936 | 367 | 1785 | 266 | 266 | 2026-02-16 17:43:15 |
| [pypy](https://github.com/pypy/pypy) | 1651 | 99 | 5176 | 179 | 758 | 2026-02-11 08:06:08 |
| [jython](https://github.com/jython/jython) | 1481 | 226 | 291 | 121 | 109 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 101 | 37 | 14 | 2025-11-13 15:58:12 |
| [Growler](https://github.com/pyGrowler/Growler) | 689 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 39 | 446 | 113 | 76 | 2026-01-19 17:12:11 |
| [circuits](https://github.com/circuits/circuits) | 316 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2026-02-17T02:49:44*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
