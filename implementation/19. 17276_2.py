# 배열 돌리기	- https://www.acmicpc.net/problem/17276

import sys
input = sys.stdin.readline

def rotate45(lst,n):
  maincross = []
  subcross = []
  centercol = []
  centerrow = []
  center = n//2

  for i in range(n):
    maincross.append(lst[i][i])
    subcross.append(lst[i][n-i-1])
    centercol.append(lst[i][center])
  centerrow = lst[center]

  for i in range(n):
    lst[i][i] = centerrow[i]
    lst[i][n-i-1] = centercol[i]
    lst[i][center] = maincross[i]
  subcross.reverse()
  lst[center] = subcross

  return lst

T = int(input())

for _ in range(T):
  n,d = map(int, input().split())
  if d < 0:
    d += 360

  X = []
  for _ in range(n):
    X.append(list(map(int, input().split())))

  for _ in range(d//45):
    X = rotate45(X,n)

  for i in range(n):
    for j in range(n):
      print(X[i][j], end=' ')
    print()