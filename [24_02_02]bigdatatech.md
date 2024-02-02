# 3. 크롤러 및 스크레이핑 개발 환경 준비와 파이썬 기본
## 2. 크롤링/스크레이핑 전용 개발 환경 준비하기
### 1. 파이썬 3 설치하기
2. 패키지 매니저를 이용해 macOS에 파이썬 설치하기
   - macOS에는 표준으로 파이썬 설치, macOS의 터미널에서 다음과같은 명령어로 버전 확인 가능
    - `$ python --version`
3. Pyenv 설치하기
   - Pyenv는 여러 파이썬 버전을 번갈아 사용할 수 있게 해 주는 도구, 깃허브에 있는 리포지터리 복제(깃허브 클론) 해서 사용
   - `$ git clone http://github.com/yyuu/pyenv.git ~/.pyenv`
4. .bash_profile을 편집해서 경로 설정하기
   - 경로 설정, cd 명령어를 사용해 터미널 홈 디렉터리로 이동
   - `$ cd`
   - 파일 앞에  .이 붙어 있는 파일은 숨긴 파일, ls 명령어에 -la 옵션을 붙여야 확인할 수 있음. 명령어 입력, 파일 존재하는지 확인
   - `$ ls -la `
   - vi 명령어 입력, .bash_profile 편집
   - `$ vi ~/.bash_profile`
   - [i] 키를 눌러 삽입모드로 변경, .bash_profile에 코드를 다음과 같이 추가
   - 
    ```
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    ```
   - [esc] 키를 눌러 삽입 모드 종료. 아래 명령어 실행 후 파일 변경 사항 저장,종료
   - `:wq`
   - 추가로 .bash_profile을 수정하녕 다음과 같은 명령어 실행, .bash_profile을 다시 읽어들여야함
   - `$ source`
5.  파이썬 설치
    - Pyenv를 사용할 수 있게 되었다면 설치할 수 있는 버전 확인, 다음 명령어 입력, 파이썬 버전 확인
    - `$ pyenv install --list`
    - 설치하려면 다음과 같은 명령어 사용
    - `$ pyenv install <설치할 버전>`
    - 설치 완료되며 다음 명령어로 설치 파이썬 버전 확인
    - `$ pyenv versions`
    - 왼쪽에 *이 붙어 있는 버전이 현재 활성화된 파이썬 버전, system이 붙은 건 macOS가 디폴트로 지원하는 파이썬 버전, 이를 새로 설치한 버전으로 바꿀때는 다음과 같은 명령어 사용
    - 
    ```python
    $ pyenv global <설치한 버전>
    $ pyenv rehash
    ```
    - 명령어 실행후 다시 버전 확인
6. 윈도우에 설치하기
   - 리눅스 가상환경 설정 후 리눅스와 동일
7. 리눅스에 설치하기
   - 파이썬 컴파일 필요 패키지 설치
   - 리눅스 배포판에 따라 다들 수 있는데 우분투(Ubuntu)와 CentOS 사용 경우, 다음과 같음
   - 우분투
     - `$ sudo apt-get install git gcc make openssl libssl-dev libbz2-dev libreadline0dev libsqlite3-dev`
   - CentOS
     - `$ sudo yum install gcc bzip2 bzip2-devel openssl openssl-devel readline readline-devel`
   - macOS 설치하기 처럼 Pyenv 사용, 파이썬 3 설치, 버전 관리
     - macOS와 이하 같음. 