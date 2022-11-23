import sys
input = sys.stdin.readline

n = int(input())
problems = input().rstrip()
cnt = 1

current = problems[0] # 현재 색깔

for i in range(1, len(problems)):
  if problems[i] == current: # 현재 색깔과 직전 색깔이 같은 경우 pass
    pass
  else: # 현재 색깔과 직전 색깔이 다른 경우    
    if problems[i] != problems[0]: # 현재 색깔이 처음 색깔과 다르면 cnt+=1
      cnt += 1
    current = problems[i] # 현재 색깔 update
print(cnt)