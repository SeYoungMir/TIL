# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 2. 공개 데이터 사용
### 1. 공개 데이터란?
2. 인증키 발급.
   - 공공 데이터 포털의 정보들은 인증키가 있어야 사용 가능. 특정 개인 또는 단체가 서버에 무리한 요청을 보내는 것을 막기 위해 인증키를 사용해 요청 제한을 거는 것.
   - 개발 계정을 신청한 후 화면 상단의 '마이페이지'에 들어가면 활용 신청이 승낙되었다고 나옴. 아래쪽에 있는 목록에서 앞서 신청한 '대기오염정보 조회 서비스'를 클릭해 상세 화면 진입.
   - '개발 계정 상세보기'에 들어가면 '일반 인증키 받기'를 클릭해서 인증키 발급.
   - 버튼을 눌렀을 때 출력된 인증키를 복사해서 저장.
   - 인증키를 발급받아도 사용하기까지 6시간 이상 걸릴 수도 있음. 'Service Key is not registered'등의 메시지가 나오면 시간을 두고 진행.
3. 공개 데이터 활용
   - 본격적으로 데이터사용. 데이터 상세 화면 아래를 보면 '미리보기' 버튼 있음. 버튼 클릭
   - 데이터 미리보기 클릭 시 다음과 같은 URL로 이동
   - ```html
     http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnTnforInqquireSvc/getMsrstnAcctoRltmMesureDnsty
     ?servieceKey=서비스키
     &numOfRows=10
     &pageNo=1
     &stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC
     &dataTerm=DAILY
     &ver=1.3
     ```
   - 이 때 기본적인 주소 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnTnforInqquireSvc/getMsrstnAcctoRltmMesureDnsty'를 '엔드 포인트(End Point)' 라고 부름. 요청의 최종 지점이라서 엔드 포인트라고 부름.
   - 이어서 '?'를 기준으로 serviceKey,numOfRows,PageNo,stationName,dataTerm,ver이라는 키와 값이'&'로 연결. 이를 '요청 매개 변수'리고 부름.
 - 공공 데이터 포털의 데이터를 사용할 때는 이처럼 엔드 포인트와 요청 매개 변수를 확실하게 알아야 함. 이러한 정보는 각각의 데이터에서 제공하는 문서에 자세하게 정리되어 있음. 이러한 데이터를 활용할 때는 예(현재 공공 데이터 포털의 경우 미리보기)와 문서를 잘 보고 활용 방법을 찾아야 함.