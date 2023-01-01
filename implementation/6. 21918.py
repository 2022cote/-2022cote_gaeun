# 전구 - https://www.acmicpc.net/problem/21918

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
bulbs = list(map(int, input().split()))

for _ in range(M):
  a,b,c = map(int,input().split())
  if a == 1:
    bulbs[b-1] = c
  else:
    for i in range(c-b+1):
      if a == 2:      
        bulbs[b+i-1] = int(not bulbs[b+i-1])
      elif a == 3:
        bulbs[b+i-1] = 0
      else:
        bulbs[b+i-1] = 1

print(*bulbs)