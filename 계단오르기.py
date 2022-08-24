dp =[0] * 301
step = [0] * 301
n = int(input())
for i in range(1, n+1):
    step[i] = int(input())
dp[1] = step[1]
dp[2] = step[1] + step[2]
#연속된 세칸을 밟으면 안되므로 (1칸 올라간 후 2칸 올라가거나) or (2칸 올라간 후 1칸 올라가거나)
dp[3] = max(step[1] + step[3], step[2] + step[3])

for i in range(4, n+1):
    #마지막 칸은 무조건 밟아야하고 연속된 세칸을 밞으면 안되므로 두 가지 방법 중 더 높은 점수를 얻을 수 있는 방법을 선택 
    dp[i] = max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i])
print(dp[n])
