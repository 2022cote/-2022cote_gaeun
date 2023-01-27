# Four Squares - https://www.acmicpc.net/problem/17626

# 방법2. 브루트포스

import math
n = int(input())

if int(math.sqrt(n)) == math.sqrt(n):  # n이 제곱수인 경우
  print(1)
  exit()

for i in range(1,int(math.sqrt(n))+1):  # n이 2개의 제곱수로 표현되는 경우
  if int(math.sqrt(n - i**2)) == math.sqrt(n - i**2):
    print(2)
    exit()

for i in range(1,int(math.sqrt(n))+1):  # n이 3개의 제곱수로 표현되는 경우
  for j in range(1,int(math.sqrt(n - i**2))+1):
    if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
      print(3)
      exit()

print(4)  # 나머지