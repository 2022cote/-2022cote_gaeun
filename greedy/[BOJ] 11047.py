import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = []
cnt = 0

for _ in range(n):
  coin = int(input())
  if coin <= k:
    coins.append(coin)

coins.sort(reverse=True)

for i in coins:
  cnt += k // i
  k %= i
print(cnt)