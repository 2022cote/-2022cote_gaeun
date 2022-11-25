import sys
input = sys.stdin.readline

n = int(input())
w = 0
ropes = []

for _ in range(n):
  ropes.append(int(input()))
  
ropes.sort()

for k in range(1, n+1):
  w = max(w, k * ropes[-k])
print(w)