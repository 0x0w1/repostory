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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196109 | 75191 | 41585 | 77208 | 2846 | 2026-06-30 04:14:17 |
| [transformers](https://github.com/huggingface/transformers) | 162034 | 33658 | 19118 | 27124 | 2452 | 2026-06-30 03:09:13 |
| [pytorch](https://github.com/pytorch/pytorch) | 101219 | 28169 | 59500 | 128406 | 18230 | 2026-06-30 04:15:56 |
| [fastapi](https://github.com/fastapi/fastapi) | 99787 | 9509 | 3539 | 5992 | 103 | 2026-06-29 12:43:58 |
| [django](https://github.com/django/django) | 88142 | 33872 | 0 | 21493 | 458 | 2026-06-29 17:36:06 |
| [cpython](https://github.com/python/cpython) | 73601 | 34789 | 76974 | 73339 | 9429 | 2026-06-30 00:12:59 |
| [flask](https://github.com/pallets/flask) | 71892 | 16886 | 2752 | 2843 | 6 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66625 | 27122 | 12167 | 21066 | 2106 | 2026-06-29 17:22:15 |
| [keras](https://github.com/keras-team/keras) | 64102 | 19744 | 12809 | 9530 | 214 | 2026-06-30 03:44:57 |
| [pandas](https://github.com/pandas-dev/pandas) | 49223 | 20060 | 28351 | 37646 | 3008 | 2026-06-30 02:49:47 |
| [ray](https://github.com/ray-project/ray) | 43056 | 7743 | 22792 | 41253 | 3480 | 2026-06-30 02:26:38 |
| [gym](https://github.com/openai/gym) | 37243 | 8698 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33704 | 4689 | 5763 | 4098 | 218 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32403 | 12501 | 13973 | 17741 | 2407 | 2026-06-30 01:27:22 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30091 | 7072 | 3967 | 5023 | 84 | 2026-06-25 23:24:23 |
| [celery](https://github.com/celery/celery) | 28629 | 5086 | 5284 | 4162 | 791 | 2026-06-27 11:27:51 |
| [dash](https://github.com/plotly/dash) | 24277 | 2302 | 2121 | 1613 | 557 | 2026-06-29 20:13:40 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22940 | 8363 | 11337 | 20571 | 1461 | 2026-06-29 20:44:00 |
| [tornado](https://github.com/tornadoweb/tornado) | 22187 | 5530 | 1876 | 1758 | 219 | 2026-06-26 00:55:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22151 | 1449 | 1358 | 6767 | 402 | 2026-06-29 13:32:56 |
| [micropython](https://github.com/micropython/micropython) | 21848 | 8888 | 6078 | 7910 | 1639 | 2026-06-30 01:37:45 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18643 | 2816 | 3362 | 2099 | 768 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1590 | 1468 | 1690 | 134 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16465 | 2335 | 3222 | 9445 | 229 | 2026-06-29 10:53:33 |
| [httpx](https://github.com/encode/httpx) | 15324 | 1183 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14789 | 5776 | 11509 | 13998 | 1828 | 2026-06-29 19:37:20 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13933 | 2115 | 2655 | 1187 | 228 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13856 | 1894 | 5541 | 6631 | 1251 | 2026-06-29 22:02:52 |
| [starlette](https://github.com/Kludex/starlette) | 12443 | 1213 | 770 | 1960 | 50 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11952 | 1705 | 8234 | 1124 | 208 | 2026-06-27 22:33:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11838 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1003 | 1131 | 1467 | 165 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9105 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8770 | 1500 | 864 | 636 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7278 | 400 | 894 | 2561 | 325 | 2026-06-29 23:32:42 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5594 | 492 | 1259 | 864 | 523 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5305 | 1025 | 916 | 309 | 206 | 2026-06-29 06:46:27 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4229 | 346 | 1186 | 228 | 120 | 2026-06-25 15:21:25 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 890 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2494 | 214 | 447 | 672 | 83 | 2026-06-29 23:43:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 909 | 1084 | 1547 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-29 17:47:29 |
| [pypy](https://github.com/pypy/pypy) | 1758 | 118 | 5228 | 265 | 739 | 2026-06-30 04:10:00 |
| [jython](https://github.com/jython/jython) | 1518 | 230 | 297 | 137 | 111 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-30T04:17:15*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
