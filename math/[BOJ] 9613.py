"""
BOJ #9613
GCD 합 (https://www.acmicpc.net/problem/9613)
"""

import sys
from math import gcd
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  testcase = list(map(int, input().split()))

  sum = 0

  for i in range(2,testcase[0]+1):
    for j in range(1,i):
      sum += gcd(testcase[i],testcase[j])
  print(sum)