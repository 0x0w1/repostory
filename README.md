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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 201367 | 78295 | 41962 | 84472 | 3499 | 2026-11-07 05:38:03 |
| [transformers](https://github.com/huggingface/transformers) | 168612 | 35126 | 19802 | 29828 | 1053 | 2026-11-07 00:48:00 |
| [pytorch](https://github.com/pytorch/pytorch) | 105224 | 31311 | 62365 | 140830 | 18089 | 2026-11-07 05:27:28 |
| [fastapi](https://github.com/fastapi/fastapi) | 104531 | 10202 | 3555 | 6571 | 59 | 2026-11-06 11:41:08 |
| [django](https://github.com/django/django) | 91672 | 35967 | 0 | 22179 | 535 | 2026-11-06 22:17:53 |
| [cpython](https://github.com/python/cpython) | 78064 | 37182 | 79169 | 79967 | 9258 | 2026-11-07 01:00:20 |
| [flask](https://github.com/pallets/flask) | 75056 | 17284 | 2777 | 2912 | 4 | 2026-10-30 15:05:22 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 68074 | 27642 | 12368 | 21769 | 2159 | 2026-11-06 12:37:21 |
| [keras](https://github.com/keras-team/keras) | 64416 | 19815 | 13067 | 10224 | 283 | 2026-11-06 21:43:00 |
| [pandas](https://github.com/pandas-dev/pandas) | 50503 | 20727 | 28667 | 39837 | 1984 | 2026-11-06 21:58:33 |
| [ray](https://github.com/ray-project/ray) | 44224 | 8251 | 23293 | 44171 | 3722 | 2026-11-07 03:19:47 |
| [gym](https://github.com/openai/gym) | 37232 | 8665 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 34034 | 4740 | 5782 | 4143 | 265 | 2026-10-27 12:27:21 |
| [numpy](https://github.com/numpy/numpy) | 33376 | 13091 | 14170 | 18971 | 2241 | 2026-11-06 19:17:55 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30228 | 7096 | 3966 | 5105 | 64 | 2026-11-05 00:01:21 |
| [celery](https://github.com/celery/celery) | 29134 | 5257 | 5360 | 4697 | 743 | 2026-11-07 03:37:19 |
| [dash](https://github.com/plotly/dash) | 24478 | 2341 | 2178 | 1822 | 447 | 2026-11-06 15:40:44 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23428 | 8543 | 11455 | 21034 | 1472 | 2026-11-06 19:14:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22460 | 1509 | 1456 | 8176 | 324 | 2026-11-07 00:29:16 |
| [micropython](https://github.com/micropython/micropython) | 22179 | 9044 | 6169 | 8220 | 1576 | 2026-11-06 12:22:36 |
| [tornado](https://github.com/tornadoweb/tornado) | 22163 | 5606 | 1891 | 1910 | 223 | 2026-11-06 22:24:20 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18879 | 2894 | 3402 | 2280 | 755 | 2026-11-06 21:47:19 |
| [sanic](https://github.com/sanic-org/sanic) | 18629 | 1615 | 1473 | 1688 | 161 | 2026-07-29 03:09:51 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16605 | 2510 | 3273 | 10660 | 302 | 2026-11-07 03:31:03 |
| [httpx](https://github.com/encode/httpx) | 15742 | 2586 | 925 | 1806 | 140 | 2026-10-02 12:53:43 |
| [scipy](https://github.com/scipy/scipy) | 15191 | 6067 | 11757 | 14856 | 1913 | 2026-11-07 05:16:56 |
| [seaborn](https://github.com/mwaskom/seaborn) | 14098 | 2158 | 2668 | 1253 | 253 | 2026-10-08 01:29:20 |
| [dask](https://github.com/dask/dask) | 13941 | 2018 | 5582 | 6810 | 1427 | 2026-09-29 10:11:03 |
| [starlette](https://github.com/Kludex/starlette) | 12711 | 1436 | 795 | 2305 | 32 | 2026-11-06 12:31:17 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12273 | 1844 | 8380 | 1260 | 215 | 2026-11-04 15:12:57 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11930 | 618 | 429 | 344 | 174 | 2026-10-19 14:08:49 |
| [falcon](https://github.com/falconry/falcon) | 9813 | 1053 | 1150 | 1568 | 165 | 2026-11-04 21:49:13 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9237 | 627 | 1057 | 610 | 155 | 2026-11-06 14:41:48 |
| [bottle](https://github.com/bottlepy/bottle) | 8798 | 1515 | 866 | 656 | 289 | 2026-10-25 16:40:59 |
| [trio](https://github.com/python-trio/trio) | 7357 | 469 | 910 | 2662 | 341 | 2026-11-03 05:35:02 |
| [hug](https://github.com/hugapi/hug) | 6871 | 391 | 466 | 465 | 189 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6750 | 737 | 979 | 594 | 30 | 2026-10-21 11:33:23 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5645 | 543 | 1307 | 988 | 563 | 2026-11-07 04:17:10 |
| [vibora](https://github.com/vibora-io/vibora) | 5580 | 300 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5445 | 1054 | 938 | 329 | 208 | 2026-09-04 08:16:50 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4467 | 391 | 1211 | 259 | 117 | 2026-10-30 14:10:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4102 | 896 | 1066 | 2742 | 91 | 2026-08-04 21:13:50 |
| [databases](https://github.com/encode/databases) | 3985 | 278 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3680 | 210 | 289 | 137 | 26 | 2026-09-12 09:07:36 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2762 | 319 | 681 | 1409 | 261 | 2026-11-07 04:41:51 |
| [anyio](https://github.com/agronholm/anyio) | 2568 | 348 | 497 | 883 | 143 | 2026-11-03 20:41:26 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2356 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2167 | 915 | 1085 | 1611 | 356 | 2026-11-03 14:17:32 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1949 | 371 | 1791 | 279 | 279 | 2026-11-06 00:44:46 |
| [pypy](https://github.com/pypy/pypy) | 1822 | 131 | 5299 | 406 | 720 | 2026-11-06 23:24:41 |
| [jython](https://github.com/jython/jython) | 1551 | 233 | 305 | 158 | 104 | 2026-10-25 14:30:44 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 84 | 103 | 39 | 16 | 2026-11-02 09:16:55 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 22 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 449 | 117 | 78 | 2026-10-11 16:30:07 |
| [circuits](https://github.com/circuits/circuits) | 316 | 55 | 149 | 196 | 41 | 2026-10-05 23:26:25 |

*Last Automatic Update: 2026-11-07T05:42:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
