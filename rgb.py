n = int(input())
dp = [[0] * 3 for _ in range(n)]
color = []
for _ in range(n):
    color.append(list(map(int, input().split())))

dp[0][0], dp[0][1], dp[0][2] = color[0][0], color[0][1], color[0][2]

for i in range(1, n):
    dp[i][0] = min(dp[i - 1][1] + color[i][0], dp[i - 1][2] + color[i][0])
    dp[i][1] = min(dp[i - 1][0] + color[i][1], dp[i - 1][2] + color[i][1])
    dp[i][2] = min(dp[i - 1][0] + color[i][2], dp[i - 1][1] + color[i][2])

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
