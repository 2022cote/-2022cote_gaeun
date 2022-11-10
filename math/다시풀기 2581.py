"""
BOJ #2581
소수 (https://www.acmicpc.net/problem/2581)
"""
#34
import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
lst = []
sum = 0

def isprimenumber(n):
  if n == 1: return False
  for i in range(2,int(n**0.5)+1):
    if n % i == 0: return False
  return True

for i in range(m,n+1):
  if isprimenumber(i):
    sum += i
    lst.append(i)

if lst:
  print(sum)
  print(lst[0])
else:
  print(-1)
