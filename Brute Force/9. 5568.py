# 카드 놓기 - https://www.acmicpc.net/problem/5568

# 순열 permutations 이용하여 구현, 중복되는 것은 제외하고 nums 리스트에 담기.

from itertools import permutations

n = int(input())
k = int(input())
cards = []
for _ in range(n):
  cards.append(input().rstrip())

nums = []

for i in permutations(cards,k):
  if ''.join(i) not in nums:
    nums.append(''.join(i))
print(len(nums))