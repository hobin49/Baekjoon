import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []
for i in range(n):
    answer.append(list(map(int, input().split())))


dp = [[0] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        dp[a][b] = dp[a][b - 1] + dp[a - 1][b] - dp[a - 1][b - 1] + answer[a - 1][b - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
