# 피로도 - https://www.acmicpc.net/problem/22864

# 그리디

import sys
input = sys.stdin.readline

A,B,C,M = map(int, input().split())
fatigue = 0
work = 0

for _ in range(24):
  if fatigue + A > M:
    if fatigue - C < 0:
      fatigue = 0
    else:
      fatigue -= C
  else:
    fatigue += A
    work += B

print(work)