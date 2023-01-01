# 스위치 켜고 끄기 - https://www.acmicpc.net/problem/1244

import sys
input = sys.stdin.readline

N = int(input())
switches = [0] + list(map(int, input().split()))
num_students = int(input())

for _ in range(num_students):
  sex, switch = map(int, input().split())
  
  if sex == 1:
    for i in range(switch, N+1, switch):
      switches[i] = int(not switches[i])

  elif sex == 2:
    if (switch + 1 > N) or (switch - 1 < 1):
      switches[switch] = int(not switches[switch])
    else:
      if switches[switch + 1] == switches[switch - 1]:
        left = switch - 1
        right = switch + 1

        while True:
          if left - 1 < 1 or right + 1 > N:
            break
          if switches[left - 1] == switches[right + 1]:
            break
          else:
            left -= 1
            right += 1
        
        for i in range(left, right + 1):
          switches[i] = int(not switches[i])
      
      else:
        switches[switch] = int(not switches[switch])

for i in range(1, N, 20):
  print(*switches[i:i+20])