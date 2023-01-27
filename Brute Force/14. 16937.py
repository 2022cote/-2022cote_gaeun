# 두 스티커 - https://www.acmicpc.net/problem/16937

import sys
input = sys.stdin.readline

H,W = map(int, input().split())
N = int(input())
rc = [list(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(len(rc)):
  for j in range(i+1,len(rc)):
    if rc[i][0] + rc[j][0] <= H and max(rc[i][1], rc[j][1]) <= W:  # 위아래로 나란히 붙이기
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])
    if rc[i][1] + rc[j][1] <= W and max(rc[i][0], rc[j][0]) <= H:  # 옆으로 나란히 붙이기
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])

    # 첫번째 스티커 90도 회전
    if rc[i][1] + rc[j][0] <= H and max(rc[i][0], rc[j][1]) <= W:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])
    if rc[i][0] + rc[j][1] <= W and max(rc[i][1], rc[j][0]) <= H:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])

    # 두번째 스티커 90도 회전
    if rc[i][0] + rc[j][1] <= H and max(rc[i][1], rc[j][0]) <= W:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])
    if rc[i][1] + rc[j][0] <= W and max(rc[i][0], rc[j][1]) <= H:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])

    # 둘 다 90도 회전
    if rc[i][0] + rc[j][0] <= W and max(rc[i][1], rc[j][1]) <= H:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])
    if rc[i][1] + rc[j][1] <= H and max(rc[i][0], rc[j][0]) <= W:
      ans = max(ans, rc[i][0]*rc[i][1] + rc[j][0]*rc[j][1])    

print(ans)