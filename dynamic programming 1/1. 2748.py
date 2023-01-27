# 피보나치 수 2 - https://www.acmicpc.net/problem/2748
# 0. 10870.py와 같은 문제

n = int(input())

d = [0]*(n+1)

if n < 2:  # 예외처리
  print(n)
else:
  d[0] = 0
  d[1] = 1
  for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]

  print(d[n])