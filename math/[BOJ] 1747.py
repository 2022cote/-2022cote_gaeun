"""
BOJ #1747
소수&팰린드롬 (https://www.acmicpc.net/problem/1747)
"""

# 팰린드롬 판별 방법1. 앞과 뒤의 대칭되는 index끼리 좁혀오면서 확인 (ispalindrome1)
# 팰린드롬 판별 방법2. 숫자를 뒤집어서 확인 (ispalindrome2)

import sys
from math import log10
input = sys.stdin.readline

def ispalindrome1(n):
  for i in range(0, int(log10(n)//2)+1):
    if str(n)[i] != str(n)[-(i+1)]: return False
  return True

def ispalindrome2(n):
  a = str(n)
  b = str(n)[::-1]
  if a == b: return True

def isprimenumver(n):
  if n == 1: return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0: return False
  return True

n = int(input())

while not ispalindrome1(n) or not isprimenumver(n):
  n += 1
print(n)