# 부록 - 유용한 라이브러리
## 3. NumPy와 SciPy 사용
### 2. SciPy
- 고급 통계 처리를 하고 싶을 때는 SciPy라는 라이브러리의 사용을 검토하면 좋음
- SciPy는 고급 과학 계산 전용 라이브럴. 배열과 행렬 연산은 이전에 설명한 NumPy로도 가능하지만, SciPy는 신호 처리, 직교 거리 회귀, 통계 등의 기능도 지원하는 굉장히 강력한 라이브러리.
1. SciPy 설치
   - pip install 명령어로 scipy 설치. NumPy도 필요하므로 설치하지 않았다면 함께 설치.
   - ```bash
     $ pip install scipy
     ```
2. 행렬 계산
   - SciPy는 여러가지 서브 모듈로 구분. 행렬 계산에는 선형 대수 기능이 있는 linalg 모듈을 사용. 행렬을 표현할 때는 NumPy 사용.
   - ```shell
     >>> from scipy import linalg
     >>> import numpy
     ```
   - inv 함수로 역행렬 계산 가능
   - ```shell
     >>> arr = numpy.array([[1,2],[3,4]])
     >>> inv_array = linalg.inv(arr)
     >>> print(inv_array)
     ```
   - det 함수로 행렬식 계산 가능
   - ```shell
     >>> arr = numpy.array([[1,2],[3,4]])
     >>> det = linalg.det(arr)
     >>> print(det)
     ```