### 파이썬 리스트
- 가변형, 시퀀스 (str, list, tuple) = [+(결합),*(반복),중첩,슬라이싱, 인덱싱],[]
- 동작 속도가 느리다.
- 콤마 요소 분리, 구별

#### numpy
- 수식 라이브러리, 수치연산, 배열 객체
- 동작 속도가 빠르다. 
- 연속적인 메모리
- 한가지 타입만 처리 가능

1. np.array로 객체 생성
2. np.arange로 객체 생성
```python
#ndarray(shape[, dtype, buffer, offset, ...])

import numpy as np
```
```python
a= np.array([0,1,2,3,4,5]) # = ndarray
print(a)
print(type(a))
print(a.dtype) #a 객체가 가진 데이터 타입
```
```python
print(dir(np.sctypeDict))
np.sctypeDict.keys() #numpy에서 사용되는 데이터 타입
```
```python
a= np.array([0.0,1.0,2.0,3.0,4.0,5.0])
print(a)
print(type(a))
print(a.dtype) 
```
- a 객체가 가진 데이터 타입 0,1 = bit * 8 = byte = 주소가 생성 ~128~127

- 주소 생성 ->메모리 할당 -> 값 대입
- 불리언 bool(1),byte(1)
- 정수형 short(2) -> int32(4) -> int64(8) -> long (8) ~ 16   #괄호 안은 바이트, 밖은 비트
- 실수형 float(4) -> double(8)
- 문자와 문자열 -> str

- ex) 'int 32' = 정수형 32bit , 'i4' = 정수형 4byte
- float 64 = f8 = 실수형 64bit= 실수형 8byte
```python
a = np.arange(10) #0~9  ,로 구분하지 않는다.
print(a)
print(type(a))
```

3. #ndarray(shape[, dtype, buffer, offset, ...]) /shape
    3-1)차원 (Rank, Dimension)을 []로 개수를 늘린다. [[[a]]] =3차원 [[b]] = 2차원
    아벨 4차원 이상 -> 컴퓨터
    
    대상 ->특징추출(x_독립변수,y_종속변수) -> 도메인 -> 설명(통계_R/python) -> 예측(ML) 
    -> ML+AI(= DL)(CNN,이미지, 영상)
    
3. 2)차원의 종류
- 1차원 : shape(x,)
- 2차원 : shape(x,y), 행렬(matrix)
- 3차원 : shape(x,y,z) ,(행,렬,면)-> (면,행,렬)로 변환, 작업 [2,2,4]
- ...n차원 : shape(x,y,z......)


- 1차원 shape(x,)
```python

a=np.arange(12)
print(a)
print(a.shape) #(12,) ->1차원
t=a.shape
print(type(t))
print((a.shape[0]))
```

- 2차원 배열의 Shape: 행(row,수직,axis=0)과  열(column,수평,axis=1)
```python
m= np.array([[0,1,2],[0,1,2]])
print(m)
print(m.shape) #(2,3) -->2차원, 행렬(matrix)
print(m.shape[0],m.shape[1]) 
```

- 3차원 배열의 Shape: (면,행,열)
```python
m= np.array([[[0,1,2],[3,4,5]],[[0,1,2],[3,4,5]]])
print(m)
print(m.shape)#(2,2,3)-->3차원
print(m.shape[0],m.shape[1],m.shape[2]) 
```

4. 배열과 슬라이싱 _reshape()

- 2차원 배열 인덱싱 슬라이싱
```python
a=np.arange(12).reshape(3,4)
print(a)
print(a.shape)
```

- a 가진 값 0,0,9를 리턴해보자 =인덱싱
```python
print(a[0][0])
print(a[0,0])
print(a[2][1])
print(a[2][3],a[2,3])
```

- 0 행의 모든 데이터를 20으로 변경 후 전체 출력해보자
```python
a[0]=20
print(a[:,:])
print(a[::2,::2]) #[start:end-1:step]
```

- 슬라이싱 요소 전체의 값을 변경해보자.
```python
print(a[:,:])
print(a[::1,::3])
```
```python
print(a[::2,::3]) #꼭짓점 추출
a[::2,::3]=0
print(a[:,:])
a[:,:]=-1
print(a[:,:])
```

