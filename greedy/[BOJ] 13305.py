# 주유소 - https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

N = int(input())
lens = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
ans = 0

for i in range(N-1):
  if min_price >= prices[i]:
    min_price = prices[i]
  ans += min_price * lens[i]

print(ans)