import sys
input = sys.stdin.readline

exp = input().rstrip()
num = "0123456789"
numlist = []
oplist = []
res = 0
toggle = False

temp = ""
# 숫자, 문자 따로 리스트에 넣어두기
for i in exp:
  if i in num:
    temp += i
  else:
    oplist.append(i)
    numlist.append(int(temp))
    temp = ""
numlist.append(int(temp))
oplist.append('+')

temp = 0
for i in range(len(oplist)):
  if not toggle:
    res -= temp
    res += numlist[i]
  else:
    temp += numlist[i]
  if oplist[i] == '-':
    toggle = not toggle
res -= temp
print(res)