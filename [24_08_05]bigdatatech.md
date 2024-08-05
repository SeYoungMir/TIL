# 부록 - 유용한 라이브러리
## 3. NumPy와 SciPy 사용
### 2. SciPy
3. 적분 계산
   - 적분을 할 때는 integerate 모듈 사용
   - ```shell
     >>> from scipy import integrate
     ```
   - quad 함수로 적분을 계산할 수 있음. 서식은 다음과 같음.
     - ```
       <결과>,<오차> = integrate.quad(<함수>,<적분 구간의 시작 지점>,<적분 구간의 종료 지점>)
       ```
   - 다음 코드는  3x+5를 계산하는 함수를 만들고 이를 적분
   - ```shell
     >>> def func(x):
     ...   return 3*x+5
     ...
     >>> res,err = integrate.quad(func,0,10)
     >>> print(res)
     >>> print(err)
     ```
   - 이 외에도 굉장히 다양한 과학 함수 존재, 흥미가 있다면 공식 문서 참고
     - 공식 문서 [[URL](https://docs.scipy.org/doc/scipy/reference/)]