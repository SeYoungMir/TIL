# 부록 - 유용한 라이브러리
## 1. 프로세스 관리 도구 Supervisor
### 1. Supervisor
1. Supervisor로 실행할 프로그램 준비
   - 다음 명령어로 python/crawler_with_celery_sampleChapter 디렉터리 생성, 디렉터리 바로 아래에 이전(5장)에 만든 crawler_with_celery_sample.py,my_logging.py,settings.py를 배치
   - ```cmd
     $ mkdir ~/python/crawler_with_celery_sample
     ``` 
   - 이어 다음 명령어 사용 ,venv 생성.
   - ```bash
     $ cd ~/python/crawler_with_celery_sample
     $ python -m venv venv_crawler_with_celery_sample
     $ source venv_crawler_with_celery_sample/bin/activate
     ```
   - crawler_with_celery_sample.py에 필요한 라이브러리를 pip install 명령어로 설치
   - ```bash
     (venv_crawler_with_celery_sample) $ pip install celery redis pydub coloring requests
     (venv_crawler_with_celery_sample) $ brew install redis ffmpeg
     ```
   - 다음 명령어를 사용, Redis 실행(이미 실행중이라면 다시 실행하지 않아도 됨)
   - ```bash
     (venv_crawler_with_celery_sample) $ brew services start redis
     ```
