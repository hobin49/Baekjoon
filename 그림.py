from collections import deque

# 입력값 받아주기
n, m = map(int, input().split())

graph = []

# 입력값 받아주기
for _ in range(n):
    graph.append(list(map(int, input().split())))


if n == 1 and m == 1:
    print(0)

# dfs 함수
def bfs(graph, x, y):
    # 델타 탐색
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cnt = 1
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        # 탐색 시작
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 탐색 범위를 벗어나지 않는지
            if (-1 < nx < n) and (-1 < ny < m):
                if graph[nx][ny] == 1:
                    # 방문처리
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1
    return cnt


# dfs 다 돌기
cnt = 0
answer = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            # 함수 돌아주고
            answer.append(bfs(graph, x, y))

if len(answer) == 0:
    print(len(answer))
    print(0)
else:
    print(len(answer))
    print(max(answer))
