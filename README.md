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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196108 | 75322 | 41591 | 77637 | 2664 | 2026-07-08 03:31:02 |
| [transformers](https://github.com/huggingface/transformers) | 162358 | 33815 | 19154 | 27270 | 2459 | 2026-07-08 02:47:18 |
| [pytorch](https://github.com/pytorch/pytorch) | 101577 | 28294 | 59674 | 128930 | 18253 | 2026-07-08 03:33:03 |
| [fastapi](https://github.com/fastapi/fastapi) | 100216 | 9560 | 3538 | 6060 | 95 | 2026-07-07 19:03:20 |
| [django](https://github.com/django/django) | 87999 | 34008 | 0 | 21523 | 458 | 2026-07-07 20:43:48 |
| [cpython](https://github.com/python/cpython) | 73584 | 34831 | 77090 | 73877 | 9403 | 2026-07-08 01:40:04 |
| [flask](https://github.com/pallets/flask) | 71855 | 16897 | 2754 | 2857 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66630 | 27163 | 12169 | 21092 | 2110 | 2026-07-07 14:16:48 |
| [keras](https://github.com/keras-team/keras) | 64153 | 19755 | 12812 | 9560 | 229 | 2026-07-07 17:53:38 |
| [pandas](https://github.com/pandas-dev/pandas) | 49150 | 20103 | 28364 | 37735 | 3020 | 2026-07-07 20:09:55 |
| [ray](https://github.com/ray-project/ray) | 43154 | 7773 | 22815 | 41384 | 3453 | 2026-07-08 03:20:45 |
| [gym](https://github.com/openai/gym) | 37244 | 8695 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33721 | 4689 | 5764 | 4099 | 220 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32335 | 12541 | 13982 | 17835 | 2398 | 2026-07-07 22:59:17 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30098 | 7073 | 3967 | 5026 | 85 | 2026-07-02 18:50:14 |
| [celery](https://github.com/celery/celery) | 28656 | 5094 | 5286 | 4170 | 787 | 2026-07-07 15:50:35 |
| [dash](https://github.com/plotly/dash) | 24298 | 2305 | 2124 | 1634 | 545 | 2026-07-07 19:54:50 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22966 | 8385 | 11349 | 20602 | 1478 | 2026-07-07 16:46:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5531 | 1876 | 1788 | 241 | 2026-07-04 19:51:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22163 | 1450 | 1364 | 6796 | 383 | 2026-07-08 01:03:29 |
| [micropython](https://github.com/micropython/micropython) | 21878 | 8905 | 6092 | 7929 | 1628 | 2026-07-06 15:22:27 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18663 | 2820 | 3365 | 2117 | 771 | 2026-07-07 13:43:21 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1588 | 1467 | 1691 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16485 | 2346 | 3222 | 9530 | 239 | 2026-07-08 01:25:07 |
| [httpx](https://github.com/encode/httpx) | 15342 | 1192 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14808 | 5793 | 11516 | 14041 | 1833 | 2026-07-07 16:38:52 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13940 | 2119 | 2655 | 1198 | 215 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13857 | 1898 | 5540 | 6642 | 1259 | 2026-07-06 22:02:56 |
| [starlette](https://github.com/Kludex/starlette) | 12458 | 1224 | 771 | 1975 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11973 | 1709 | 8239 | 1136 | 218 | 2026-07-07 19:57:06 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11850 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1011 | 1133 | 1475 | 169 | 2026-07-01 06:50:52 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9119 | 598 | 1038 | 518 | 215 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1501 | 865 | 638 | 286 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7288 | 404 | 895 | 2567 | 327 | 2026-07-06 22:45:42 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6746 | 740 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5600 | 493 | 1260 | 867 | 523 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5318 | 1025 | 918 | 310 | 203 | 2026-07-02 05:35:42 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4242 | 348 | 1187 | 229 | 121 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2497 | 216 | 451 | 681 | 96 | 2026-07-07 20:43:24 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1084 | 1556 | 362 | 2026-07-03 11:15:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-07-06 17:55:11 |
| [pypy](https://github.com/pypy/pypy) | 1760 | 118 | 5230 | 270 | 739 | 2026-07-08 03:06:20 |
| [jython](https://github.com/jython/jython) | 1523 | 231 | 297 | 138 | 111 | 2026-06-30 12:03:48 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-08T03:33:24*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
