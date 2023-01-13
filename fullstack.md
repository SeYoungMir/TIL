웹 크롤링
데이터 엔지니어링
머신 러닝 & 딥러닝
분산처리 시스템

제일 먼저 물어보는 것
1. 파이썬
2. 리눅스


미니 프로젝트
-시각화


웹 크롤링
쟝고
엑셀 파일 공공데이터 분석 -> 시각화

머신러닝, 딥러닝 프로젝트

웹 서비스 -> 쟝고

전체 서비스 구현 

현업의 기획부

`프로젝트 1년 짜리`

`1년 전 3~4개월 기획`

프로그램은 타이핑부터 치진 않음

외국에서는 생각부터.

순서도, 알고리즘.

### Cloud Computing
- I as S 
  - Infra structure as Structure 
- P as S 
  - Platfom as Structure
- S as S 
  - Software as Structure
- [NIST](NIST.gov)
- `가상화 기술`
  1. 메모리 가상화
      - 하드디스크의 일부를 메모리처럼 사용
      - 논리적으로 선언  
  2. 자원 분할
      - OS,CPU,memory,storage,network...
  3. 자원 통합
     - OS,CPU,memory,storage,network...
     - 복수 물리 자원을 논리적으로 통합, 단일한 물리 자원처럼 동작
     - 서버 클러스터링: 복수의 서버 통합, 단일 서버로 동작
  4. Scale Out/Up
      - 확장 -> Out /Up
      - 축소 -> In /Out
      - Scale Up과 Out의 차이는?
        - 서버 자체의 크기를 늘리면 UP, 서버 대수의 수를 늘리면 Out
      - autoscale ->예측
  #### Definition
   - 클라우드 컴퓨팅은 인터넷(Network)기술을 이용하여 내,외부 고객들에게 확장성(Scalable)이 있고 탄력적(Elastic)인 IT 서비스가 제공되는 방식
   - 확장성(범위성)은 늘어나는 것만이 아니라 줄어드는 것도 포함
   - 컴퓨팅 자원이 필요한 만큼 늘어나거나 적정 수준으로 줄어들 수 있음
   - 이러한 작업(요청)이 수분에서 수십분 이내로 가능
   - 확장성은 범위, 탄력성은 시간
   - 제한점
     - 인터넷 연결 필요
     - 보안 문제
     - 프라이버시 문제
     - 벤더에 묶이는 문제(올기기 어려움)
   - 특징
     - 주문형 셀프 서비스
     - 광대역망 액서스
     - 자원 공동관리
     - 빠른 요구탄력성
     - 도수제
   - On Premise
     - 회사 내부적으로만 
   - OffPremise
     - 그 외부적으로도 사용 가능
- VM(EC2)
- OS(윈도우 서버, 리눅스 서버)
  - Host- HyperBASUSER <VM1/VM2/VM3..
- 컨테이너 (도커, 쿠버네토스)
  -  서버(OS+Sever) +Config 설정
  -  web-server
  -  mail-server
