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
i = 2

for _ in range(n):
  if n == 1: break
  if n % i == 0:
    n = n // i
    print(i)
  else:
    i += 1