# 8진수 2진수 - https://www.acmicpc.net/problem/1212

# n진수 => 10진수: int(num,n진수)
# 10진수 => n진수: bin(),oct(),hex()

import sys
input = sys.stdin.readline

print(bin(int(input(),8))[2:])