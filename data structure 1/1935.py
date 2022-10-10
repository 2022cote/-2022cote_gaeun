"""
후위 표기식2
문제)
후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

입력)
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

출력)
계산 결과를 소숫점 둘째 자리까지 출력한다.
"""
#풀다가 막혀서 해설 참고했습니다. ㅠㅠ

import sys
from collections import deque

def input(): #입력을 표준입력으로, 한줄씩, 공백없애서 받기
  return sys.stdin.readline().strip()

num = deque() #피연산자 대응되는 입력값 담을 deque 생성. 넣은 순서대로 꺼내야하므로 큐 사용.
dic = {} #피연산자 담아둘 dic 생성. 각 알파벳에 해당하는 값 담아야하므로 딕셔너리 사용.
oper = '+-*/' #연산자
stack = [] #계산과정에서 계산값 담아둘 스택 list 생성.

N = int(input()) #피연산자의 개수 N 입력받기
exp = list(input()) #후위 표기식 입력받기
for i in range(N): #각 피연산자에 대응하는 값 입력받기
  num.append(int(input()))

for i in exp: #후위표기식 돌면서, 중복 아니면서 + 연산자 아닌 피연산자 값을 dic에 담기.
  if (i not in dic and i not in oper):
    dic[i] = num.popleft()

for i in exp: #후위표기식 돌면서,
  if i not in oper: #피연산자 알파벳에 해당하는 값을 딕셔너리에서 찾아 stack 리스트 뒷부분에 추가
    stack.append(dic[i]) 
  elif i == "+": #더하기+ 연산자 만나면, 스택 맨 뒤+맨뒤에서 바로 앞 값을 빼서 계산 후 stack 리스트 뒷부분에 추가
    stack.append(stack.pop() + stack.pop())
  elif i == "-":
    stack.append(stack.pop()*(-1) + stack.pop()) #pop 순서 주의!!!! 뒷값이 먼저 pop되므로, -1 곱하여 더하기로 구현.
  elif i == "*":
    stack.append(stack.pop() * stack.pop())
  elif i == "/":
    stack.append(stack.pop()**(-1) * stack.pop()) #pop 순서 주의!!!! 분모가 먼저 pop되어 꺼내지므로, 분모에 지수 -1제곱 해서 곱하기.

print("%.2f" %stack.pop()) #최종 계산값을 stack 리스트에서 꺼내, 소수점2자리 실수로 출력