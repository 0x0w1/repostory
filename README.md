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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196366 | 75564 | 41604 | 78189 | 2712 | 2026-07-16 03:12:32 |
| [transformers](https://github.com/huggingface/transformers) | 162634 | 33896 | 19186 | 27438 | 2491 | 2026-07-16 03:12:03 |
| [pytorch](https://github.com/pytorch/pytorch) | 101839 | 28511 | 59850 | 129665 | 18356 | 2026-07-16 03:20:46 |
| [fastapi](https://github.com/fastapi/fastapi) | 100558 | 9621 | 3540 | 6097 | 93 | 2026-07-15 14:37:14 |
| [django](https://github.com/django/django) | 88225 | 34178 | 0 | 21558 | 455 | 2026-07-15 12:10:33 |
| [cpython](https://github.com/python/cpython) | 73834 | 35016 | 77193 | 74257 | 9427 | 2026-07-15 18:15:25 |
| [flask](https://github.com/pallets/flask) | 71945 | 16906 | 2756 | 2866 | 10 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66688 | 27177 | 12179 | 21122 | 2111 | 2026-07-15 20:24:20 |
| [keras](https://github.com/keras-team/keras) | 64174 | 19739 | 12824 | 9573 | 213 | 2026-07-16 02:56:30 |
| [pandas](https://github.com/pandas-dev/pandas) | 49198 | 20126 | 28388 | 37850 | 2986 | 2026-07-16 01:52:43 |
| [ray](https://github.com/ray-project/ray) | 43254 | 7796 | 22846 | 41551 | 3453 | 2026-07-16 03:21:35 |
| [gym](https://github.com/openai/gym) | 37246 | 8690 | 1839 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33741 | 4692 | 5767 | 4102 | 225 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32372 | 12562 | 14000 | 17922 | 2398 | 2026-07-16 02:50:20 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30101 | 7073 | 3967 | 5026 | 84 | 2026-07-12 05:49:41 |
| [celery](https://github.com/celery/celery) | 28692 | 5103 | 5288 | 4182 | 781 | 2026-07-15 14:53:36 |
| [dash](https://github.com/plotly/dash) | 24318 | 2309 | 2128 | 1646 | 539 | 2026-07-15 18:26:57 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 23004 | 8394 | 11357 | 20625 | 1473 | 2026-07-15 21:50:39 |
| [RustPython](https://github.com/RustPython/RustPython) | 22196 | 1466 | 1373 | 6842 | 392 | 2026-07-15 22:23:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22190 | 5541 | 1876 | 1797 | 247 | 2026-07-08 17:05:41 |
| [micropython](https://github.com/micropython/micropython) | 21896 | 8906 | 6097 | 7956 | 1596 | 2026-07-15 05:36:42 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18679 | 2821 | 3368 | 2107 | 774 | 2026-07-09 14:52:06 |
| [sanic](https://github.com/sanic-org/sanic) | 18632 | 1588 | 1467 | 1692 | 133 | 2026-07-15 18:25:33 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16504 | 2346 | 3222 | 9577 | 220 | 2026-07-15 15:18:34 |
| [httpx](https://github.com/encode/httpx) | 15355 | 1205 | 0 | 1805 | 144 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14822 | 5804 | 11530 | 14082 | 1843 | 2026-07-15 15:46:58 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13960 | 2126 | 2656 | 1202 | 220 | 2026-07-06 02:11:55 |
| [dask](https://github.com/dask/dask) | 13860 | 1905 | 5540 | 6654 | 1264 | 2026-07-14 13:22:10 |
| [starlette](https://github.com/Kludex/starlette) | 12476 | 1228 | 771 | 1976 | 60 | 2026-07-04 05:14:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 12000 | 1713 | 8243 | 1140 | 207 | 2026-07-16 02:53:15 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11859 | 610 | 417 | 324 | 154 | 2026-07-14 16:30:56 |
| [falcon](https://github.com/falconry/falcon) | 9788 | 1014 | 1134 | 1481 | 173 | 2026-07-13 14:45:43 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9135 | 602 | 1039 | 524 | 220 | 2026-07-08 11:44:15 |
| [bottle](https://github.com/bottlepy/bottle) | 8772 | 1501 | 865 | 640 | 288 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7295 | 407 | 896 | 2572 | 328 | 2026-07-13 23:34:29 |
| [hug](https://github.com/hugapi/hug) | 6883 | 390 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6745 | 739 | 979 | 591 | 28 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5607 | 498 | 1263 | 874 | 531 | 2026-07-06 15:08:13 |
| [vibora](https://github.com/vibora-io/vibora) | 5591 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5321 | 1028 | 921 | 312 | 204 | 2026-07-10 05:48:53 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4261 | 351 | 1188 | 233 | 124 | 2026-06-30 21:02:03 |
| [pyramid](https://github.com/Pylons/pyramid) | 4088 | 890 | 1065 | 2738 | 88 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 261 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3647 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2756 | 314 | 675 | 1337 | 314 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2505 | 220 | 453 | 695 | 94 | 2026-07-14 15:06:39 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2363 | 137 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 913 | 1084 | 1567 | 359 | 2026-07-15 12:12:28 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1944 | 366 | 1785 | 268 | 266 | 2026-07-13 18:13:27 |
| [pypy](https://github.com/pypy/pypy) | 1764 | 118 | 5236 | 271 | 737 | 2026-07-15 17:57:42 |
| [jython](https://github.com/jython/jython) | 1525 | 231 | 298 | 139 | 103 | 2026-07-13 11:30:52 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-07-14 21:14:06 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 395 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-07-16T03:24:30*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
