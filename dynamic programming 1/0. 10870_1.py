# 피보나치 수 5 - https://www.acmicpc.net/problem/10870

# 방법1. 탑다운(재귀)

n = int(input())

d = [0]*(n+1)  # 메모이제이션 위한 리스트

def fibo(i):
  if i == 0 or i == 1:  # 종료 조건
    return i
  if d[i] != 0:  # 이미 계산한 적 있다면 값 반환
    return d[i]
  d[i] = fibo(i-1) + fibo(i-2)  # 계산한 적 없다면 점화식으로 계산해 반환
  return d[i]                                          

print(fibo(n))