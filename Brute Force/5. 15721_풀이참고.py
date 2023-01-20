# 번데기 - https://www.acmicpc.net/problem/15721

A = int(input())
T = int(input())
word = int(input())

bundegi = []
bun = degi = 1
turn = 0

while True:
  prev_turn = bun
  turn += 1

  for _ in range(2):
    bundegi.append((bun,0))
    bundegi.append((degi,1))
    bun += 1
    degi += 1
  for _ in range(turn+1):
    bundegi.append((bun,0))
    bun += 1
  for _ in range(turn+1):
    bundegi.append((degi,1))
    degi += 1

  if prev_turn < T <= bun:
    print(bundegi.index((T,word)) % A)
    break