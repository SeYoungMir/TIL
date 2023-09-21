### 3. 조건문
1. if
   1. 기본 형식 : if(조건) {명령어}
   2. 만약 조건이 참이라면 명령어를 실행함
   3. 만약 조건이 거짓이면 명령어를 실행하지 않음
   4. 조건은 조건식이나 변수값, 혹은 상수값이 사용됨
   5. 예시
    ```C
    #include <stdio.h>
    void main()
    {
        int num = 0
        if(num ==0)
        {
            printf("num=0 이다 \n")
        }
    }
    ```
2. if - else
   1. 기본 형식 : if (조건) {명령문 1} else {명령문 2}
   2. 만약 조건이 참이면 명령어 1을 실행함
   3. 만약 조건이 거짓이면 명령어 2를 실행함
   4. 조건은 조건식이나 변수값 혹은 상수값이 사용됨
   5. 예시
   ```C
    #include <stdio.h>
    void main()
    {
        int num = 75
        if(num > 90)
            printf("성적은 A")
        else if (num < 90 )
            printf("성적은 B")
        else if (num < 80 )
            printf("성적은 C")
        else if (num < 70 )
            printf("성적은 D")
        else 
            printf("성적은 F")
    }
   ```
3. switch
   1. switch는 여려 가지 조건 중 만족하는 조건을 택하는 것임
   2. 기본 구조:
   ```C
   switch(internal expression)
   {
        case 조건:

        case 정수, 문자:
        실행문장 ;
        break ;
            case 정수,문자:
        실행 문장;
        break ;
        ......
        default :
        statement ;
   }
   ```
   3. break 문을 만나면 switch 문을 빠져 나와 다음 문을 실행
   4. floating point나 식을 평가하여야 하는 경우는 switch를 쓸 수 없음
   5. 예시
    ```C
    #include <stdio.h>
    void main()
    {
        char ch = 'a' ;

        switch(ch)
        {
            case 'a' : prinf("character is %c\n",ch);
            break ;
            case 'b' : prinf("character is %c\n",ch);
            break ;
            case 'c' : prinf("character is %c\n",ch);
            break ;
            default : printf("other character")
        }

    }
    ```