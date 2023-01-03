n = int(input())
k = list(map(int, input().split()))

# 리스트의 모든 요소의 값
dp = k[:]
dp[0] = k[0]

for i in range(1, n):
    for j in range(i):
        if k[j] < k[i]:
            dp[i] = max(dp[i], dp[j] + k[i])

print(max(dp))
