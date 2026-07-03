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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 195977 | 75258 | 41584 | 77408 | 2631 | 2026-07-03 03:04:47 |
| [transformers](https://github.com/huggingface/transformers) | 162173 | 33730 | 19134 | 27172 | 2463 | 2026-07-03 03:28:11 |
| [pytorch](https://github.com/pytorch/pytorch) | 101266 | 28228 | 59595 | 128652 | 18280 | 2026-07-03 03:39:16 |
| [fastapi](https://github.com/fastapi/fastapi) | 99925 | 9530 | 3538 | 6036 | 99 | 2026-07-01 16:35:19 |
| [django](https://github.com/django/django) | 87970 | 33942 | 0 | 21498 | 453 | 2026-07-03 02:38:41 |
| [cpython](https://github.com/python/cpython) | 73459 | 34809 | 77016 | 73568 | 9447 | 2026-07-03 02:56:16 |
| [flask](https://github.com/pallets/flask) | 71796 | 16894 | 2754 | 2851 | 7 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66538 | 27139 | 12166 | 21076 | 2109 | 2026-07-02 17:30:11 |
| [keras](https://github.com/keras-team/keras) | 64105 | 19751 | 12808 | 9546 | 217 | 2026-07-01 17:25:07 |
| [pandas](https://github.com/pandas-dev/pandas) | 49111 | 20077 | 28353 | 37673 | 3012 | 2026-07-02 17:16:07 |
| [ray](https://github.com/ray-project/ray) | 43098 | 7751 | 22804 | 41330 | 3475 | 2026-07-03 01:06:05 |
| [gym](https://github.com/openai/gym) | 37247 | 8697 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33707 | 4690 | 5763 | 4099 | 219 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32301 | 12525 | 13978 | 17782 | 2418 | 2026-07-02 22:23:28 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30088 | 7071 | 3967 | 5025 | 84 | 2026-07-02 18:50:14 |
| [celery](https://github.com/celery/celery) | 28643 | 5090 | 5286 | 4165 | 794 | 2026-07-01 04:36:29 |
| [dash](https://github.com/plotly/dash) | 24286 | 2302 | 2122 | 1615 | 548 | 2026-07-02 20:24:31 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22947 | 8367 | 11342 | 20584 | 1466 | 2026-07-02 18:16:04 |
| [tornado](https://github.com/tornadoweb/tornado) | 22188 | 5530 | 1875 | 1775 | 233 | 2026-06-26 00:55:24 |
| [RustPython](https://github.com/RustPython/RustPython) | 22155 | 1449 | 1360 | 6773 | 386 | 2026-07-02 07:41:31 |
| [micropython](https://github.com/micropython/micropython) | 21859 | 8893 | 6080 | 7914 | 1636 | 2026-07-03 03:56:01 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18652 | 2817 | 3363 | 2100 | 769 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18627 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16471 | 2340 | 3222 | 9474 | 247 | 2026-07-02 11:11:23 |
| [httpx](https://github.com/encode/httpx) | 15329 | 1186 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14799 | 5788 | 11514 | 14016 | 1830 | 2026-07-02 12:19:45 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13935 | 2115 | 2655 | 1187 | 228 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13859 | 1894 | 5538 | 6634 | 1250 | 2026-07-01 16:46:02 |
| [starlette](https://github.com/Kludex/starlette) | 12446 | 1217 | 770 | 1966 | 54 | 2026-07-01 19:18:01 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11955 | 1703 | 8237 | 1126 | 212 | 2026-06-27 22:33:10 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11844 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9796 | 1005 | 1132 | 1469 | 164 | 2026-07-01 06:50:52 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9113 | 598 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8769 | 1500 | 864 | 637 | 285 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7282 | 402 | 894 | 2565 | 326 | 2026-07-01 07:17:50 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6743 | 739 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5596 | 493 | 1260 | 864 | 524 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5590 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5307 | 1025 | 917 | 310 | 203 | 2026-07-02 05:35:42 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4233 | 345 | 1187 | 228 | 120 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 891 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3646 | 202 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2754 | 313 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2496 | 214 | 448 | 674 | 86 | 2026-06-29 23:43:55 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 911 | 1084 | 1552 | 359 | 2026-07-02 16:06:40 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-29 17:47:29 |
| [pypy](https://github.com/pypy/pypy) | 1757 | 119 | 5229 | 266 | 740 | 2026-07-01 20:31:28 |
| [jython](https://github.com/jython/jython) | 1520 | 231 | 297 | 137 | 110 | 2026-06-30 12:03:48 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-03T03:59:09*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
