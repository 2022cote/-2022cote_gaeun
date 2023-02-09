# 치킨 배달 - https://www.acmicpc.net/problem/15686

from itertools import combinations
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []  # 집들의 좌표
chickens = []  # 치킨집들의 좌표
ans = 9999

for i in range(N):
  for j in range(N):
    if city[i][j] == 1:
      houses.append([i,j])
    elif city[i][j] == 2:
      chickens.append([i,j])

for i in combinations(chickens, M):  # M개의 치킨집 선택
  city_chick_dist = 0
  for j in houses:
    house_chick_dist = 9999
    for k in i:
      house_chick_dist = min(abs(k[0]-j[0]) + abs(k[1]-j[1]), house_chick_dist)
    city_chick_dist += house_chick_dist
  ans = min(city_chick_dist, ans)

print(ans)