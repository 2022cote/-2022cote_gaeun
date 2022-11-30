"""
2로 나눠지면 /2,
안 나눠지면 -1 /10
"""
import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 0

while True:
  if b % 2 == 0:
    b /= 2
    cnt += 1
  elif (b - 1)%10 == 0:
    b = (b - 1)/10
    cnt += 1
  else:
    b = 0
  
  if a == b: break
  if a >= b:
    cnt = -2
    break

print(cnt+1)