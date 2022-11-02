"""
BOJ #9934 
완전 이진 트리 (https://www.acmicpc.net/problem/9934)
"""

# 문제 접근: 
# 중위 순회 결과를 보고, 거꾸로 트리 만들기.

# 추가 메모:
# 포화 이진 트리인 경우, 가운데 값이 루트가 된다는 점을 이용해 풀었는데, 만약 마지막 레벨이 일부만 채워져 있는 완전이진트리라면 어떻게 되는지? 
# (백준 예시는 모두 포화 이진 트리길래 이렇게 구현했지만..)

import sys
input = sys.stdin.readline

K = int(input().rstrip()) # 레벨 입력받기
res = list(map(int, input().split())) # 중회순회 결과 입력받기

# 트리
tree = [[] for _ in range(K)]

def reverse_inorder(level, res):
  # 중회순회결과인 res의 가운데 값을, 트리의 'level' 레벨에 넣기
  center = len(res)//2
  tree[level].append(res[center])
  # 재귀 종료 조건
  if len(res) == 1: return
  # 왼쪽 하위트리로 이동해서 재귀적으로 수행
  reverse_inorder(level+1, res[0:center])
  # 오른쪽 하위트리로 이동해서 재귀적으로 수행
  reverse_inorder(level+1, res[center+1:])

reverse_inorder(0, res)

for i in range(K):
  print(*tree[i]) # *리스트 : 리스트 [1,2,3] => 1 2 3 과 같이 출력됨