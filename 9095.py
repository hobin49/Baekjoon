dp = [0] * 11 #n의 크기만큼 리스트를 만들어준다. 
dp[1] = 1
dp[2] = 2
dp[3] = 4 #dp[3]은 dp[1] + dp[2]

for i in range(4, 10):
    dp[i] = dp[i -1] + dp[i - 2] + dp[i -3] #패턴을 대입한다.

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])