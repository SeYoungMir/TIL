## 4. 보안 기능 - 이어서
2. 보안 기능의 보안 약점
<table>
    <tr>
        <th>종류</th>
        <th>보안 약점</th>
        <th>해결 방법</th>
    </tr>
    <tr>
        <td>적절한 인가 없이 중요기능 허용</td>
        <td>보안 검사를 우회하여 인증 과정 없이 중요 정보 또는 기능에 접근 및 변경 가능</td>
        <td>중요 정보나 기능을 수행하는 페이지에는 재인증 기능을 수행</td>
    </tr>
    <tr>
        <td>부적절한 인가</td>
        <td>접근 제어 기능이 없는 실행경로를 통해 정보 또는 권한 탈취</td>
        <td>모든 실행 경로에 대해 접근 제어 검사 수행 사용자에게는 반드시 필요한 접근 권한만 부여</td>
    </tr>
    <tr>
        <td>중요한 자원에 대한 잘못된 권한 설정</td>
        <td>권한 설정이 잘못된 자원에 접근하여 임의로 사용</td>
        <td>관리자만 자원들에 접근하도록 설정 <br> 인가되지 않은 사용자의 중요 자원 접근 여부 검사</td>
    </tr>
    <tr>
        <td>취약한 암호화 알고리즘 사용</td>
        <td>암호화 된 환경설정 파일을 해독하여 중요정보 탈취</td>
        <td>안전한 암호화 알고리즘 사용 <br> IT 보안 인증사무국이 안정성을 확인한 암호모듈을 이용</td>
    </tr>
    <tr>
        <td>중요정보 평문 저장 및 전송</td>
        <td>암호화되지 않은 평문 데이터를 탈취해 중요 정보 혹득</td>
        <td>중요 정보 저장, 전송 시 암호화과정을 거침, 보안 채널 이용</td>
    </tr>
    <tr>
        <td>하드코드 된 비밀번호</td>
        <td>소스코드 유출 시 내부에 하드코드 된 패스워드 이용</td>
        <td>패스워드를 암호화하여 별도 파일 저장 <br> 기본 설정 패스워드나 키의 사용을 피함</td>
    </tr>
</table>

3. 소프트웨어 보안 3 요소
   1. 정보보안의 3가지 요소인 무결성, 기밀성, 가용성 등을 지키며 서버 취약점을 미리 예방해 내외부 위협으로부터 리스크를 최소화하는 구축 방식을 의미함
* 참고
  * 취약점 진단을 실행하기 위한 하드웨어 환경의 구성
    <table>
        <tr>
            <th>하드웨어</th>
            <th>설명</th>
        </tr>
        <tr>
            <td>진단 서버</td>
            <td>취약점 진단을 수행하기 위해 필요한 CPU, 메모리 등 각종 하드웨어가 장착된 서버임</td>
        </tr>
        <tr>
            <td>스토리지</td>
            <td>취약점 진단을 수행하기 위해 필요한 데이터를 담아두는 저장 공간으로 이러한 데이터를 취약점 진단 데이터라고함</td>
        </tr>
        <tr>
            <td>네트워크</td>
            <td>서버와 클라이언트를 연결해 주는 연결망으로 기업 내부에서는 근거리 유선망(LAN,Local Area Network)로 구성됨</td>
        </tr>
    </table>
   
   2. 소프트웨어 개발 보안의 위협, 위험 개념도
      - 위험
        - 자산
           - 취약점
           - 취약점
         - 위협원 > 자산 위협
* 참고
  * 소프트웨어 개발보안 요구공학 프로세스
    * 요구사항 개발(CMMi L3 PA)
      * 도출(Elicitation)
      * 분석(Analysis)
        * 명확화 > 도출
      * 명세(Specification)
      * 확인(Validation)
        * 재작업 > 명세
        * 수정차이 해소 > 도출
    * 요구사항 관리 (CMMi L2 PA)
      * 요구사항 변경 관리, 추적 관리