# 큰 수 구성하기 - https://www.acmicpc.net/problem/18511

# 다른 풀이를 참고하여, 중복순열 product로 해결.
# 예제는 정답인데 채점 시 틀리는 경우 많았음. -> 예외처리를 잘 하자!

from itertools import product

N,len_K = map(int, input().split())
K = list(input().split())
K.sort(reverse=True)
len_N = len(str(N))
ans = 0

flag = 0
while not flag:
  prod = []  # 중복순열 product 이용해 K로 생성 가능한 모든 경우의수 저장
  for i in product(K, repeat=len_N):
    prod.append(int(''.join(i)))
  
  for i in prod:
    if i <= N:
      print(i)
      flag = 1
      break
  
  len_N -= 1