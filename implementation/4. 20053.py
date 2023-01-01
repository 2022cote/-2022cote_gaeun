# 최소, 최대 2 - https://www.acmicpc.net/problem/20053

# 각 리스트를 sort 해서 [0],[-1] 값 뽑기

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())
  nums = list(map(int,input().split()))

  nums.sort()
  print(str(nums[0]) +' '+ str(nums[-1]))
