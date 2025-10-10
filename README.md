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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191969 | 74902 | 40841 | 59101 | 1891 | 2025-10-10 01:07:56 |
| [transformers](https://github.com/huggingface/transformers) | 150822 | 30710 | 18031 | 22871 | 2045 | 2025-10-09 23:42:11 |
| [pytorch](https://github.com/pytorch/pytorch) | 93796 | 25508 | 54200 | 110442 | 16984 | 2025-10-10 01:44:08 |
| [fastapi](https://github.com/fastapi/fastapi) | 90548 | 8020 | 3470 | 4767 | 199 | 2025-10-09 22:43:57 |
| [django](https://github.com/django/django) | 85356 | 33069 | 0 | 19874 | 351 | 2025-10-09 18:03:14 |
| [flask](https://github.com/pallets/flask) | 70519 | 16555 | 2699 | 2707 | 11 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69250 | 33048 | 73859 | 65086 | 9143 | 2025-10-09 22:36:40 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63614 | 26310 | 11755 | 19577 | 2136 | 2025-10-09 16:01:50 |
| [keras](https://github.com/keras-team/keras) | 63464 | 19625 | 12563 | 8383 | 258 | 2025-10-09 19:51:29 |
| [pandas](https://github.com/pandas-dev/pandas) | 46780 | 19097 | 27771 | 34817 | 3617 | 2025-10-09 15:40:23 |
| [ray](https://github.com/ray-project/ray) | 39260 | 6864 | 21545 | 35724 | 3166 | 2025-10-10 01:48:26 |
| [gym](https://github.com/openai/gym) | 36649 | 8706 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32620 | 4594 | 5723 | 4071 | 208 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30541 | 11536 | 13581 | 16270 | 2360 | 2025-10-10 00:08:15 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29542 | 7013 | 3945 | 4843 | 102 | 2025-10-09 17:47:30 |
| [celery](https://github.com/celery/celery) | 27310 | 4856 | 5171 | 3682 | 756 | 2025-10-09 22:09:29 |
| [dash](https://github.com/plotly/dash) | 24146 | 2214 | 2009 | 1348 | 577 | 2025-10-10 00:26:34 |
| [tornado](https://github.com/tornadoweb/tornado) | 22289 | 5535 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21794 | 8059 | 11003 | 19598 | 1627 | 2025-10-08 23:01:10 |
| [micropython](https://github.com/micropython/micropython) | 20929 | 8473 | 5843 | 7262 | 1773 | 2025-10-08 23:40:14 |
| [RustPython](https://github.com/RustPython/RustPython) | 20582 | 1351 | 1221 | 4900 | 451 | 2025-10-06 13:41:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18509 | 1577 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17813 | 2722 | 3263 | 1963 | 724 | 2025-10-09 18:25:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16027 | 2130 | 3149 | 8176 | 265 | 2025-10-09 13:27:20 |
| [httpx](https://github.com/encode/httpx) | 14616 | 958 | 919 | 1740 | 101 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14073 | 5494 | 11064 | 12668 | 1759 | 2025-10-09 07:03:47 |
| [dask](https://github.com/dask/dask) | 13523 | 1802 | 5441 | 6360 | 1195 | 2025-10-09 09:59:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13484 | 2036 | 2629 | 1149 | 191 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11529 | 1043 | 754 | 1718 | 47 | 2025-10-09 08:49:35 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11314 | 578 | 391 | 289 | 144 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10986 | 1584 | 8096 | 988 | 220 | 2025-10-09 19:56:55 |
| [falcon](https://github.com/falconry/falcon) | 9727 | 966 | 1105 | 1376 | 165 | 2025-10-08 07:26:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8670 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8610 | 527 | 950 | 440 | 416 | 2025-10-01 08:01:23 |
| [hug](https://github.com/hugapi/hug) | 6897 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6888 | 368 | 872 | 2458 | 311 | 2025-10-06 22:56:19 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5629 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5320 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5028 | 947 | 871 | 261 | 168 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4048 | 885 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3930 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3675 | 292 | 1162 | 196 | 117 | 2025-10-09 19:54:15 |
| [quart](https://github.com/pallets/quart) | 3485 | 188 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2691 | 303 | 652 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2312 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2241 | 166 | 405 | 524 | 67 | 2025-10-08 12:15:25 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1924 | 369 | 1780 | 264 | 260 | 2025-10-06 17:57:17 |
| [pypy](https://github.com/pypy/pypy) | 1517 | 88 | 5149 | 171 | 737 | 2025-10-08 06:58:26 |
| [jython](https://github.com/jython/jython) | 1439 | 224 | 282 | 113 | 102 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-06 17:16:06 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-10T01:55:56*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
