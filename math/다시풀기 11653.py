"""
BOJ #11653
소인수분해 (https://www.acmicpc.net/problem/11653)
"""

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
