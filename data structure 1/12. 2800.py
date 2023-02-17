# 괄호 제거 - https://www.acmicpc.net/problem/2800

# '('와 ')'의 위치를 쌍으로 저장해두고, 조합으로 뽑아서 해당 값은 ''로 replace

from itertools import combinations
import sys
input = sys.stdin.readline

temp = [i for i in input().rstrip()]
left = []
pairs = []
ans = []

for i in range(len(temp)):
  if temp[i] == '(':
    left.append(i)
  elif temp[i] == ')':
    pairs.append([left.pop(), i]) # [3,5]

for i in range(1,len(pairs)+1):
  comb = combinations(pairs,i)
  for j in comb: # ([3, 5], [0, 6])
    target = temp.copy() # 얕은복사 주의!
    for k in j:
      target[k[0]] = ''
      target[k[1]] = ''
    ans.append(''.join(target))

ans = set(ans) # 중복되는 값 제거 - list 대신 set 적용

for i in sorted(ans):
  print(i)