import heapq
import math
n, m = map(int, input().split())

graph = []

INF = math.inf

for _ in range(m):
    graph.append(list(map(int, input())))


distance = [[INF] * n for _ in range(m)]



def dijkstra(x, y):
    start = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    queue = []
    heapq.heappush(queue, (x, y, start))
    distance[x][y] = 0
    while queue:
        x, y, dist = heapq.heappop(queue)

        if dist > distance[x][y]:
            continue


        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]


            if (-1 < nx < m) and (-1 < ny < n):
                if dist + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(queue, (nx, ny, distance[nx][ny]))




dijkstra(0, 0)
print(distance[m-1][n-1])