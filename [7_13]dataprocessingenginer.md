### 2. 데이터 조작 프로시저 테스트
#### 1. SQL*Plus 활용
1. SQL과 SQL*Plus 차이점
<table>
    <tr>
        <th>SQL</th>
        <th>SQL*Plus</th>
    </tr>
    <tr>
        <td>데이터베이스와 통신</td>
        <td>SQL 명령어를 서버에 전송하는 Tool</td>
    </tr>
    <tr>
        <td>ANSI 표준</td>
        <td>Oracle 사 제공</td>
    </tr>
    <tr>
        <td>Data와 Table에 대한 정의 가능</td>
        <td>Data에 대한 정의 불가</td>
    </tr>
    <tr>
        <td>SQL Buffer 사용</td>
        <td>SQL Buffer 사용하지 않음</td>
    </tr>
    <tr>
        <td>다중 행 입력 가능</td>
        <td>다중 행 입력 불가</td>
    </tr>
    <tr>
        <td>키워드 축약 불가</td>
        <td>키워드 축약 가능</td>
    </tr>
</table>

2. SQL*Plus 명령어 유형

<table>
    <tr>
        <th>구분</th>
        <th>유형</th>
    </tr>
    <tr>
        <td>파일 명령어</td>
        <td>SAVE, GET, SPOOL 등</td>
    </tr>
    <tr>
        <td>편집 명령어</td>
        <td>A, C, L, I ,DEL, n(숫자) 등 </td>
    </tr>
     <tr>
        <td>실행 명령어</td>
        <td>START, @ , RUN , / 등</td>
    </tr>
     <tr>
        <td>환경 명령어</td>
        <td>SET HEAD[LINE/PAGE/PAUSE] ON[OFF] 등</td>
    </tr>
</table>

