import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 0

while True:
  cnt += 1
  temp = b
  if b % 10 == 1:
    b //= 10
  elif b % 2 == 0:
    b //= 2
  
  if temp == b: # 무한루프
    print(-1)
    break
  elif b == a: # 종료
    print(cnt + 1)
    break