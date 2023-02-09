# 제곱수 찾기 - https://www.acmicpc.net/problem/1025

# 예제는 모두 정답인데, bj 채점 시 틀렸다고 뜸. ㅠㅠ 

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
table = [input().rstrip() for _ in range(N)]

nums = []

def is_square(num):  # 완전제곱수 판별 함수
  return int(num**(1/2))**2 == num

for i in range(N):  # 시작 행 지점
  for j in range(M):  # 시작 열 지점
    for gap_n in range(-N+1,N):  # 행 등차
      for gap_m in range(-M+1,M):  # 열 등차
        number = ''
        row = i
        col = j
        if gap_n == 0 and gap_m == 0:  # 등차가 0,0인 경우 무한루프 방지
          continue
        while 0 <= row < N and 0 <= col < M:  # 표 벗어나지 않는 범위에서 진행
          number += table[row][col]
          row += gap_n
          col += gap_m
          if is_square(int(number)):   # 서로 다른 1개 이상의 칸을 선택하는 것이므로, while문 안에 들어가는 것!! (틀린 이유)
            nums.append(int(number))
nums.sort()
if nums:
  print(nums[-1])
else:
  print(-1)