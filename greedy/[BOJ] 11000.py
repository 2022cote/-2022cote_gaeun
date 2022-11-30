import sys
input = sys.stdin.readline

classes = []
n = int(input())
for _ in range(n):
  classes.append(list(map(int, input().split())))

classes.sort(key=lambda x: x[0])
classes.sort(key=lambda x: x[1])

cnt = 1
last = classes[0][1]
for i,j in classes:
  if i == last:
    cnt += 1
    last = j
  elif i > last:
    last = j
print(cnt)