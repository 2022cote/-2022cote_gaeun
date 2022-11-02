"""
BOJ #14675 
단절점과 단절선 (https://www.acmicpc.net/problem/14675)
"""

# 문제 접근: 
# 트리의 단절점 = 루트 or 리프노드가 아님
# 트리의 단절선 = 모든 간선
# 해당 문제는 어떤 정점이 루트노드 or 리프노드인지 판단하는 문제. = 연결된 노드가 2개 미만인지 찾으면 됨!

import sys
input = sys.stdin.readline

def is_cut_vertex(k,tree):
  if len(tree[k]) < 2: print("yes")
  else: print("no")

N = int(input().rstrip()) # 트리의 정점 개수

# 트리
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
  a,b = map(int, input().split())
  tree[a].append(b)
  tree[b].append(a)

q = int(input().rstrip()) # 질의의 개수

# t가 1이면, is_cut_vertex 수행하여 연결된 노드가 2개 미만인지 확인
# t가 2이면, 트리의 간선은 모두 단절선이므로 "yes"
for _ in range(q):
  t, k = map(int, input().split())
  if t == 1:
    is_cut_vertex(k,tree)
  else:
    print("yes")