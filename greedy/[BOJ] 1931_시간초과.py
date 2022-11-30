"""
매번 가능한 것들 중, 끝나는 시간 제일 빠른 것 찾기.

딕셔너리에서 끝나는 시간 제일 빠른 것 찾고,
그거보다 시작시간 빠른 것들 지움.
cnt += 1.

"""
import sys
input = sys.stdin.readline

n = int(input())
meetings = {}
for i in range(n):
  start, end = list(map(int, input().split()))
  if start in meetings.keys():
    meetings[start].append(end)
  else:
    meetings[start] = [end]

end_point = max(meetings.values())[0]

cnt = 0
end_time = 0
while True:
  cnt += 1
  end_time = min(meetings.values())[0]
  if end_time == end_point:
    break
  for key in meetings.keys():
    if key < end_time:
      meetings[key] = [end_point + 1] # 타입 에러 주의

print(cnt)