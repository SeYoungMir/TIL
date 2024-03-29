### 4. 인터페이스 보안 기능 적용
#### 1. 구현된 인터페이스 주요 보안 취약점
1.  데이터 통신 시 데이터 탈취 위협
    - 인터페이스를 위한 송 , 수신 시스템 간의 데이터 통신 시 Sniffing, Spoofing, Sniffer등을 통해 통신 내역을 훼손할 수 있음
2.  시큐어 코딩
    - 소프트웨어를 개발함에 있어 개발자의 실수, 논리적 오류 등으로 인해 소프트웨어에 내포될 수 있는 보안 취약점을 배제하기 위한 코딩 기법을 뜻함
    <table>
        [시큐어 코딩 가이드]
        <tr>
            <th>유형</th>
            <th>설명</th>
            <th>대표적 보안 약점</th>
        </tr>
        <tr>
            <td>입력데이터 검증 및 표현</td>
            <td>프로그램 입력값에 대한 검증 누락 혹은 부적절한 검증, 데이터의 잘못된 현식 지정으로 발생할 수 있는 보안 약점</td>
            <td>SQL 삽입, 크로스사이트 스크립팅 등 26개</td>
        </tr>
        <tr>
            <td>보안 기능</td>
            <td>보안 기능을 적절하지 않게 구현 시 발생할 수 있는 보안 약점</td>
            <td>부적절한 인가, 중요정보 평문저장 등 24개</td>
        </tr>
        <tr>
            <td>시간 및 상태</td>
            <td>동시 또는 거의 동시 수행을 지원하는 병렬 시스템</td>
            <td>경쟁조건, 제어문을 사용하지 않는 재귀함수 등 7개</td>
        </tr>
        <tr>
            <td>에러 처리</td>
            <td>에러 처리하지 않거나, 불충분하게 처리하여 에러정보에 중요 정보가 포함될 때 발생할 수 있는 보안 약점</td>
            <td>취약한 패스워드 요구 조건, 오류 메시지를 통한 정보노출 등 4개</td>
        </tr>
        <tr>
            <td>코드 오류</td>
            <td>타입 변환 오류, 자원의 부적절한 반환 등과 같이 개발자가 범할 수 있는 코딩오류로 인해 유발되는 보안 약점</td>
            <td>널 포인터 역참조, 부적절한 자원 해제 등 7개</td>
        </tr>
        <tr>
            <td>캡슐화</td>
            <td>중요한 데이터 또는 기능성을 불충분하게 캡슐화했을 때 인가되지 않는 사용자에게 데이터 누출이 가능해지는 보안 약점</td>
            <td>제거되지 않고 남은 디버거 코드, 시스템 데이터 정보 노출 등 8개</td>
        </tr>
        <tr>
            <td>API 오용</td>
            <td>의도된 사용에 반하는 방법으로 API를 사용하거나 보안에 취약한 API를 사용하여 발생할 수 있는 보안 약점</td>
            <td>DNS Lookup에 의존한 보안결정, 널 매개변수 미조사 등 7개</td>
        </tr>
    </table>
    #### 2. 데이터베이스 암호화
    1. 데이터베이스 암호화 알고리즘
        <table>
            <tr>
                <th>구분</th>
                <th>내용</th>
            </tr>
            <tr>
                <td>대칭 키 암호 알고리즘</td>
                <td>ARIA 128/192/256, SEED</td>
            </tr>
            <tr>
                <td>해시 알고리즘</td>
                <td>SHA -256/384/512, HAS -160</td>
            </tr>
            <tr>
                <td>비대칭 키 알고리즘</td>
                <td>RSA, ECDSA</td>
            </tr>
        </table>
    2. 데이터베이스 암호화 기법
        <table>
            <tr>
                <th>구분</th>
                <th>API 방식</th>
                <th>Filter 방식</th>
                <th>Hybrid 방식</th>
            </tr>
            <tr>
                <td>개념</td>
                <td>APP 레벨에서 암호 모듈을 적용하는 APP 수정 방식</td>
                <td>DB레벨의 확장성 프로시저 기능을 이용, DBMS에 Plug-in 또는 Snap-in 모듈로 동작하는 방식</td>
                <td>API 방식과 Filter 방식을 결합</td>
            </tr>
            <tr>
                <td>암호화/보안 방식</td>
                <td>별도의 AP 개발/ 통합</td>
                <td>DB 내 설치/ 연동</td>
                <td>어플라이언스/DB 내 설치</td>
            </tr>
            <tr>
                <td>서버 성능 부하</td>
                <td>APP 서버에 암/복호화, 정책 관리</td>
                <td>DB 서버에 암/복호화, 정책 관리, 키 관리 부하 발생</td>
                <td>DB와 어플라이언스에서 부하 분산</td>
            </tr>
            <tr>
                <td>시스템 통합 용이성</td>
                <td>APP개발 통합 기간 필요</td>
                <td>APP 변경 불필요</td>
                <td>APP 변경 불필요</td>
            </tr>
            <tr>
                <td>관리 편의성</td>
                <td>APP 변경 및 암호화 필드 변경에 따른 유지 보수 필요</td>
                <td>관리자용 GUI 이용, 다수 DB 통합 관리 가능 편의성 높음</td>
                <td>관리자용 CUI 이용, 다수 DB 통합 관리 가능 편의성 높음</td>
            </tr>
        </table>