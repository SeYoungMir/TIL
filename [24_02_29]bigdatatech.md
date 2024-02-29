# 5. 크롤러 설계/개발(응용)
## 5. 병렬 처리
### 1. 병렬 처리
- 여러 개의 URL을 가진 리스트를 반복 처리해서 하나 하나 처리하는 것이 기본적인 크롤러의 형태
- 여러 개의 페이지를 추출할 때 1개씩 내용을 추출한다면 요청 전체에 걸리는 시간은 <하나의 요청에 걸리는 시간> * <전체 개수>만큼 소요
- 크롤러를 실행하는 환경의 CPU, 메모리, 네트워크 대역에 여유가 있고, 상대방의 서버에 큰 무리를 주지 않을 수 있을 때는 요청을 병렬 처리, 전체 처리 시간을 줄일 수 있음
- 웹 브라우저에서 여러 파일을 내려받을 때, 한 번에 여러 파일을 내려받는 것도 일종의 병렬 처리
- 다양한 상황에서 리소스를 효율적으로 사용할 수 있게 해줌.
* 병행과 병렬
  - 여러 개의 스레드를 사용, 여러 처리를 하면 병행 (여러 작업을 번갈아 가면서 진행)
  - 여러 개의 프로세스를 사용, 여러 처리를 하면 병렬 (여러 작업을 동시 진행)
  
### 2. 표준 라이브러리 사용(한 대의 머신 병렬화)
- 파이썬에 어떤 표준 병렬 처리 라이브러리가 있는지는 공식 문서를 통해 확인
  - 대표적 병렬 처리 라이브러리로는 multithread,multiprocess,concurrent.Future가 있음.
  - 추가로 비동기 처리 라이브러리인 asyncio가 있음. asyncio는 파이썬 3.4부터 추가된 라이브러리, 콜백을 사용 다중 처리 구현
  - 이러한 표준 라이브러리 사용 시 세부적인 다중 처리 제어를 할 수 있음. 하지만 병렬 프로그램 자체가 굉장히 복잡해지기 쉬움. 따라서 크롤러 만드는 것보다 오래 걸릴수 있음.
  - 비교적 다루기 쉬운 concurrent.Future 라이브러리 사용
1. concurrent.Future 라이브러리
   - Future는 다른 프로그래밍 언어 또는 라이브러리에서 promise 또는 delay라고 부르는 것으로, 어떤 처리의 결과가 이후에 추출된다는 것을 전제로 처리를 구현할 수 있게 해 주는 기능
   - Future를 사용하면 결과를 기다리지 않고 곧바로 후속 처리를 실행할 수 있으므로 쉽게 병렬처리를 구현 가능.
   - 결과물을 꺼내려면 사전에 다른 처리가 완료되어 있어야함(멀티 스레드 프로그래밍으로 비유하면 join메서드에 해당)
   - 병렬 처리를 멀티 스레드로 하고 싶을 때는 ThreadPoolExecutor 메서드 사용
   - 멀티 프로세스로 하고 싶은 경우에는 ProcessPoolExecutor 메서드 사용
2. 병렬로 내려받기
   - 저작권 소멸 곡을 archive.org에서 병렬로 다운.
   - 이하 코드 작성
    ```python
    """ 음악 파일을 병렬로 내려받는 예제"""
    import concurrent.futures
    import random
    import time
    from collections import namedtuple
    from os import path
    from urllib import parse
    import requests
    from my_logging import get_my_logger

    logger = get_my_logger(__name__)

    # 음악 파일의 이름과 데이터를 저장하기 위한 이름이 있는 튜플 정의
    Music = namedtuple('music','file_name','file_content')
    
    # 크롤링 요청별 간격 리스트 정의
    RANBOM_SLEEP_TIMES =[x*0.1 for x in range(10,40,5)]

    #크롤링 대상 URL 리스트
    MUSIC_URLS = ['https://archive.org/download/ThePianoMusicOfMauriceRavel]~',#생략]

    def download(url,timeout=180)
        # mp3 파일 이름 추출
        parsed_url = parse.urlparsr(url)
        file_name = path.basename(parsed_url.path)

        # 요청 간격을 랜덤하게 선택
        sleep_time = random.choice(RAMDOM_SLEEP_TIMES)
        
        # 내려받기 시작을 로그에 출력
        logger.info("[download start] sleep : {time}{file_name}".format(time=sleep_time,file_name=file_name))
        
        #요청 대기
        time.sleep(sleep_time)

        #음악 파일 내려받기
        r = requests.get(url, timeout=timeout)

        # 내려받기 종료를 로그에 출력
        logger.info("[download finished] {file_name}".format(file_name=file_name))
        
        #이름 있는 튜플에 파일 이름과 mp3 데이터를 넣어 반환
        return Music(file_name=file_name,file_content=r.content)
    if __name__='__main__':
        # 동시에 2개의 처리를 하기 위한 executor 생성
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            logger.info("[main start]")
        # executor.submit()으로 download 함수를 병행 실행
        # download() 함수의 매개 변수로 music_url 전달
        # 병행 실행 처리의 결과는 futures 변수에 입력
        futures = [executor.submit(download,music_url) for music_url in MUSIC_URLS]

        # download() 함수의 처리가 완료되면 반복문에서 반복해 결과 출력
        for  future in concurrent.futures.as_completed(futures):
            #download()함수의 실행 결과는 result() 메서드로 확인 가능
            music=future.result()
            
            #music.filename에는 mp3 파일의 파일명 들어있음.
            #이를 사용해 music.file_content에 저장된 데이터를 파일로 저장
            with open(music.file_name,'wb') as fw:
                fw.write(music.file_content)
            logger.info("[main finished]")
    ```
    - executor.submit 메서드에는 병렬 실행하고 싶은 함수 이름과매개 변수 전달
    - concurrent.futures as_completed 메서드를 사용하면 실행 종료, 순차적으로 완료 객체 반환
    - 이러한 객체에 future.result 메서드 적용 시 내부의 내용 추출 가능
    - ThreadPoolExecutor 메서드에 max_workers=2 매개변수 지정, 한번에 2개씩 병렬실행한다는 의미
1. 콘솔에 출력
   - 다음 명령어 실행
   - `$ python music_download_with_future.py`
   - 콘솔의 출력 시 max_workers의 지정 횟수에 따라 동시 실행수 변화, 단시간에 처리 완료 가능. 상대방의 서버에 높은 부하 줄 수 있음.