# 5. 크롤러 설계/개발(응용)
## 5. 병렬 처리
### 3. 작업 큐(여러 개의 머신을 사용, 병렬 처리) - 이어서
2. Celery 예제:mp3 내려받기
   - 이전 예제와 같은 mp3 파일 내려받는 예제를 Celery로 구현.
   - 내려받는 예제만으로는 태스크들을 연동하는 방법을 살펴보기 어려우므로 내려받은 mp3 데이터의 앞부분을 5초정도 잘라서 저장하는 기능 추가
   - 큐는 Redis 사용. Redis는 brew 명령어로 설치 가능
    ```python
    $ brew install redis
    $ brew services start redis

    $ ps auxw | grep redis
    ```
3. Celery와  Redis 모듈 설치
   - Celery는 pip install 명령어로 설치, Redis 모듈도 같이 설치
    ```
    $ pip install redis
    $ pip install celery
    ```
   - 오류가  생긴다면 Celery 버전 확인 후 상위 버전 설치
4. FFmpeg와 Pydub 설치
   - mp3 데이터 조작 시 pip install 명령어로 FFmpeg와 Pydub이라는 2개의 라이브러리 설치 필요
   - FFmpeg는 음성 파일 조작에 사용되는 대표적인 도구/라이브러리, 다양한 프로그래밍 언어의 바인딩 존재
   - Pydub은 간단한 음성 파일 조작 파이썬 라이브러리
    ```
    $ brew install ffmpeg
    $ brew install pydub
    ```