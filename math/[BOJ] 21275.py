"""
BOJ #21275
폰 호석만 (https://www.acmicpc.net/problem/21275)
"""

# str.isdigit() 는 주어진 문자열의 모든 문자가 숫자면 True, 문자가 포함되어 있으면 False를 반환하는 함수.
# Python 진법 변환: https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# 진법 변환 시 오류: https://yeko90.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98N%EC%A7%84%EC%88%98-10%EC%A7%84%EC%88%98-10%EC%A7%84%EC%88%98-N%EC%A7%84%EC%88%98
# 리스트 교집합 찾기: https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B9%84%EA%B5%90-%EA%B0%99%EC%9D%80%EA%B0%92-%EB%8B%A4%EB%A5%B8%EA%B0%92set%EC%9E%90%EB%A3%8C%ED%98%95%ED%95%A9%EC%A7%91%ED%95%A9%EA%B5%90%EC%A7%91%ED%95%A9%EC%B0%A8%EC%A7%91%ED%95%A9

import sys
from collections import defaultdict
input = sys.stdin.readline

a,b = input().split()

num = '0123456789abcdefghijklmnopqrstuvwxyz'
a2x = defaultdict(list)
b2x = defaultdict(list)

for i in range(num.index(max(a)), 37):
  if i != 1:
    a2x[int(a,i)].append(i)
for i in range(num.index(max(b))+1, 37):
  if i != 1:
    b2x[int(b,i)].append(i)

xlst = set(a2x.keys()) & set(b2x.keys())

for i in xlst:
  if len(a2x[i]) > 1 or len(b2x[i]) > 1:
    print("Multiple")
  elif not len(xlst) or a2x[i] == b2x[i]:
    print("Impossible")
  else:
    print(i, *a2x[i], *b2x[i], end=" ")