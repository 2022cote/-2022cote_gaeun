# Four Squares - https://www.acmicpc.net/problem/17626

# 방법1. dp => 시간초과. ㅠㅠ
# 점화식: 
# a(i) = 합이 i과 같게 되는 제곱수들의 최소 개수
# 각 num마다, a(i) = min(a(i), a(i-num**2)+1)

n = int(input())

d = [50001] * (n+1)
d[0] = 0

for i in range(1,int(n**(1/2))+1):
  for j in range(i,n+1):
    d[j] = min(d[j], d[j-i**2]+1)

print(d[n])