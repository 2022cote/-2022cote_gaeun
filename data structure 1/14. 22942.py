# 데이터 체커 - https://www.acmicpc.net/problem/22942

# 방법1. N의 최대가 200,000 이므로 원 두개를 뽑는 방법 O(N^2) 은 불가.
# 방법2. 스택 이용. 
# 시작점,끝점을 나누어 저장한 후, sort. 
# 앞에서부터 left면 스택에 계속 저장하다가, right 값이 나오면 stack.pop()과 같은 원인지 비교. 같지 않다면 겹친 것이므로 ans = 'NO'.

from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
circles = []
for i in range(N):
  x,r = map(int, input().split())
  circles.append([x-r,i,'left'])
  circles.append([x+r,i,'right'])

circles.sort()
stack = []
ans = 'YES'

for i in circles:
  if i[2] == 'left':
    stack.append(i)
  else:
    if stack.pop()[1] != i[1]:
      ans = 'NO'
      break

print(ans)