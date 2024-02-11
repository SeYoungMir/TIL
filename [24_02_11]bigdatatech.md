# 4. 스크레이핑 기본
## 1. 라이브러리 설치하기
### 1. pip으로 라이브러리 설치하기
4. 설치된 라이브러리 출력하기
   - 설치된 라이브러리 출력할 때는 pip freeze 명령어 사용
    ```python
    $ pip freeze
    ```
    - pip freeze 명령어 실행 시 라이브러리의 이름과 설치된 버전 목록 출력
## 2. 웹 페이지 스크레이핑
### 1. 라이브러리 설치
1. Requests, lxml, cssselect
     - Requests는 간단하게 웹 페이지를 추출할 수 있게 해주는 라이브러리, 사람이 쉽게 사용할 수 있게 만들어진 간단한 HTTP 라이브러리
     - lxml은 C 언어로 작성된 libxml2와 libxslt의 파이썬 바인딩, 유연하게 xml/html 조작 가능
     - cssselect는 이름 그대로 CSS 선택자 라이브러리
     - 3개의 라이브러리를 사용하면 XPath 와 Css 선택자를 사용,HTML에서 요소 추출 가능
     - 세 개의 라이브러리 모두 pip install 명령어 사용 설치 가능
    ```python
    $ pip install Requests
    $ pip install lxml
    $ pip install cssselect
    ```
### 2.  웹에 있는 리소스 추출
1. Requests를 사용해 웹에 있는 리소스 추출
   - 파이썬은 표준적으로 URL 지정, 리소스 추출할 수 있게 해주는 urllib 모듈 있음.
   - 단순하게 웹 페이지 추출 시 urllib으로도 충분, HTTP 헤더에 정보를 넣어 접근하거나 BASIC 인증을 위해서는 urllib으로는 힘듦
   - Requests는 다음과 같이 HTTP 메서드와 같은 이름의 메서드 제공
    ```python
    $ python
    >>> import requests
    >>> requests.get("URL")
    >>> requests.post("URL")
    >>> requests.put("URL")
    >>> requests.delete("URL")
    >>> requests.head("URL") ## header 추출
    ```
    - get 메서드에 매개 변수 추가 시 다음과 같이 get 메서드에 params 키워드 매개 변수 지정
    ```python
    >>> import requests
    >>> requests.get("URL",params={"key1":"value1","key2":"value2"})
    ```
    - API 호출 시 대부분 POST 요청의 body에 JSON 인코딩한 매개 변수를 넣는 경우 많음. 이런 경우라면 표준으로 제공되는 JSON 모듈을 사용, JSON 인코딩한 데이터를 다음과 같이 data 키워드 매개 변수에 지정하면 됨
    ```python
    >>> import json
    >>> import requests
    >>> requests.get("URL",data=json.dumps({"key1":"value1","key2":"value2"}))
    ```