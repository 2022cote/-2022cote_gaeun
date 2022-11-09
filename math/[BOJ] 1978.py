"""
BOJ #1978
소수 찾기 (https://www.acmicpc.net/problem/1978)
"""

# 문제 접근: 
# 소수 판별 알고리즘, '에라토스테네스의 체' 이용.

# 추가 메모: 

import sys
input = sys.stdin.readline

def isprimenumber(n):
  if n == 1 : return False # 1은 소수가 아니므로 예외처리
  for i in range(2,int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

n = int(input())
lst = list(map(int, input().split()))
num = 0

for i in lst:
  if isprimenumber(i):
    num += 1

print(num)