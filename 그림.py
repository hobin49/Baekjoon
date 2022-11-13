from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 넓이
    area = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (-1 < nx < n) and (-1 < ny < m):
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    area += 1
    return area


answer = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            answer.append(bfs(graph, x, y))

if len(answer) == 0:
    print(len(answer))
    print(0)

else:
    print(len(answer))
    print(max(answer))
