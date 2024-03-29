# 2. 크롤러 설계
## 3. 배치를 만들 때의 주의점
### 1. 배치란?
2. 중간 데이터 저장해두기
   - 각각의 공정을 나누려면 네트워크 요청한 데이터 등의 중간 데이터를 저장해두는 것이 좋음
   - 어떤 페이지 스크레이핑에 실패했을 때 해당 페이지의 HTML 소스 코드를 저장해뒀다면 스크레이핑 프로그램만 수정하고 재실행하며 디버깅 가능
   - 네트워크 요청에는 시간이 걸리므로 요청에 실패한 페이지가 있다면 실패한 페이지만 다시 요청할 수 있는 구조로 설계하는 것이 좋음. 그렇게 하면 데이터를 보충할 때도 시간을 단축할 수 있음
   - 또한 이렇게 설계 시 다른 이유로 몇몇 페이지에 크롤러가 접근할 수 없을 때도 수동으로 해당 페이지만 내려받고 다음 공정으로 넘어갈 수 있음
3. 실행 시간 알아 두기
   - 대상 사이트에 스크레이핑하는 페이지가 많을 때는 실행 시간을 알아두면 이후에 설계할 때 조금 더 효율적으로 설계할 수 있음. 예를 들어 어떤 사이트를 크롤링할 때 어느 정도 시간이 걸리느지 알고 있는데 같은 사이트를 다시 크롤링할 때 시간이 오래 걸리면 어디선가 오류 발생 가능성 판단 가능
   - 크롤러 개발 시 크롤링 경과 상태도 알 수 있게 하면 좋음. 처리중인 URL 또는 현재 진행하고 있는 공정이 무엇인지 출력하면 생각한대로 프로그램이 동작하는지 판단 가능
   - 크롤링 할 때 여러 상태를 저장해두면 이후 판단하는데 도움
   - 네트워크 요청을 할 때 HTTP 상태 코드를 저장 시 대상 데이터를 추출할 수 없었을 때 링크가 깨진 것인지, 서버에 오류가 발생한 것인지, 유지 보수 중이엇는지 판단 가능
4. 중지 조건을 명확하게 하기
   - 재귀적으로 링크를 추출, 재귀적으로 스크레이핑 시 정지 조건을 명확하게 해 두지 않으면 무한 루프 가능
   - 크롤링하는 계층과 도메인을 한정 혹은 내려받을 파일의 상한을 정하는 등 조건에 따라 크롤링이 끝나게 만들면 좋음
5. 함수의 매개 변수를 간단하게 하기
   - 디버깅할 때는 공정의 처리를 부분적으로 재현해야 할 때 있음.
   - 복잡한 객체를 함수의 매개변수로 한다면 객체 재현 시 오랜 시간 걸릴 수 있으며, 객체 실수로 잘못 만들어 상황이 제대로 재현되지 않는 문제 발생 가능.
   - 중간 데이터를 꼭 저장해두고, 이를 매개변수로 전달하면 좋음
6. 날짜를 다룰 때의 주의 사항
   - 데이터베이스에 데이터의 변경일을 저장할 때는 UTC로 저장하는 것이 좋음. 크롤링 대상 데이터에 날짜가 포함되어 있을 때 한국 표준시로만 표기되어 있지 않을 수 있기 때문에 UTC로 통일 추천.
   - 크롤링을 실행하는 머신의 날짜와 시간도 UTC로부터 큰 차이가 발생하지 않게 NTP를 넣어서 정확한 날짜와 시간 지정이 좋음.
### 2. 설계 예
- 정석 설계 패턴이 있지만 목적과 대상에 따라 설계 상이
- 출판사 사이트에서 데이터 크롤링 예시
1. 소스 확인
   - 페이징이 구성되어 있지 않고, 한 페이지에서 300개가 넘는 도서 정보를 제공,
   - 이 목록 전체를 크롤링
   - 출판사의 책은 그렇게 자주 안나오므로 빈도는 일주일에 한 번, 데이터가 급히 필요한 게 아니라면 빈도가 높을 필요는 없으므로, 재시도 처리는 패스
   - HTML 소스 파싱 방법
   - <xmp><meta caherset="UTF-8"></xmp> 에서 사이트가 UTF-8로 만들어진 사이트라는 걸 알 수 있고, Curl 명령어로 다음과 같이 읽어들일 수 있음
   - ```$ curl -Ss <URL> | head '```
   - 위와 같은 명령어로 한글 부분이 잘 나오면 정상적으로 잘 읽히므로 문자 코드를 따로 고려하지 않아도 됨.
