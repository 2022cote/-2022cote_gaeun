"""
BOJ #2609
최대공약수와 최소공배수 (https://www.acmicpc.net/problem/2609)
"""

# 문제 접근: 
# 파이썬 라이브러리 math의 gcd, lcm 사용

# 추가 메모: 
# 라이브러리 사용하지 않고 손수 구현한다면,
# ex) 24, 16
# gcd = 8
# lcm = (24 // gcd) * (16 // gcd) * gcd

import sys
from math import gcd, lcm
input = sys.stdin.readline

num1, num2 = map(int, input().split())

print(gcd(num1, num2))
print(lcm(num1, num2))