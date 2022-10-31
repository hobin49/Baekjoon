n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
result = -1001

for i in range(n):
    dp[i] = max(dp[i - 1] + lst[i], lst[i])
    result = max(dp[i], result)

print(result)
