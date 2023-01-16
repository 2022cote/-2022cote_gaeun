# 시각 - https://www.acmicpc.net/problem/18312

# 시,분,초를 돌면서 상위단위에서 3이 들어가면 하위단위들 모두 cnt에 더함.

N,K = list(map(int, input().split()))
cnt = 0

for i in range(N+1):
  if i//10 == K or i%10 == K:
    cnt += 3600
    continue
  else:
    for j in range(60):
      if j//10 == K or j%10 == K:
        cnt += 60
        continue
      else:
        for k in range(60):
          if k//10 == K or k%10 == K:
            cnt += 1

print(cnt)