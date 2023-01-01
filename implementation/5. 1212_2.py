# 8진수 2진수 - https://www.acmicpc.net/problem/1212

import sys
input = sys.stdin.readline

eight_to_ten = int(input(),8)

def not_using_lib(n,q):
  reverse_base = ''
  while n > 0:
    n, mod = divmod(n, q)
    reverse_base += str(mod)
  return reverse_base[::-1]

print(not_using_lib(eight_to_ten,2))