# 1. 빅데이터 이해하기
## 7. 빅데이터와 보안
### 2. 접근제어 보안
- 빅데이터 시스템의 접근제어(인증, 권한)를 완벽하게 처리하는데에는 어려움이 있음
- 분산 환경의 복잡 다양한 빅데이터 오픈소스 소프트웨어를 대상으로 접근 보안 정책을 적용하기 위해서 오픈소스를 수정 혹은 유료 버전을 구입해야 하는 상활 발생 가능.
- 빅데이터 시스템의 물리적(네트워크) 위치는 대부부분 방화벽 안쪽으로 외부 공격이나 불특정 다수의 접근이 원천적으로 불가하며, 데이터는 앞서 설명한 비식별화된 데이터로 저장되어 있어 보통은 저수준의 접근 제어 정책을 적용.
- 일부 금융권 및 민감한 빅데이터 시스템의 경우 엄격한 접근제어 정책과 보안 준수를 요구하고 있으며, 이를 해결하기 위한 기술로 아파치 녹스(Apache Knox), 아파치 센트리(Apache Sentry), 아파치 레인저(Apache Ranger), 케르베로스(Kerberos)등을 활용 가능
- 아파치 녹스의 경우 네트워크 상의 DMZ에 위치시킴으로써 외부 클라이언트가 하둡 에코시스템에 직접 접근할는 것을 막고, 항상 녹스를 거쳐 통신하게 하는 중간 게이트웨이 역할로 주로 사용됨. 이 때 들어온 요청에 대한 접근 인증을 LDAP(Lightweight Directory Access Protocol)과 KDC(Key Distribution Center)로 제공 가능
- 아파치 센트리는 하둡 파일시스템에 상세한 접근 제어(하둡 파일/ 디렉터리, 하이브 테이블 등) 가 필요할 때 사용. 하둡 데이터에 접근하려는 클라이언트는 센트리 에이전트(Sentry Agent)를 반드시 설치해야하고, 센트리 에이전트가 중앙에 있는 센트리 서버와 통신하면서 접근 권한을 획득하게 됨. 접근 이력을 관리하는 기능이 있어 향후 감사 로그를 편리하게 조회 가능.
- 아파치 레인저는 센트리와 유사한 아키텍처와 역할을 가지고 있음. 아파치 레인저는 호튼웍스, 센트리는 클라우데라에서 지원. 레인저에서 지원하는 에코시스템이 많아 범용성이 좀 더 높음. 레인저를 사용할 경우 플러그인을 통해 레인저 서버와 통신하게 되고, 센트리와 마찬가지로 접근 이력을 관리하는 감사 로그 기능을 제공함.
- 케르베로스는 KDC(Key Distribution Center) 시스템으로 불리며, 빅데이터 ㅇ외에도 이미 다양한 곳에서 활용되고 있는 범용화된 인증 시스템임. 케르베로스는 크게 AS(Authentication Service)라는 인증 서버와 TGS(Ticket Granting Service)라는 티켓 발행 서버로 구성. 하둡 파일 시스템에 접근하려는 클라이언트 에코시스템은 AS 인증 서버를 통해 최초 인증을 수행하고 TGS 티켓 발행 서버로부터 하둡 파일 시스템에 접근을 허용하는 티켓을 발행받고, 이후부터는 유효한 티켓만 있으면 하둡 파일시스템에 인증 없이 접근 가능.
- 실제 프로젝트에서는 녹스, 센트리, 레인저, 케르베로스 등 구성 시 필요한 인증/권한 정보를 자체적으로 생성하지 않고, 기존의 계정/권한 통합 관리시스템(IAM, EAM, LDAP 등)과 연동 및 동기화 작업을 통해 구축함.
