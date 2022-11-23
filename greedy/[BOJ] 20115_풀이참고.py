# 시간초과되어 풀이 참고 후 수정

import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)

sum = drinks[0]

for i in range(1, len(drinks)):
  sum += drinks[i]/2
print(sum)