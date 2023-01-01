import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int,input().split())
a = list(map(int, input().split()))

max_len = 0
left,right = 0,0
cnt = defaultdict(int)

while right < n:
  if cnt[a[right]] < k:
    cnt[a[right]] += 1
    right += 1
  else:
    cnt[a[left]] -= 1
    left += 1
  max_len = max(max_len, right - left)

print(max_len)