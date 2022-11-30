import sys
input = sys.stdin.readline

meetings = []
n = int(input())
for _ in range(n):
  meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

cnt = 0
last = 0
for i,j in meetings:
  if i >= last:
    cnt += 1
    last = j
print(cnt)