n, k = map(int, input().split())
number = []

dp = [0] * (k + 1)
dp[0] = 1
for _ in range(n):
    number.append(int(input()))

# 1: 1
# 2: 1 1, 2
# 3: 1 1 1, 1 2
# 4: 1 1 1 1, 1 1 2, 2 2
# 5: 1 1 1 1 1, 1 1 1 2, 1 2 2, 5
for c in number:
    for d in range(c, k + 1):
        # 1: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # 2: [1, 1, 1+1. 1+1, 2+1, 2+1, 3+1, 3+1, 4+1, 4+1, 5+1]
        # 5: [1, 1, 1+1, 1+1, 2+1, dp[5]+ dp[5-5]=4, dp[6] + dp[6-5] =5, dp[7] + dp[7-5] = 6, dp[8] + dp[8-5] = 7, dp[9] + dp[9-5] = 8, dp[10] + dp[10-5] = 10]
        dp[d] = dp[d] + dp[d - c]
print(dp[k])
