# 수학은 비대면강의입니다 - https://www.acmicpc.net/problem/19532
# 버추얼 광공 ...?

# 가감법 이용한 풀이_1 (브루트 포스 이용한 풀이_2)

a,b,c,d,e,f = list(map(int, input().split()))

if a == 0:
  y = c / b
  x = (f - e * y) / d
else:
  y = (c * d - f * a) / (b * d - e * a)
  x = (c - b * y) / a

print(int(x),int(y))