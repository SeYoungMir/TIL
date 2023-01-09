기본 data load
```python 
import pandas as pd
import numpy as np 

emp =pd.read_csv('../data/emp.csv')
emp
dept =pd.read_csv('../data/dept.csv')
dept
```

 Q1 ) select job, max(sal) from emp group by job;
- reset_index() 키워드는 Series(칼럼)로 출력하는 게 아니라 
DataFrame(테이블)으로 출력하는 키워드
```python 
result =emp.groupby('job')['sal'].max().reset_index()
print(type(result))
print(result)
```

Q2) `select deptno, sum(sal)
    from emp
    where deptno != 20
    group by deptno;`
```python 
result=emp.groupby('deptno')['sal'].sum().reset_index()
result[['deptno','sal']][result['deptno']!=20]
```
Q3) 부서번호, 부서별 평균월급을 구해보자

`    select deptno,avg(sal)
    from emp
    groupby deptno;
`
```python 
result= emp.groupby('deptno')['sal'].mean().reset_index()
result
```
Q4) Q3에서 평균 월급 출력 시 정수 부분만 출력

```python 
print(result)
print(type(result))
#print(help(result.astype))

result= emp.groupby('deptno')['sal'].mean().reset_index().astype(int)
result
```
Q5) 부서 위치, 부서별 월급의 합을 출력 (join=merge)

 `   select d.loc,sum(e.sal)
    from emp e, dept d
    where e.deptno = d.deptno
    groupby d.loc;`

`
    select d.loc,sum(e.sal)
    from emp join dept using(deptno)  ->from emp join dept on(emp.deptno=dept.deptno)
    groupby loc;
`

```python 
emp =pd.read_csv('../data/emp.csv')
dept =pd.read_csv('../data/dept.csv')

result=pd.merge(emp,dept,on ='deptno').groupby('loc')['sal'].sum().reset_index
result
```
Merge 함수
- `DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)`

- pandas.merge(emp_left,dept_right,how='inner',on='deptno')

  - how에 따라서

    - how='inner' :emp와 dept 데이터 프레임에 공통적으로 존재하는 교집합일 경우에만 추출
    - how='outer' :열의 데이터가 양쪽 데이터 프레임에 공통적으로 존재하는 교집합이 아니어도 추출 
    - how='left' : 왼쪽 데이터 프레임의 키열에 속하는 데이터 값을 기준으로 병합
    - how='right' :오른쪽 데이터 프레임의 키열에 속하는 데이터 값을 기준으로 병합


Q6) 
    `select loc,sum(sal)
    from emp outer right join dept using(deptno)
    group by loc;`

```python 
result= pd.merge(emp,dept,how='outer',on='deptno').groupby('loc')['sal'].sum().reset_index()
result

result= pd.merge(emp,dept,how='right',on='deptno').groupby('loc')['sal'].sum().reset_index()
print(result)
```
Q7) csv 모듈을 이용해서 emp.csv를 읽어와보자.
```python 
import csv
print(dir(csv))

emp_res=csv.reader('emp.csv')
print(type(emp_res))

print(dir(emp_res))
emp_res=csv.reader('emp.csv')
for m_list in emp_res:
    print(m_list)

emp_res=csv.reader('emp02.csv')
for m_list in emp_res:
    print(m_list)

emp_res=csv.reader('emp.csv')
for m_list in emp_res:
    print(m_list[0])
    
print(help(csv.reader)) #파이썬 파일로 오픈해서 csv 객체로 관리

file=open('../data/emp02.csv')
emp_res=csv.reader(file)
for m_list in emp_res:
    print(m_list)
```

Q8) emp_res 객체를 통해서 이름과 봉급을 구하자, 단 봉급은 월급 *11.2% 인상으로 구하자

```python 
file=open('../data/emp02.csv')
emp_res=csv.reader(file)
for m_list in emp_res:
    
    print(m_list[1],round(float(m_list[5])*1.112,4))
```
Q9) emp_res 에서 직업이 'salesman'인 사원의 이름과 직업을 출력해보자
```python 
file=open('../data/emp02.csv')
emp_res=csv.reader(file)
for m_list in emp_res:
    if m_list[2] =='SALESMAN':
        print(m_list[1],m_list[2])
```
Q10) emp.csv를 결측치를 확인하자
결측치 NaN= Not a number
```python 
emp =pd.read_csv('../data/emp.csv')
print(emp[['ename','comm']])

#커미션을 결측치를 확인해보자.
print(emp[['ename','comm']][emp['comm'].isnull()])

#커미션을 결측치가 아닌사원을 확인해보자.
print(emp[['ename','comm']][~emp['comm'].isnull()])

#emp.csv의 결측치를 다시 확인
print(emp.isnull()) #NAN 확인을 TRUE

#emp.csv의 결측치의 개수를 확인해보자
print(emp.isnull().sum())
```
Q11) 파생 데이터 생성 =파생 변수 =기존의 데이터를 가지고 가공해서 만든 새로운 데이터의 칼럼
```python 
#emp에 있는 sal을 sal02라는 칼럼을 생성해서 추가하자
emp =pd.read_csv('../data/emp.csv')
emp['sal02']=emp['sal']
emp
```

Q12) 이름과 부서 위치를 출력 해보자(join 이용)
- 조인 확인 후 result.loc을 emp 끝에 추가해 파생 변수를 생성하자
```python 
result=pd.merge(emp,dept,on='deptno')
result[['ename','loc']]

emp['loc']=result['loc']
emp
```

