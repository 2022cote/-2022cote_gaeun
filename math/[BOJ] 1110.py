"""
BOJ #1110
더하기 사이클 (https://www.acmicpc.net/problem/1110)
"""

import sys
input = sys.stdin.readline

n = input().rstrip()

# 문자열의 각 자리수를 뽑을때는 index로 뽑지 말고, 몫과 나머지로 처리하자!

a = int(n)//10
b = int(n)%10
new = "-1"
cycle = 0

while (int(new) != int(n)):
  num2 = (a + b)%10
  new = str(b) + str(num2)
  a = int(new)//10
  b = int(new)%10
  cycle += 1

print(cycle)