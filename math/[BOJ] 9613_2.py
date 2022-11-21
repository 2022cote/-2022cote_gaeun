"""
BOJ #9613
GCD 합 (https://www.acmicpc.net/problem/9613)
"""

# 방법2. 라이브러리 사용. 
# from itertools import combinations

import sys
from math import gcd
from itertools import combinations
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  testcase = list(map(int, input().split()))

  sum = 0
  nCr = combinations(testcase[1:], 2)
  for i in nCr:
    sum += gcd(i[0],i[1])
  print(sum)