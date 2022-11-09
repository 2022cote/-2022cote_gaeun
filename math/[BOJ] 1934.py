"""
BOJ #1934
최소공배수 (https://www.acmicpc.net/problem/1934)
"""

# 문제 접근: 
# 파이썬 라이브러리 math의 lcm 사용

# 추가 메모: 

import sys
from math import lcm
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  a,b = map(int, input().split())
  print(lcm(a,b))