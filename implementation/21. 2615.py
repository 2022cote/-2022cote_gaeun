# 오목 - https://www.acmicpc.net/problem/2615

import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19):
  for j in range(19):
    if board[i][j]:
      target = board[i][j]

      for k in range(4):
        cnt = 1
        x = i + dx[k]
        y = j + dy[k]

        while 0 <= x < 19 and 0 <= y < 19 and board[x][y] == target:
          cnt += 1

          if cnt == 5:
            # 육목 체크
            if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and board[i - dx[k]][j - dy[k]] == target:
              break
            if 0 <= x + dx[k] < 19 and 0 <= y + dy[k] < 19 and board[x + dx[k]][y + dy[k]] == target:
              break
            # 육목이 아니라면 성공
            print(target)
            print(i+1, j+1)
            sys.exit()

          x += dx[k]
          y += dy[k]

print(0)