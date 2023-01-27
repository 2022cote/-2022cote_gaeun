# 2×n 타일링 - https://www.acmicpc.net/problem/11726

# 점화식: a(i) = a(i-1) + a(i-2)
# d[1] = 1, d[2] = 2 

# 예외처리 확실히 해서 런타임 에러 막기!

n = int(input())

d = [0]*(n+1)  # dp 테이블

if n < 3:  # 예외처리
  print(n)
else:
  d[1] = 1
  d[2] = 2

  for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

  print(d[n] % 10007)