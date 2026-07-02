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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195888 | 75245 | 41584 | 77350 | 2647 | 2026-07-02 04:11:21 |
| [transformers](https://github.com/huggingface/transformers) | 162101 | 33719 | 19128 | 27153 | 2460 | 2026-07-02 01:49:47 |
| [pytorch](https://github.com/pytorch/pytorch) | 101030 | 28208 | 59566 | 128572 | 18274 | 2026-07-02 04:10:31 |
| [fastapi](https://github.com/fastapi/fastapi) | 99869 | 9520 | 3538 | 6029 | 93 | 2026-07-01 16:35:19 |
| [django](https://github.com/django/django) | 87919 | 33921 | 0 | 21495 | 458 | 2026-07-02 02:03:34 |
| [cpython](https://github.com/python/cpython) | 73408 | 34804 | 77005 | 73503 | 9465 | 2026-07-02 03:22:21 |
| [flask](https://github.com/pallets/flask) | 71792 | 16895 | 2753 | 2843 | 6 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66524 | 27134 | 12166 | 21071 | 2108 | 2026-07-01 15:33:00 |
| [keras](https://github.com/keras-team/keras) | 64104 | 19749 | 12808 | 9540 | 214 | 2026-07-01 17:25:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49108 | 20069 | 28353 | 37657 | 3001 | 2026-07-01 22:12:32 |
| [ray](https://github.com/ray-project/ray) | 43082 | 7749 | 22800 | 41301 | 3477 | 2026-07-02 04:00:19 |
| [gym](https://github.com/openai/gym) | 37247 | 8698 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33705 | 4690 | 5763 | 4099 | 219 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32295 | 12519 | 13978 | 17762 | 2410 | 2026-07-01 21:07:00 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30086 | 7072 | 3967 | 5024 | 83 | 2026-07-01 13:12:05 |
| [celery](https://github.com/celery/celery) | 28635 | 5088 | 5286 | 4164 | 793 | 2026-07-01 04:36:29 |
| [dash](https://github.com/plotly/dash) | 24284 | 2303 | 2121 | 1614 | 549 | 2026-07-01 01:20:54 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22947 | 8364 | 11340 | 20578 | 1462 | 2026-07-01 19:17:53 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5530 | 1875 | 1770 | 228 | 2026-06-26 00:55:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22153 | 1449 | 1359 | 6773 | 391 | 2026-06-30 14:49:27 |
| [micropython](https://github.com/micropython/micropython) | 21854 | 8892 | 6080 | 7914 | 1639 | 2026-07-02 01:58:00 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18648 | 2817 | 3363 | 2100 | 770 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18628 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16468 | 2340 | 3222 | 9465 | 240 | 2026-07-01 11:18:52 |
| [httpx](https://github.com/encode/httpx) | 15327 | 1186 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14796 | 5786 | 11512 | 14013 | 1828 | 2026-07-01 21:45:54 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13936 | 2115 | 2655 | 1187 | 228 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13857 | 1895 | 5538 | 6633 | 1250 | 2026-07-01 16:46:02 |
| [starlette](https://github.com/Kludex/starlette) | 12442 | 1215 | 770 | 1966 | 54 | 2026-07-01 19:18:01 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11952 | 1704 | 8236 | 1126 | 212 | 2026-06-27 22:33:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11843 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9797 | 1004 | 1132 | 1468 | 163 | 2026-07-01 06:50:52 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9111 | 598 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8769 | 1499 | 864 | 636 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7281 | 403 | 894 | 2564 | 325 | 2026-07-01 07:17:50 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5594 | 493 | 1260 | 864 | 524 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5304 | 1025 | 916 | 310 | 204 | 2026-07-01 09:02:58 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4231 | 345 | 1186 | 228 | 119 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 891 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3646 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2493 | 214 | 448 | 674 | 86 | 2026-06-29 23:43:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 910 | 1084 | 1549 | 363 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-29 17:47:29 |
| [pypy](https://github.com/pypy/pypy) | 1757 | 119 | 5229 | 266 | 740 | 2026-07-01 20:31:28 |
| [jython](https://github.com/jython/jython) | 1519 | 231 | 297 | 137 | 110 | 2026-06-30 12:03:48 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-02T04:12:26*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
