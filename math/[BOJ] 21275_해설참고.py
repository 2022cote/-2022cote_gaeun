"""
BOJ #21275
폰 호석만 (https://www.acmicpc.net/problem/21275)
"""

import sys
input = sys.stdin.readline

a,b = input().split()
cnt = 0

for i in range(2, 37):
  try: 
    a_temp = int(a,i)
  except: 
    continue

  for j in range(2, 37):
    try: 
      b_temp = int(b,j)

      if a_temp == b_temp:
        x = a_temp
        a = i
        b = j
        cnt += 1
    except: continue

if x == 0: cnt += 1

if cnt == 1:
  print(x, a, b)
elif cnt > 1:
  print("Multiple")
else:
  print("Impossible")
