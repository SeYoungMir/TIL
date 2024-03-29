## 간단하면서 기본적인 정렬 알고리즘: 선택 정렬과 삽입 정렬
### 정렬 알고리즘
- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용
#### 선택 정렬
- 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복
- 선택 정렬의 시간 복잡도
  - 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 함
  - 구현 방식에 따라서 사소한 오차는 있을 수 있지만 전체 연산 횟수는 다음과 같음. <br>$N+(N-1)+(N-2)+...+2$
  - 이는 $(N^2+N-2)/2$로 표현할 수 있는데, 빅 오 표기법에 따라 $O(N^2)$이라고 작성
#### 삽입 정렬
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
- 선택 정렬에 비해 구현 난이도는 높은 편, 일반적으로 더 효율적으로 동작
- 삽입 정렬의 시간 복잡도
  - 삽입 정렬의 시간 복잡도는 $O(N^2)$이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용
  - 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
    - 최선의 경우 $O(N)$의 시간 복잡도
    - 이미 정렬되어 있는 상태에서 다시 삽입정렬 수행시 $O(N)$의 시간 복잡도