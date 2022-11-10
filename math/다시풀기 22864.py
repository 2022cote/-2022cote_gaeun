"""
BOJ #22864
피로도 (https://www.acmicpc.net/problem/22864)
"""

import sys
input = sys.stdin.readline

a,b,c,m = map(int, input().split())

fatigue = 0
work = 0

for _ in range(24):
  if fatigue + a <= m:
    work += b
    fatigue += a
  else:
    fatigue -= c
    if fatigue < 0:
      fatigue = 0
print(work)