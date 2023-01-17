# 분해합 - https://www.acmicpc.net/problem/2231

# 0부터 N까지 모든 수를 돌며 생성자 있는지 찾는다(브루트포스)

N = int(input())

for i in range(N):
  nums = []  # 생성자의 각 자리수 기록하는 리스트
  _len = len(str(i))
  while _len:
    nums.append(str(i//10**(_len-1))[-1])
    _len -= 1
  
  generator = int(''.join(nums))
  nums = map(int, nums)
  if sum(nums) + generator == N:
    print(generator)
    exit() 

print(0)  # 예외처리