"""
BOJ #11279 
최대 힙 (https://www.acmicpc.net/problem/11279)
"""

# 풀이(해설 찾아봄): 
# 파이썬 heapq (우선순위 큐) 모듈 사용. 파이썬의 리스트를 최소힙처럼 다룰 수 있도록 함.
# heappush(리스트, 값) / heappop(리스트) / heapify(리스트)
# heapq 모듈은 최소힙 자료구조만 제공. 따라서 최대힙 구현을 위해 heappush() 할때 값에 -1을 곱하고, heappop() 시에 다시 값에 -1을 곱해주었다.


import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
  x = int(sys.stdin.readline().rstrip())
  if x > 0:
    heapq.heappush(heap, (-1)*x)
  elif x == 0:
    if heap:
      print((-1)*heapq.heappop(heap))
    else:
      print(0)