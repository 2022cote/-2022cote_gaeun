"""
BOJ #2960
에라토스테네스의 체 (https://www.acmicpc.net/problem/2960)
"""

# 풀이를 참고하였습니다.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = [True] * (n+1) # 방문 예정 arr 리스트 생성(0~n까지, 길이 n+1, 2~n만 사용). 아직 모두 방문되지 않은, 방문 예정 상태.
cnt = 0 # cnt번째 방문

for i in range(2, n+1): # 아직 지우지 않은 수 중 가장 작은 수 i
  for j in range(i, n+1, i): # 소수 i의 배수를 방문
    if arr[j] == True:
      arr[j] = False
      cnt += 1
      if cnt == k:
        print(j)
        break
