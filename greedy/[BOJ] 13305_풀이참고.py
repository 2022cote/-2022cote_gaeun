import sys
input = sys.stdin.readline

n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = costs[0]
sum = 0

for i in range(0, n-1):
  if costs[i] < min_cost:
    min_cost = costs[i]
  sum += distances[i] * min_cost

print(sum)

# for i in range(1, costs):
#   if costs[i] <= costs[i-1]:
#     sum += distances[i] * costs[i]
#   else:
#     sum += distances[i] * costs[i-1]


# for i in range(cost.index(min(cost)),len(cost)):
#   sum += distances[i]
# print(sum * min(cost))