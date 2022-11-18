"""
BOJ #22943
수 (https://www.acmicpc.net/problem/22943)
"""

import sys
input = sys.stdin.readline

def isprimenumber(n):
  if n == 0 or n == 1: return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0: return False
  return True
  
def iscondition1(n):
  for i in range(1, n+1):
    if i != n-i and isprimenumber(i) and isprimenumber(n-i): return True
  return False

def iscondition2(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      if isprimenumber(i) and isprimenumber(n//i): return True
  return False

k,m = list(map(int, input().split()))
cnt = 0

for i in range(1,10**k):
  j = i
  while j % m == 0:
    j //= m
  if iscondition1(i) and iscondition2(j):
    cnt += 1
print(cnt)