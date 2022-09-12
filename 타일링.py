dp = [0] * 1001
dp[1] = 1
dp[2] = 3
dp[3] = 5
mod = 10007

for i in range(4, 1001):
    dp[i] = dp[i-2] *2 + dp[i-1]

n = int(input())

print(dp[n] % mod)
