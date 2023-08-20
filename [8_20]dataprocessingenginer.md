* 참고
  * 소스 Code
    1. 소스 코드 최적화는 읽기 쉽고 변경 및 추가가 쉬운 클린 코드를 작성하는 것을 의미함
    2. 소스코드 품질을 위해 기본적으로 지킬 원칙과 기준을 정의하고 있음
    3. Bad Code
       1. 내용
          - 타 개발자가 로직을 이해하기 어렵게 작성한 코드를 의미함
          - 예를 들어 처리 로직의 제어가 정제되지 않고 서로 얽혀 있는 스파게티 코드, 변수나 메소드에 대한 이름 정의를 알 수 없는 코드, 동일한 처리 로직이 중복되게 작성된 코드 등이 있음
       2. 특징
          - 소스 코드 이해가 안 되어 계속 덧붙이기 할 경우에 코드 복잡도가 증가하게 됨
          - 스파게티 코드의 경우 잦은 오류가 발생할 가능성이 존재함
    4. Clean Code
       1. 내용
          - 잘 작성되어 가독성이 높음
          - 단순하며 의존성을 줄이고 중복을 최소화하여 깔끔하게 정리된 코드를 의미함
       2. 특징
          - 버그를 찾기 쉬워지며, 프로그래밍 속도가 빨라지게 됨
          - 중복 코드 제거로 인해 애플리케이션의 설계가 개선되어짐
          - 가독성이 높기 때문에 애플리케이션의 기능에 대해 용이하게 이해할 수 있음

* 참고
  - 클린 코드의 작성 원칙
    <table>
        <tr>
            <th>작성 원칙</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>추상화의 원칙</td>
            <td>세부적 내용은 하위 클래스, 메소드, 함수 등에서 구현함<br>클래스, 메소드, 함수 등에 대해서 서로 같은 수준의 추상화를 함</td>
        </tr>
        <tr>
            <td>중복성의 원칙</td>
            <td>공통된 코드를 활용함<br>중복된 코드를 제거함</td>
        </tr>
        <tr>
            <td>단순성의 원칙</td>
            <td>클래스,메소드,함수 등을 최소 단위로 구분함<br>한 번에 한 가지 처리만을 수행함</td>
            <tr>
            <td>가독성의 원칙</td>
            <td>코드 작성 시에 들여쓰기 기능을 활용함<br>이해하기 용이한 용어를 활용함</td>
        </tr>
        <tr>
            <td>의존성의 원칙</td>
            <td>코드 변경이 타 부분에 영향이 없게 작성하게함<br>영향도를 최소화시킴</td>
        </tr>
    </table>

* 참고
  - 소스 코드 품질품석 도구
    <table>
        <tr>
            <th>구분</th>
            <th>도구명</th>
            <th>도구 설명</th>
            <th>지원환경</th>
            <th>개발도구 지원</th>
            <th>홈페이지</th>
        </tr>
        <tr>
            <td rowspan=4>정적 분석 도구</td>
            <td>pmd</td>
            <td>자바 및 타 언어 소스코드에 대한 버그, 데드 코드 분석</td>
            <td>Linux,Windows</td>
            <td>Eclipse,Netbeans</td>
            <td>pmd.github.io</td>
        </tr>
        <tr>
            <td>cppcheck</td>
            <td>C/C++ 코드에 대한 메모리 누수, 오버플로우 등 문제 분석</td>
            <td>Windows</td>
            <td>Eclipse,gedit</td>
            <td>cpcheck.sourceforge.net</td>
        </tr>
        <tr>
            <td>SonarQube</td>
            <td>소스코드 품질 통합 플랫폼, 플러그인 확장 가능</td>
            <td>Cross-Platform</td>
            <td>Eclipse</td>
            <td>www.sonarqube.org</td>
        </tr>
        <tr>
            <td>checkstyle</td>
            <td>자바 코드에 대한 코딩 표준 준수 검사 도구</td>
            <td>Cross-Platfrom</td>
            <td>Ant,Eclipse,Netbeans</td>
            <td>checkstyle.sourceforge.net</td>
        </tr>
        <tr>
            <td rowspan=2>코드 복잡도</td>
            <td>ccm</td>
            <td>다양한 언어의 코드 복잡도 분석 도구, Linux,Mac환경 CLI형태 지원</td>
            <td>Cross-Platform</td>
            <td>VisualStudio</td>
            <td>github.com/jonasblunck/ccm</td>
        </tr>
        <tr>
            <td>cobertura</td>
            <td>jcoverage 기반의 테스트 커버리지 측정 도구</td>
            <td>Cross-Platform</td>
            <td>Ant,Maven</td>
            <td>cobertura.github.io/cobbertura</td>
        </tr>
        <tr>
            <td rowspan=2>동적 분석 도구</td>
            <td>Avalanche</td>
            <td>Valgrind 프레임워크 및 STP 기반 소프트웨어 에러 및 취약점 동적 분석 도구</td>
            <td>Linux,Android</td>
            <td>-</td>
            <td>code.google.com/archive/p/avalanche</td>
        </tr>
        <tr>
            <td>Valgrind</td>
            <td>자동화된 메모리 및 쓰레드 결함 발견 분석 도구</td>
            <td>Cross-Platform</td>
            <td>Eclipse,NetBeans</td>
            <td>valgrind.org</td>
        </tr>
    </table>