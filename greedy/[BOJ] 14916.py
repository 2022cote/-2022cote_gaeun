import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

if n == 1 or n == 3: # 거슬러 줄 수 없는 경우
  cnt = -1
else:
  cnt += n//5
  if (n%5) % 2 == 1:
    cnt -= 1
  cnt += (n - cnt*5)//2

print(cnt)