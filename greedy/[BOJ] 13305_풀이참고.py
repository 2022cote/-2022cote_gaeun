import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
total = 0

for i in range(n-1):
  if costs[i] <= min_cost:
    min_cost = costs[i]
  total += distances[i] * min_cost

print(total)