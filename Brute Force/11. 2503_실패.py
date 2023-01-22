# 숫자 야구 - https://www.acmicpc.net/problem/2503

# 예제정답인데 제출 시 틀림. 이유를 모르겠음. ㅠㅠ

# 모든 가능한 세자리 수를 돌면서, 해당 수와 매 입력값의 스트라이크&볼수가 일치하는지 체크. 모든 입력값과 일치한다면 해당 수를 ans 리스트에 추가.

from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
qna = []
for _ in range(N):
  qna.append(list(map(int, input().split())))

nums = list(permutations([i for i in range(1,10)],3))  # 모든 가능한 세자리 수

ans = []

for i in nums:
  flag = 0
  for j in qna:
    strike = ball = 0

    for k in range(3):
      if str(i[k]) == str(j[0])[k]:  # 데이터타입 바꿔주는 것 주의하기!
        strike += 1
      elif str(i[k]) in str(j[0]):
        ball += 1

    if strike == j[1] and ball == j[2]:
      flag += 1
  if flag == 4:
    ans.append(i)

print(len(ans))