- 3차원 배열 인덱싱 슬라이싱
```python
a=np.arange(12).reshape(2,2,3)
print(a,a.shape)
```

- 인덱싱
```python
print(a[0][0][0])
print(a[0,0,0])
```
- 5 추출
```python
print(a[0,1,2])
```

- 슬라이싱
```python
print(a[:,:,:]) #전체출력
print('-'*15)
print(a[:,1:,1:])
print('-'*15)
```

1) case 1: 3차원 출력
```python
# 6,7 
print(a[1:,:1, :2])
# 4,5
print(a[:1,1:, 1:])
# 6,7 
print(a[1:,:-1, :2])
# 4,5
print(a[:-1,1:, 1:])
```
2) case 2: 2차원 출력
```python
print(a[1,:-1,:-1],a[0,1:,1:])
```
3) case 3: 1차원 출력
```python
print(a[1,:1,:-1],a[0,1,1:])
```

5. 불리언 인덱싱 :조건식을 이용한 인덱싱, 조건 검색 필터를 사용한 추출값(중요!)
```python
a=np.arange(1,7)
print(a)

print(a>2)
#배열의 객체 a에서 2보다 큰 값을 배열로 리턴
print(a[a>2]) # -> 이미지의 사례 >빨간 사과 -> 이상 값(노이즈) 추출 후 변경하고싶다

bool_index =np.array([True, False,  True,  False,  True,  False])
print(bool_index)
print(a[bool_index])
print(a[a%2==1])

#배열 a에서 3이 아닌 요소를 추출
print(a[a!=3])
#2보다 크고 6보다 작은 요소를 추출
print (a[(a>2)&(a<6)])
#짝수만 추출
print(a[a%2==0])
#평균보다 작은값을 추출해보자

print(a[a<a.mean()])
```
6. 배열의 형상 다루기 : reshape(),flatten()(편평화),transpose()(전치)

- flatten():다차원 배열을 1차원으로 만든다.
```python
a=np.arange(12).reshape(3,4)
print(a,a.shape)

f= a.flatten()
print(f,f.shape)
```

- 데이터 순서를 거꾸로 변경
```python
print(a[::-1]) #행의 순서를 거꾸로
print(a[:,::-1]) #열의 순서를 거꾸로
print(a[::-1,::-1]) #행과 열의 순서를 거꾸로
print ('-'*20)
```

- transpose()
  - 전치 행렬, 행과 열을 서로 맞바꾸는 함수
```python
t=a.transpose()
print(t,t.shape) #(3,4) --> (4,3), (x,y)--> (y,x)
print(a.T) #transpose()함수와 동일한 결과

print(dir(a.T))

a.flat=0 #임시로 1차원으로 변경 후 값 대입 후 차원 다시 리턴  (= a.flatten().reshape(원래 차원) )
print(a)
```

7. numpy의 속성 (Attribute): 멤버변수, 메서드
- dtype,shape,ndim,flat,T,size,nbytes
```python
d = np.arange(12).reshape(3,4)
print(d,d.shape)
print(d.dtype)  # int32 or int64
print(d.ndim)   # 2차원  ==> print(len(d.shape)) 와 동일
print(d.T)      # transpose()함수와 동일한 결과, 전치행렬
print(d.size)   # 12개 , 요소의 갯수
print(d.nbytes) # 48 bytes : 32bit(4 byte) * 12 
d.flat = 1
print(d)
```
- numpy 통계 함수들
```python
a = np.arange(12).reshape(3,4)
print(a,a.shape)

print(a.max(),np.max(a)) #최대값
print()
print(a.min(),np.min(a)) #최솟값
print()

print(a.sum()) #합
print(a.mean()) #평균

print(a.std()) #표준 편차
print(a.var()) #분산
print(np.median(a)) #중위수
```

- 사분위수
```python
print('25%:',np.percentile(a,25)) #1사분위수(Q1)
print('50%:',np.percentile(a,50)) #2사분위수(Q2),median()과 같은 값
print('75%:',np.percentile(a,75)) #3사분위수(Q3)
```
