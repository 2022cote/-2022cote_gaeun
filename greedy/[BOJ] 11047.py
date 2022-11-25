import sys
input = sys.stdin.readline

n,k = map(int, input().split())
a = []
cnt = 0
for _ in range(n):
  a.append(int(input())) # 몫이 어차피 0 나오니까 입력값 걸러줄 필요 없음!

a.sort(reverse=True)

for i in a:
  cnt += k//i
  k %= i
print(cnt)