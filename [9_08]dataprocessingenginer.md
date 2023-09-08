## 5. DCL - 이어서
2. 데이터베이스 제어어(DCL)
    <table>
        <tr>
            <th>명령어</th>
            <th>동작</th>
            <th>기능</th>
        </tr>
        <tr>
            <td>COMMIT</td>
            <td>정상 완료</td>
            <td>작업이 정상적으로 완료되었음을 관리자에게 알려줌</td>
        </tr>
        <tr>
            <td>ROLLBACK</td>
            <td>비정상 종료</td>
            <td>작업이 비정상적으로 종료되었을 때 원래의 상태로 복구</td>
        </tr>
        <tr>
            <td>GRANT</td>
            <td>사용권한 부여</td>
            <td>데이터베이스 사용자에게 사용 권한을 부여</td>
        </tr>
        <tr>
            <td>REVOKE</td>
            <td>사용권한 취소</td>
            <td>데이터베이스 사용자의 사용 권한을 취소</td>
        </tr>
    </table>
3. COMMIT 과 ROLLBACK
   1. COMMIT : 결과가 정상 완료 되어 물리적 디스크로 저장됨
   2. ROLLBACK : 결과에 문제가 발생하여 데이터가 원래 상태로 복구됨
4. GRANT(권한 부여) 기본 문법
   ```SQL
   1 GRANT 권한 ON 테이블명 TO 사용자명
   2 [WITH GRANT OPTION]
   ```
   1. 테이블에 사용자 권한 부여
   2. 권한 옵션
      1. 권한으로는 ALL, INSERT, DELETE, UPDATE,SELECT를 옵션으로 사용 가능

5. GRANT 예제
   1. 사용자 KIM 에게 수강 테이블의 검색 권한을 부여하시오
      GRANT SELECT ON 수강 TO KIM
      KIM 사용자는 검색 권한을 부여받았지만 다른 사람에게 권한을 부여할 수는 없음
6. REVOKE(권한 해제) 기본 문법
   ```SQL
   1 REVOKE 권한 ON 테이블명 FROM 사용자명
   2 [CASCADE]
   ```
   1. 테이블에 사용자 권한 해제
   2. 연쇄 권한 해제 여부(WITH GRANT OPTION) 옵션으로 부여된 사용자들의 권한까지 연쇄 해제 할 수 있음.
7. REVOKE 예제
   1. KIM에게 부여된 수강 테이블의 읽기(SELECT)권한과 다른 사용자에게 부여한 권한도 연쇄 해제함
   REVOKE SELECT ON 수강 FROM KIM [CASCADE]
   CASCADE는 권한을 부여받은 사용자가 다른 사용자에게 부여한 권한도 취소하는 옵션임
   2. 사용자 BBB에게 부여된 수강 테이블에서의 갱신(UPDATE) 권한을 해제함
   REVOKE UPDATE ON 수강 FROM KIM