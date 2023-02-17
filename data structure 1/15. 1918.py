# 후위 표기식 - https://www.acmicpc.net/problem/1918

"""
1. () 를 확인한다.
2. * /인지를 확인하고 먼저 들어온, 같은 우선순위에 있는 * / 는 모두 결과문자열에 추가해준다.
3. 그리고 현재 문자를 다시 스택에 추가
4. +, - 인지 확인한다. + ,- 는 이들보다 낮은 우선순위의 연산자가 없으므로 자신보다 우선순위가 높은 것들을 모두 결과 문자열에 추가해준다.
5. ) 를 발견하면 ( 와 ) 사이에 있는 모든 연산자들을 결과문자열에 추가하고 (를 pop해준다.
6. 마지막으로 남아있는 stack을 pop하며 결과문자열에 추가.
"""

import sys
input = sys.stdin.readline

equation = list(input().rstrip())
ans = ''
stack = []

for i in equation:
  if i.isalpha():
    ans += i
  else:
    if i == '(':
      stack.append(i)
    elif i == '*' or i == '/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        ans += stack.pop()
      stack.append(i)
    elif i == '+' or i == '-':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.append(i)
    elif i == ')':
      while stack and stack[-1] != '(':
        ans += stack.pop()
      stack.pop()
while stack:
  ans += stack.pop()

print(ans)