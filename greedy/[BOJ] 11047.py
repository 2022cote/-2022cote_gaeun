# 동전 0 - https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

N,K = map(int, input().split())
coins = [int(input()) for i in range(N)]
coins.sort(reverse=True)

ans = 0
for i in coins:
  ans += K//i
  K %= i
print(ans)