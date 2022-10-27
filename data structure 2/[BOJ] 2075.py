"""
BOJ #2075
N번째 큰 수 (https://www.acmicpc.net/problem/2075)
"""

# 첫번째 풀이(실패): 
# 배열에 값을 하나씩 넣은 후 정렬해 값을 출력하려고 했다. 
# -> 메모리 초과

# 두번째 풀이(해설 찾아보고 구현): 
# 파이썬 heapq 모듈, 우선순위 큐 이용.
# 우선 한 줄만 입력받아 리스트(lst)에 저장한 후, 해당 리스트를 오름차순 정렬
# 다음줄부터는 입력값이 lst의 최솟값보다 크면 최소값 heappop 후, 입력값을 heappush.
# 반복문 마친 후, 큐의 index 0번째 값 출력. (N번째로 큰 수)

import sys
import heapq

N = int(input())

lst = list(map(int, sys.stdin.readline().split())) 
lst.sort()

for i in range(N-1):
  newlst = list(map(int, sys.stdin.readline().split()))
  for j in newlst:
    if lst[0] < j:
      heapq.heappop(lst)
      heapq.heappush(lst,j)  

print(lst[0])