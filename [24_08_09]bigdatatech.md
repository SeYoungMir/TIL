# 부록 - 유용한 라이브러리
## 4. 베이그런트로 윈도우에 우분투 가상 환경 설치
### 3. 베이그런트로 우분투 가상 환경 실행
- 지금까지의 과정은 한 번만 설정하면 되는 내용. 지금부터 설명하는 내용은 리눅스 가상 환경에 들어갈 때 입력하는 명령어이므로 컴퓨터를 종료했다가 다시 실행하면 그 때 마다 실행해 줘야 하는 명령어.
- ```bash
  # 가상 환경 실행(처음 실행 시 설치때문에 시간이 걸림)
  C:\vagrant> vagrant up
  (처음 실행시 설치 진행)
  
  # 접속하기
  C:\vagrant> vagrant ssh
  ```
- 두 명령어를 입력시 우분투 가상환경으로 진입

### 4. 파일 공유
- 기본적으로는 vagrant는 vagrant 명령어를 실행한 디렉터리를 \vagrant 디렉터리로 공유. 따라서 여기에 원하는 파이썬 코드 등을 올려 두면 우분투 가상 환경에서 사용 가능
- 예를 들어 다음과 같은 코드를 작성하고 test.py라는 이름을 공유 디렉터리에 넣었다고 해 보자.
- ```python
  print("Hello Python")
  ```
- 현재 공유 디렉터리에는 위 파일을 하나 넣음.
- vagrant ssh를 실행한 명령 프롬프트로 돌아와서 파일 공유 확인.
- cd \vagrant 명령어로 \vagrant 폴더로 이동, ls -l 명령어를 입력. cat 명령어로 파일의 내용을 출력해 보면 파일의 내용이 출력.
- 참고로 vagrant는 이 외에도 프로그래밍 공부를 위한 다양한 환경 제공.