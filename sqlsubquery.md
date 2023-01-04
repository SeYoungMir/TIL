### 복습
```sql
--use my_emp;
-- 데이터 사용
```
1. 각 직위별로 총 월급을 출력하되 월급이 낮은 순으로 출력하라.
```sql
SELECT JOB, SUM(SAL)
FROM EMP
GROUP BY JOB
ORDER BY SUM(SAL) ;
```
2. 직위별 월급을 출력하되, 직위가 MANAGER인 사원들은 제외한다. 그리고 그 총 월급이 5000보다 큰 직위와 총 월급만 출력하라
```sql
SELECT JOB,SUM(SAL)
FROM EMP
WHERE JOB !='MANAGER'
GROUP BY JOB
HAVING SUM(SAL) > 5000;
```
3. 직위별 최대월급을 출력하되, 직위가 CLEARK인 사원들은 제외하라. 그리고 그 최대월급이 2000이상인 직위와 최대직급을 최대 월급이 높은 순으로 정렬하여 출력하라.
```sql
SELECT JOB,MAX(SAL)
FROM EMP
WHERE JOB != 'CLEARK'
group by JOB
HAVING MAX(SAL) >= 2000
ORDER BY MAX(SAL) DESC ;
```
4. 부서별 총 월급을 구하되 30번 부서를 제외하고 그 총월급이 8000 이상인 부서만 나오게 하고 총월급이 높은 순으로 출력하라.
```sql
SELECT DEPTNO,SUM(SAL)
FROM EMP
WHERE DEPTNO != 30
GROUP BY DEPTNO
HAVING SUM(SAL) >= 8000
ORDER BY SUM(SAL) DESC;
```
5. 부서별 평균월급을 구하되 커미션이 책정된 사원만 가져오고,  그 평균월급이 1000달러 이상인 부서만 나오게 하고 , 평균월급이 높은 순으로 출력하라.
```sql
SELECT DEPTNO,AVG(SAL)
FROM EMP
WHERE COMM IS NOT NULL
GROUP BY DEPTNO
HAVING AVG(SAL) >= 1000
ORDER BY AVG(SAL) DESC;
```

## 서브 쿼리
1. 'JONES'의 월급보다 많은 월급을 받는 사원의 이름과 월급을 출력
- STEP 1. 'JONES'의 월급
```sql
SELECT ENAME,SAL
FROM EMP
WHERE ENAME = 'JONES'; -- 2975
```
- STEP 2. 많은 월급을 받는 사원의 이름과 월급을 출력.
```sql
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 2975;
```
- 서브 쿼리
  - SINGLE ROW SUBQUERY 서브 쿼리의 결과가 1개의 ROW인경우
    - '>, <, =, >=, <=' 등의 단일값 비교연산자
  -  참조형 데이터의 경우 

```sql SELECT ENAME,SAL
FROM EMP
WHERE SAL> (SELECT SAL
		FROM EMP
		WHERE ENAME = 'JONES');
```

 - MULTI ROW SUBQUERY 서브 쿼리의 결과가 여러 개의 ROW인경우
1. 직업이 'SALESMAN' 인 사원들과 같은 월급을 받는 사원의 이름과 월급을 출력
     -  `IN, NOT IN, >ANY, <ANY, >ALL, <ALL` 등의 연산자 사용
