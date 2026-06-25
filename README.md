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
| [tensorflow](https://github.com/tensorflow/tensorflow) | 196036 | 75192 | 41567 | 76875 | 3520 | 2026-06-25 03:59:50 |
| [transformers](https://github.com/huggingface/transformers) | 161882 | 33590 | 19103 | 27054 | 2438 | 2026-06-25 00:47:38 |
| [pytorch](https://github.com/pytorch/pytorch) | 101136 | 28122 | 59405 | 128105 | 18300 | 2026-06-25 04:10:45 |
| [fastapi](https://github.com/fastapi/fastapi) | 99637 | 9477 | 3535 | 5973 | 103 | 2026-06-24 22:37:32 |
| [django](https://github.com/django/django) | 88114 | 33866 | 0 | 21477 | 455 | 2026-06-25 01:21:55 |
| [cpython](https://github.com/python/cpython) | 73528 | 34776 | 76882 | 72934 | 9409 | 2026-06-25 00:25:41 |
| [flask](https://github.com/pallets/flask) | 71856 | 16874 | 2752 | 2841 | 6 | 2026-06-10 18:03:29 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 66437 | 27104 | 12160 | 21042 | 2099 | 2026-06-25 02:44:22 |
| [keras](https://github.com/keras-team/keras) | 64101 | 19738 | 12806 | 9496 | 221 | 2026-06-24 23:38:24 |
| [pandas](https://github.com/pandas-dev/pandas) | 49051 | 20036 | 28336 | 37579 | 3140 | 2026-06-24 19:14:32 |
| [ray](https://github.com/ray-project/ray) | 43009 | 7725 | 22772 | 41169 | 3483 | 2026-06-25 04:06:20 |
| [gym](https://github.com/openai/gym) | 37232 | 8701 | 1838 | 1468 | 128 | 2026-03-26 23:13:27 |
| [spaCy](https://github.com/explosion/spaCy) | 33696 | 4689 | 5762 | 4098 | 217 | 2026-05-19 06:48:57 |
| [numpy](https://github.com/numpy/numpy) | 32243 | 12488 | 13960 | 17703 | 2389 | 2026-06-24 23:28:07 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 30087 | 7074 | 3967 | 5022 | 85 | 2026-06-23 19:13:08 |
| [celery](https://github.com/celery/celery) | 28625 | 5081 | 5282 | 4156 | 788 | 2026-06-24 15:07:52 |
| [dash](https://github.com/plotly/dash) | 24271 | 2301 | 2118 | 1601 | 555 | 2026-06-23 18:42:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 22929 | 8359 | 11328 | 20555 | 1461 | 2026-06-24 19:13:25 |
| [tornado](https://github.com/tornadoweb/tornado) | 22186 | 5531 | 1873 | 1754 | 215 | 2026-06-22 19:29:28 |
| [RustPython](https://github.com/RustPython/RustPython) | 22138 | 1448 | 1358 | 6729 | 387 | 2026-06-24 12:58:58 |
| [micropython](https://github.com/micropython/micropython) | 21832 | 8884 | 6072 | 7898 | 1637 | 2026-06-24 04:29:39 |
| [plotly.py](https://github.com/plotly/plotly.py) | 18627 | 2815 | 3363 | 2098 | 768 | 2026-06-22 22:58:40 |
| [sanic](https://github.com/sanic-org/sanic) | 18626 | 1590 | 1467 | 1690 | 133 | 2026-05-31 19:42:26 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 16464 | 2333 | 3215 | 9433 | 220 | 2026-06-24 10:53:32 |
| [httpx](https://github.com/encode/httpx) | 15315 | 1180 | 0 | 1805 | 145 | 2026-03-29 00:19:16 |
| [scipy](https://github.com/scipy/scipy) | 14774 | 5773 | 11499 | 13971 | 1826 | 2026-06-24 18:07:56 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13930 | 2114 | 2655 | 1185 | 226 | 2026-01-22 13:03:07 |
| [dask](https://github.com/dask/dask) | 13854 | 1893 | 5539 | 6627 | 1248 | 2026-06-23 14:17:10 |
| [starlette](https://github.com/Kludex/starlette) | 12427 | 1207 | 770 | 1955 | 49 | 2026-06-19 00:03:19 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 11948 | 1700 | 8234 | 1120 | 206 | 2026-06-23 21:21:46 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11831 | 609 | 416 | 323 | 156 | 2026-05-04 16:01:08 |
| [falcon](https://github.com/falconry/falcon) | 9795 | 1004 | 1130 | 1467 | 164 | 2026-06-17 14:35:27 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 9103 | 599 | 1038 | 518 | 216 | 2026-06-09 15:46:32 |
| [bottle](https://github.com/bottlepy/bottle) | 8771 | 1501 | 864 | 636 | 284 | 2026-03-23 15:39:32 |
| [trio](https://github.com/python-trio/trio) | 7277 | 397 | 892 | 2555 | 320 | 2026-06-22 22:13:40 |
| [hug](https://github.com/hugapi/hug) | 6883 | 391 | 466 | 463 | 187 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6742 | 738 | 979 | 590 | 27 | 2026-03-24 09:19:21 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5593 | 490 | 1259 | 860 | 519 | 2026-06-23 15:33:16 |
| [vibora](https://github.com/vibora-io/vibora) | 5592 | 299 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [opencv-python](https://github.com/opencv/opencv-python) | 5299 | 1023 | 914 | 307 | 208 | 2026-06-19 16:35:32 |
| [alembic](https://github.com/sqlalchemy/alembic) | 4221 | 342 | 1186 | 226 | 119 | 2026-06-22 11:24:56 |
| [pyramid](https://github.com/Pylons/pyramid) | 4086 | 890 | 1065 | 2737 | 87 | 2026-06-19 08:42:21 |
| [databases](https://github.com/encode/databases) | 4000 | 260 | 319 | 211 | 131 | 2024-05-21 19:58:17 |
| [quart](https://github.com/pallets/quart) | 3644 | 203 | 284 | 132 | 69 | 2025-09-01 18:49:41 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2754 | 312 | 673 | 1335 | 310 | 2026-06-20 18:07:32 |
| [anyio](https://github.com/agronholm/anyio) | 2486 | 212 | 446 | 664 | 90 | 2026-06-24 20:55:27 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2361 | 136 | 429 | 402 | 1 | 2026-06-07 18:17:21 |
| [web2py](https://github.com/web2py/web2py) | 2169 | 910 | 1084 | 1548 | 361 | 2026-06-22 00:46:59 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1943 | 365 | 1785 | 268 | 266 | 2026-06-22 17:49:00 |
| [pypy](https://github.com/pypy/pypy) | 1757 | 117 | 5226 | 263 | 735 | 2026-06-24 10:13:44 |
| [jython](https://github.com/jython/jython) | 1518 | 230 | 297 | 137 | 111 | 2026-06-09 14:51:06 |
| [tg2](https://github.com/TurboGears/tg2) | 813 | 82 | 102 | 38 | 14 | 2026-06-05 20:41:50 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 40 | 448 | 114 | 78 | 2026-06-12 07:57:46 |
| [circuits](https://github.com/circuits/circuits) | 317 | 57 | 149 | 197 | 41 | 2026-05-03 22:02:47 |

*Last Automatic Update: 2026-06-25T04:15:53*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
