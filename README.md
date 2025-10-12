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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191981 | 74907 | 40855 | 59219 | 1921 | 2025-10-12 00:19:57 |
| [transformers](https://github.com/huggingface/transformers) | 150902 | 30734 | 18040 | 22894 | 2050 | 2025-10-10 20:27:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 93849 | 25523 | 54228 | 110546 | 16963 | 2025-10-12 01:37:24 |
| [fastapi](https://github.com/fastapi/fastapi) | 90634 | 8025 | 3469 | 4770 | 195 | 2025-10-11 19:36:57 |
| [django](https://github.com/django/django) | 85379 | 33081 | 0 | 19878 | 351 | 2025-10-11 17:03:38 |
| [flask](https://github.com/pallets/flask) | 70544 | 16558 | 2699 | 2707 | 11 | 2025-09-20 00:33:34 |
| [cpython](https://github.com/python/cpython) | 69301 | 33068 | 73891 | 65152 | 9140 | 2025-10-11 22:52:02 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 63632 | 26313 | 11757 | 19590 | 2141 | 2025-10-11 07:00:01 |
| [keras](https://github.com/keras-team/keras) | 63465 | 19621 | 12564 | 8385 | 260 | 2025-10-11 04:36:53 |
| [pandas](https://github.com/pandas-dev/pandas) | 46799 | 19115 | 27776 | 34833 | 3635 | 2025-10-09 15:40:23 |
| [ray](https://github.com/ray-project/ray) | 39291 | 6867 | 21549 | 35750 | 3146 | 2025-10-12 01:25:27 |
| [gym](https://github.com/openai/gym) | 36661 | 8707 | 1837 | 1467 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32631 | 4596 | 5723 | 4071 | 208 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30553 | 11553 | 13584 | 16281 | 2359 | 2025-10-11 16:21:21 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29548 | 7013 | 3945 | 4843 | 102 | 2025-10-09 17:47:30 |
| [celery](https://github.com/celery/celery) | 27326 | 4859 | 5171 | 3683 | 757 | 2025-10-09 22:09:29 |
| [dash](https://github.com/plotly/dash) | 24151 | 2214 | 2009 | 1350 | 573 | 2025-10-10 18:50:23 |
| [tornado](https://github.com/tornadoweb/tornado) | 22292 | 5534 | 1852 | 1674 | 207 | 2025-09-17 17:43:47 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21804 | 8062 | 11006 | 19599 | 1629 | 2025-10-10 18:28:41 |
| [micropython](https://github.com/micropython/micropython) | 20931 | 8479 | 5843 | 7264 | 1769 | 2025-10-10 23:49:42 |
| [RustPython](https://github.com/RustPython/RustPython) | 20596 | 1351 | 1221 | 4902 | 453 | 2025-10-06 13:41:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18513 | 1578 | 1450 | 1627 | 145 | 2025-09-14 20:50:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17822 | 2723 | 3264 | 1964 | 725 | 2025-10-09 18:25:56 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16029 | 2132 | 3150 | 8184 | 268 | 2025-10-11 18:54:15 |
| [httpx](https://github.com/encode/httpx) | 14622 | 959 | 919 | 1740 | 101 | 2025-10-04 17:54:39 |
| [scipy](https://github.com/scipy/scipy) | 14077 | 5497 | 11070 | 12674 | 1769 | 2025-10-11 23:26:04 |
| [dask](https://github.com/dask/dask) | 13525 | 1803 | 5441 | 6360 | 1194 | 2025-10-10 12:26:51 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13487 | 2036 | 2630 | 1149 | 192 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/Kludex/starlette) | 11539 | 1043 | 754 | 1719 | 48 | 2025-10-11 10:39:18 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11317 | 578 | 391 | 292 | 143 | 2025-10-10 03:26:18 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11001 | 1585 | 8097 | 988 | 219 | 2025-10-11 20:05:20 |
| [falcon](https://github.com/falconry/falcon) | 9730 | 966 | 1106 | 1376 | 166 | 2025-10-08 07:26:57 |
| [bottle](https://github.com/bottlepy/bottle) | 8669 | 1485 | 855 | 624 | 284 | 2025-09-19 11:25:45 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8611 | 527 | 950 | 440 | 416 | 2025-10-10 15:53:50 |
| [hug](https://github.com/hugapi/hug) | 6897 | 388 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [trio](https://github.com/python-trio/trio) | 6894 | 368 | 872 | 2458 | 311 | 2025-10-06 22:56:19 |
| [eve](https://github.com/pyeve/eve) | 6734 | 745 | 978 | 576 | 31 | 2025-08-31 06:07:38 |
| [vibora](https://github.com/vibora-io/vibora) | 5629 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5326 | 439 | 1195 | 713 | 500 | 2025-09-23 12:07:12 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5027 | 947 | 871 | 261 | 168 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4049 | 884 | 1061 | 2720 | 89 | 2025-09-04 12:08:14 |
| [databases](https://github.com/encode/databases) | 3930 | 260 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3680 | 292 | 1162 | 196 | 117 | 2025-10-11 18:40:46 |
| [quart](https://github.com/pallets/quart) | 3490 | 189 | 277 | 122 | 62 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2692 | 303 | 652 | 1261 | 309 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2313 | 131 | 426 | 392 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2244 | 166 | 406 | 524 | 68 | 2025-10-08 12:15:25 |
| [web2py](https://github.com/web2py/web2py) | 2166 | 908 | 1077 | 1460 | 368 | 2025-10-01 15:22:46 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1925 | 369 | 1780 | 264 | 260 | 2025-10-06 17:57:17 |
| [pypy](https://github.com/pypy/pypy) | 1525 | 88 | 5149 | 171 | 737 | 2025-10-10 06:55:50 |
| [jython](https://github.com/jython/jython) | 1438 | 224 | 282 | 113 | 101 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 810 | 82 | 100 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-10-06 17:16:06 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-10-12T02:00:13*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
