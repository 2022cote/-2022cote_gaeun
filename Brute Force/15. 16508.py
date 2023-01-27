# 전공책 - https://www.acmicpc.net/problem/16508

"""
1. 조합을 이용해 가능한 모든 책의 조합을 combi 리스트에 저장한다. 이때, 책 이름 다 합친 문자열을 조합 맨 뒤에 저장.
(예시: ['ALGORITHM', 'NETWORK', 'ALGORITHMNETWORK'])
2. 각 조합 중, T에 해당하는 문자를 다 갖고있는 조합은(temp==4) arr 리스트에 저장한다.
(이때, 오려진 글자는 한 번만 사용 가능하므로, 조합[-1]에서 T의 각 문자를 갖고있는지 체크하면서, 갖고있다면 ''로 replace 이용하여 제거.)
3. arr를 돌며 T가 존재하는 책 조합의 가격 합들을 ans 리스트에 저장한다.
4. min(ans)를 출력한다. 이때, ans에 아무것도 없다면(=T 만들 수 없다면) -1 출력.
"""

from itertools import combinations

T = input()
N = int(input())
price = []
name = []
for _ in range(N):
  p, n = input().split()
  price.append(int(p))
  name.append(n)

combi = []  # 가능한 모든 책 조합
arr = []  # T가 존재하는 책 조합
ans = []  # T가 존재하는 책 조합의 가격 합들

for i in range(1, N + 1):
  for j in combinations(name, i):
    temp = list(j)
    temp.append(''.join(list(j)))  # 책 이름 다 합친 문자열을 맨 뒤에 저장
    combi.append(temp)

for i in range(len(combi)):
  temp = 0
  for j in range(len(T)):
    if T[j] in combi[i][-1]:
      replaced = combi[i][-1].replace(T[j],'',1)  # replace는 원본 변경 아닌, 할당해줘야 사용 가능.
      combi[i][-1] = replaced
      temp += 1
  if temp == len(T):
    arr.append(combi[i])

for i in arr:
  temp = 0
  for j in range(len(i) - 1):  # 마지막 string 제외
    temp += price[name.index(i[j])]
  ans.append(temp)

if ans:
  print(min(ans))
else:
  print(-1)
