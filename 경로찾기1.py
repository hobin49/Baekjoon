from collections import deque

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


visited = [[0] * n for _ in range(n)]

k = [0 for _ in range(n)]


def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]

    while queue:
        x = queue.popleft()

        for i in range(n):
            if check[i] == 0 and graph[x][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1


for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)
