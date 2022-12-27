import sys

input = sys.stdin.readline


n, m = map(int, input().split())

lecture = list(map(int, input().split()))


left = 0
right = len(lecture)


# 최소 크기 후보 = 15
mid = left + right // 2

standard = sum(lecture) // m

# 레슨 길이의 합이 mid 보다 작도록 나누면
group = []
s = 0
for i in range(n - 1):
    s += lecture[i]
    if s + lecture[i + 1] >= standard:
        group.append(s)
        s = 0

# 그룹의 수가 > 블루레이 m 보다 크면
if len(group) > m:
    left = mid + 1
else:
    right = mid - 1
