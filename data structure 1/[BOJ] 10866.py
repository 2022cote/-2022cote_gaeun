"""
덱
문제)
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

입력)
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력)
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

import sys
from collections import deque

dq = deque() #dq 덱 생성

N = int(input()) #주어지는 명령의 수 N 입력받기

for i in range(N):
  data = sys.stdin.readline().strip().split() #명령마다 한줄씩, 문자열 입력받고, split해서 data에 담기. index 0은 문자, 1는 숫자(push인 경우만 있음)
  length = len(dq) #dq 길이 미리 구해두기

  if data[0] == "push_front":
    dq.appendleft(data[1])
  elif data[0] == "push_back":
    dq.append(data[1])
  elif data[0] == "pop_front":
    if length:
      print(dq.popleft())
    else:
      print(-1)
  elif data[0] == "pop_back":
    if length:
      print(dq.pop())
    else:
      print(-1)
  elif data[0] == "size":
    print(length)
  elif data[0] == "empty":
    if length:
      print(0)
    else:
      print(1)
  elif data[0] == "front":
    if length:
      print(dq[0])
    else:
      print(-1)
  elif data[0] == "back":
    if length:
      print(dq[-1])
    else:
      print(-1)