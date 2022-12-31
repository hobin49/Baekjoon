def solution(triangle):
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(
                triangle[row + 1][col], triangle[row + 1][col + 1]
            )
    return triangle[0][0]


n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int, input().split())))
print(solution(dp))


# dp = []
# for _ in range(n):
#     dp.append(list(map(int, input().split())))

# for i in range(1, n):
#     for j in range(i + 1):
#         if j == 0:
#             dp[i][j] = dp[i - 1][j] + dp[i][j]
#         elif i == j:
#             dp[i][j] = dp[i - 1][j - 1] + dp[i][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j] + dp[i][j], dp[i - 1][j - 1] + dp[i][j])

# print(max(dp[n - 1]))
