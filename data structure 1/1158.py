"""
문제)
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력)
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력)
예제와 같이 요세푸스 순열을 출력한다.
"""
import sys
from collections import deque #FIFO 구조 구현 위해 큐 사용

N, K = map(int, sys.stdin.readline().split()) #split으로 공백,줄바꿈 제거 + map함수 사용해서 str->int 변환

dq = deque() #deque 생성
_list = [] #요세푸스 순열 담을 list 생성

for i in range(N): #dq = [1,2,...N] 생성
  dq.append(i+1)

while dq: #dq에 값이 있는 한 반복
  dq.rotate(-K) #dq 안의 값들 뒤에서 앞으로, K만큼 회전
  _list.append(dq.pop()) #회전에서 맨 뒤로 간 값을 dq에서 pop하고, _list에 넣어줌

print("<" + ", ".join(map(str,_list)) + ">") #요세푸스 순열 출력
#출력 형식 <int,int,int> 을 맞추기 위해
#문자열 합쳐주는 join 함수를 이용하기 위해, map함수를 이용해 리스트 안 int->str 변환.