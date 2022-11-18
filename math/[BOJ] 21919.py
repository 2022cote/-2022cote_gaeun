"""
BOJ #21919
소수 최소 공배수 (https://www.acmicpc.net/problem/21919)
"""

import sys
from math import lcm
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

def isprimenumber(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0: return False
  return True

primes = []

for i in a:
  if isprimenumber(i):
    primes.append(i)

if len(primes):
  print(lcm(*primes))
else:
  print(-1)