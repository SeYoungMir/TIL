# 1. 크롤링과 스크레이핑
## 1. 크롤링과 스크레이핑
### 1. 크롤러와 크롤링
- 크롤러는 자동으로 웹 페이지에 있는 정보를 수집하는 프로그램.
- 사람이 브라우저로 웹 페이지를 조회하고, 정보를 수집하는 것과 비교할 수 없을 정도로 대규모의 정보를 단시간에 수집
- 다른 이름으로 봇,로봇,스파이더라고도 부름
- 크롤러로 정보를 수집하는 일을 크롤링이라 함
- 크롤러로 가장 쉽게 생각해볼 수 있늩 것은 구글 등의 검색 엔진
- 검색 엔진은 크롤러를 사용, 전 세계에 있는 웹 페이지의 정보를 모아서 축적, 사용자가 키워드를 검색하면 축적된 방대한 정보에서 적당한 웹 페이지를 찾아 제공
### 2. 스크레이핑
- 크롤러는 정보를 수집하고, 이렇게 수집한 정보를 분석해 필요한 정보를 추출하는 것이 스크레이핑
- 크롤러과 스크레이핑은 분리 불가
## 2. 크롤러가 주목받게 된 이유
- 많은 회사가 크롤러를 사용, SNS와 블로그 등에 올라온 회사에서 만든 제품과 관련된 글을 수집
- 또 다른 회사는 크래시 리포트를 분석하는 서비스를 기반, 배포한 애플리케이션의 크래시 정보(crash report)를 크롤러로 추출, 회사 직원들이 사용하는 채팅 시스템(슬랙 등)에 올리기도 함
- 사람의 힘으로 하면 방대한 시간이 걸리는 작업을 자동화할 때 크롤러 사용
- 직접 하면 비용이 많이 들고, 사업에서 신속한 판단을 위한 속도로 정보 수집이 힘듦
- 개인적인 용도로 크롤러를 사용하는 경우, 여러 사이트를 한꺼번에 순회, 특정 키워드가 있을 때 알림을 보낸다던지 하는 방법으로 필요한 정보를 찾는데 걸리는 시간이 크게 단축
## 3. 크롤링/스크레이핑 할 때의 주의 사항
- 크롤링/스크레이핑을 할 때는 정보를 다룰 때 몇 가지 주의해야 할 점이 있음
### 1. 웹 사이트에 접근할 때의 주의 사항
- 웹 사이트에 접근할 때는 다음 사항에 주의
  - 웹사이트의 이용 규약을 확인하고 지킴
  - robots.txt와 robots 메타 태그의 접근 제한 사항을 지킴
  - 제한이 없더라도 상대 서버에 부하가 가지 않을 정도의 속도로 접근
  - rel="nofollow"가 설정되어 있으면 크롤러로 접근하지 않음
  - 크롤링을 거부하는 조치가 있으면 즉시 크롤링을 중단, 이미 추출한 정보를 모두 삭제
### 2. 수집한 데이터를 다룰 때의 주의 사항
- 수집한 데이터는 저작권을 지켜서 사용
  - 저작권에 문제가 있으면 개인적인 용도로만 사용
  - 수집한 데이터를 기반으로 검색 서비스를 제공하는 경우 웹 사이트와 API등의 사용 규약을 확인하고 문제가 없을 때만 제공
  - 이용 규약이 따로 없을 때도 상대방에게 확인한 뒤에 데이터를 공개
- 상대방의 웹 사이트와 API에 피해를 주지 않는 것도 굉장히 중요