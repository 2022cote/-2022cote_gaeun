# 퇴사 - https://www.acmicpc.net/problem/14501

# 풀이참고: https://pacific-ocean.tistory.com/199

import sys
input = sys.stdin.readline

N = int(input())
TP = [list(map(int,input().split())) for _ in range(N)]

d = [0] * (N+1)

# dp 거꾸로 채운다. (N-1,...,0)
for i in range(N-1,-1,-1):
  if i + TP[i][0] > N:  # 상담에 필요한 일수가 퇴사일을 넘어가면, 전날 d값 가져옴.
    d[i] = d[i+1]
  else:
    # max(오늘 상담x => 전날 d값, 오늘 상담o => d[i+t[i]] + p[i])
    d[i] = max(d[i+1], d[i+TP[i][0]] + TP[i][1])

print(d[0])