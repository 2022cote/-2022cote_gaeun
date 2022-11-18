"""
BOJ #21275
폰 호석만 (https://www.acmicpc.net/problem/21275)
"""

# str.isdigit() 는 주어진 문자열의 모든 문자가 숫자면 True, 문자가 포함되어 있으면 False를 반환하는 함수.
# Python 진법 변환: https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95
# 진법 변환 시 오류: https://yeko90.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98N%EC%A7%84%EC%88%98-10%EC%A7%84%EC%88%98-10%EC%A7%84%EC%88%98-N%EC%A7%84%EC%88%98

import sys
input = sys.stdin.readline

a,b = input().split()
print(type(a))

a2x = []

if a.isdigit():
  for i in range(2,36):
    a2x.append(int(a,i))