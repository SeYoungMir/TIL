# 12. 제품 소프트웨어 패키징 - 이어서
## 2. 릴리즈 노트
6. 릴리즈 노트 작성 시의 항목
7. <table>
        <tr>
            <th>작성 항목</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>Header</td>
            <td>문서 이름(릴리즈 노트 이름), 제품 이름, 릴리즈 날짜, 버전 번호, 노트 버전, 참고 날짜 등</td>
        </tr>
        <tr>
            <td>개요</td>
            <td>제품 및 변경 등에 관한 간략한 전반적인 개요</td>
        </tr>
        <tr>
            <td>목적</td>
            <td>릴리즈 버전의 새로운 기능 목록 및 릴리즈 노트의 목적에 관한 간략한 개요, 버그 수정 및 새로운 기능의 기술</td>
        </tr>
        <tr>
            <td>이슈 요약</td>
            <td>버그의 간단한 설명 또는 릴리즈 추가 항목에 대한 요약</td>
        </tr>
        <tr>
            <td>재현 항목</td>
            <td>버그 발견에 따른 재현 단계의 기술</td>
        </tr>
        <tr>
            <td>수정 및 개선의 내용</td>
            <td>수정 및 개선 등의 간단한 설명 기술</td>
        </tr>
        <tr>
            <td>SW 지원 영향도</td>
            <td>버전 변경에 따른 SW의 지원 프로세스 및 영향도 기술</td>
        </tr>
        <tr>
            <td>사용자 영향도</td>
            <td>버전 변경에 따른 최종 사용자 기준의 기능 및 응용 프로그램 상의 영향도 기술</td>
        </tr>
        <tr>
            <td>노트</td>
            <td>SW 및 HW Install 항목, 제품, 문서를 포함한 업그레이드 항목 메모</td>
        </tr>
        <tr>
            <td>면책조항</td>
            <td>회사 및 표준 제품과 연관된 메시지, 프리웨어, 불법 복제 방지, 중복 등 참조에 관한 고지 사항</td>
        </tr>
        <tr>
            <td>연락정보</td>
            <td>사용자 지원 및 문의 관련한 연락처 정보 등</td>
        </tr>
    </table>
7. 릴리즈 노트 추가 작성 및 개선 사항 발생의 예외 케이스
   1. 테스트 단계에서의 베타 버전 출시
      - 제품 소프트웨어의 차기 버전이나 신규 버전의 베타 버전 테스트 단계에서도 릴리즈 버전으로 정보를 체크하여 릴리즈 노트를 작성할 수 있음
      - 이럴 때는 자체에서 기준을 수립하여 현 베타 버전을 신규 소스로 하여 릴리즈를 할지, 예외 사항으로 베타 버전에 대한 릴리즈 노트를 따로 만들지 사전에 정의해야 함
   2. 긴급 버그 수정 시
      - 긴급한 버그가 발견되어 이를 수정할 경우의 릴리즈 노트 작성임
      - 통상적으로 긴급히 버그가 수정되면 릴리즈 노트 작성을 놓치는 경우가 많음
      - 반드시 버그 번호를 포함한 모든 수정된 버그를 기술하여 릴리즈 노트에 추가함
   3. 자체 기능 향상을 포함한 모든 추가 기능의 향상
      - 자체적으로 기능 개선을 완료했을 때 정식으로 릴리즈 버전을 추가하고, 이에 따른 신규 릴리즈 노트를 작성함
      - 업그레이드는 SW 및 HW에 대한 항목까지 포함됨
   4. 사용자 요청에 따른 특이한 케이스 발생
      - 제품 소프트웨어가 사용자에 배포됨에 따라 기존에 포된 릴리즈 노트의 연락처 정보를 통해 사용자의 의견이 접수된 경우임
      - 개발 팀 내부에서 허용되는 범위 내에서 요청이 접수될 경우 이를 자체 기능 향상과는 별도의 버전으로 새로 추가하여 릴리즈 노트를 작성할 수 있음.