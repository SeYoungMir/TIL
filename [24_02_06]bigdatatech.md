# 3. 크롤러 및 스크레이핑 개발 환경 준비와 파이썬 기본
## 3. 파이썬 기초
### 4. 문자열
3. 분할
   - split 메서드를 사용하면 문자열을 지정한 문자로 자를 수 있음
   ```python
   split("자를 문자")
   ```
   - split 메서드를 사용하는 대표적인 경우는 CSV 파일을 처리할 때
   - CSV 파일은 값이 쉼표로 구분되므로 다음과 같이 쉼표로 잘라서 사용
   ```python
   >>> string = "one,two,three"
   >>> string.split(",")
   ['one','two','three']
   ```
   - split 메서드를 사용해서 문자열을 분할, 이 때 반환되는 값은 리스트 자료형으로 반환
4. 결합
   - 파이썬으로 문자열을 결합하는 가장 간단한 방법은 + 연산자 사용
   ```python
   >>> a = "Hello"
   >>> b = "World"
   >>> a + b
   'HelloWorld'
   ```
   - 리스트의 join 메서드를 사용하면 자른 문자열을 다시 지정한 문자로 결합 가능. CSV 파일 만들 때 사용
   ```python
   >>> array = ['one','two','three']
   >>> ",".join(array)
   'one,two,three'
   ```
### 5.자료구조
1. 리스트
   - 다른 프로그래밍 언어에서 '배열'의 역할을 하는 자료 구조가 파이썬에서는 리스트. 리스트의 요소는 인덱스를 사용해 참조하고 변경 가능
   ```python
   >>> array = ['one','two','three']
   >>> array[1]
   'two'
   ```
   - 요소를 여러 가지 자료형으로 구성 가능
   ```python
   >>> array = ['one',2,'three']
   ```
   - 다른 프로그래밍 언어와 다른 점으로 * 연산자를 사용해서 요소를 반복하여 새로운 리스트를 만들 수 있음
   ```python
   >>> array = [0]*10
   >>> print(array)
   [0,0,0,0,0,0,0,0,0,0,0]
   ```
   - 리스트에 있는 요소의 개수는 len 함수를 사용해 확인할 수 있음
   ```python
   >>> array = ['one',2,'three']
   >>> len(array)
   3
   ```
   - 리스트 끝에 요소를 추가할 때는 append 메서드, 지정한 위치에 요소를 삽입할 때는 insert 메서드를 사용
   ```python
   >>> array = ['one',2,'three']
   >>> array.append(4)
   >>> print(array)
   ['one',2,'three',4]
   ```
   - insert 메서드는 첫 번째 매개 변수에 삽입하고 싶은 인덱스를 지정, 두 번째 매개변수에 요소를 지정
   ```python
   >>> array = ['one',2,'three']
   >>> array.insert(1,1.5)
   >>> print(array)
   ['one',1.5,2,'three']
   ```
2. 튜플
   - 파이썬에는 튜플이라는 자료형 존재
   - 튜플은 리스트처럼 여러 요소로 구성, 요소들이 순서를 가지고 있음
   - 리스트와 다르게 한 번 생성된 이후에는 요소를 변경할 수 없음
   - 튜플은 (요소,요소,...) 처럼 작성, 요소가 1개밖에 없을 때는 마지막 위치에 쉼표 입력
   ```python
   num = (5,)
   ```
   - 요소를 변경할 수 없으므로 요소를 변경하려 하면 오류 발생
   ```python
   >>> num = (5, 10, 15)
   >>> num[0] = 3
   Traceback (most recent call last):
        File "<stdin>".line 1, in <module>
   TypeError: 'tuple' object does not support item assignment
   ```