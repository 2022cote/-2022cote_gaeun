"""
두개씩 골라 더한 값의 최대값이 최소가 되도록.

홀수인 경우 최대값은 빼고,
가장 큰 값 + 가장 작은 값
그다음 큰 값 + 그 다음 작은 값 
...
이 중 최대값을 구하면 된다!
"""

import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
m = []

t.sort()

if n % 2 == 1:
  m.append(t.pop())

for i in range(n//2):
  m.append(t[i] + t[-(i+1)])

print(max(m))