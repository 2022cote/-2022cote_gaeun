import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))
P.sort(reverse=True)

ans = 0
for i in range(N):
  ans += (i+1) * P[i]
print(ans)