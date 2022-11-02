"""
BOJ #11725 
트리의 부모 찾기 (https://www.acmicpc.net/problem/11725)
"""

# 문제 접근:
# 항상 부모 -> 자식 순서로 이동하는 DFS 사용하여, 자식을 방문할 때 그 자식 번호에 해당하는 list 에 부모 번호 저장해두고 출력.

# 추가메모:
# 저는 DFS 이용했지만 BFS로도 구현 가능하다고 해서, 추후 BFS로도 구현해보면 공부가 될 것 같습니다.

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# 노드의 개수
N = int(input())

# 트리
tree = [[] for _ in range(N+1)]
# 방문여부
visited = [False for _ in range(N+1)]

# 트리 구조 입력
for _ in range(N-1):
  node1, node2 = map(int, input().split())
  tree[node1].append(node2)
  tree[node2].append(node1)

# root부터 DFS 탐색 시작,
# 연결된 자식노드들 중 방문하지 않은 노드를 방문하면서,
# 그 노드의 visited 값을 부모노드 번호로 바꿔둠 (True 값이 되므로 방문처리됨)
def dfs(parent):
  for i in tree[parent]:
    if visited[i] == False:
      visited[i] = parent
      dfs(i)

dfs(1)

# 2번 노드부터 차례대로 visited 값 (= 부모노드 번호) 출력
for i in range(2,N+1):
  print(visited[i])