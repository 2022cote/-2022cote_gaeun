"""
BOJ #14425
문자열 집합 (https://www.acmicpc.net/problem/14425)
"""

# 풀이(정답):
# 딕셔너리 이용하여 조회

import sys

N, M = map(int,sys.stdin.readline().split())
S = {}
num = 0
for i in range(N):
  S[sys.stdin.readline().rstrip()] = i
for i in range(M):
  if sys.stdin.readline().rstrip() in S:
    num += 1
print(num)