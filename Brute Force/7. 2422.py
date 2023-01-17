# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 - https://www.acmicpc.net/problem/2422
 
# 앞에서부터 가능한 모든 3개 조합을 보며 (브루트포스) combination에 없는 조합이면 cnt+=1

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
combination = [[] for _ in range(N+1)]  # 섞으면 안 되는 조합을 이중리스트로 저장.
for _ in range(M):
  a,b = map(int, input().split())
  combination[a].append(b)
  combination[b].append(a)

cnt = 0

for i in range(1,N+1):
  for j in range(i+1,N+1):
    for k in range(j+1,N+1):
      if j in combination[i] or k in combination[i] or k in combination[j]:
        continue
      else:
        cnt += 1
print(cnt)