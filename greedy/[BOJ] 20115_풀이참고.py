import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)

total = drinks[0]

del drinks[0]
total += sum(drinks) / 2

# for i in range(1, len(drinks)):
#   total += drinks[i]/2
print(total)