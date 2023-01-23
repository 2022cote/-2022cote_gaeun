# 1로 만들기 - https://www.acmicpc.net/problem/1463

# 점화식: a(i) = min(a(i-1),a(i/2),a(i/3)) + 1

N = int(input())

d = [0]*(N+1)  # dq 테이블

# dq 진행 (bottom-up)
for i in range(2,N+1):
  # 현재의 수에서 1 빼는 경우
  d[i] = d[i-1]+1
  # 현재의 수가 2로 나누어 떨어지는 경우
  if i%2 == 0:
    d[i] = min(d[i],d[i//2]+1)
  # 현재의 수가 3로 나누어 떨어지는 경우
  if i%3 == 0:
    d[i] = min(d[i],d[i//3]+1)

print(d[N])