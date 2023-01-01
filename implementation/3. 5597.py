# 과제 안 내신 분..? - https://www.acmicpc.net/problem/5597

# [false for _ in range 30] 만들고 입력받으면 true 로 바꿈. 그 후 앞에서부터 돌며 false인 값 출력.

import sys
input = sys.stdin.readline

students = [False for _ in range(30)]

for _ in range(28): # 30이 아니라 28임!
  students[int(input()) - 1] = True

for i in range(30):
  if students[i] == False:
    print(i+1)