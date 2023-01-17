# DNA - https://www.acmicpc.net/problem/1969

# 각 자리에서 가장 많은 뉴클레오타이드를 택한다.

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
dna = []
for _ in range(N):
  dna.append(input().rstrip())

ans = [[] for _ in range(M)]  # 각 자리에서 가장 많은 뉴클레오타이드 저장
cnt = {'A':0,'C':0,'G':0,'T':0}  # 각 자리 별 뉴클레오타이드 count 하는 딕셔너리
hd = 0  # Hamming Distance

for i in range(M):
  for j in dna:
    cnt[j[i]] += 1
  for k,v in cnt.items():
    if v == max(cnt.values()):
      ans[i].append(k)
  hd += sum(cnt.values()) - max(cnt.values())
  cnt = {'A':0,'C':0,'G':0,'T':0}

for i in range(M):
  print(min(ans[i]), end='')
print()
print(hd)