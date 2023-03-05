# 잃어버린 괄호 - https://www.acmicpc.net/problem/1541

import sys
input = sys.stdin.readline

exp = input().split('-')

ans = 0
arr = []

for i in exp:
  temp = 0
  templist = i.split('+')
  for j in templist:
    temp += int(j)  
  arr.append(temp)

ans = arr[0]
for i in arr[1:]:
  ans -= i
print(ans)