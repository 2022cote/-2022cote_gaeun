# 치킨치킨치킨 - https://www.acmicpc.net/problem/16439

# 가능한 모든 치킨 3개 조합 만든 후(브루트포스), 각 조합마다 멤버별로 해당 조합 만족도의 max값을 만족도합에 더해주기. 만족도합 중 최대값을 출력.
# for문 순서 주의, 데이터타입 주의.

# 그리디로도 가능한가?

from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
members = []
for _ in range(N):
  members.append(list(map(int, input().split())))

total = 0  # 조합 별 멤버들의 만족도합
ans = 0  # 만족도합 중 최대값

permut = []  # 가능한 모든 치킨 3개 조합
for i in combinations([i for i in range(M)],3):
  permut.append(list(i))

for i in range(len(permut)):
  for j in members:
    total += max(j[permut[i][0]], j[permut[i][1]], j[permut[i][2]])
  ans = max(ans,total)
  total = 0
print(ans)