## 2. 명령문 및 함수
### 2. 함수
- 컴퓨터 프로그램은 주어진 입력 데이터를가지고 원하는 출력 데이터를 만드는 것
1. printf()
   1. printf(): 화면에 데이터를 출력하는 함수
   2. 프린터 타입
      - %d : integer type(10진수)
      - %f : floating point
      - %c : charactor
      - %s : charactor string
      - %o : integer type(8진수)
      - %x : integer type(16진수)
      - %e : 지수형
   3. 예시
    ```c
    #include "stdio.h"
    void main()
    {
        int num=10
        float dnum =10.3;
            printf("정수는 %d 실수는 %1f \n",num,dnum);
    }
    ``` 
2. scanf()
   1. scanf() : 키보드에서 데이터를 읽어들이는 함수
   2. printf() 와 반대되는 역할을 수행
   3. 사용 형식 : scanf("&제어문자, 변수);
   4. &은 변수가 저장된 메모리 위치를 나타내는 연산자
   5. 예시
    ```c
    1 scanf("%d",&num) 
    2 scanf("%d %o %x" &i, &j, &k);
    ```
    1. 정수 입력
    2. 여러가지 수치 입력