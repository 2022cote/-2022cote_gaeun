"""
BOJ #11653
소인수분해 (https://www.acmicpc.net/problem/11653)
"""

# 문제 접근: 
# 2부터 시작, 나눠지면 계속 나누다가, 안 나눠지면 +1해서 나누기. 
# 소수가 아닌 걸로 나눈다고 해도, 이미 그 약수로 나눠지지 않으니까 pass 될 것임.

# 추가 메모: 

import sys
input = sys.stdin.readline

n = int(input())
lst = []
num = 2

while(n):
  if n == 1: break
  else:
    if n % num == 0:
      n = n//num
      lst.append(num)
    else:
      num += 1

for i in lst:
  print(i)