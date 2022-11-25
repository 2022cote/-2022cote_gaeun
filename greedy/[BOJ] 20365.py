import sys
input = sys.stdin.readline

n = int(input())
colors = input().rstrip()

# 처음 색으로 일단 전체 칠하기
cnt = 1
first_color = colors[0]

for i in range(1, len(colors)):
  if colors[i] != first_color and colors[i] != colors[i-1]: # 색이 바뀌고, 처음 색도 아닌 경우
    cnt +=1
print(cnt)