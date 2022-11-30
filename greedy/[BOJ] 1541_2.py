import sys
input = sys.stdin.readline

exp = input().split('-')

arr = []

for i in exp:
  temp = 0
  templist = i.split('+')
  for j in templist:
    temp += int(j)
  arr.append(temp)

res = arr[0]
for i in range(1,len(arr)):
  res -= arr[i]
print(res)