# 블랙잭 - https://www.acmicpc.net/problem/2798

# 앞부터 일일이 3개합을 구해가며 풀이(브루트포스)

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0

for i in range(N):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      _sum = cards[i] + cards[j] + cards[k]
      if _sum <= M and _sum > ans:  # 3개 합이 M 이하이고, 이제껏 합 중 최대이면 ans값 대체.
        ans = _sum

print(ans)