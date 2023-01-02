n = int(input())
k = list(map(int, input().split()))

dp = [0] * 1001
dp[0] = k[0]

for i in range(1, n):
    for j in range(i):
        if k[j] < k[i]:
            dp[i] = max(dp[i], dp[j] + k[i])
        else:
            dp[i] = max(dp[i], k[i])

print(max(dp))
