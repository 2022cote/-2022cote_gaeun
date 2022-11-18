"""
BOJ #4134
다음 소수 (https://www.acmicpc.net/problem/4134)
"""

# 스스로 풀지 못해 검색하여 해결.

import sys
input = sys.stdin.readline

def isprimenumber(n):
  if n == 0 or n == 1: return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0: return False
  return True

test = int(input())
for _ in range(test):
  n = int(input())
  while not isprimenumber(n):
    n += 1
  if isprimenumber(n):
    print(n)
    


