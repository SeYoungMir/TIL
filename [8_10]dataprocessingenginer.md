## 9. UI 프로토 타입 제작 및 검토
1. UI 프로토타입의 개요
   1. 사용자 요구사항을 기반으로 실제 동작하는 것처럼 만든 동적인 형태의 모형을 말함
   2. 테스트가 가능해야함
   3. 최대한 간결하게 만들어야 함
   4. 실제 사용자를 대상으로 테스트 해야 함
   5. 일부 핵심적인 기능을 제공하지만 최종 제품의 작동 방식을 이해시켜줄 기능은 반드시 포함되어야 함
   * 참고
     - 프로토타입 제작 구분
        <table>
            <tr>
                <th>구분</th>
                <th>설명</th>
            </tr>
            <tr>
                <td>주요 키의 위치와 기능</td>
                <td>화면 상에 공통적으로 배치되는 주요 키의 위치와 기능을 설명한 것으로 여러 화면 간의 일관성을 보장하기 위한 것임</td>
            </tr>
            <tr>
                <td>공통 UI 요소</td>
                <td>체크 박스, 라디오 버튼, 스크롤 바, 텍스트 입력 필드, 상하/좌우 휠, 모드 설정, 탭, 팝업 등의 각 UI 요소를 언제 사용하며 어떤 형태인지 정의하고 사용자의 조작에 어떻게 반응하는지 그 흐름을 상세하게 설명한 것임</td>
            </tr>
            <tr>
                <td>기본 스크린 레이아웃(Basic Screen Layouts)</td>
                <td>여러 화면 내에 공통적으로 나타나는 Indicators, Titles, Ok/Back, Soft Key, Option, Functional Buttons 등의 위치와 속성을 정의한 것으로서 여러 기능들 간에 화면 레이아웃의 일관성을 보장하기 위한 것임</td>
            </tr>
            <tr>
                <td>기본 인터렉션 규칙(Basic Interaction Rules)</td>
                <td>터치 제스처 등의 공통적으로 사용되는 조작의 방법, 홈 키의 동작 방식과 같은 운항 규칙, 실행, 이전, 다음, 삭제, 이동 등의 화면 전환 효과등에 대해 기술한 것임</td>
            </tr>
            <tr>
                <td>공통 단위 태스크 흐름(Task Flows)</td>
                <td>많은 기능들에 공통적으로 자주 나타나는 삭제, 검색, 매너 모드 상태에서의 소리 재생 등의 인터랙션 흐름을 설명한 것임</td>
            </tr>
            <tr>
                <td>케이스 문서</td>
                <td>다양한 상황에서의 공통적인 시스템 동작에 대해 정의한 문서임(ex. 사운드, 조명, 이벤트 케이스 등)</td>
            </tr>
        </table>

2. UI 프로토타입의 장단점
   1. 장점
      - 사전 오류의 검출이 가능함
      - 사용자를 설득 및 이해시키기가 용이
      - 요구사항을 점검하며 혼선은 예방함으로써 개발 시간을 감소킬 수 있음.
   2. 단점
      - 필요 이상의 자원 소모가 발생할 수 있음
      - 부분적으로 작업 시 중요한 작업이 생략될 수 있음
      - 프로토타입 제작으로 인해 작업 시간을 증가시킬 수 있음
3. 프로토 타이핑의 종류
   1. 페이퍼 프로토타입
      - 아날로그 방법(스케치, 글, 그림)등을 이용하여 직접 작성함
      - 제작 기간이 짧으며 제작비용이 적을 경우, 업무 회의가 빠를 경우,급하게 만들어야 하는 경우에 사용
   2. 디지털 프로토타입
      - 프로그램을 사용하여 작성함
      - 재사용이 필요하거나, 완성 제품과 비슷하게 만들어야 하거나, 숙련된 전문가가 있을 때 사용.
   * 참고
     - 프로토타입 제작 방법의 구분
        <table>
            <tr>
                <th>구분</th>
                <th>방법</th>
                <th>비고</th>
            </tr>
            <tr>
                <td>아날로그</td>
                <td>화이트보드, 펜, 종이를 이용, 포스트잇 사용</td>
                <td>손으로 직접 작성</td>
            </tr>
            <tr>
                <td>디지털</td>
                <td>파워포인트, 아크로뱃, 비지오, Invision,Marvel, Adobe XD, Flinto,Principle, Keynote , UX pin, HTML</td>
                <td>툴을 사용하여 작성</td>
            </tr>
        </table>