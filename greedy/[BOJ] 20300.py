import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
m = []

t.sort()

if n % 2 == 1:
  m.append(t.pop())

for i in range(n//2):
  m.append(t[i] + t[-(i+1)])

print(max(m))