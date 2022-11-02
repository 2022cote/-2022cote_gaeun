"""
BOJ #1991 
트리 순회 (https://www.acmicpc.net/problem/1991)
"""

# 문제 접근:
# 트리는 딕셔너리로 구현, 재귀함수를 이용해 트리 순회.

import sys
input = sys.stdin.readline

N = int(input().rstrip())

# 트리
tree = {}

# 트리 구조 입력
for _ in range(N):
  root, left, right = input().split()
  tree[root] = [left, right]


def preorder(root):
  if root == ".": return
  print(root, end="")
  preorder(tree[root][0])
  preorder(tree[root][1])

def inorder(root):
  if root == ".": return
  inorder(tree[root][0])
  print(root, end="")
  inorder(tree[root][1])

def postorder(root):
  if root == ".": return
  postorder(tree[root][0])
  postorder(tree[root][1])
  print(root, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
