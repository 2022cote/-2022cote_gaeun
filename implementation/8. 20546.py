# 🐜 기적의 매매법 🐜 - https://www.acmicpc.net/problem/20546

import sys
input = sys.stdin.readline

money = int(input())
stocks = list(map(int, input().split()))

def bnp(money, stocks):
  left_money = money
  num_stocks = 0
  for i in stocks:
    num_stocks += left_money // i
    left_money = left_money % i
    if left_money == 0:
      break
  return left_money + num_stocks * stocks[-1]

def timing(money, stocks):
  left_money = money
  num_stocks = 0
  for i in range(len(stocks)-4):
    if stocks[i] < stocks[i+1] < stocks[i+2] < stocks[i+3]:
      left_money += num_stocks * stocks[i+3]
      num_stocks = 0
    if stocks[i] > stocks[i+1] > stocks[i+2] > stocks[i+3]:
      num_stocks += left_money // stocks[i+3]
      left_money = left_money % stocks[i+3]
  return left_money + num_stocks * stocks[-1]

jun_total = bnp(money, stocks)
sung_total = timing(money, stocks)

if jun_total > sung_total:
  print('BNP')
elif jun_total < sung_total:
  print('TIMING')
else:
  print('SAMESAME')