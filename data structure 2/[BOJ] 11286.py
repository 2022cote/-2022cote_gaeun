"""
BOJ #11286
절댓값 힙 (https://www.acmicpc.net/problem/11286)
"""

# 풀이(해설 찾아봄):
# 절댓값 부분 어떻게 해결할 지 모르겠어서 풀이 찾아봤습니다. ㅠㅠ
# (절대값, 원래 입력값) 쌍의 튜플 형태로 heapq에 넣는 것으로 해결. -> 힙큐는 절대값 기준으로 정렬됨.


import sys
import heapq

N = int(input())
heap = []

for i in range(N):
  x = int(sys.stdin.readline().rstrip())
  if x != 0:
    heapq.heappush(heap, (abs(x), x) )
  else:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap)[1])