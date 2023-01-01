import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = []

a_pointer = 0
b_pointer = 0
a_len = len(a)
b_len = len(b)

while a_pointer != a_len or b_pointer != b_len:
  if a_pointer == a_len:
    arr.append(b[b_pointer])
    b_pointer += 1
  elif b_pointer == b_len:
    arr.append(a[a_pointer])
    a_pointer += 1
  else:
    if a[a_pointer] < b[b_pointer]:
      arr.append(a[a_pointer])
      a_pointer += 1
    else:
      arr.append(b[b_pointer])
      b_pointer += 1

print(*arr)