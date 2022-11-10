"""
BOJ #5618
공약수 (https://www.acmicpc.net/problem/5618)
"""

import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
lst = []

if n == 2:
  a,b = map(int,input().split())
  gcd_ = gcd(a,b)
else:
  a,b,c = map(int,input().split())
  gcd_ = gcd(a,b,c)

# 소수 찾을때 무조건 제곱근 이용하여 시간복잡도 줄이기
for i in range(1,int(gcd_**0.5)+1):
  if gcd_ % i == 0:
    lst.append(i)
    if i**2 != gcd_:
      lst.append(gcd_//i)
lst.sort()
for i in lst:
  print(i)