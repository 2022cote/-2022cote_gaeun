import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
total = 0

p.sort(reverse=True)

for i in range(len(p)):
  total += p[i] * (i+1)
print(total)