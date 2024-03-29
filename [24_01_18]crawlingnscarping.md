# 1. 크롤링과 스크레이핑
## 2. Wget으로 시작하는 크롤러 개발
### 1. 처음 만들어보는 크롤러 - 이어서
#### 1. Wget을 크롤러로 사용
- 재귀적으로 내려받기
  - 재귀적으로 내려받을때는 -r 옵션 지정
  - 재귀적으로 내려받을때는 기본적으로 5단계까지 순회
  - 5단계는 어느정도 깊은 단계이며 내려받는데 시간도 꽤 걸림
  - 따라서 -l 옵션을 사용, 몇번째 단계까지 순회할 것인지 지정 가능
  - -l1이라고 지정하면 1단계까지만 링크 타고 순회, 따라서 지정한 URL 내부에 있는 링크까지만 내려받음
  - 일반적으로 Wget 사용 시 1단계까지만 순회해도 충분, -l1을 지정, 서버에 불필요한 부하를 회피
  - ```$ wget -r -l1 <URL 링크>```
- 내려받을 간격 지정
  - 재귀적으로 여러 파일을 내려받으면 접근 집중 가능
  - 재귀적으로 내려받을 때 내려받을 간격 지정 옵션은 -w
  - -w옵션은 내려받기 시작 전 지정한 시간만큼 대기
  - ```$ wget -r -l1 -w3 <URL 링크>```
- 특정 확장자의 파일만 내려받기
  - 크롤러 사용 이미지 수집 시 '확장자가 jpg인 파일만 내려받음' 방식을 생각 가능
  - -A 옵션 사용 시 확장자 jpg인 파일만 ㅐㄴ려받기 가능, 여러개 확장자를 지정시 -A jpg,png,gif 처럼 쉼표로 구분
  - ```$ wget -r -l1 -A jpg,png,gif <URL 링크>```
- 특정 확장자 파일 내려받기 대상에서 제외
  - 이미지 파일이 용량이 커서 네트워크 부하가 생기므로 제외 와 같은 경우 사용
  - -R 옵션 사용, 여러 확장자 지정 시 쉼표로 구분 지정
  - ```$ wget -r -li -R jpg,png,gif <URL 링크>```
- 부모 디렉터리를 크롤링 대상에서 제외
  - 부모 디렉터리를 크롤링 대상에서 제외하면 특정 디레거리 아래의 대상만 크롤링 가능
  - -np 옵션 사용
  - ```$ wget -r -np <부모 디렉터리 URL링크>```
#### 2. 크롤링 실습
- -r 옵션 사용, 재귀적 내려받기
- -l 옵션과 -w 옵션 지정, 링크 내려받는 깊이와 내려받는 시간 간격 지정
- 부모 디렉터리 -np 옵션, -r 옵션으로 이미지 파일 제ㅚ
- ```$ wget -r -l1 -w3 -np -R jpg,png,gif <URL 링크>```
1. tree 명령어로 트리 출력
   - Homebrew로 tree 설치
   - ```brew insstall tree```
   - tree 명령어 사용 시 디렉터리 구성 간단확인 가능, -R 옵션 사용으로 섬네일 이미지 등 내려받기 제외 확인 가능
## 3. 유닉스 명령어
### 1. 명령 라인 셀 사용
- HTML 파일 스크레이핑
- 파이썬과 강력한 라이브러리를 사용하지 않아도 스크레이핑 가능
- 유닉스 명령어 조합하여 텍스트 처리 및 데이터 추출
- 명령 라인 셸의 파이프 기능 사용
- |를 사용하면 어떤 명령어의 처리 결과를 다른 명령어로 넘기기 가능
- ps 명령어에 x 옵션 지정, 현재 실행 중 프로세스 출력 가능
- 실행 중 프로세스 중에서 /user/libexec과 관련된 프로세스 추출 시
- ```$ ps x | grep /usr/libexec```
- wget 옵션 중 -O 옵션에 하이픈 지정, 표준 출력 시 파이프 활용, 결과를 다른 유닉스 명령어 넘기기 가능
- 추가로 파이프를 계속 연결 시 여러 명령어 연결 가능