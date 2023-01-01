# 빙고 - https://www.acmicpc.net/problem/2578

import sys
import itertools
input = sys.stdin.readline

user_board = [list(map(int, input().split())) for _ in range(5)]
check_board = [list(map(int, input().split())) for _ in range(5)]
nums = list(itertools.chain(*check_board))
check = 0

def bingo_function(user):
  bingo = 0
  for i in range(5):
    if sum(user[i]) == 0:
      bingo += 1

  vertical = list(map(list, zip(*user)))
  for i in range(5):
    if sum(vertical[i]) == 0:
      bingo += 1

  diagonal = user[0][0] + user[1][1] + user[2][2] + user[3][3] + user[4][4]
  if diagonal == 0:
    bingo += 1
  diagonal = user[4][0] + user[3][1] + user[2][2] + user[1][3] + user[0][4]
  if diagonal == 0:
    bingo += 1

  return bingo

for i in nums:
  for j in range(5):
    for k in range(5):
      if i == user_board[j][k]:
        user_board[j][k] = 0
        check += 1
        bingo = bingo_function(user_board)
        if bingo >= 3:
          print(check)
          exit()