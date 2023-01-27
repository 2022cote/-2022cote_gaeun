# 동전 1 - https://www.acmicpc.net/problem/2293
# BOJ 2294과 같이 풀기

# 점화식:
# a(i) = a(i) + a(i-coin)

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [0] * (k+1)
d[0] = 1

for i in coins:
  for j in range(i,k+1):
    d[j] += d[j-i]

print(d[k])