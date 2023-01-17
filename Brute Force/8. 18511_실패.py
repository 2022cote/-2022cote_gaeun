# 큰 수 구성하기 - https://www.acmicpc.net/problem/18511

# 예제는 정답인데 채점 시 틀림.

# N의 큰자리부터 비교하면서, K 중 같은 값이 나오면 해당 값 선택 후 다음으로 넘어가기 반복. 그러다 같지 않은 값 나오면 K 중 그 미만인 값 선택 후 나머지 모두 최대값으로 넣음.

N,num_K = input().split()
K = list(map(int, input().split()))
K.sort(reverse=True)

ans = []
flag = 1
i = 0
while flag and i < len(N):
  for j in K:
    if int(N[i]) < K[-1]:
      ans = [K[0] for _ in range(len(N) - 1)]
      flag = 0
      break
    else:
      if j < int(N[i]):
        ans.append(j)
        ans += [K[0] for _ in range(len(N) - i - 1)]
        flag = 0
        break
      elif j == int(N[i]):
        ans.append(j)
        break
  i += 1

for i in range(len(ans)):
  print(ans[i], end='')