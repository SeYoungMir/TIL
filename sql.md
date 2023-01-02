## My SQL

cmd 
mysql -h localhost -u user -p
current_date

select '1234'

select 100,100,100:
select 100+100:
select 100-100,100+100,10*2,10/5, 10%2:

select 90.2:
select 'a',"abc",'''abc''':
select 'a'+100: >warning
select 100+'a': >warning

source 파일 경로

select 100;
select 100+200;
- Q1)오늘의 날짜를 출력해보자
SELECT NOW();

#USE MY_EMP

- Q2) SELECT 컬럼리스트 ,,, * FROM 테이블 명; 
- 사원 테이블에 있는 전체 내용을 확인해보자

SELECT *
FROM EMP;

- Q3)부서 테이블에 있는 전체 내용을 확인해보자.
SELECT *
FROM DEPT;

- Q4)my_emp의 내용중에 전체 테이블 목록을 확인 해 보자
show tables;

- Q5) 사원 테이블의 스키마 구조를 확인해보자. 필드면, 데이터타입, null값 유무, key값, 초기값, 기타
desc emp;

- Q6) 사원테이블에서 사원의 이름, 사원의 번호, 매니저, 봉급을 출력해보자
select Ename, empno, mgr, sal
from emp;

- Q7) 부서테이블에서 부서번호, 부서명 출력해보자
select deptno, dname
from dept;

- Q8) 두개의 테이블의 모든 내용을 출력해보자.
select *
from emp,dept;

- Q9) 별칭 : 컬럼의 별칭, 테이블 별칭 / 컬럼 as 별칭, 테이블 as 별칭
- 사원 테이블에서 사원의 이름 ,사원의 번호로 두개의 컬럼을 출력해보자 
select ename '사원의 이름', empno '사원의 번호'
from emp
- Q10) 별칭 : 컬럼의 별칭, 테이블 별칭 / 컬럼 as 별칭, 테이블 as 별칭
- 사원 테이블에서 사원의 이름 ,사원의 번호로 두개의 컬럼을 출력해보자 
select ename as '사원의 이름', empno as '사원의 번호'
from emp
- Q11) 별칭 : 컬럼의 별칭, 테이블 별칭 / 컬럼 as 별칭, 테이블 as 별칭
- 사원 테이블에서 사원이름 ,사원번호로 두개의 컬럼을 출력해보자 
select ename as 사원이름, empno as 사원번호
from emp;

- Q12) 별칭 : 컬럼의 별칭, 테이블 별칭 / 컬럼 as 별칭, 테이블 as 별칭
- 사원 테이블에서 사원의 이름 ,사원의 번호로 두개의 컬럼을 출력해보자 
select ename 사원이름, empno 사원번호
from emp;

- Q13) 테이블의 별칭을 주자 사원의 이름, 부서번호, 부서명을 출력해보자
SELECT ENAME,DEPT.DEPTNO,DNAME
FROM EMP, DEPT;

- Q14) 테이블의 별칭을 주자 사원의 이름, 부서번호, 부서명을 출력해보자
SELECT ENAME,D.DEPTNO,DNAME
FROM EMP, DEPT D;

- Q15) 테이블의 별칭을 주자 사원의 이름, 부서번호, 부서명을 출력해보자
SELECT ENAME,부서.DEPTNO,DNAME
FROM EMP, DEPT AS 부서;

- Q16) 테이블의 별칭을 주자 사원의 이름, 부서번호, 부서명을 출력해보자
SELECT ENAME,DEPT.DEPTNO,DNAME
FROM EMP, DEPT as 부 서;

- 함수
  - SELECT~ FROM
  - WHERE 
    - 조건문, 숫자 비교, 문자 비교, 대소문자 비교, NULL, 날짜값 비교
-   HAVING 
    -   GROUP BY의 비교연산
- GROUP BY 
  -  집계연산 -> SUM, AVG, VAR, MEAN, MAX,MIN/ 함수
 - ORDER BY 
   - 정렬, 서브쿼리
*/