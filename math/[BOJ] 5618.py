"""
BOJ #5618
공약수 (https://www.acmicpc.net/problem/5618)
"""

# 문제 접근: 
# 최대공약수의 약수를 완전탐색으로 찾기
# 시간 초과. ㅠㅠ

# 추가 메모:
# gcd 구현하지 말고, 파이썬 라이브러리 math의 gcd를 사용해도 가능.

import sys
from math import gcd
input = sys.stdin.readline

# 최대공약수 구하는 함수 gcd (반복문 사용)
"""
def gcd(a,b):
  if a > b :
    a, b = b, a
  while b: # b==0까지 반복
    a, b = b, a % b
  return a
"""
""" 최대공약수 구하는 함수 gcd (재귀함수 사용) - 실행 안 됨
def gcd2(a,b):
  if a > b :
    a, b = b, a
  if a % b == 0: return b
  return gcd2(b, a % b)
"""
res = []
n = int(input())

# 입력값(=2,3)에 따라 gcd 진행
if n == 2:
  num1, num2 = map(int, input().split())
  gcd_ = gcd(num1, num2)
elif n == 3:
  num1, num2, num3 = map(int, input().split())
  gcd_ = gcd(gcd(num1, num2), num3)

# 최대공약수의 약수들을 완전탐색으로 찾기
for i in range(1,gcd_+1):
  if gcd_%i == 0:
    res.append(i)

# 순서대로 정렬
res.sort()

# 결과 출력
for i in res:
  print(i)