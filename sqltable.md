## DB 작성하기

1. CREATE TABLE로 새 테이블 만들기
2. CREATE TABLE에서 기본 키 (PRIMARY KEY) 제약 조건 지정
3. CREATE TABLE에서 고유 키(UNIQUE KEY) 제약 조건 지정
4. CREATE TABLE에서 검사 (CHECK) 제약 조건 지정
5. CREATE TABLE에서 열에 기본값 지정
6. CREATE TABLE에서 외래 키 (FOREIGN KEY) 제약 조건 지정
```sql
CREATE DATABASE  STUDENTS;
USE STUDENTS;
```
1. 학생 정보를 유지하기 위한 students 테이블 생성 

- student_id
  -  레코드 ID(정수 유형) - INT
- student_number
  -  학생 번호(최대 10자리 문자열 유형) -VARCHAR
- first_name
  -  아래 이름(최대 50자리 문자열 유형) -VARCHAR
- last_name
  -  이름(최대 50자리 문자열 유형) -VARCHAR
- middle_name
  -  중간 이름(최대 50자리 문자열 유형) -VARCHAR
- birthday
  -  생일(날짜형) -DATE
- gender
  - 성별(문자열 형식으로 M: 남성, F: 여성) -ENUM
- paid_flag 
  -  수업료를 지불했는지 여부 플래그 (BOOL 형식으로 FALSE (0) : 미결제, TRUE (1) : 지불됨)-BOOL
```sql
CREATE TABLE STUDENTS(
					student_id INT NOT NULL,
                    student_number VARCHAR(10) NOT NULL,
                    first_name	VARCHAR(50) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    middle_name VARCHAR(50) NULL,
                    birthday DATE NOT NULL,
                    gender ENUM ('M','F'),
                    paid_flag BOOL);
DESC STUDENTS;

INSERT INTO  STUDENTS VALUES (1,1,1,1,1,NOW(),'m',true) ;
INSERT INTO  STUDENTS VALUES (1,1,1,1,1,NOW(),'f',0);
SELECT * FROM STUDENTS;
```
2.  CREATE TABLE에서 기본 키 (PRIMARY KEY) 제약 조건 지정
- 식별 키, 테이블당 하나의 칼럼만 지정 가능. null, 중복 비허용
```sql
CREATE TABLE STUDENTS02(
					student_id INT NOT NULL,
                    student_number	 VARCHAR(10) NOT NULL,
                    first_name	  	VARCHAR(50) NOT NULL,
                    last_name		 VARCHAR(50) NOT NULL,
                    middle_name	 VARCHAR(50) NULL,
                    birthday 	DATE NOT NULL,
                    gender		ENUM ('M','F') NOT NULL,
                    paid_flag 	BOOL   NOT NULL,
                    PRIMARY KEY(student_id));
DESC STUDENTS02;

INSERT INTO  STUDENTS02 VALUES (1,1,1,1,1,NOW(),'m',true) ;
INSERT INTO  STUDENTS02 VALUES (2,1,1,1,1,NOW(),'f',0);
INSERT INTO  STUDENTS02 VALUES (null,1,1,1,1,NOW(),'f',0);
SELECT * FROM STUDENTS02;
```
- primary key로 식별, 동일한 값을 넣을 수 없음

3. CREATE TABLE에서 고유 키(UNIQUE KEY) 제약 조건 지정
```sql
DROP TABLE STUDENTS03;
CREATE TABLE STUDENTS03(
					student_id INT,
                    student_number	 VARCHAR(10) ,
                   
                    PRIMARY KEY(student_id)); 
DESC STUDENTS03
```
- PRIMARY KEY를 넣으면 NOT NULL 자동 설정
```sql
DROP TABLE STUDENTS04;
CREATE TABLE STUDENTS04(
					student_id INT	AUTO_INCREMENT, 
    -- COLUMN 뒤에 선언, COLUMN LABEL
                    student_number	 VARCHAR(10) ,
                   
                    PRIMARY KEY(student_id)); 
    -- KEY값은 TABLE LABEL, COLUMN LABEL 둘다 됨
DESC STUDENTS04;
INSERT INTO  STUDENTS04 VALUES (1,1);
INSERT INTO  STUDENTS04 VALUES (2,NULL);
INSERT INTO  STUDENTS04 VALUES (2,NULL); 
-- 중복값은 넣을 수 없다 
INSERT INTO  STUDENTS04 VALUES (NULL,NULL); 
-- AUTO_INCREMENT로 인해 PRIMARY KEY가 자동으로 3으로 지정
INSERT INTO  STUDENTS04(STUDENT_NUMBER) VALUES (NULL); 
-- 반복 시 자동 KEY값 증가

SELECT * FROM STUDENTS04;
```
```sql
DROP TABLE STUDENTS05;
CREATE TABLE STUDENTS05(
					student_id INT	AUTO_INCREMENT, 
    -- 다른 DB에서는 CREATE SEQUENCE
                    student_number	 VARCHAR(10) DEFAULT 'ABC', -- DEFAULT는 해결 불가 
                   
                    PRIMARY KEY(student_id,STUDENT_NUMBER));
DESC STUDENTS05;
 -- 왜 PRIMARY KEY가 2개가 되는가? 
 -- 복합 키 구조로 묶였기 때문에.
INSERT INTO  STUDENTS05 VALUES (1,1);
INSERT INTO  STUDENTS05 VALUES (1,2);
INSERT INTO  STUDENTS05 VALUES (2,1);
INSERT INTO  STUDENTS05 VALUES (2,2);
INSERT INTO  STUDENTS05 VALUES (3,NULL); 
-- AUTO_INCREMENT가 없으므로 X
INSERT INTO  STUDENTS05 VALUES (NULL,3);
 -- AUTO_INCREMENT가 없으므로 X 주면 ok
INSERT INTO  STUDENTS05 VALUES (NULL,NULL);
SELECT * FROM STUDENTS05;
```
3. CREATE TABLE에서 고유 키(UNIQUE KEY) 제약 조건 지정
4. CREATE TABLE에서 검사 (CHECK) 제약 조건 지정

