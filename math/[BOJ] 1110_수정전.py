"""
BOJ #1110
더하기 사이클 (https://www.acmicpc.net/problem/1110)
"""

# 문제 접근: 

# 추가 메모: 
# 처음에 n 입력받을때, rstrip 안 해줘서 공백이 포함되어 오류. 주의!
# 문자열 비교시, "08"=="8" -> False 주의!

import sys
input = sys.stdin.readline

n = input().rstrip()

if int(n) >= 10:
  a = n[0]
  b = n[1]
else:
  a = "0"
  b = n

cycle = 0
new = "-1"

while (int(new) != int(n)):
  sum = str(int(a) + int(b))
  if int(sum) >= 10:
    num2 = sum[1]
  else:
    num2 = sum
  new = b + num2
  a = new[0]
  b = new[1]
  cycle += 1

print(cycle)