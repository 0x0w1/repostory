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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196311 | 75516 | 41598 | 77990 | 2656 | 2026-07-14 03:10:22 |
| [transformers](https://github.com/huggingface/transformers) | 162577 | 33877 | 19177 | 27401 | 2480 | 2026-07-14 03:05:30 |
| [pytorch](https://github.com/pytorch/pytorch) | 101795 | 28479 | 59779 | 129410 | 18350 | 2026-07-14 03:13:21 |
| [fastapi](https://github.com/fastapi/fastapi) | 100446 | 9601 | 3540 | 6074 | 99 | 2026-07-13 19:49:34 |
| [django](https://github.com/django/django) | 88191 | 34170 | 0 | 21544 | 455 | 2026-07-13 20:54:48 |
| [cpython](https://github.com/python/cpython) | 73782 | 35006 | 77166 | 74166 | 9418 | 2026-07-13 23:13:24 |
| [flask](https://github.com/pallets/flask) | 71920 | 16901 | 2756 | 2862 | 8 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66674 | 27164 | 12174 | 21113 | 2103 | 2026-07-14 02:41:34 |
| [keras](https://github.com/keras-team/keras) | 64171 | 19737 | 12822 | 9567 | 226 | 2026-07-14 00:22:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 49183 | 20115 | 28383 | 37834 | 3018 | 2026-07-14 02:55:55 |
| [ray](https://github.com/ray-project/ray) | 43234 | 7790 | 22841 | 41498 | 3478 | 2026-07-14 00:43:32 |
| [gym](https://github.com/openai/gym) | 37251 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33741 | 4691 | 5766 | 4102 | 224 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32356 | 12558 | 13998 | 17901 | 2400 | 2026-07-14 01:19:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30100 | 7075 | 3967 | 5026 | 84 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28680 | 5100 | 5287 | 4178 | 788 | 2026-07-13 16:57:57 |
| [dash](https://github.com/plotly/dash) | 24311 | 2305 | 2126 | 1646 | 543 | 2026-07-13 18:03:53 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22993 | 8389 | 11355 | 20620 | 1473 | 2026-07-11 04:57:56 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5539 | 1876 | 1794 | 245 | 2026-07-08 17:05:41 |
| [RustPython](https://github.com/RustPython/RustPython) | 22182 | 1464 | 1371 | 6836 | 404 | 2026-07-13 14:11:23 |
| [micropython](https://github.com/micropython/micropython) | 21894 | 8903 | 6097 | 7947 | 1612 | 2026-07-13 14:20:49 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18678 | 2822 | 3367 | 2105 | 773 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18631 | 1588 | 1467 | 1691 | 133 | 2026-07-12 07:17:35 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16509 | 2344 | 3222 | 9563 | 212 | 2026-07-14 01:18:18 |
| [httpx](https://github.com/encode/httpx) | 15360 | 1202 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14816 | 5802 | 11523 | 14075 | 1845 | 2026-07-13 22:23:17 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13954 | 2124 | 2656 | 1202 | 220 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13855 | 1904 | 5540 | 6653 | 1264 | 2026-07-13 23:31:34 |
| [starlette](https://github.com/Kludex/starlette) | 12473 | 1225 | 771 | 1975 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11990 | 1711 | 8243 | 1138 | 209 | 2026-07-12 22:57:45 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11855 | 610 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9789 | 1013 | 1133 | 1479 | 170 | 2026-07-13 14:45:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9132 | 600 | 1039 | 520 | 216 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1502 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7293 | 409 | 895 | 2571 | 327 | 2026-07-13 23:34:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5605 | 497 | 1263 | 871 | 529 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5322 | 1029 | 920 | 312 | 204 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4253 | 349 | 1187 | 230 | 122 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 312 | 675 | 1335 | 312 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2503 | 218 | 453 | 691 | 92 | 2026-07-13 23:43:53 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 913 | 1084 | 1565 | 359 | 2026-07-13 09:42:09 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 266 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1764 | 118 | 5235 | 271 | 738 | 2026-07-13 09:42:23 |
| [jython](https://github.com/jython/jython) | 1524 | 232 | 298 | 139 | 103 | 2026-07-13 11:30:52 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-14T03:18:10*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
