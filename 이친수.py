n = int(input())
dp = [0] * 91
dp[0] = 0
dp[1] = 1
dp[2] = 1

# 0 - 0개, 1 - 1개 2(10) - 1개
# 3(100, 101) -2개, 4(1000, 1001, 1010) - 3개,
# 5(10000, 10001, 10010, 10100, 10101) - 5개,
# 6(100000, 100001, 1000010, 100100, 100101, 101000, 101010, 101001) - 8개
for i in range(3, 91):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])
