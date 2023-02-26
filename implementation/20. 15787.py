# 기차가 어둠을 헤치고 은하수를	- https://www.acmicpc.net/problem/15787

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
trains = [deque([0 for _ in range(20)]) for _ in range(N)]

for _ in range(M):
  command = list(map(int, input().split()))
  
  if command[0] == 1:
    if trains[command[1]-1][command[2]-1] != 1:
      trains[command[1]-1][command[2]-1] = 1
  elif command[0] == 2:
    if trains[command[1]-1][command[2]-1] == 1:
      trains[command[1]-1][command[2]-1] = 0
  elif command[0] == 3:
    trains[command[1]-1].pop()
    trains[command[1]-1].appendleft(0)
  elif command[0] == 4:
    trains[command[1]-1].popleft()
    trains[command[1]-1].append(0)

ans = []
for i in trains:
  if i not in ans:
    ans.append(i)

print(len(ans))