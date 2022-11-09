"""
BOJ #5347
LCM (https://www.acmicpc.net/problem/5347)
"""

# 문제 접근: 
# 파이썬 라이브러리 math의 lcm 사용

# 추가 메모: 

import sys
from math import lcm
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  a,b = map(int, input().split())
  print(lcm(a,b))