```sql
SELECT ENAME, SAL   
FROM EMP
WHERE SAL = (SELECT ,SAL
			FROM EMP
			WHERE JOB = 'SALESMAN'); -- ERROR

SELECT ENAME, SAL -- > 메인 쿼리 (2번으로 실행)
FROM EMP
WHERE SAL IN (SELECT SAL  -- > 서브 쿼리, 부 쿼리 (1번으로 실행)
			FROM EMP
			WHERE JOB = 'SALESMAN'); 
```
2. 부서번호가 10번인 사원들과 같은 월급을 받는 사원의 이름과 월급을 출력하라.
```sql
SELECT ENAME, SAL
FROM EMP 
WHERE SAL IN (SELECT SAL
			  FROM EMP
              WHERE DEPTNO = 10);
```              
3. 직업이 CLERK인 사원과 같은 부서에서 근무하는 사원의 이름과 월급과 부서 출력하라.
```sql
SELECT ENAME, SAL,DEPTNO
FROM EMP 
WHERE DEPTNO IN (SELECT DEPTNO
			  FROM EMP
              WHERE JOB = 'CLERK');
```
4. 'CHICAGO' 에서 근무하는 사원들과 같은 부서에서 근무하는 사원의 이름과 월급을 출력하라.
```sql
SELECT ENAME, SAL
FROM EMP
WHERE DEPTNO IN (SELECT DEPTNO
				FROM DEPT
				WHERE LOC ='CHICAGO');
```
5. 부하직원이 있는 사원의 사원번호와 이름을 출력하라.
- 자기 자신이 관리자 
```sql
SELECT EMPNO, ENAME
FROM EMP
WHERE EMPNO IN (SELECT MGR
				FROM EMP);   
    -- (DATA OR DATA OR ...NULL) = ANY
```
6. 부하직원이 없는 사원의 사원번호와 이름을 출력하라. 
   - 자기 자신이 말단
```sql
SELECT EMPNO, ENAME
FROM EMP
WHERE EMPNO NOT IN (SELECT IFNULL(MGR,0)
				FROM EMP);    
 -- 왜 없는가? NOT IN 구문에 NULL값 (KING이 NULL값)
								
 -- (DATA AND DATA AND ...NULL) != ALL
```

### ANY (DATA OR DATA OR ...NULL)

 - `= ANY `	 
   - 하나라도 만족하는 값이 있으면 결과를 리턴하며 IN과 동일함
 - `> ANY` 	 
   - 값들 중 최소값 보다 크면 결과를 리턴
 - `>= ANY` 	 
   - 값들 중 최소값 보다 크거나 같으면 결과를 리턴
 - `< ANY `	 
   - 값들 중 최대값 보다 작으면 결과를 리턴
 - `<= ANY` 	
   -  값들 중 최대값 보다 작거나 같으면 결과를 리턴
 - `<> ANY` 	 
   - 모든 값들 중 다른 값만 리턴 ,값이 하나일 때만 가능함

### ALL (DATA AND DATA AND ...NULL)

 - `> ALL` 	 
   - 값들 중 최대값 보다 크면 결과를 리턴
 - `>= ALL` 	
   -  값들 중 최대값 보다 크거나 같으면 결과를 리턴
 - `< ALL` 	
   -  값들 중 최소값 보다 작으면 결과를 리턴
 - `<= ALL` 
   - 값들 중 최소값 보다 작거나 같으면 결과를 리턴
 - `= ALL` 	 
   - 모든 값들과 같아야 결과를 리턴, 값이 하나일 때만 가능함
 - `<> ALL `	
 -  모든 값들과 다르면 결과를 리턴

