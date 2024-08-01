# 부록 - 유용한 라이브러리
## 3. NumPy와 SciPy 사용
### 1. NumPy란
- NumPy는 대규모 다차원 배열과 행렬을 지원, 이를 조작할 수 있게 해 주는 고수준의 수학 함수를 제공하는 숫자 계산 라이브럴. 파이썬으로 뉴럴 네트워크를 구현할 때 굉장히 많이 사용됨.
1. NumPy 설치
   - 다른 라이브러리와 마찬가지로 pip install 명령어를 이용해 설치
   - ```bash
     $ pip install numpy
     ```
   - 설치가 완료되면 다음 명령어로 인터렉티브 셸 실행
   - ```bash
     $ python
     ```
2. 배열 조작
   - NumPy는 ndarray 클래스가 가장 중요한 클래스. 이 클래스는 이름 그대로 N차원 배열을 다루기 위한 클래스, 1차원 배열은 벡터, 2차원 배열은 행렬, 3차원 배열은 텐서에 해당
   - array 함수를 사용, 배열(ndarray 클래스)를 생성 가능
   - ```python
     >>> import array
     >>> arr = numpy.array([1,2,3])
     >>> print(arr)
     ```
   - 다차원 배열도 마찬가지 방법으로 조작 가능.
   - ```python
     >>> arr = numpy.array([1,2,3],[4,5,6],[7,8,9])
     >>> print(arr)
     ```
   - '차원 수'와 '각 차원의 요소 수(행과 열의 수)' 는 각각 ndim,shape로 확인 가능
   - ```python
     >>> arr.ndim
     >>> arr.shape
     ```
   - 배열 요소의 자료형은 numpy.dtype 라는 객체로 다룸. 불 자료형, 부호 있는 정수 자료형, 부호 없는 정수 자료형, 복소수 자료형 등을 지정 가능
     - Scipy 공식 문서(Data types)[[URL](https://docs.scipy.org/doc/numpy/user/basics.types.html)]

   - array 함수로 배열을 만들 때 dtype를 지정하면 데이터의 자료형을 지정 가능. 예를 들어 int32 자료형의 배열을 만들고 싶다면 다음과 같이 지정
   - ```python
     >>> arr = numpy.array([1,2,3], dtype = numpy.int32)
     >>> arr
     ```