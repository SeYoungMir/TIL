# 5. 인터페이스 구현
## 1. 인터페이스 설계서 확인하기
### 1. 외부, 내부 모듈 간 공통 기능 및 데이터 인터페이스 확인
#### 1. 인터페이스 설계서
1. 인터페이스 설계서(정의서)
   - 시스템의 인터페이스 현황을 한 눈에 확인하기 위하여 시스템의 인터페이스 목록 및 각 인터페이스의 상세 데이터 명세와 각 기능의 세부 인터페이스 정보를 정의한 문서
2. 인터페이스 목록
   - 시스템에서 가지고 있는 인터페이스 목록을 보여주며, 인터페이스 번호 및 시스템 정보 관련 요구사항 ID를 리스트 형태로 보여줌
3. 인터페이스 명세
   - 인터페이스 목록에 있는 각 인터페이스의 상세 정보를 보여줌. 각 인터페이스 번호당 인터페이스 되는 데이터, 형식, 송수신 시스템의 정보 등을 구체화
4. 상세 기능별 인터페이스 정의서
   - 인터페이스를 통한 각 세부 기능의 개요, 세부 기능이 동작하기 전에 필요한 사전 ㄷ조건, 사후 조건 및 인터페이스 파라미터, 호출 이후 결과를 확인하기 위한 반환값등을 정의한 문서
   - 상세 기능 별 인터페이스 정의서 주요 항목
     - 인터페이스 ID : 인터페이스를 구분하는 식별자
     - 인터페이스 명 : 인터페이스의 고유 명칭
     - 오퍼레이션 명 : 세부 동작 명칭
     - 오퍼레이션 개요 : 세부 설명
     - 사전 조건 : 선행 되어야 하는 상태
     - 사후 조건 : 정상적인 구현 상태 기술
     - 파라미터 : 구성 항목 값
     - 반환값 : 전송 후 반환값
#### 2. 정적 $\cdot$동적 모형, 데이터 포맷 형태에 따른 인터페이스 설계서
- 정적, 동적 모형으로 각 시스템의 구성 요소를 표현한 다이어그램을 통해 시스템, 컴포넌트 별 인터페이서와 요구 조건을 확인 가능
1. 정적, 동적 모형을 통한 인터페이스 설계서
   - 시스템을 구성하는 주요 구성 요소 간 트랜잭션을 보여 주고, 이를 통해 시스템에서 인터페이스는 어디에 속하고 어떤 트랜잭션이 인터페이스를 통해 상호 교환되는지 확인할 수 있음
2. 데이터 정의를 통한 인터페이스 설계서
   - 제공하는 인터페이스 서비스에 대한 상세 명세를 표현하는 산출물, 제공 서비스 목록과 이에 대한 인터페이스 방식 및 명세, 리턴 형태까지 정의를 상세화하여 개발 수준에서 인터페이스를 어떻게 구현해야 할지 명시되어 있음
     - 데이터 정의를 통한 인터페이스 설계서 예시
       - [3.3.1 제공 서비스 목록]
        <table>
            <tr>
                <th>순번</th>
                <th>제공 서비스</th>
                <th>항목 설명</th>
            </tr>
            <tr>
                <td>1</td>
                <td>제품 리콜 정보 조회</td>
                <td>아이디, 제품명, 상품명</td>
            </tr>
            <tr>
                <td>2</td>
                <td>제품 리콜 정보 상세 조회</td>
                <td></td>
            </tr>
        </table>
      - [3.3.1.1 제품 리콜 정보 조회]
        <table>
            <tr>
                <th>HTTP Method</th>
                <th>GET</th>
            </tr>
            <tr>
                <td>HTTP URL</td>
                <td>http://www.co.kr/open_api/recallList.Joy?conditionkey=[검색구분]&conditionValue[검색어]</td>
            </tr>
            요청메시지 URL
        </table>

        <table>
            <tr>
                <th>항목명(영문)</th>
                <th>항목명(국문)</th>
                <th>항목 구분</th>
                <th>항목 설명</th>
            </tr>
            <tr>
                <td>conditonkey</td>
                <td>검색 구분</td>
                <td>필수</td>
                <td>Recall_ID : 리콜 아이디<br>ModelName : 상표명 <br>ProductName : 제품명</td>
            </tr>
            <tr>
                <td>conditionValue</td>
                <td>검색어</td>
                <td>필수</td>
                <td></td>
            </tr>
            요청메시지 명세
        </table>

        <table>
            <tr>
                <th>항목명(영문)</th>
                <th>항목명(국문)</th>
                <th>항목 설명</th>
            </tr>
            <tr>
                <td>recall_Id</td>
                <td>리콜 아이디</td>
                <td>유일한 식별키</td>
            </tr>
            <tr>
                <td>modelName</td>
                <td>모델명</td>
                <td>대표적 식별 가능</td>
            </tr>
            <tr>
                <td>productName</td>
                <td>제품명</td>
                <td>상세제품 번호 표기</td>
            </tr>
            응답메시지 명세
        </table>

        <table>
            <tr>
                <td>JOY</td>
            </tr>
            <tr>
                <td>
                {<br>"resultMsg" : "Success",<br>"resultCode" : 2000, <br>"resultData" : {<br>&nbsp;&nbsp;"recall_Id" : "33131",<br>&nbsp;&nbsp;"modelName" : "WW 태블릿",<br>&nbsp;&nbsp;"productName" : "PDK18E09K"
                <br>&nbsp;&nbsp;}<br>
                }
                </td>
            </tr>
            응답메시지 형태
        </table>