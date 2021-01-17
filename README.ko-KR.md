> #### Language
> [English](README.md) Korean

# reqWrapper
reqWrapper는 [requests](https://pypi.org/project/requests/) 패키지에 재시도와 status code 필터링을 지원하는 확장입니다.

```python
import reqWrapper

sess = reqWrapper.Session()
sr = reqWrapper.get('https://github.com/', session=sess)

print(sr.success)  # True
print(sr.status_code)  # 200
type(sr.response)  # <class 'requests.models.Response'>
```

## 설치
[PyPI](https://pypi.org/project/reqWrapper/) 를 통해 설치할 수 있습니다.
```console
python -m pip install reqWrapper
```

### Dependencies
requests >= 2.*

## request
reqWrapper 하위의 함수, 클래스등은 대부분 requests와 대응합니다. 단, `request`, `get`, `options`, `head`, `post`, `put`, `patch`, `delete` 함수(이하 요청함수)는 해당 패키지를 통해 처리됩니다.

### 요청 보내기
reqWrapper의 요청함수는 reqWrapper상의 재시도 함수를 거쳐 requests 패키지를 직접 이용하므로 requests 패지의 함수와 기본 인자는 같습니다.

reqWrapper는 요청의 성공 여부를 포함한 [`SafeResponse`](#saferesponse) 객체를 반환합니다.
```python
import requests
import reqWrapper

params = {"tab": "repositories"}

# requests
requests.get("https://github.com/box-archived", params=params)

# reqWrapper
reqWrapper.get("https://github.com/box-archived", params=params,
               session=None, retry=5, wait=1, status=None)
```
reqWrapper의 요청함수는 재시도 설정을 변수로 받습니다. (Optional)
- `session`: 요청에 사용할 `Session`객체를 받습니다. (기본값 None)
- `retry`: 최대 재시도 횟수를 설정합니다. (기본값 5)
- `wait`: 재시도 사이의 간격을 설정합니다. 단위는 초 입니다. (기본값 1)
- `status`: 필터링 할 status code를 설정합니다. (기본값 None)

`status` 변수는 [`StatusFilter`](#statusfilter) 객체와 int, list 타입을 모두 받을 수 있으며, int, list 타입일 경우 자동으로 `StatusFilter`객체로 변환합니다.


## SafeResponse
reqWrapper의 요청함수는 SafeResponse 객체를 반환합니다.
```python
import reqWrapper

sr = reqWrapper.get('https://github.com')
if sr.success:
    sr.status_code
    sr.response
    sr.session
```
- `success`: 요청의 성공 여부를 `bool`타입으로 반환합니다.
- `status_code`: 응답의 status code를 `int`타입으로 반환합니다. 요청에 실패했을 경우 `None`
- `response`: 요청에 대한 `requests.Response`객체를 반환합니다. 요청에 실패했을 경우 `None`
- `session`: 요청에 사용된 `requests.Session`객체를 반환합니다. 요청에 실패했을 경우 `None`


## StatusFilter
StatusFilter 객체는 status code 통과에 대한 옵션을 가집니다. StatusFilter는 `set`타입의 서브클래스이며 `interpret_options`, `pass_list`, `check`메소드를 가집니다.

### 초기화
StatusFilter는 `List[int]`타입의 status code를 이용해 선언하며 양수(+)는 통과, 음수(-)는 거부를 의미합니다
```python
from reqWrapper import StatusFilter

# 제한사항 없음, 모두 통과
StatusFilter()

# 200 통과, 나머지는 거부
StatusFilter([200])

# 200 통과, 400 거부, 나머지는 거부
StatusFilter([200, -400])

# 404 거부, 나머지는 통과
StatusFilter([-404])

# 통과옵션에서 거부옵션을 제거하는 방식이므로 거부옵션이 우위
# 따라서 200 거부. 나머지는 거부
# 아래의 경우 모든 요청을 거부하는 필터이다
StatusFilter([200, -200])

# range를 이용한 초기화
# 2xx 통과, 나머지는 거부
StatusFilter(range(200, 300))

# range를 list 항목으로 추가하여 사용할 수 있다
# 2xx 통과, 400 통과, 나머지는 거부
StatusFilter([range(200, 300), 400])
```
통과규칙(양수)이 없는 경우 모든 status code를 통과하는것으로 간주합니다. 여기서 모든 status code는 `range(100, 600)`의 범위를 뜻합니다.

### check()
주어진 status code가 통과인지 확인합니다. 통과일경우 `True`, 거부일경우 `False`를 리턴합니다


### interpret_options()
주어진 옵션을 통과옵션과 거부옵션으로 분리합니다. `tuple(통과 set, 거부 set)`의 형태로 리턴합니다.
```python
from reqWrapper import StatusFilter

status = StatusFilter([200, -200, -404, 204, 203])
print(status.interpret_options())
# ({200, 203, 204}, {-200, -404})
```

#### pass_list()
통과하는 모든 status code 목록을 리턴합니다.
```python
from reqWrapper import StatusFilter

status = StatusFilter()
print(status.pass_list())
# [100, 101, 102, ... , 597, 598, 599]

status = StatusFilter([200, -200, -404, 204, 203])
print(status.pass_list())
# [203, 204]
```