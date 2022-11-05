# 입력값을 받고
n = int(input())
# 10007로 나눈 나머지를 구하기 위한 변수
mod = 10007
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp = [[1] * 10 for _ in range(n + 1)]
# 1은 이미 dp에 있으니까 2부터 입력값까지
for i in range(2, n + 1):
    # 1부터 9까지 돌고 이전 수와 전 레벨의 수를 더해준다.
    for j in range(1, 10):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

# 총합을 나머지로 나눠준다.
print(sum(dp[n]) % mod)