7. 'KING'에게 보고하는 즉, 직속상관(MGR)이 'KING'인 사원의 이름과 월급을 출력하라
```sql
SELECT ENAME,SAL
FROM EMP
WHERE MGR = (SELECT EMPNO
				FROM EMP
				WHERE ENAME= 'KING');
```               
8. 20번 부서의 사원 중 가장 많은 월급을 받는 사원들보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하라.
```sql
SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT MAX(SAL)
			FROM EMP
			WHERE DEPTNO =20);
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ALL(SELECT SAL
			FROM EMP
			WHERE DEPTNO =20);
```            
9. 20번 부서의 사원 중 가장 적은 월급을 받는 사원들보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하라.
```sql
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ANY(SELECT SAL
			FROM EMP
			WHERE DEPTNO =20);
            SELECT ENAME, SAL
FROM EMP
WHERE SAL > (SELECT MIN(SAL)
			FROM EMP
			WHERE DEPTNO =20);
```
10. 직업이 'SALESMAN인 사원 중 가장 큰 월급을 받는 사원보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력하라.
- 단, MIN(),MAX()등 함수를 사용하지 않고, 연산자를 이용할 것.
```sql
SELECT ENAME,SAL
FROM EMP
WHERE SAL > ALL(SELECT SAL
				FROM EMP
				WHERE JOB = 'SALESMAN');
```
11. 직업이 'SALESMAN인 사원 중 가장 적은 월급을 받는 사원보다 더 적은 월급을 받는 사원들의 이름과 월급을 출력하라.
- 단, MIN(),MAX()등 함수를 사용하지 않고, 연산자를 이용할 것.
```sql
SELECT ENAME,SAL
FROM EMP
WHERE SAL < ALL(SELECT SAL
				FROM EMP
				WHERE JOB = 'SALESMAN');
```                
##  MULTI COLUMN SUBQUERY
1. 직업이 'SALESMAN'인 사원과 같은 부서에서 근무하고
- AND 사용
-   같은 월급을 받는 사원들의 이름, 월급, 부서번호를 출력하라

```sql
SELECT ENAME, SAL,DEPTNO
FROM EMP
WHERE DEPTNO IN (SELECT DEPTNO
				FROM EMP
				WHERE JOB = 'SALESMAN') 
AND SAL IN (select SAL
			FROM EMP
			WHERE JOB = 'SALESMAN');
```                    
2. 30번 부서 사원들과 같은 월급 같은 커미션을 받는 사원들의 이름, 월급, 커미션를 출력하라
```sql
SELECT ENAME,SAL,COMM
FROM EMP
WHERE SAL IN(SELECT SAL
			FROM EMP
			WHERE DEPTNO = 30)
AND IFNULL(COMM,0) IN (SELECT IFNULL(COMM,0)
			FROM EMP
			WHERE DEPTNO  = 30);
```            
1. TEST 라는 테이블을 EMP 테이블로 만들어보자 
- 테이블 제약 규칙은 오지 않는다.
```sql
CREATE TABLE TEST
AS
SELECT * FROM EMP;

DESC TEST;

SELECT * FROM TEST ;
```

2. TEST02 라는 테이블을 EMP 테이블로 원하는 칼럼만 추려서만들어보자
```sql
CREATE TABLE TEST02 
AS
SELECT ENAME,EMPNO, SAL
FROM EMP;
DESC TEST02;
SELECT * FROM TEST02;
```
3. TEST03 라는 테이블을 EMP 테이블로 원하는 칼럼과 원하는 칼럼명으로 만들어보자 
- 테이블 제약 규칙은 오지 않는다.
```sql
CREATE TABLE TEST03 
AS
SELECT ENAME AS '사원명' ,EMPNO AS '사원번호', SAL AS '사원봉급'
FROM EMP;
DESC TEST03;
SELECT * FROM TEST03;

CREATE TABLE TEST03 ('A','B','C'_) 
-- 안됨, 이걸 해결하는 방법. 
AS
SELECT ENAME ,EMPNO , SAL 
FROM EMP;

DROP TABLE TEST03;
CREATE TABLE TEST03 (NAME VARCHAR(50))  
AS
SELECT ENAME ,EMPNO , SAL 
FROM EMP;
DESC TEST03;
SELECT * FROM TEST03;
```
1. TEST04 라는 테이블을 EMP 테이블로 만들어보자 
   - 테이블 제약 규칙은 오지 않는다.
- CHICAHO에서 근무하는 사원들과 같은 부서에서 근무하는 사원의 이름과 월급으로 TEST 04를 만들어보자
```sql
CREATE TABLE TEST04 
AS 
SELECT ENAME,SAL
FROM EMP
WHERE DEPTNO = (SELECT DEPTNO
				FROM DEPT
                WHERE LOC='CHICAGO');
DESC TEST04;
SELECT *FROM TEST04;

DROP TABLE TEST,TEST02,TEST03,TEST04;
``` 