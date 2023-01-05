## 기본 CRUD 문법
```sql
insert into  table_name(,,,) values(,,,);
update table_name set condition
delete from table_name

#USE MY_EMP;
#set sql_safe_updates=0;
```


1.사원 테이블에서 사원 번호가 7499인 사원의 월급을 5000 으로 변경
```sql
SELECT * FROM MY_EMP;
UPDATE MY_EMP SET SAL = 5000 
WHERE EMPNO =7499;
```
2.부서 번호가 20번인 사원의 월급을 2000으로 변경
```sql
UPDATE MY_EMP SET SAL =2000
WHERE DEPTNO = 20;
SELECT * FROM MY_EMP WHERE DEPTNO=20;
```
3. MY_DEPT 테이블에 데이터를 입력해보자. 번호 50, RESERCH, BOSTON
```sql
SELECT * FROM MY_DEPT;
INSERT INTO MY_DEPT VALUES(50,'RESERCH','BOSTON');
```
4. 방금 입력한 데이터를 삭제해보자
```sql
DELETE FROM MY_DEPT
WHERE DEPTNO = 50;
```
5. FORD의 월급을 4000으로 변경하고 부서번호를 30으로 변경한다.

```sql
SELECT * FROM MY_EMP WHERE ENAME= 'FORD';
UPDATE MY_EMP SET SAL= 4000, DEPTNO= 30
WHERE ENAME = 'FORD';
```
6. 사원 번호가 7698인 사원의 부서번호를 7934 번 사원의 부서번호로 변경한다.
```sql
SELECT * FROM MY_EMP;

SELECT DEPTNO
FROM MY_EMP
WHERE EMPNO=7934;
```
- INNER JOIN을 줘야 함 (MYSQL,마리아 DB에서는 자기 테이블이 열려있을 때 참조(이중참조) 불가능)
-시험 문제용
```sql
UPDATE MY_EMP SET DEPTNO = (SELECT DEPTNO FROM MY_EMP WHERE EMPNO = 7934)  
WHERE EMPNO =7698;

-- You can't specify target table my_emp for update ...
```

```sql
UPDATE MY_EMP SET DEPTNO = (SELECT DEPTNO FROM EMP WHERE EMPNO = 7934)  
WHERE EMPNO =7698; -- 실행 가능
```
7. MY_EMP 테이블에 값을 추가해보자
```sql
DESC MY_EMP;
SELECT * FROM MY_EMP;
INSERT INTO MY_EMP VALUES (0001,'HONGGILDONG','CLERK','7783',NOW(),9000,NULL,10);
INSERT INTO MY_EMP VALUES (0001,'HONGGILDONG','CLERK','7784',NOW(),9000,NULL,10);
INSERT INTO MY_EMP VALUES (0001,'HONGGILDONG','CLERK','7785',NOW(),9000,NULL,10);
DELETE FROM MY_EMP
WHERE EMPNO=1;
```
7. 1)사원의 번호가 1이고 매니저가 7785인 사원을 삭제하자
```sql
DELETE FROM my_emp
WHERE EMPNO=1 AND MGR=7785;
```
7. 2)데이터 다양한 추가.
```sql
SELECT * FROM MY_EMP;
INSERT INTO MY_EMP(EMPNO,ENAME) VALUES (0002,'HONGGILDONG2');
```
7. 3)사번 0002에 DEPTNO 20을 입력해보자
```sql
UPDATE MY_EMP SET DEPTNO = 20 WHERE EMPNO = 2;
```
7. 4)MY_EMP 내용을 삭제하자.(전체 내용 삭제)
```sql
DELETE FROM MY_EMP;
```
8. 서브 쿼리를 이용한 INSERT,UPDATE,DELETE를 해보자 
- 서브 쿼리 결과를 가상의 테이블로 만들어 리턴해야 함
```sql
DROP TABLE MY_EMP;
CREATE TABLE MY_EMP
AS 
SELECT * FROM EMP;
SELECT COUNT(*)FROM MY_EMP;
```
8. 1)WARD와 같은 직업을 가진 사원을 모두 삭제하라
```sql
DELETE FROM my_emp
WHERE JOB = (SELECT M_NEW.JOB FROM 
			(SELECT JOB FROM MY_EMP WHERE ENAME = 'WARD')
            M_NEW);
```
-T ABLE 별칭은 한칸 공백, COLUMN은 AS 사용

8. 2)'WARD'의 월급을 'SMITH'의 월급과 같게 수정하라.
```sql
UPDATE MY_EMP SET SAL =(SELECT M_NEW.SAL FROM (SELECT SAL FROM MY_EMP WHERE ENAME= 'SMITH') M_NEW)
WHERE ENAME = 'WARD';

SELECT * FROM MY_EMP;
```
8. 3)'ALLEN'의 직업을 'WARD'의 직업과 같게 수정하라.
```sql
UPDATE MY_EMP SET JOB =(SELECT M_NEW.JOB FROM (SELECT JOB FROM MY_EMP WHERE ENAME= 'WARD') M_NEW)
WHERE ENAME = 'ALLEN';
```
8. 4)사원번호가 7499번인 사원과 같은 직업을 가진 사원들의 입사일을 오늘 날짜로 변경
```sql
UPDATE MY_EMP SET HIREDATE = NOW()
WHERE JOB = (SELECT M_NEW.JOB FROM (SELECT JOB FROM MY_EMP WHERE EMPNO= '7499') M_NEW);
```
9. 트랜잭션을 연동해보자. 
- ROLLBACK (취소); COMMIT (저장); 
```sql
SET AUTOCOMMIT = FALSE;
START TRANSACTION;

DELETE 
FROM my_emp
WHERE DEPTNO =10 ;
SELECT COUNT(*) FROM MY_EMP;
COMMIT;

DELETE 
FROM my_emp
WHERE DEPTNO =20 ;
SELECT COUNT(*) FROM MY_EMP;
ROLLBACK;
```
### 트랜잭션?(=SAVE POINT) 
- 공유하는 파일에 대하여 동시 작업 중일 때 현재 상태를 저장, 내가 수정한다고 하면 
- 그 수정은 내 상태에만 적용, 공유되는 파일에는 저장 X
- COMMIT 하면 작업을 저장. ROLLBACK은 COMMIT 직후로 돌아감.
- 병렬로 동일한 작업에 접근, COMMIT이 되기 전까진 다른 쪽에서는 변경된 데이터를 확인 불가.

- DDL은 트랙잭션이 적용되지 않는다 (CREATE,ALTER,DROP)
### 영역 크기
- SERVER(클라이언트가 접근 할 수 있는 단위)
- APPLICATION(서버에 접속할 수 있는 프로세스 단위)
- CONTEXT(웹 어플리케이션 자체)
- SESSION(클라이언트가 서버에 접속하게 되면 생성되는 객체,
- 세션의 모든 정보는 서버에 저장되어 기록된다반대로 쿠키는 클라이언트에 저장된다.)
- REQUEST(PAGE)(웹 어플리케이션에 접속할 때 생성되는 객체)
- c:\programfiles\mysql\mysqlserver 8.0\bin\sql.exe 로 서버 실행
- /test/a.html ->was->web으로 접근 -> 주소 = localhost:80/test/a.html( 쟝고의 경우)
- IP -DNS -> 별칭= localhost:3306
- IP:port로 접근 -> 소켓 통신 ->connect.

### if문, 
```sql
SELECT STRCMP('abcd','abd'),STRCMP('a','abcd'),STRCMP('a','a');

SELECT 10>2;
```