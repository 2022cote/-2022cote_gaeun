import sys
input = sys.stdin.readline

board = str(input().split())
cnt = 0
arr = []
result = []

for i in board:
  if i == 'X':
    cnt += 1
  elif i == '.':
    if cnt != 0:
      arr.append(cnt)
    arr.append(0)
    cnt = 0
  elif i == ']':
    arr.append(cnt)

for i in arr:
  if i % 2 != 0:
    result = []
    result.append(-1)
    break
  elif i == 0:
    result.append('.')
  elif i % 4 == 0:
    for i in range(i//4):
      result.append('AAAA')
  elif i % 4 == 2:
    for i in range(i//4):
      result.append('AAAA')
    result.append('BB')
  else:
    for i in range(i//2):
      result.append('BB')

for i in result:
  print(i, end='')