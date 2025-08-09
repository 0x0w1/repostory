# 파이썬 레포지토리 트랜드 트래커

GitHub에서 인기 있는 파이썬 프로젝트들의 스타 수, 포크 수, 이슈 수를 자동으로 추적하고 순위를 매기는 도구입니다.

## 🚀 데모

실시간 순위 및 차트를 확인하려면 [데모 페이지](https://0x10.kr)를 방문하세요.

## 📊 프로젝트 소개

이 도구는 다양한 카테고리의 파이썬 프로젝트들을 모니터링하여 다음과 같은 기능을 제공합니다:

- **자동 데이터 수집**: GitHub GraphQL API를 사용하여 정확한 스타, 포크, 이슈, PR 수를 수집
- **히스토리 추적**: 일별 변화량을 추적하여 시간에 따른 트렌드 분석 가능
- **실시간 업데이트**: GitHub Actions를 통한 매일 자동 업데이트
- **다양한 카테고리**: 웹 프레임워크, 머신러닝, 데이터 과학, Python 구현체 등 포함

## 🎯 추적 카테고리

- **웹 프레임워크**: Django, Flask, FastAPI, Tornado 등
- **머신러닝/AI**: TensorFlow, PyTorch, scikit-learn, Keras 등  
- **데이터 과학**: Pandas, NumPy, SciPy, Matplotlib 등
- **비동기 프로그래밍**: asyncio, trio, anyio 등
- **Python 구현체**: CPython, PyPy, Jython, MicroPython 등

## 🛠️ 스크립트 문서

### 핵심 스크립트

- **`fetcher.py`** - 메인 데이터 수집 및 README 생성 스크립트
  - GitHub API에서 저장소 데이터 수집
  - 로컬 JSON 데이터 파일을 일별 변경사항으로 업데이트
  - 영어 및 한글 README 파일 생성
  - GraphQL API를 사용한 정확한 이슈/PR 수 조회

- **`readme_generator.py`** - 독립형 README 생성 유틸리티
  - 기존 로컬 JSON 파일에서 데이터 로드
  - 선택적으로 현재 GitHub 데이터로 업데이트
  - 전체 데이터 수집 없이 README 파일 생성
  - 빠른 README 업데이트를 위한 경량화 대안

- **`repo_data_initializer.py`** - 단일 저장소 데이터 수집기
  - 단일 GitHub 저장소 데이터 초기화
  - GraphQL을 사용한 과거 스타 데이터 수집
  - repo_data/ 디렉토리에 초기 JSON 데이터 파일 생성

- **`batch_repo_initializer.py`** - 배치 저장소 처리기
  - 여러 저장소를 병렬로 처리
  - 설정 가능한 워커 스레드 (기본값: 3 CPU)
  - 모든 저장소의 초기 데이터 수집에 이상적

- **`generate_history_from_repo_data.py`** - 히스토리 집계기
  - 일별 저장소 데이터를 누적 합계로 변환
  - 트렌드 분석을 위한 repository_histories.json 생성
  - 모든 repo_data/*.json 파일 처리

### 사용 예시

```bash
# 전체 데이터 수집 및 README 생성
uv run python/fetcher.py

# README만 빠르게 업데이트
uv run python/readme_generator.py

# 단일 저장소 초기화
uv run python/repo_data_initializer.py https://github.com/owner/repo

# 모든 저장소 배치 처리
uv run python/batch_repo_initializer.py --workers 8

# 히스토리 집계 생성
uv run python/generate_history_from_repo_data.py
```

| 프로젝트 이름 | 스타 수 | 포크 수 | 전체 이슈 | 전체 PR | 오픈 이슈 | 최근 커밋 |
| ------------ | ----- | ----- | ------------ | --------- | ----------- | ----------- |
| [tensorflow](https://github.com/tensorflow/tensorflow) | 191105 | 74764 | 40706 | 55840 | 1491 | 2025-08-09 01:17:04 |
| [transformers](https://github.com/huggingface/transformers) | 148102 | 29956 | 17730 | 21743 | 1963 | 2025-08-08 20:32:26 |
| [pytorch](https://github.com/pytorch/pytorch) | 92216 | 24898 | 52974 | 106807 | 16757 | 2025-08-09 01:38:33 |
| [fastapi](https://github.com/tiangolo/fastapi) | 88176 | 7704 | 3466 | 4653 | 301 | 2025-08-08 10:32:11 |
| [django](https://github.com/django/django) | 84520 | 32774 | 0 | 19650 | 355 | 2025-08-08 19:39:50 |
| [flask](https://github.com/pallets/flask) | 70142 | 16516 | 2692 | 2685 | 16 | 2025-06-12 20:48:14 |
| [cpython](https://github.com/python/cpython) | 68256 | 32522 | 73199 | 63454 | 9274 | 2025-08-08 19:07:15 |
| [keras](https://github.com/keras-team/keras) | 63296 | 19604 | 12519 | 8264 | 288 | 2025-08-08 23:06:18 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 62938 | 26119 | 11635 | 19146 | 2151 | 2025-08-08 16:17:51 |
| [pandas](https://github.com/pandas-dev/pandas) | 46235 | 18771 | 27640 | 34389 | 3696 | 2025-08-08 19:54:59 |
| [ray](https://github.com/ray-project/ray) | 38389 | 6691 | 20842 | 34249 | 2994 | 2025-08-09 01:24:57 |
| [gym](https://github.com/openai/gym) | 36350 | 8687 | 1837 | 1464 | 127 | 2024-10-11 20:07:05 |
| [spaCy](https://github.com/explosion/spaCy) | 32130 | 4556 | 5715 | 4064 | 196 | 2025-05-28 15:28:05 |
| [numpy](https://github.com/numpy/numpy) | 30111 | 11178 | 13475 | 15990 | 2326 | 2025-08-08 23:55:01 |
| [django-rest-framework](https://github.com/encode/django-rest-framework) | 29357 | 6989 | 3945 | 4817 | 101 | 2025-08-08 18:18:02 |
| [celery](https://github.com/celery/celery) | 26965 | 4822 | 5153 | 3632 | 760 | 2025-08-06 08:30:26 |
| [dash](https://github.com/plotly/dash) | 23901 | 2184 | 1970 | 1311 | 545 | 2025-08-09 00:05:42 |
| [tornado](https://github.com/tornadoweb/tornado) | 22083 | 5537 | 1851 | 1666 | 206 | 2025-08-08 18:27:46 |
| [matplotlib](https://github.com/matplotlib/matplotlib) | 21525 | 7949 | 10932 | 19436 | 1652 | 2025-08-07 21:18:23 |
| [micropython](https://github.com/micropython/micropython) | 20705 | 8339 | 5770 | 7074 | 1757 | 2025-08-07 07:02:51 |
| [RustPython](https://github.com/RustPython/RustPython) | 20379 | 1335 | 1204 | 4815 | 432 | 2025-08-08 22:41:13 |
| [sanic](https://github.com/channelcat/sanic) | 18463 | 1576 | 1448 | 1625 | 142 | 2025-06-26 19:43:32 |
| [plotly.py](https://github.com/plotly/plotly.py) | 17574 | 2687 | 3232 | 1937 | 710 | 2025-08-07 21:42:57 |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 15900 | 2112 | 3140 | 7965 | 259 | 2025-08-08 16:28:50 |
| [httpx](https://github.com/encode/httpx) | 14439 | 936 | 911 | 1704 | 97 | 2025-08-07 13:52:25 |
| [scipy](https://github.com/scipy/scipy) | 13900 | 5437 | 10963 | 12472 | 1752 | 2025-08-07 04:02:43 |
| [dask](https://github.com/dask/dask) | 13390 | 1791 | 5417 | 6331 | 1185 | 2025-08-04 17:59:07 |
| [seaborn](https://github.com/mwaskom/seaborn) | 13353 | 2024 | 2621 | 1147 | 185 | 2025-07-10 13:20:45 |
| [starlette](https://github.com/encode/starlette) | 11324 | 1029 | 750 | 1679 | 47 | 2025-08-01 19:39:07 |
| [uvloop](https://github.com/MagicStack/uvloop) | 11122 | 567 | 387 | 287 | 140 | 2025-04-17 15:20:26 |
| [sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | 10751 | 1572 | 8063 | 975 | 237 | 2025-08-07 14:52:25 |
| [falcon](https://github.com/falconry/falcon) | 9698 | 960 | 1091 | 1352 | 158 | 2025-08-08 20:09:45 |
| [bottle](https://github.com/bottlepy/bottle) | 8643 | 1486 | 853 | 621 | 283 | 2025-06-28 07:31:03 |
| [django-ninja](https://github.com/vitalik/django-ninja) | 8436 | 517 | 933 | 428 | 412 | 2025-08-08 15:26:58 |
| [hug](https://github.com/timothycrosley/hug) | 6894 | 389 | 465 | 463 | 186 | 2024-07-04 14:37:30 |
| [eve](https://github.com/pyeve/eve) | 6728 | 745 | 978 | 574 | 29 | 2025-06-04 12:19:40 |
| [trio](https://github.com/python-trio/trio) | 6682 | 359 | 863 | 2438 | 311 | 2025-08-07 04:47:26 |
| [vibora](https://github.com/vibora-io/vibora) | 5636 | 301 | 0 | 103 | 140 | 2020-12-23 01:00:55 |
| [tortoise-orm](https://github.com/tortoise/tortoise-orm) | 5236 | 434 | 1183 | 705 | 490 | 2025-08-03 04:51:47 |
| [opencv-python](https://github.com/opencv/opencv-python) | 4934 | 922 | 860 | 258 | 156 | 2025-07-30 13:23:12 |
| [pyramid](https://github.com/Pylons/pyramid) | 4039 | 890 | 1060 | 2712 | 82 | 2025-02-23 16:39:21 |
| [databases](https://github.com/encode/databases) | 3934 | 264 | 319 | 211 | 133 | 2024-05-21 19:58:17 |
| [alembic](https://github.com/sqlalchemy/alembic) | 3508 | 286 | 1150 | 193 | 114 | 2025-07-16 03:27:03 |
| [quart](https://github.com/pallets/quart) | 3388 | 184 | 277 | 120 | 62 | 2025-07-29 15:07:12 |
| [ironpython3](https://github.com/IronLanguages/ironpython3) | 2672 | 302 | 648 | 1261 | 306 | 2025-07-17 01:58:34 |
| [masonite](https://github.com/MasoniteFramework/masonite) | 2295 | 130 | 426 | 391 | 20 | 2025-03-25 15:52:44 |
| [anyio](https://github.com/agronholm/anyio) | 2166 | 163 | 399 | 496 | 67 | 2025-08-04 18:10:59 |
| [web2py](https://github.com/web2py/web2py) | 2150 | 907 | 1077 | 1458 | 369 | 2025-07-14 00:48:55 |
| [cherrypy](https://github.com/cherrypy/cherrypy) | 1918 | 369 | 1779 | 264 | 260 | 2025-08-04 17:44:33 |
| [pypy](https://github.com/pypy/pypy) | 1463 | 83 | 5138 | 166 | 732 | 2025-08-08 13:06:27 |
| [jython](https://github.com/jython/jython) | 1416 | 216 | 278 | 113 | 100 | 2025-05-04 16:52:25 |
| [tg2](https://github.com/TurboGears/tg2) | 811 | 80 | 98 | 36 | 13 | 2025-02-18 22:52:59 |
| [Growler](https://github.com/pyGrowler/Growler) | 688 | 21 | 16 | 3 | 5 | 2020-03-08 07:53:32 |
| [morepath](https://github.com/morepath/morepath) | 396 | 37 | 446 | 110 | 77 | 2025-06-23 17:01:19 |
| [circuits](https://github.com/circuits/circuits) | 317 | 56 | 147 | 190 | 42 | 2024-04-05 16:12:35 |

*Last Automatic Update: 2025-08-09T10:56:34*

*Inspired by https://github.com/mingrammer/python-web-framework-stars*
