"""
BOJ #1747
소수&팰린드롬 (https://www.acmicpc.net/problem/1747)
"""

import sys
from math import log10
input = sys.stdin.readline

def ispalindrome(n):
  for i in range(0, int(log10(n)//2)+1):
    if str(n)[i] != str(n)[-(i+1)]: return False
  return True

def isprimenumver(n):
  if n == 1: return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0: return False
  return True

n = int(input())

while not ispalindrome(n) or not isprimenumver(n):
  n += 1
print(n)