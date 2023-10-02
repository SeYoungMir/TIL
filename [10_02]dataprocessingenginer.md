## 4. 라이브러리 활용 - 이어서
### 1. 라이브러리  - 이어서
4. Visual C++ 라이브러리 DLL 제작
    ```C++
    extern "C"__declspec(dllexport) int print()
    {
        AfxMessageBox(_T("DLL을 제작합니다/"));
        ...
    }
    ```
    DLL 생성
    1. 함수 선언
    2. 실행 프로그램
5. 아두이노 라이브러리
   1. 라이브러리 기본 형태
      1. Examples: 라이브러리 예제 폴더
      2. Src : 라이브러리 구성하는 헤더(.h)와 소스파일(.CCP)
      3. Keywords : 아두이노 IDE에서 코드를 볼 때 강조표시(다른 색상)할 문구 지정
      4. library.properties : 라이브러리의 기본 정보 파일
      5. README.md : 라이브러리의 간단한 설명, 있어도 되고 없어도 됨
   2. Keywords (강조 항목)
      1. 키워드 항목
        ```C++
        ########
        #Syntax Coloring Map For Ethernet
        ########

        #######
        #Datatypes(KEYWORDS1)
        ########

        Eternet KEYWORD1 Ethernet
        EtherneClient KEYWORD1 EthernetClient
        ~~~~

        ######
        # Methods and Functions(KEYWORD2)
        ########

        status KEYWORD2
        connect KEYWORD2
        ~~~~~~

        ```
      2. 프로그램 강조 예
        ```C++
        #include <PMsensor.h>

        PMsensor PM;
        
        /////(infrared LED pin, sensor pin) /////
        PM.init(3,A0);
        
        
        void loop(){
            float data = 0;
            int err = PMsensorErrSuccess;
        if((err = PM.read(&data,true,0.1)) != PMsensorErrSuccess){
        }
        }
        ```
       3.  library.properties(라이브러리 설명)
        ```C++
        name = Ethernet
        version = 2.0.0
        ~~~
        ```
           1.   이름
           2.   버전
           3.   제작자
           4.   설명
           5.   라이브러리 카테고리 등
           6.   잘못 작성되면 라이브러리 등록이 안될수도 있음
       4.  아두이노 라이브러리 .h 제작
        ```C++
        // 두개의 수를 받아 더하는 라이브러리
        class Calc
        {
            private:
                int a = 0;
                int b = 0;

            public:
                Calc(int val1, int val2){
                    a=val1;
                    b=val2;
                }
            int sum(){
                return a+b;
            }
        }
        ```
6. Open Source
   1. 공개(Git Hub)
   2. 공개되어 있어도 무조건 오픈소스는 아님
   3. 무단 사용을 해도 된다는 의미가  아님
   4. 일반적으로는 상업적 이용도 가능/불가능
   5. 오픈소스 라이선스를 따라야 함
   6. 자유로운 사용 복제 배포 수정의 권리를 보장 $\larr$ 무조건 아님(의무사항)
   7. 오픈소스 라이센스를 따르는 프로젝트
7. Open Source 라이센스 정책
   1. MIT
      1. 라이선스 저작권 명시
      2. 소스 공개의무 없음
   2. BSD
      1. 라이선스 저작권 명시
      2. 소스 수정시 공개의무 없음
   3. 아파치(Apache)
      1. 라이선스 저작권 명시
      2. 소스 수정시 공개 의무 없음
   4. MPL(Mozila Public License)
      1. 단순 사용시 공개 의무 없음
      2. 소스 수정 시 MPL로 공개
   5. 이클립스(Eclipse)
      1. 단순 사용 시 공개 의무 없음
      2. 소스 수정시 MPL로 공개
   6. GPL
      1. 단순 사용이나 수정 시 소스코드를 GPL로 공개
   7. LGPL
      1. 단순 사용 시 공개 의무 없음
      2. 배포 시 함께 배포 금지(사용자 추가 설치)
   8. AGPL(제약 조건 : 최상)
      1. 모든 소스 무조건 AGPL로 공개