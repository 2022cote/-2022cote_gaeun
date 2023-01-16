# 수학은 비대면강의입니다 - https://www.acmicpc.net/problem/19532

# (x,y) 쌍 모두 비교하며 구하기 (브루트포스)
# for문 두번 도는데, 시간복잡도

a,b,c,d,e,f = list(map(int, input().split()))

for i in range(-999,1000):
  for j in range(-999,1000):
    if a*i + b*j == c and d*i + e*j == f:
      print(i,j)
      exit()