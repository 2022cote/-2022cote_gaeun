"""
BOJ #1620 
나는야 포켓몬 마스터 이다솜 (https://www.acmicpc.net/problem/1620)
"""

# 첫번째 풀이(시간초과): 
# 포켓몬을 리스트에 저장하고, 입력값이 숫자인 경우 index로 이름 검색, 숫자가 아닌 경우 이름으로 index 검색했다.
# 리스트에서의 탐색, index() 함수의 시간복잡도는 O(n). 10만개의 포켓몬들 중에서 찾을때는 최악의 경우 매번 10만번을 탐색한다. 10만x10만=100억. :(
"""
import sys
N, M = map(int, sys.stdin.readline().split()) 
#리스트에 포켓몬 저장
pocketmon = []
for i in range(N):
  pocketmon.append(sys.stdin.readline().rstrip())
for i in range(M):
  problem = sys.stdin.readline().rstrip() 
  if problem.isdigit(): 
    print(pocketmon[int(problem) - 1]) 
  else: 
    print(pocketmon.index(problem) + 1) 
"""

# 두번째 풀이(정답): 
# 해쉬 자료구조의 시간복잡도는 O(1). 파이썬의 hash 자료형인 딕셔너리 사용.

import sys

N, M = map(int, sys.stdin.readline().split()) 

#딕셔너리에 포켓몬 저장
pocketmon_int_key = {}
pocketmon_str_key = {}

for i in range(N):
  name = sys.stdin.readline().rstrip()
  pocketmon_int_key[i] = name
  pocketmon_str_key[name] = i
for i in range(M):
  problem = sys.stdin.readline().rstrip() 
  if problem.isdigit(): 
    print(pocketmon_int_key[int(problem) - 1]) 
  else: 
    print(pocketmon_str_key[problem] + 1) 