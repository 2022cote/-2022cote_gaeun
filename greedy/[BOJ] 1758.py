import sys
input = sys.stdin.readline

n = int(input())
total_tip = 0
line = []

for _ in range(n):
  line.append(int(input()))

line.sort(reverse=True)

for i in range(len(line)):
  tip = line[i] - i
  if tip > 0:
    total_tip += tip

print(total_tip)