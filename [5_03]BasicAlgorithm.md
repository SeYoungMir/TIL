## 최소 공통 조상: 트리에서의 최소 공통 조상을 찾는 알고리즘
### 최소 공통 조상(Lowest Common Ancestor)
- 최소 공통 조상(LCA) 문제는 두 노드의 공통된 조상 중에서 가장 가까운 조상을 찾는 문제
### 기본적인 최소 공통 조상(LCA) 알고리즘
- 최소 공통 조상 찾기 알고리즘
  1. 모든 노드에 대한 깊이(depth)계산
  2. 최소 공통 조상을 찾을 두 노드 확인
     1. 먼저 두 노드의 깊이(depth)가 동일하도록 거슬러 올라감
     2. 이후 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
  3. 모든 LCA(a,b)연산에 대하여 2번 과정 반복
### 기본적인 최소 공통 조상(LCA) 알고리즘: 시간 복잡도 분석
- 매 쿼리마다 부모 방향으로 거슬러 올라가기 위해 최악의 경우 $O(N)$의 시간 복잡도 요구
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 $O(NM)$
### 최소 공통 조상(LCA) 알고리즘 개선
- 각 노드가 거슬러 올라가는 속도를 빠르게 만드는 방법
- if 15칸 거슬러 올라가면
  - 8>4>2>1
- 2의 제곱 형태로 거슬러 올라가도록 하면 $O(logN)$의 시간 복잡도 보장
- 메모리를 조금 더 사용하여 각 노드에 대하여 $2^i$번째 부모에 대한 정보 기록
### 개선된 최소 공통 조상(LCA) 알고리즘 :시간 복잡도 분석
- 다이나믹 프로그래밍(dynamic programming)을 이용해 시간 복잡도 개선 가능
  - 세그먼트 트리를 이용하는 방법도 존재
- 매 쿼리마다 부모를 거슬러 올라가기 위해 $O(logN)$의 복잡도 필요
  - 따라서 모든 쿼리를 처리할 때의 시간 복잡도는 $O(MlogN)$