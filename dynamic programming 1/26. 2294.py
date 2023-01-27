# 동전 2 - https://www.acmicpc.net/problem/2294
# BOJ 2293과 같이 풀기

# 점화식: 
# a(i-coin)존재o -> a(i) = min(a(i), a(i-coin)+1).
# a(i-coin)존재x -> a(i) = 10001

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

d = [10001]*(k+1)  # dp 테이블. 합이 k가 되는 화폐 개수.
d[0] = 0

for i in coins:
  for j in range(i,k+1):
      d[j] = min(d[j], d[j - i] + 1)

if d[k] == 10001:
  print(-1)
else:
  print(d[k])