import sys

sys.setrecursionlimit(100000)

n = int(input())

board = []
for _ in range(n):
    k = list(map(int, input().split()))
    board.append(k)
# 최대 높이
max_num = max(k)
# 지금까지 안전개수 나중에 안전개수가 안 나올 것을 대비
result = -1000

# 사방탐색
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# dfs 탐색
def dfs(x, y, num):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if (-1 < nx < n) and (-1 < ny < n) and visited[nx][ny] == 0:
            if board[nx][ny] > num:
                visited[nx][ny] = 1
                dfs(nx, ny, num)


for i in range(max_num):
    visited = [[0] * n for _ in range(n)]
    # 안전한 영역 개수 확인
    cnt = 0
    for j in range(n):
        for k in range(n):
            if board[j][k] > i and visited[j][k] == 0:
                cnt += 1
                visited[j][k] = 1
                dfs(j, k, i)

    result = max(result, cnt)

print(result)
