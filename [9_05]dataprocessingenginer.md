## 2. 함수
1. 함수의 정의
   1. 관계형 데이터베이스에서는 단일 행 기준의 처리가 주로 이루어짐
   2. 총합, 평균 등의 데이터 분석을 위해서는 복수 행 기준의 데이터를 모아서 처리함
   3. 원 데이터와 그 데이터를 유도하는 방법을 기술한 절차적 방법임
   4. 두 개 이상의 테이블의 데이터를 연결하여 하나로 결합하는 방법임
   5. 두 개 이상의 질의를 하나의 결과로 만들어줌
   6. 관계를 처리하기 위해 연산자와 연산 규칙을 제공하는 언어로 검색 질의를 기술하는 표현임
2. 데이터 분석 함수의 유형
   1. 집계 함수(Aggrecate Function)
   2. 그룹 함수(Group Function)
   3. 윈도우 함수(Window Function)
3. 집계 함수
   1. GROUP BY 구문을 그룹핑하여 분석 결과 데이터를 반환함
   2. GROUP BY 구문 뒤에는 테이블을 구분하는 컬럼을 기재하여 그룹화함
   3. HAVING 구문은 그룹화된 집합에 대한 조건을 지정할 경우 사용함
   4. WHERE 조건은 데이터 집합으로부터 그룹화된 집합에 대한 조건 선택 시에 HAVING 을 사용함
   5. HAVING 구문은 선택으로, 상수나 집약 함수, 집약 키를 사용할 수 있음
4. 집계함수 종류
    <table>
        <tr>
            <th>함수</th>
            <th>의미</th>
            <th>사용 가능한 속성의 타입</th>
        </tr>
        <tr>
            <td>COUNT</td>
            <td>속성 값의 개수</td>
            <td rowspan=3>모든 데이터</td>
        </tr>
        <tr>
            <td>MAX</td>
            <td>속성 값의 최대값</td>
        </tr>
        <tr>
            <td>MIN</td>
            <td>속성 값의 최솟값</td>
        </tr>
        <tr>
            <td>SUM</td>
            <td>속성 값의 합계</td>
            <td rowspan=2>숫자 데이터</td>
        </tr>
        <tr>
            <td>AVG</td>
            <td>속성 값의 평균</td>
        </tr>
    </table>
5. 집계함수 기본 구조
    ```SQL
    SELECT [COLUMN1,COLUMN2,..]
        <GROUP FUNCTION>
        FROM <TABLE NAME>
        WHERE
        GROUP BY [COLUMN1,COLUMN2,...]
      [HAVING] 조건 (GROUP FUNCTION)
    ```
6. GROUP BY 구문
   1. 테이블에서 특정 속성의 값이 같은 튜플을 모아 그룹을 만들고, 그룹별로 검색하기 위한 것으로 그룹에 대한 조건을 추가하려면 GROUP BY 키워드를 HAVING 키워드와 함께 사용함
   2. NULL 값을 가지는 ROW는 제외함
   3. WHERE는 GROUPBY보다 먼저 실행되며, 단일 행을 사전에 선별함
   4. 데이터 분석 값을 보고자 하는 컬럼 단위를 선정할 때 사용하는 기준이 됨
7. HAVING
   1. WHERE 구문 내에는 사용할 수 없는 집계 함수를 적용하여 계산 결과를 조건별로 적용함
   2. GROUP BY 뒤에 사용하며, 기준 항목이나 소그룹 집계 함수를 활용한 조건을 적용함