### if문, 
```sql
SELECT STRCMP('abcd','abd'),STRCMP('a','abcd'),STRCMP('a','a');

SELECT 10>2;
```
```sql
USE MY_EMP;
CALL COMPARE(1,1, @RESULT); -- 유저 커스텀 함수
SELECT @RESULT; -- 호출 

CALL COMPARE(3,1, @RESULT); 
SELECT @RESULT;
CALL COMPARE(1,4, @RESULT); 
SELECT @RESULT;

CALL MY_HAP(10,20,@HAP);
SELECT @HAP;

CALL TEST(1,10 );
CALL TEST(100,200);
-- STORED PROCEDURES -> NEW
-- PROCEDURE는 RETURN이 없음  OUT으로 RETURN 대체

call doiterate(1);
SELECT @X;

```


- 사번을 입력받아 MY_EMP를 삭제하는 쿼리 MY_DELETE로 저장
-  자주쓰는 기능을 간단히 하기 위해

```sql
CALL MY_DELETE(7902);
SELECT *FROM MY_EMP;
```
- CURSOR RETURN이  한개 이상일때, 여러개를 한번에 리턴 
- 
```sql
CALL MY_SELECT();
```