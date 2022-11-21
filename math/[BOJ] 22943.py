"""
BOJ #22943
수 (https://www.acmicpc.net/problem/22943)
"""

import sys
from itertools import permutations
input = sys.stdin.readline

primelist = [True] * 10**5
primelist[0] = primelist[1] = False
for i in range(2, 10**5):
  for j in range(2*i, 10**5, i):
    if primelist[j] == True:
      primelist[j] = False

def iscondition1(n):
  for i in range(1, n//2+1):
    if i != n-i and primelist[i] and primelist[n-i]: return True
  return False

def iscondition2(n):
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      if primelist[i] and primelist[n//i]: return True
  return False

k,m = list(map(int, input().split()))
cnt = 0

for i in permutations(range(10),k):
  if i[0] == 0: 
    continue
  i = int(''.join(map(str, i)))
  j = i
  while j % m == 0:
    j //= m
  if iscondition2(j) and iscondition1(i):
      cnt += 1

print(cnt)