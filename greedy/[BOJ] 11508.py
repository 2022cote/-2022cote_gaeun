import sys
input = sys.stdin.readline

n = int(input())
c = []
cost = 0

for _ in range(n):
  c.append(int(input()))

c.sort(reverse=True)

for i in range(2,n,3):
  c[i] = 0

for i in c:
  cost += i
print(cost)