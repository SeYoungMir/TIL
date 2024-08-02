# 부록 - 유용한 라이브러리
## 3. NumPy와 SciPy 사용
### 1. NumPy란
3. 단위행렬 생성
   - 단위행렬을 만드는 identity 함수도 있음. 매개 변수로 행렬의 크기를 지정
   - ```python
     >>> arr= numpy.identity(5)
     >>> print(arr)
     ```
4. 배열 계산
   - 배열을 스칼라와 곱하거나 배열끼리 계산 가능
   - ```python
     >>> arr = numpy.array([[1,2,3],[4,5,6]])
     >>> arr*5

     >>> arr1 = numpy.array([1,2,3])
     >>> arr2 = numpy.array([[4,5,6],[7,8,9]])
     >>> arr1+arr2
     ```
5. 통계 함수 사용
   - NumPy는 숫자 계산 라이브러리이므로 다음과 같은 기본적인 통계 함수도 제공
   - <table>
        <tr>
            <th>함수이름</th>
            <th>설명</th>
        </tr>
        <tr>
            <td>amax()</td>
            <td>최댓값</td>
        </tr>
        <tr>
            <td>amin()</td>
            <td>최솟값</td>
        </tr>
        <tr>
            <td>ptp()</td>
            <td>값의 범위</td>
        </tr>
        <tr>
            <td>mean()</td>
            <td>산술 평균</td>
        </tr>
        <tr>
            <td>median()</td>
            <td>중앙값</td>
        </tr>
        <tr>
            <td>std()</td>
            <td>표준 편차</td>
        </tr>
        <tr>
            <td>var()</td>
            <td>분산</td>
        </tr>
     </table>
   - 이러한 함수들을 사용해보자.
   - ```python
     >>> arr = numpy.array([10,100,300,500,1000])
     >>> numpy.amax(arr)
     >>> numpy.amin(arr)
     >>> numpy.ptp(arr)
     >>> numpy.mean(arr)
     >>> numpy.median(arr)
     >>> numpy.std(arr)
     >>> numpy.var(arr)
     ```