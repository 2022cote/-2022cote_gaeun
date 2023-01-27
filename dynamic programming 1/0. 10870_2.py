# 피보나치 수 5 - https://www.acmicpc.net/problem/10870

# 방법2. 바텀업(반복)
# 예외처리 확실히 해서 런타임에러 막기

n = int(input())

d = [0]*(n+1)  # dp테이블

if n > 0:  # 예외처리
  d[1] = 1
  for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])