"""
BOJ #21920
서로소 평균 (https://www.acmicpc.net/problem/21920)
"""

import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum = 0
len = 0

for i in a:
  if gcd(i,x) == 1:
    sum += i
    len += 1    
print('%0.9f'%(sum/len))