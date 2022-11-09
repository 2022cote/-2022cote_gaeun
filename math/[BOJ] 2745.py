"""
BOJ #2745
진법 변환 (https://www.acmicpc.net/problem/2745)
"""

# 문제 접근: 
# N의 숫자를 하나씩 돌면서 실행
# 해당 자릿수가 문자라면(A:65 ~ Z:90), 아스키코드 -55 값으로 계산 수행
# -> 메모리 초과. ㅠㅠ (해결완료)

# 다른 풀이 찾아보니, 
# 하나의 문자열에 "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 로 넣어두고, 그 인덱스 값을 계산에 사용.

import sys
input = sys.stdin.readline

N, B = input().split()
B = int(B)
res = 0
string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1] # 순서 뒤집기

for i,n in enumerate(N):
  res += (string.index(n))*(B**i)
print(res)

"""
# N의 숫자를 하나씩 돌면서 실행
for i in reversed(range(len(N))): # for loop 순서 뒤집어 줘야 함!
  # 해당 자릿수가 문자라면(A:65 ~ Z:90), 아스키코드 -55 값으로 계산 수행
  if(N[i].isalpha()):
    num = ord(N[i]) - 55
    res += num*(B**i)
  else:
    res += N[i]*(B**i)

print(res)
"""