```sql
DROP TABLE STUDENTS06;
CREATE TABLE STUDENTS06(
					student_id INT	,
                    student_number	 VARCHAR(10), 
                    birthday 	DATE,
                    UNIQUE KEY(STUDENT_ID),
                    CHECK( BIRTHDAY >= '2000-01-01')
);
DESC STUDENTS06; 

INSERT INTO  STUDENTS06(STUDENT_ID) VALUES (1); -- 중복데이터 불가
INSERT INTO  STUDENTS06(STUDENT_ID) VALUES (NULL); 
-- NULL값 허용

SELECT * FROM STUDENTS06;
INSERT INTO  STUDENTS06(STUDENT_ID,BIRTHDAY) VALUES (1,NOW()); 
INSERT INTO  STUDENTS06(STUDENT_ID,BIRTHDAY) VALUES (2,NOW()); 
INSERT INTO  STUDENTS06(STUDENT_ID,BIRTHDAY) VALUES (3,'1999-09-09'); 
-- CHECK에 위배, 넣을 수 없음
```
6. CREATE TABLE에서 외래 키 (FOREIGN KEY) 제약 조건 지정
- FOREIGN KEY(자신의 테이블 컬럼명) REFERENCES 다른테이블명(다른테이블의 칼럼명)
```sql
DROP TABLE STUDENTS07;
CREATE TABLE STUDENTS07(
					student_id INT	AUTO_INCREMENT, 
                    student_number	 VARCHAR(10) DEFAULT 'ABC', 
                   
                    PRIMARY KEY(student_id));
DESC STUDENTS07; 
INSERT INTO  STUDENTS07 VALUES (1,1);
INSERT INTO  STUDENTS07 VALUES (2,2); 

SELECT * FROM STUDENTS07;
-- 현재 STUDENTS_MY 테이블의 STUDENT_ID를 STUDENTS07에서 STUDENT_ID로 참조)
CREATE TABLE STUDENT_MY (
	STUDENT_ID INT NOT NULL,
	FOREIGN KEY(STUDENT_ID) REFERENCES STUDENTS07 (STUDENT_ID)
    );
INSERT INTO  STUDENT_MY VALUES (7);
INSERT INTO  STUDENT_MY VALUES (1);
INSERT INTO  STUDENT_MY VALUES (NULL);
SELECT * FROM STUDENT_MY;

-- 제약조건 확인
SELECT *FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS06';
SELECT *FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS07';
SELECT *FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS05';
SELECT *FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENT_MY';
```
7. 제약조건을 삭제해보자
```sql
SELECT * FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS04';

ALTER TABLE STUDENTS03 DROP PRIMARY KEY;
SELECT * FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS03';
```
8. 제약조건을 추가해보자
```sql
SELECT * FROM INFORMATION_sCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME= 'STUDENTS03';
ALTER TABLE STUDENTS03 ADD CONSTRAINT PRIMARY KEY(STUDENT_ID);
DESC STUDENTS03;
```
9.예시 실행
```sql
CREATE TABLE t1 (a INTEGER, b CHAR(10));
DESC T1;
ALTER TABLE t1 RENAME t2;
DESC T2;
ALTER TABLE t2 MODIFY a TINYINT NOT NULL, CHANGE b c CHAR(20);
DESC T2;
ALTER TABLE t2 ADD d TIMESTAMP;
DESC T2;
ALTER TABLE t2 ADD INDEX (d), ADD UNIQUE (a);
DESC T2;
ALTER TABLE t2 DROP COLUMN c;
DESC T2;
ALTER TABLE t2 ADD c INT UNSIGNED NOT NULL AUTO_INCREMENT,
  ADD PRIMARY KEY (c);
  DESC T2;
```