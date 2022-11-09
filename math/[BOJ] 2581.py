"""
BOJ #2581
소수 (https://www.acmicpc.net/problem/2581)
"""

# 문제 접근: 
# 소수 판별 알고리즘, '에라토스테네스의 체' 이용.

# 추가 메모: 

import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
lst = []
sum = 0

def isprimenumber(number):
  if number == 1: return False
  for i in range(2,int(number**0.5)+1):
    if number % i == 0: return False
  return True

for i in range(m, n+1):
  if isprimenumber(i):
    lst.append(i)
    sum += i

if lst:
  print(sum)
  print(lst[0])
else:
  print(-1)