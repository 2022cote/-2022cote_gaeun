# 회의실 배정 - https://www.acmicpc.net/problem/1931
# 정렬 -> 1. 종료시간의 오름차순 2. 시작시간의 오름차순

import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key=lambda x: (x[1],x[0]))
# meetings.sort(key=lambda x: x[0])  # 또 다른 방법
# meetings.sort(key=lambda x: x[1])

ans = 0
end = 0

for i,j in meetings:
  if i >= end:
    end = j
    ans += 1
print(ans)