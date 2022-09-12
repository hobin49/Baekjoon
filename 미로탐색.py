#이중 for문 탐색
def dfs(x, y):
    #델타 탐색
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    cnt = 0
    #델타 탐색 시작 
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        #탐색 범위 벗어나면 안 돼
        if (-1 < nx < n) and (-1 < ny < m):
            if maze[nx][ny] == 1:
                cnt += 1
                maze[nx][ny] = 0
    return cnt

n, m = map(int, input().split())

maze = [list(map(int, input())) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if maze[x][y] == 1:
            dfs(x, y)




