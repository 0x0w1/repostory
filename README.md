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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196387 | 75592 | 41614 | 78405 | 2823 | 2026-07-20 03:50:08 |
| [transformers](https://github.com/huggingface/transformers) | 162747 | 33942 | 19200 | 27487 | 2461 | 2026-07-17 16:52:51 |
| [pytorch](https://github.com/pytorch/pytorch) | 101781 | 28433 | 59917 | 129951 | 18303 | 2026-07-20 03:48:00 |
| [fastapi](https://github.com/fastapi/fastapi) | 100676 | 9643 | 3541 | 6109 | 97 | 2026-07-17 14:03:18 |
| [django](https://github.com/django/django) | 88176 | 34116 | 0 | 21575 | 455 | 2026-07-17 18:44:35 |
| [cpython](https://github.com/python/cpython) | 73829 | 34953 | 77287 | 74575 | 9525 | 2026-07-19 22:19:32 |
| [flask](https://github.com/pallets/flask) | 71982 | 16910 | 2756 | 2868 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66726 | 27198 | 12188 | 21148 | 2129 | 2026-07-20 01:52:16 |
| [keras](https://github.com/keras-team/keras) | 64166 | 19744 | 12847 | 9594 | 233 | 2026-07-17 21:24:44 |
| [pandas](https://github.com/pandas-dev/pandas) | 49229 | 20146 | 28401 | 37873 | 2966 | 2026-07-20 00:32:39 |
| [ray](https://github.com/ray-project/ray) | 43288 | 7807 | 22857 | 41615 | 3479 | 2026-07-19 21:56:41 |
| [gym](https://github.com/openai/gym) | 37241 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33755 | 4696 | 5768 | 4104 | 228 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32398 | 12577 | 14007 | 17947 | 2374 | 2026-07-19 09:24:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30105 | 7074 | 3967 | 5027 | 85 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28699 | 5109 | 5288 | 4190 | 784 | 2026-07-19 16:04:39 |
| [dash](https://github.com/plotly/dash) | 24333 | 2308 | 2130 | 1648 | 535 | 2026-07-17 13:33:19 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23019 | 8407 | 11364 | 20646 | 1479 | 2026-07-19 02:37:15 |
| [RustPython](https://github.com/RustPython/RustPython) | 22209 | 1466 | 1384 | 6869 | 397 | 2026-07-19 05:13:47 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5541 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21910 | 8912 | 6101 | 7967 | 1587 | 2026-07-17 13:35:37 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18683 | 2826 | 3372 | 2113 | 779 | 2026-07-16 19:56:56 |
| [sanic](https://github.com/sanic-org/sanic) | 18634 | 1588 | 1468 | 1692 | 133 | 2026-07-15 18:25:33 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16501 | 2355 | 3224 | 9603 | 217 | 2026-07-20 00:51:19 |
| [httpx](https://github.com/encode/httpx) | 15355 | 1211 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14830 | 5808 | 11537 | 14101 | 1849 | 2026-07-19 20:47:01 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13970 | 2127 | 2656 | 1204 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13862 | 1907 | 5541 | 6656 | 1263 | 2026-07-14 13:22:10 |
| [starlette](https://github.com/Kludex/starlette) | 12488 | 1233 | 771 | 1978 | 62 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12006 | 1721 | 8245 | 1144 | 206 | 2026-07-19 15:07:27 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11864 | 611 | 417 | 325 | 155 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9792 | 1021 | 1138 | 1486 | 173 | 2026-07-19 20:57:19 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9139 | 602 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7297 | 409 | 896 | 2573 | 327 | 2026-07-16 04:09:29 |
| [hug](https://github.com/hugapi/hug) | 6884 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5609 | 499 | 1264 | 875 | 533 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5325 | 1029 | 921 | 313 | 205 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4263 | 351 | 1189 | 233 | 125 | 2026-07-16 17:14:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 262 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3648 | 204 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2755 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2509 | 224 | 455 | 702 | 96 | 2026-07-19 22:04:37 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 913 | 1084 | 1573 | 362 | 2026-07-17 15:38:00 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 367 | 1785 | 269 | 267 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1767 | 119 | 5237 | 271 | 724 | 2026-07-19 20:20:02 |
| [jython](https://github.com/jython/jython) | 1527 | 231 | 298 | 140 | 102 | 2026-07-19 06:34:16 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-20T03:51:11*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
