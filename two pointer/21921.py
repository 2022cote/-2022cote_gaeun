import sys
input = sys.stdin.readline

n,x = map(int,input().split())
visits = list(map(int,input().split()))

cnt = 0
end = 0
_sum = 0
max_visit = 0
period = 0

for i in range(n):
  while cnt < x and end < n:
    cnt += 1
    _sum += visits[end]
    end += 1
  if cnt == x:
    if max_visit == _sum:
      period += 1
    elif max_visit < _sum:
      max_visit = _sum
      period = 1
  _sum -= visits[i]
  cnt -= 1

if max_visit:
  print(max_visit)
  print(period)
else:
  print('SAD')