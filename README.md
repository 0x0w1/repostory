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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196577 | 75624 | 41631 | 78945 | 2872 | 2026-07-28 03:15:28 |
| [transformers](https://github.com/huggingface/transformers) | 163049 | 34043 | 19238 | 27623 | 2344 | 2026-07-28 02:38:02 |
| [pytorch](https://github.com/pytorch/pytorch) | 102027 | 28559 | 60038 | 130612 | 18334 | 2026-07-28 03:00:43 |
| [fastapi](https://github.com/fastapi/fastapi) | 100958 | 9696 | 3542 | 6152 | 88 | 2026-07-27 17:33:01 |
| [django](https://github.com/django/django) | 88234 | 34011 | 0 | 21564 | 446 | 2026-07-28 00:34:53 |
| [cpython](https://github.com/python/cpython) | 73957 | 35026 | 77425 | 75023 | 9488 | 2026-07-28 02:30:28 |
| [flask](https://github.com/pallets/flask) | 72024 | 16924 | 2757 | 2876 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66796 | 27223 | 12204 | 21194 | 2112 | 2026-07-27 18:36:58 |
| [keras](https://github.com/keras-team/keras) | 64184 | 19742 | 12852 | 9627 | 222 | 2026-07-28 02:47:45 |
| [pandas](https://github.com/pandas-dev/pandas) | 49344 | 20175 | 28421 | 37966 | 2885 | 2026-07-27 21:39:23 |
| [ray](https://github.com/ray-project/ray) | 43373 | 7841 | 22881 | 41779 | 3492 | 2026-07-28 02:06:02 |
| [gym](https://github.com/openai/gym) | 37246 | 8687 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33779 | 4699 | 5767 | 4106 | 229 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32438 | 12593 | 14023 | 18011 | 2323 | 2026-07-27 22:51:36 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30107 | 7075 | 3966 | 5033 | 72 | 2026-07-27 22:18:34 |
| [celery](https://github.com/celery/celery) | 28732 | 5113 | 5288 | 4195 | 782 | 2026-07-27 14:09:39 |
| [dash](https://github.com/plotly/dash) | 24355 | 2308 | 2131 | 1662 | 534 | 2026-07-27 16:48:28 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23040 | 8419 | 11374 | 20684 | 1472 | 2026-07-27 23:07:30 |
| [RustPython](https://github.com/RustPython/RustPython) | 22229 | 1468 | 1400 | 6929 | 409 | 2026-07-28 01:20:05 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5546 | 1876 | 1790 | 240 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21942 | 8917 | 6110 | 7990 | 1572 | 2026-07-27 04:26:11 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18692 | 2826 | 3372 | 2119 | 775 | 2026-07-28 01:45:57 |
| [sanic](https://github.com/sanic-org/sanic) | 18641 | 1591 | 1470 | 1696 | 138 | 2026-07-20 04:32:32 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16505 | 2358 | 3226 | 9697 | 214 | 2026-07-28 00:02:16 |
| [httpx](https://github.com/encode/httpx) | 15371 | 1218 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14854 | 5827 | 11546 | 14151 | 1842 | 2026-07-27 22:29:43 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13978 | 2128 | 2655 | 1205 | 222 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13871 | 1916 | 5544 | 6667 | 1275 | 2026-07-27 22:03:03 |
| [starlette](https://github.com/Kludex/starlette) | 12501 | 1241 | 772 | 1985 | 70 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12029 | 1724 | 8249 | 1153 | 208 | 2026-07-27 15:12:30 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11870 | 612 | 417 | 326 | 156 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9791 | 1021 | 1139 | 1493 | 162 | 2026-07-27 04:23:32 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9152 | 602 | 1040 | 526 | 222 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8773 | 1503 | 865 | 642 | 287 | 2026-07-19 07:21:52 |
| [trio](https://github.com/python-trio/trio) | 7307 | 410 | 898 | 2582 | 327 | 2026-07-27 21:57:27 |
| [hug](https://github.com/hugapi/hug) | 6884 | 389 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6748 | 738 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5608 | 500 | 1265 | 877 | 536 | 2026-07-25 01:15:20 |
| [vibora](https://github.com/vibora-io/vibora) | 5588 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5333 | 1028 | 923 | 314 | 198 | 2026-07-27 05:59:11 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4281 | 356 | 1190 | 235 | 124 | 2026-07-20 11:25:23 |
| [pyramid](https://github.com/Pylons/pyramid) | 4092 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4001 | 265 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3653 | 202 | 284 | 133 | 42 | 2026-07-23 20:25:20 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2757 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2515 | 230 | 458 | 711 | 95 | 2026-07-27 23:44:03 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2360 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2168 | 915 | 1084 | 1580 | 358 | 2026-07-24 11:00:35 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1945 | 367 | 1785 | 269 | 267 | 2026-07-27 17:48:12 |
| [pypy](https://github.com/pypy/pypy) | 1771 | 121 | 5237 | 276 | 722 | 2026-07-27 20:57:40 |
| [jython](https://github.com/jython/jython) | 1527 | 231 | 299 | 147 | 105 | 2026-07-26 19:12:04 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 83 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-28T03:22:33*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
