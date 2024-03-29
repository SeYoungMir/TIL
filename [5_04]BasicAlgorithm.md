## 위상 정렬: 방향성을 거스르지 않도록 전체 노드를 나열하기
### 위상 정렬
- 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
### 진입차수와 진출차수
- 진입차수(Indegree):특정한 노드로 들어오는 간선의 개수
- 진출차수(Outdegree):특정한 노드에서 나가는 간선의 개수
### 위상 정렬 알고리즘
- 큐를 이용하는 위상 정렬 알고리즘의 동작 과정
  1. 진입차수가 0인 모든 노드를 큐에 투입
  2. 큐가 빌 때까지 다음의 과정 반복
     1. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
     2. 새롭게 진입차수가 0이 된 노드를 큐에 투입
- $\rarr$결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 동일
### 위상 정렬의 특징
- 위상 정렬은 DAG에 대해서만 수행 가능
  - DAG(Direct Acyclic Graph):순환하지 않는 방향 그래프
- 위상 정렬에서는 여러가지 답이 존재 가능
  - 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상인 경우가 존재한다면 여러가지 답이 존재
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다 판단
  - 사이클에 포함된 원소 중 어떠한 원소도 큐에 들어가지 못함
- 스택을 활용한 DFS를 이용해 위상 정렬 수행 가능
### 위상 정렬 알고리즘 성능 분석
- 위상 정렬을 위해 차례대로 모든 노드를 확인하며 각 노드에서 나가는 간선 차례대로 제거 해야 함
  - 위상 정렬 알고리즘의 시간 복잡도는 $O(V+E)$
