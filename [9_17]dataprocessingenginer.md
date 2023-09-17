# 10. 프로그래밍 언어 활용
## 1. 기본문법 활용하기
### 1. 컴퓨터의 구성 요소
1. 컴퓨터의 기본 요소
   - CPU(Central Processing Unit) : 중앙 처리 장치
   - Main memory : 주 기억 장치
   - Data storages : 데이터 저장 장치 (예) 하드 디스크, CD 등
   - I/O devices : 입출력 장치
   - Other peripheral devices
2. 중앙 처리 장치(CPU)
   - 연산 처리 장치, 전기 회로로 구성
   - 연산 장치, 제어 장치, registers로 구성
   - arithmetic/logic unit : 데이터 처리
   - control unit : 컴퓨터의 동작을 제어
   - registers : CPU에 내재한 기억 장치, 빠른 처리 속도
3. 기계어 (Machine Language)
   - CPU가 알아들을 수 있는 instruction
   - main memory에 저장된 각 bit pattern 들에 대응하는 machine
   - instruction을 결정
   - coding system과 각 code에 대응되는 명령의 집합
### 2. 프로그래밍 언어
1. 프로그래밍 언어 기본 요소
   - C 프로그램은 한개 이상의 함수(Function)들로 구성되어 있음
   - 함수 : 어떤 특정한 작업을 수행하도록 한 독립적인 모듈(module)은 서로 독립적이며 인자(argument)를 통하여 정보를 전달함
   - 이름 : 여러 함수를 구별하기 위한 수단이 됨
   - 함수나 변수의 이름은 임의로 정할 수 있음
   - 모든 실행 가능한 프로그램은 main()이라는 이름을 가진 함수를 포함해야함
   - 함수의 이름은 숫자, 알파벳 문자(대,소), underscore '_'만 사용 가능
   - 함수의 내용 표시 : 함수 내용의 시작과 끝은 항상 중괄호 {와}임
2. main() 함수
   - 실행 가능한 C 프로그램은 항상 main() 함수를 포함해야함
   - 프로그램의 실행은 main() 함수로부터 실행됨
   - main()은 일종의 함수이며 기본 모듈임
### 3. 컴파일(Compile)
1. 언어의 기본 구조
   1. 프로그램 언어의 기본 구조
     - 변수 : 기본형(정수, 실수, 문자), 확장형(열거, 배열, 포인터, 구조체, 공용체)
     - 연산자 : 논리 연산자, 비트 연산자
     - 제어문 : 분기문(if else, switch case), 반복문(while, for ,do , while)
     - 함수 : 사용자 정의 함수, 재귀함수
   2. 프로그램 작성 단계
      - 편집(edit) :  에디터를 이용하여 컴퓨터 프로그래밍 작업의 내용을 기술하여 소스 코드 작성
        - 소스 파일(Source file) : 소스 코드가 들어 있는 텍스트 파일 (예) test.c, test.java
      - 컴파일(compile) : 사람이 알 수 있는 소스 파일을 기계가 알 수 있는 기계어로 변환
        - 오브젝트 파일(object file) : 기계어로 변환된 파일 (예) test.obj, test.class
      - 링크(link) : 오브젝트 파일들을 라이브러리 파일들과 연결하여 하나의 실행 파일 생성
        - 실행 하는 파일 (예) : test.exe, test.com
2. compile이란?
   - 프로그래밍 언어를 사용하여 작성된 프로그램을 기계어(machine language)로 바꾸어 주는 것
   - 프로그램을 컴퓨터(CPU)가 알아들을 수 있는 기계어로 바꾸는 것
     - source code : 프로그래머가 작성한 프로그램 (.c, .java 확장자)
     - object code(executable code) : 컴퓨터 CPU 에서 실행 가능한 code(.com, .exe)