"""
BOJ #22864
피로도 (https://www.acmicpc.net/problem/22864)
"""

# 일 -> time +1, fatigue +a, work +b
# 쉼 -> time +1, fatigue -c, work +0

# 문제 접근: 
# 일단 피로도가 M을 넘지 않으면 계속 일을 시키고, 더이상 일하면 M을 넘을때만(fatigue + a <= m) 쉰다. => 그리디

import sys
input = sys.stdin.readline

a,b,c,m = map(int,input().split())

fatigue = 0
work = 0

for _ in range(24):
  if fatigue + a <= m:
    fatigue += a
    work += b
  else:
    if fatigue - c >= 0:
      fatigue -= c
    else:
      fatigue = 0
print(work)
