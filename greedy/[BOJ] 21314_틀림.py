"""
가장 큰 수: 최대한 큰 덩어리
-> 끝자리 k 기준으로 끊기.
가장 작은 수: 최대한 작은 덩어리
-> k 나오면 그 앞에서 끊기.
"""
import sys
input = sys.stdin.readline

num = input().rstrip()

def result(num):
  arr = num.split('/')
  res = ''
  for i in arr:
    if len(i) > 0:
      temp = 10**(len(i)-1)
      if i[-1] == 'K':
        temp *= 5
      res += str(temp)
  return res

max_num = num.replace('K','K/')
min_num = num.replace('K','/K/')

print(result(max_num))
print(result(min_num))