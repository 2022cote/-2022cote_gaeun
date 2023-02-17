# 탑 - https://www.acmicpc.net/problem/2493

# 방법1. N이 최대 500,000이므로 브루트포스 O(N^2)은 불가.
# 방법2. 스택 이용
# stack은 수신 가능한 탑의 (인덱스,높이) 쌍.
# stack에 값이 있으면 stack[-1] 을 ans에 추가. 없으면 0 추가. => 큰
# 탑 순서대로 돌면서 stack[-1] 이 더 높으면 stack[-1] 을 ans에 추가, 본인 push.
# 낮으면 본인보다 높은 값 나올때까지 pop. 높은 값 나오면 본인 push. 높이 내림차순으로 들어가게 됨

"""
import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
heights = heights[::-1]
heard = [0] * N # 수신한 탑들의 인덱스 번호(1부터 시작)

for i in range(N):
  for j in range(i+1,N):
    if heights[i] < heights[j]:
      heard[i] = N - j
      break
print(heard[::-1])
"""

import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

stack = [] # 수신 가능한 탑의 (인덱스,높이) 쌍
ans = [] # 수신한 탑들의 인덱스 번호

for i in range(N):
  while stack: # 수신 가능한 탑 있을때,
    if stack[-1][1] > heights[i]: # stack[-1] 이 더 높으면 stack[-1] 을 ans에 추가
      ans.append(stack[-1][0]+1)
      break
    else: # 본인보다 높은 값 나올때까지 pop
      stack.pop()

  if not stack: # 수신 가능한 탑 없을때,
    ans.append(0)

  stack.append([i,heights[i]]) # 어떤 경우든 항상 마지막에 본인 push.

print(*ans)