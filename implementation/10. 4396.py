# 지뢰 찾기 - https://www.acmicpc.net/problem/4396

import sys
input = sys.stdin.readline

n = int(input())
bomb_map = [list(input().rstrip()) for _ in range(n)]
current = [list(input().rstrip()) for _ in range(n)]

is_bomb = False
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]

for i in range(n):
  for j in range(n):
    if current[i][j] == "x":
      if bomb_map[i][j] == "*":
        is_bomb = True

      cnt = 0
      for k in range(8):
        if (0<= i+dx[k] < n and 0 <= j+dy[k] < n and bomb_map[i + dx[k]][j + dy[k]] == "*"):
          cnt += 1
        current[i][j] = str(cnt)

if is_bomb:
  for i in range(n):
    for j in range(n):
      if bomb_map[i][j] == '*':
        current[i][j] = '*'

for i in current:
  print(''.join(i))