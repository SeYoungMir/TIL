# 4. 스크레이핑 기본
## 3. RSS 스크레이핑
### 1. 라이브러리 설치 
2. XML 분석하기- 이어서
   - feed의 제목은 다음과 같이 확인
       ```python
       >>> rss["feed"]["title"]
       ```
   - 가장 중요한 RSS의 엔트리(item요소)는 다음과 같이 확인
        ```python
        >>> rss["entries"]
        ``` 
    - 신간 정보 엔트리의 타이틀과 링크 출력
        ```python
        >>> for content in rss["entries"]:
                print(content["title"])
                print(content["link"])
        ```
    - RSS 버전은 다음과 같이 확인
        ```python
        >>> print(rss.version)
        ```
    - RSS의 사양에는 필수 항목과 옵션 항목이 있음. RSS 제공자에 따라서 옵션 항목은 포함되어 있지 않을 수도 있어서 추출할 수 있는 정보가 조금씩 달라짐.
    - 실제로 스크레이핑 프로그램을 만들때는 예외 처리를 잊지 말아야함.
## 4. 데이터를 데이터베이스에 저장, 분석
### 1. 데이터를 데이터베이스에 저장해서 호출
- 스크레이핑한 정보는 이후에 분석에 사용하거나 웹 API로 만들어서 애플리케이션에서 활용할 수 있게 함
- 이때 파일로 저장하는 것보다 데이터베이스에 저장하는 것이 다루기 쉬움
- 또한 처리 속도적인 측면에서도 데이터베이스를 사용하는 것이 좋음
- 오픈소스 관계형 데이터베이스 관리 시스템(RDBMS) 중의 하나인 MySQL을 사용
- MySQL은 빠르고, 사용하기 쉬워서 임대 서버의 데이터베이스로 많이 사용
- 오래전부터 많이 사용된 RDBMS라서 다양한 프로그래밍 언어에서 MySQL을 다룰 수 있는 라이브러리를 제공한다는 것도 장점
### 2. MySQL 설치
1. macOS에 MySQL 설치
   - Homebrew 의 brew install 명령어를 사용해서 MySQL을 설치
   ```python
   $ brew install mysql
   ```
   - 설치 완료되면 버전 확인
   ```python
   $ mysqld --version
   ```
   - 다음 명령어로 MySQL 실행
   ```python
   $ mysql.server start
   ```
2. 리눅스에 MySQL 설치
   - 파이썬을 설치할때와 마찬가지, 각 배포판에서 제공되는 패키지 매니저를 사용해 설치.
   - 우분투에서는 APT 이용해 설치, 설치할 때 root 비밀번호 필요. 비밀번호는 하나 이상의 숫자, 하나 이상의 알파벳, 하나 이상의 특수 문자를 모두 포함해야함
   ```python
   $ sudo apt-get install -y mysql-server
   ```
   - 설치하고 나면 자동으로 MySQL 실행. 만약 실행되지 않는다면 다음 명령어를 입력
   ```python
   $ sudo service mysql start 
   ```
 - macOS에 Homebrew를 사용해서 설치 시 MySQL 사이트에서 파일을 내려받아 설치했을때와 보안 정책이 약간 다름