1. SQL*Plus 명령어 유형 별 내용
   1. 파일 명령어
    <table>
         <tr>
            <th>명령어</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>EDIT {파일명}</td>
            <td>버퍼의 내용을 편집기로 불러옴</td>
        </tr>
         <tr>
            <td>SAVE {파일명}</td>
            <td>버퍼의 내용을 파일에 저장</td>
        </tr>
         <tr>
            <td>START {파일명}(=@)</td>
            <td>저장된 SQL script를 실행</td>
        </tr>
         <tr>
            <td>GET {파일명}</td>
            <td>파일의 내용을 버퍼로 읽어옴</td>
        </tr>
         <tr>
            <td>SPOOL {파일명}</td>
            <td>조회결과를 파일로 저장</td>
        </tr>
         <tr>
            <td>SPOOL OFF</td>
            <td>저장된 파일 확인</td>
        </tr>
         <tr>
            <td>HOST (=!와 동일한 효과)</td>
            <td>운영체제(shell)로 빠져 나감</td>
        </tr>
         <tr>
            <td>EXIT</td>
            <td>운영체제(OS) prompt로 빠져 나감</td>
        </tr>
         <tr>
            <td>CONNECT {uid/pwd}</td>
            <td>다른 사용자로 접속할 때 사용</td>
        </tr>
         <tr>
            <td>COL col FOR "999,999"[A15]</td>
            <td>Col 내용을 일정 Format으로 변경</td>
        </tr>
    </table>

   2. 편집 명령어

    <table>
         <tr>
            <th>명령어</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>A{문자스트링}</td>
            <td>현재 버퍼의 끝에 새로운 문자 스트링 추가</td>
        </tr>
         <tr>
            <td>C</td>
            <td>현재 행의 무자열을 치환</td>
        </tr>
         <tr>
            <td>L</td>
            <td>버퍼의 전체 리스트 출력</td>
        </tr>
         <tr>
            <td>I</td>
            <td>버퍼에 새로운 행 추가</td>
        </tr>
         <tr>
            <td>DEL n</td>
            <td>현재 행 삭제</td>
        </tr> 
        <tr>
            <td>N(숫자)</td>
            <td>현재 행 출력</td>
        </tr>
         <tr>
            <td>CLEAR BUFFER</td>
            <td>버퍼의 전체 내용 삭제</td>
        </tr>
    </table>

   3. 실행 명령어
    <table>
         <tr>
            <th>명령어</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>START {파일명}</td>
            <td>SQL script를 실행할 때</td>
        </tr>
         <tr>
            <td>@ {파일명}</td>
            <td>SQL script를 실행할 때</td>
        </tr>
         <tr>
            <td>RUN {파일명}</td>
            <td>버퍼의 내용을 실행할 때</td>
        </tr>
         <tr>
            <td>/</td>
            <td>버퍼의 내용을 실행할 때</td>
        </tr>
    </table>

   4. 환경 명령어
  <table>
         <tr>
            <th>명령어</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>SET ECHO {off/on}</td>
            <td>SQL script 실행 시 명령어의 출력 여부</td>
        </tr>
        <tr>
            <td>FEED[BACK] {6/n/off/on}</td>
            <td>조회결과 메시지 출력 여부</td>
        </tr>
        <tr>
            <td>HEAD[ING] {on/off}</td>
            <td>칼럼의 Head 출력 여부</td>
        </tr>
        <tr>
            <td>LINE[SIZE] {80/n}</td>
            <td>출력될 한 라인의 길이</td>
        </tr>
        <tr>
            <td>PAGE{SIZE} {24/n}</td>
            <td>출력 Page 당 라인 수</td>
        </tr>
        <tr>
            <td>PAU[SE] {off/on}</td>
            <td>화면 이동제어(한 Page씩 보고 싶을때)</td>
        </tr>
        <tr>
            <td>SQLPREFIX {#/c}</td>
            <td>SQL 명령어 사이에 SQL*Plus 명령어 사용할 때</td>
        </tr>
        <tr>
            <td>NULL</td>
            <td>NULL값을 대체할 text 정보를 설정할 때</td>
        </tr>
        <tr>
            <td>SERVEROUTPUT {on/off}</td>
            <td>PL/SQL 처리 결과를 화면에 출력할 때</td>
        </tr>
        <tr>
            <td>SPACE {1/n}</td>
            <td>출력된 칼럼 간의 여유공간을 설정할 때</td>
        </tr>
        <tr>
            <td>UNDERLINE {기호/on/off}</td>
            <td>칼럼의 heading 밑에 사용될 Underline 설정</td>
        </tr>
        <tr>
            <td>WRAP {on/off}</td>
            <td>칼럼들의 지정된 Linesize를 초과할 때 출력 여부</td>
        </tr>
    </table>

   5. 형식 명령어
        <table>
            <tr>
                <th>명령어</th>
                <th>내용</th>
            </tr>
            <tr>
                <td>COLUMN</td>
                <td>칼럼의 Format을 변경할 때</td>
            </tr>
            <tr>
                <td>TTITLE</td>
                <td>보고서의 제목을 설정할 때</td>
            </tr>
            <tr>
                <td>BTITLE</td>
                <td>보고서의 꼬리말을 설정할 때</td>
            </tr>
            <tr>
                <td>BREAK</td>
                <td>칼럼 또는 행의 값이 바뀔 때 마다 새로운 보고서 Format을 설정할 때</td>
            </tr>
        </table>

   6. 대화 명령어
        <table>
            <tr>
                <th>명령어</th>
                <th>내용</th>
            </tr>
            <tr>
                <td>DEFINE</td>
                <td>CHAR 데이터형의 사용자 변수를 생성</td>
            </tr>
            <tr>
                <td>UNDEFINE</td>
                <td>정의한 사용자 변수를 해제</td>
            </tr>
            <tr>
                <td>PROMPT</td>
                <td>PROMPT 지정</td>
            </tr>
            <tr>
                <td>ACCEPTED</td>
                <td>변수를 생성하여 특정 칼럼에 가변 값을 입력</td>
            </tr>
        </table>