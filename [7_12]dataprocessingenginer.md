## 3.데이터 조작 프로시저 작성하기
### 1. 데이터 조작 프로시저 개발
#### 1. SQL 분류

1. 데이터 정의어 (DDL: Data Definition Language)
   1. 종류: CREATE,DROP,ALTER,RENAME 등
   2. 저장하고 있는 데이터를 테이블 등의 구조로 생성하고 변경하기 위하여 사용되는 명령어를 지칭
2. 데이터 조작어(DML: Data Maniplation Language)
   1. 종류: INSERT,UPDATE,DELETE 등
   2. 데이터를 변경하거나 검색하기 위하여 사용되는 명령어
   3. 트랜잭션 제어를 활용하여 실행 전 상태로 복귀 가능한 명령어
3. 데이터 제어어(DCL: Data Control Language)
   1. 종류: ROLE,GRANT,REVOKE 등
   2. 사용자 별로 데이터베이스에 접근할 수 있는 권한을 부여하거나 회수하는 명령어
#### 2. 트랜잭션 제어어(TCL: Transaction Control Language)
1. 종류: COMMIT, ROLLBACK, SAVEPOINT 등
   1. COMMIT: 트랜잭션을 완료하여 데이터 변경사항을 최종반영
   2. ROLLBACK: 데이터 변경사항을 이전 상태로 회귀
   3. SAVEPOINT: 지정된 특정 시점까지 Rollback 가능한 명령어
#### 3. 절차형 데이터 조작 프로시저 및 저장형 객체 활용
1. PL/SQL
   1. 최근의 프로그래밍 언어의 특성을 수용한, SQL의 확장 기능이라 할 수 있음
   2. Compile이 필요 없어 Script 생성 및 변경 후 바로 실행 가능
   3. 프로그램 모듈화 가능
   4. 식별자를 선언 가능
   5. Error 처리가 가능
   6. 성능 향상을 기대
   7. 선언부(DECLARE,Optional), 실행부(BEGIN/END,Mandatory), 예외처리부(Exception,Optional)로 구조화된 블록 구조로 구성
2. PL/SQL 처리 절차
   1. PL/SQL로 작성된 블럭을 오라클 서버로 보내어 PL/SQL 엔진이 SQL문과 Non SQL문을 구분
   2. Non SQL 문은 PL/SQL 엔진 내의 PL Statement Executor가, SQL문은 SQL Statement Executor가 처리
   3. Non SQL 은 Client 환경에서, SQL은 Server에서 실행
   4. PL/SQL 사용시 서버의 작업 양의 감소를 통해 네트워크 부하를 동시에 감소시켜 성능 향상에 장점
#### 4. PL/SQL을 활용한 저장형 객체 활용
1. 저장 함수(Stored Function)
   1. 특징
      - 개발자가 업무에 맞게 직접 PL/SQL로 만든 함수를 말함
      - IN 파라미터만 사용할 수 있음
      - 저장된 프로시저(Stored Procedure)와 달리 RETURN 값이 있는 경우에 사용할 수 있음
   2. 문법 예시
```sql
CREATE OR REPLACE FUNCTION function name
[(argument...)]
RETURN datatype //반환되는 값의 datatype임
IS
    [변수 선언 부분]
BEGIN
    [PL/SQL Block]
        // 'PL/SQL' 블록에는 적어도 한 개의 RETURN문이 있어야 함
        // 'PL/SQL' Block은 함수가 수행할 내용을 정의한 몸체부분임
END;
```
2. 저장 프로시저(Stored Procedure)
   1. 특징
      - 특정 작업 수행 목적의 Name Value를 가짐
      - 매개 변수를 받고, 반복적으로 사용 가능
      - 연속 실행 또는 구현이 복잡한 트랜잭션을 수행하는 PL/SQL블록을 DB에 저장하기 위해 생성
   2. 문법 예시
```sql
CREATE OR REPLACE PROCEDURE procedure_name
    IN argument
    OUT argument
IS
    [변수의 선언]
BEGIN
    [PL/SQL Block]
    //'SQL' 문장, 'PL/SQL' 제어 문장
    [EXCEPTION] // 선택
    // error가 발생할 때 수행하는 문장
END;
```
   3. Parameter의 타입
    <table>
        <tr>
            <th>구분</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>IN</td>
            <td>실행환경에서 Program으로 값을 전달</td>
        </tr>
        <tr>
            <td>OUT</td>
            <td>Program에서 실행환경으로 값을 전달</td>
        </tr>
        <tr>
            <td>INOUT</td>
            <td>실행환경에서 Program으로 값을 전달, 다시 Program에서 실행환경으로 변경된 값을 전달</td>
        </tr>
    </table>
3. 저장된 패키지(Stroed Package)
   1. 특징
      - 오라클 데이터 베이스에 저장되어 있는 연관성 있는 PL/SQL 프로시저와 함수의 집합
      - 패키지는 선언부와 본문으로 나뉨
   2. 문법 예시
      - 패키지 선언부
        ```sql
        CREATE [OR REPLACE] PACKAGE 패키지명 IS | AS [변수 선언절] [커서 선언절] [예외 선언절][PROCEDURE 선언절][FUNCTION 선언절]
        END 패키지명;
        /
        ```
      - 패키지 본문
        ```sql
        CREATE [OR REPLACE] PACKAGE BODY 패키지명 IS |AS [변수 선언절] [커서 선언절] [예외 선언절][PROCEDURE 선언절][FUNCTION 선언절]
        END 패키지명;
        /
        ```
4. 트리거(Trigger)
   1. 특징
      - INSERT, UPDATE, DELETE 문이 TABLE에 대해 행해질 때 묵시적으로 수행
      - TABLE과는 별도로 DATABASE에 저장
   2. 문법 예시
    ```sql
    CREATE [OR REPLACE] TRIGGER 트리거명
    [시점][이벤트] [OF] ON 테이블명
    [FOR EACH ROW]
    [WHEN]
    DECLARE
    변수 선언 ...
    BEGIN
    ...
    END;
    /
    ```