## 유용한 표준 라이브러리 소개
### 실전에서 유용한 표준 라이브러리
- 내장 함수: 기본 입출력 함수부터 정렬 함수까지 기본적 함수들 제공
  - 파이썬 프로그램을 작성할 때 없어서는 안되는 필수적 기능 포함
- itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들 제공
  - 특히 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용
- heapq: 힙(Heap) 자료구조를 제공
  - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
- bisect: 이진 탐색(Binary Search)기능 제공
- collections: 덱(deque),카운터(Counter) 등의 유용한 자료구조 포함
- math: 필수적 수학적 기능 제공
  - 팩토리얼, 제곱근, 최대공약수(GCD),삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함
### 자주 사용되는 내장 함수
- sum()
- min(),max()
- eval()
- sorted()
- sorted() with key
### 순열과 조합
- 모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용하는가
- 순열: 서로 다른 $n$ 개에서 서로 다른 $r$개를 선택하여 일렬로 나열
- 조합: 서로 다른 $n$개에서 순서에 상관 없이 사로 다른 $r$개를 선택하는 것
- 순열의 수: $nPr=n\ast(n-1)\ast(n-2)\ast\cdots\ast(n-r+1)$<br>조합의 수:$nCr={{n\ast(n-1)\ast(n-2)\ast\cdots\ast(n-r+1)}\over{r!}}$
- 순열: from itertools import permutations
- 조합 : from itertools import combinations
- 중복 순열: rom itertools import product
- 중복 조합: rom itertools import combinations_with_replacement
### Counter
- 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능 제공
- 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌
### 최대 공약수와 최소 공배수
- 최대 공약수를 구해야 할 때는 math 라이브러리의 gcd() 함수 이용 가능
- 최소 공배수를 구해야 할 때는 math 라이브러리의 lcm() 함수 이용 가능
