# 내가 몰랐던 부분
# 1. 1번 1행 1열부터 시작하는데 라스트의 인덱스는 0부터 시작 이걸 어떻게 해결해야하나?
# 해결점: 그래프 문제 풀었을때 노드도 1번 노드부터 시작한다.
# 그래서 dp = [[0] * (n + 1) for i in range(n + 1)] 해서 0행이 아닌 1행부터 시작할 수 있게
# 2. 내가 원하는 범위만큼 누적합을 어떻게 구할 것이냐? 예를 들어 27을 구하려면 (2,2) ~ (3,4) = 27인데
# (3,1)이 포함이 되지 않는 부분에서 이해가 가지 않았습니다.
# 해결점: 사각형 범위에 있는 값을 구하는 문제였다는 것 - 아이디어가 떠오르지 않았다.(힌트를 봤습니다)


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []
for i in range(n):
    answer.append(list(map(int, input().split())))


dp = [[0] * (n + 1) for i in range(n + 1)]

# 1번행 1번열부터 누적된 값을 넣어야하기 때문에 1부터 시작
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 3 -> 8이 되기 위한 과정
        # dp[2][2]를 구해야한다.
        # dp[2][2] = dp[2][1](3) + dp[1][2](3) - dp[1][1](1) + answer[1][1](3)
        # dp는 1행 1열부터 시작하니까 answer에서 해당하는 값을 구하려면 answer[i-1][j-1]을 해야한다.
        dp[a][b] = dp[a][b - 1] + dp[a - 1][b] - dp[a - 1][b - 1] + answer[a - 1][b - 1]


for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 27을 구하기 위한 과정
    # dp[3][4](42) - dp[3][1](6) - dp[1][4](10) + dp[1][1](1) = 27
    result = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
    print(result)
