### 2. 프로시저 작성
1. 프로시저의 개념
   1. 프로시저는 절차형 SQL을 활용하여 특정 기능을 수행할 수 있는 트랜잭션 언어임
   2. 프로시저 호출을 통해 실행되며, 이를 통해 일련의 SQL 작업을 포함하는 데이터 조작어(DML : Data Manipulate Language)를 수행하는 것이 일반적임
   3. 시스템에서의 일일 마감 작업, 또는 일련의 배치 작업 등을 프로시저를 활용하여 관리하고 주기적으로 수행하기도 함
2. 프로시저 구성
   1. DECLARE : 프로시저의 명칭, 변수와 인수와 데이터 타입을 정의하는 선언부임
   2. BEGIN/END : 프로시저의 시작과 종료를 나타내며, BEGIN/ END를 쌍을 이루어 추가함
   3. CONTROL : 조건에 따라 문장을 실행하거나 다른 조건일 경우 조건에 맞는 문장을 실행함. 또는 조건에 따라 반복 수행할 수도 있음.
   4. SQL : DML문을 (SELECT,INSERT,UPDATE,DELETE)사용함
   5. EXCEPTION : 문장을 실행할 때 예외 발생 시 예외 처리를 함
   6. TRANSACTION : DCL을 수행하는 부로 DBMS의 적용 또는 실행시 COMMIT(승인) / ROLLBACK(취소)를 실행함
3. 프로시저의 문법
   1. CREATE 명령어로 프로시저를 생성함
   2. [OR REPLACE]명령은 새로 컴파일 하여 기존내용으로 덮어쓴다는(Overwrite)것임.
   3. PARAMETER는 외부에서 프로시저 호출 시 변수를 입력 또는 출력하는 것임
   4. IN : 운영 체제에서 프로시저로 전달함
   5. OUT : 프로시저의 결과가 운영체제로 전달됨
   6. INOUT : IN과 OUT 기능이 동시에 수행
4. 프로시저 기본 구조
   - ```SQL > EXECUTE [PROCEDURE_NAME](PARAMETER1,PARAMETER2,...)```;
5. 프로시저 예제
   - ```SQL > EXECUTE SALES_CLOSING('123456');```