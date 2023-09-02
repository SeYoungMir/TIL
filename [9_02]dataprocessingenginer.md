## 3.트리거
1. 트리거의 개념
   1. 데이터베이스의 이벤트 프로그래밍으로 일정 조건이 충족될 경우 이벤트(데이터 삽입, 수정, 삭제 등)가 발생하는 것임
   2. 특정 테이블에 삽입, 수정, 삭제 등의 데이터 변경 이벤트가 발생하면 DBMS애서 자동적으로 실행되도록 구현된 SQL 프로그램 명령임
   3. 사용자가 직접 호출하는 것이 아니라, 데이터베이스에서 자동적으로 호출되어 실행되는 것을 말함
   4. 데이터 무결성 유지와 로그 메시지 출력 등의 처리 등에 사용됨
2. 트리거의 목적
   1. 데이터를 변경해야 할 시점에서 시작 설정하여 이벤트에 의해 자동적으로 수행함
   2. 이벤트와 관련된 데이터 삽입, 추가, 삭제 작업을 자동적으로 실행시키는데 활용됨
   3. 데이터 무결성 유지 및 로그 메시지 출력 등의 별도 처리를 위해 사용함
3. 트리거 정의 함수 기본 문법
   ```SQL
   1. CREATE [OR REPLACE] TRIGGER 트리거명
   2. [BEFORE | AFTER] ON
   3. [FOR EACH ROW]
      [WHEN (condition)]
      DECLARE(변수선언)
      BEGIN
   4.      {SQL 명령 작성}
           {EXCEPTION}
      END;
    ```
      1. 트리거 선언
      2. BEFORE : INSERT, UPDATE ,DELETE 문이 실행되기 전에 트리거 실행명령
      3. AFTER : INSERT, UPDATE ,DELETE 문이 실행 후 트리거가 실행됨
      4. FOR EACH ROW : 행 트리거 옵션
      5. 필요한 SQL 명령어 작성
4. 트리거 명령어
   1. CREATE TRIGGER : 트리거 선언
   2. BEFORE : 트리거 명령 실행 전
   3. DECLARE : 트리거 명칭
   4. BEGIN ~ END : 트리거 시작 시 실행 될 명령의 (시작 ~ 종료)
   5. CONTROL : 순차적인 명령어 처리 및 조건에 따른 LOOP
   6. SQL : 일반적으로 DML 수행(INSERT, DELETE, UPDATE, SELECT)
   7. EXCEPTION : 예외 발생 정의
   8. TRANSACTION : DML 명령의 수행 및 취소 여부 결정
5. 트리거 예제 
   ```SQL
   1. CREATE TRIGGER T_SUBJECT
   2. BEFORE INSERT ON SUBJECT
      BEGIN
   3.  IF(MAT < 60 ) THEN
   4.     RAISE_APPLICATION_ERROR
   5.     (-12345, '과락입니다');
       ENDIF;
    END;
    ```
      1. T_SUBJECT(과목) 트리거 명 선언
      2. 삽입(INSERT) 명령어 실행 전
      3. 수학 점수가 60점 미만일 경우
      4. 에러가 발생
      5. 12345번 에러 발생하며 '과락입니다'표시
6. 트리거 작성 시 주의 사항
   1. 데이터 제어어(DCL, Data Control Language) 는 사용해서는 안됨
   2. COMMIT 이나 ROLLBACK를 사용하면 컴파일 에러가 발생함
   3. 트리거에서 발생하는 모든 후속 절차에도 동일하게 적용됨
   4. 트리거 실행 시 타 프로시저를 호출할 수도 있지만, 이 때 호출된 문장에 DCL 문이 포함되어 있다면 에러가 발생