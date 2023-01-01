# 소가 길을 건너간 이유 1 - https://www.acmicpc.net/problem/14467

# 해당 인덱스의 값이 바뀌면 +1

import sys
input = sys.stdin.readline

cows = [None for _ in range(11)] # 파이썬은 null이 아닌 None
switch = 0
N = int(input())


for _ in range(N):
  num,location = map(int,input().split())
  if cows[num] != None and cows[num] != location :
    switch += 1
  cows[num] = location

print(switch)