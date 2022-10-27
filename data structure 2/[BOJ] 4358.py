"""
BOJ #4358
생태학 (https://www.acmicpc.net/problem/4358)
"""

# 풀이: 
# 나무이름과 나무개수 쌍으로 기록하기 위해 딕셔너리 사용.

# 파이썬 소수점 자리수 제한 방법 3가지: https://blockdmask.tistory.com/534

import sys

trees = {}
num = 0 #전체 나무 개수

while True:
  tree = sys.stdin.readline().rstrip()
  if not tree: #입력값 없는경우 while문 break
    break
  if tree not in trees: #처음 입력받는 나무종은 딕셔너리 value를 0으로 초기화해 추가한 후 value +1
    trees[tree] = 0
  trees[tree] += 1
  num += 1 

strees = dict(sorted(trees.items())) #딕셔너리 key값 이용한 정렬 (결과값이 list) -> 딕셔너리로 다시 바꿈

for k,v in strees.items():
  print(k + ' ' + str("{:.4f}".format(100*v/num)))