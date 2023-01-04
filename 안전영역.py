from collections import deque

n = int(input())

k = [list(map(int, input().split())) for _ in range(n)]

# 방문표시
visited = [False * n for _ in range(n)]

print(visited)
# 사방탐색을 위한 리스트
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# def dfs(x, y):
#     visited[0][0] = True

#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if -1 < nx <= n and -1 < ny <= n:
#             if visited[nx][ny] == -1 and visited[nx][ny] <=
