## Join
- 테이블 칼럼 간 공통 값(VALUE)추출하는 것.
-  JOIN/ ANSI JOIN이 있고 ANSI JOIN은 공통 
-  USING(공통 칼럼) ON (칼럼 명 다를때)

-  INNER JOIN = JOIN 
   -  같은 값만 추출/FALSE, NULL은 출력 x
-  OUTER JOIN
   -  주종 관계 (주 테이블은 전체 출력, 종 테이블은 INNER JOIN(같은 값 추출))
	- LEFT OUTER JOIN /RIGHT OUTER JOIN
- CROSS JOIN
  - 비교 칼럼이 속한 모든 테이블 출력 

1. INNER JOIN을 이용해서 사원의 이름과 사원이 속해있는 부서를 출력하자
```sql
USE MY_EMP;

CREATE TABLE MY_EMP
AS 
SELECT * FROM EMP;
CREATE TABLE MY_DEPT
AS
SELECT * FROM DEPT;
```

```sql
 -- ANSI
SELECT ENAME, DNAME
FROM MY_EMP JOIN MY_DEPT USING(DEPTNO);

-- MYSQL
SELECT ENAME, DNAME
FROM MY_EMP , MY_DEPT
WHERE MY_EMP.DEPTNO = MY_DEPT.DEPTNO;
```
2. 전체 칼럼을 리턴해서 출력해보자 (Q1을 이용)
```sql
SELECT *
FROM MY_EMP JOIN MY_DEPT USING(DEPTNO);
```
3. 간단한 테이블을 생성, INNER JOIN 확인
```sql
CREATE TABLE X(
X1 VARCHAR(5),
X2 VARCHAR(5));
CREATE TABLE Y(
Y1 VARCHAR(5),
Y2 VARCHAR(5));

INSERT INTO X VALUES('A','D');
INSERT INTO Y VALUES('A','1');
INSERT INTO Y VALUES('B','2');
INSERT INTO Y VALUES('C','3');
INSERT INTO Y VALUES(NULL,'1');

SELECT * FROM X;
SELECT * FROM Y;
```
- 연습 데이터
```sql
X1 X2   Y1  Y2
A  D    A   1
		B   2
        C   3
        NULL 1
```

```sql
SELECT *
FROM X,Y 
WHERE X1 = Y1; 

SELECT *
FROM X JOIN Y ON (X1 =Y1);
```
5. 주종관계를 이용한 조인을 출력해보자
```sql
SELECT *
FROM X RIGHT OUTER JOIN Y
	ON X1 = Y1; -- Y가 주테이블, X가 종 테이블

SELECT *
FROM X LEFT OUTER JOIN Y
	ON X1 = Y1;  -- X가 주 테이블, Y가 종테이블
```
- ANSI에서 쓰는 JOIN, LEFT+RIGHT OUTER JOIN
```sql
SELECT *
FROM X FULL OUTER JOIN Y
ON X1 = Y1;
```

6. 급여 등급 테이블을 작성해보자
```sql
CREATE TABLE SALGRADE(
	GRADE INT,
    LOSAL INT,
    HISAL INT);
insert into salgrade values (1, 700, 1200);
insert into salgrade values (2, 1201, 1400);
insert into salgrade values (3, 1401, 2000);
insert into salgrade values (4, 2001, 3000);
insert into salgrade values (5, 3001, 9999);

SELECT * FROM SALGRADE;
SELECT * FROM MY_EMP;
```
7. NONEQI JOIN
```sql
각 사원의 이름과 월급 그리고 그 사원의 급여 등급을 출력해보자
SELECT ENAME, SAL, GRADE
FROM MY_EMP JOIN SALGRADE ON ( SAL BETWEEN LOSAL AND HISAL);
```
8. 각 사원의 이름과 월급, 급여등급, 부서이름을 출력해보자
- 테이블 제약사항이 있는 것을 선 조인, 나머지를 후 조인
```sql
SELECT ENAME, SAL, GRADE, DNAME
FROM  MY_EMP JOIN MY_DEPT USING (DEPTNO) 
    -- 처음 병합
	JOIN SALGRADE ON (SAL BETWEEN LOSAL AND HISAL); 
    -- 두번째 병합
```
8. SELF JOIN : 테이블 하나에 같은 값을 가진 칼럼을 조인하는 것
- 사원의 이름, 사원의 번호, 관리자의 번호와 이름을 출력해보자
- 사원의 MGR과 관리자의 EMPNO 같은 값을 조인한다.
- 테이블의 별칭 지정 후 조인
```sql
SELECT 사원.ENAME AS 사원이름, 사원.EMPNO AS 사원번호, 관리자.ENAME AS 관리자이름, 관리자.EMPNO AS 관리자번호
FROM MY_EMP AS 사원 LEFT OUTER JOIN MY_EMP AS 관리자 ON 사원.MGR =관리자.EMPNO;
-- 이 경우 사원은 주, 관리자는 종으로 넣어야함 (KING이 NULL값이므로)
```